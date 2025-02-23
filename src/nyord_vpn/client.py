"""Main NordVPN client implementation.

This module contains the main Client class that coordinates:
- API interactions via NordVPNAPIClient
- VPN connections via VPNConnectionManager
- Server selection via ServerManager
"""

import json
import os, sys
import random
import signal
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, TypedDict, Union, cast

import psutil
from loguru import logger
import requests
from dotenv import load_dotenv
import shutil
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.logging import RichHandler

load_dotenv()
logger.configure(
    handlers=[
        {
            "sink": RichHandler(),
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        }
    ]
)

from ._templates import OPENVPN_TEMPLATE
from .base import NordVPNClient
from .models import (
    ConnectionError,
    CredentialsError,
    ServerError,
    DisconnectionError,
    VPNError,
)
from .utils import (
    API_HEADERS,
    CACHE_DIR,
    CONFIG_DIR,
    DATA_DIR,
    NORDVPN_COUNTRY_IDS,
    OPENVPN_AUTH,
    OPENVPN_CONFIG,
    OPENVPN_LOG,
    load_vpn_state,
    save_vpn_state,
)
from .server_manager import ServerManager
from .api_client import NordVPNAPIClient
from .vpn_manager import VPNConnectionManager

# Constants
PACKAGE_DIR = Path(__file__).parent
CACHE_FILE = DATA_DIR / "countries.json"

# Rich console for pretty output
console = Console()


# Store cache in the package directory
COUNTRIES_CACHE = PACKAGE_DIR / "data" / "countries.json"


# Type definitions for country data
class City(TypedDict):
    """City information from NordVPN API."""

    dns_name: str
    hub_score: int
    id: int
    latitude: float
    longitude: float
    name: str
    serverCount: int


class Country(TypedDict):
    """Country information from NordVPN API."""

    cities: List[City]
    code: str
    id: int
    name: str
    serverCount: int


class CountryCache(TypedDict):
    """Cache file structure."""

    countries: List[Country]
    last_updated: str


# Fallback country list in case API is unreachable
FALLBACK_DATA: CountryCache = {
    "countries": [
        {
            "cities": [
                {
                    "dns_name": "new-york",
                    "hub_score": 0,
                    "id": 8971718,
                    "latitude": 40.7141667,
                    "longitude": -74.0063889,
                    "name": "New York",
                    "serverCount": 529,
                }
            ],
            "code": "US",
            "id": 228,
            "name": "United States",
            "serverCount": 529,
        },
        {
            "cities": [
                {
                    "dns_name": "london",
                    "hub_score": 0,
                    "id": 2989907,
                    "latitude": 51.514125,
                    "longitude": -0.093689,
                    "name": "London",
                    "serverCount": 785,
                }
            ],
            "code": "GB",
            "id": 227,
            "name": "United Kingdom",
            "serverCount": 785,
        },
        {
            "cities": [
                {
                    "dns_name": "frankfurt",
                    "hub_score": 0,
                    "id": 2215709,
                    "latitude": 50.116667,
                    "longitude": 8.683333,
                    "name": "Frankfurt",
                    "serverCount": 301,
                }
            ],
            "code": "DE",
            "id": 81,
            "name": "Germany",
            "serverCount": 301,
        },
    ],
    "last_updated": "2024-02-23T00:00:00Z",
}

# Cache expiry in seconds (24 hours)
CACHE_EXPIRY = 24 * 60 * 60


class Client:
    """Main NordVPN client that coordinates API, VPN, and server management."""

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verbose: bool = False,
        auto_init: bool = True,
    ):
        """Initialize NordVPN client.

        Args:
            username: Optional username (defaults to NORD_USER env var)
            password: Optional password (defaults to NORD_PASSWORD env var)
            verbose: Enable verbose logging
            auto_init: Whether to automatically initialize the environment
        """
        # Get credentials
        username_str = username or os.getenv("NORD_USER")
        password_str = password or os.getenv("NORD_PASSWORD")
        if not username_str or not password_str:
            raise CredentialsError(
                "NORD_USER and NORD_PASSWORD environment variables must be set"
            )

        # Initialize components
        self.verbose = verbose
        self.api_client = NordVPNAPIClient(username_str, password_str, verbose)
        self.vpn_manager = VPNConnectionManager(verbose)
        self.server_manager = ServerManager(self.api_client)
        self._failed_servers = set()  # Track failed servers in this session

        # Set up logging
        self.logger = logger
        if verbose:
            self.logger.add(sys.stdout, level="DEBUG")

        # Initialize if requested
        if auto_init:
            try:
                self.init()
            except Exception as e:
                if verbose:
                    self.logger.warning(f"Failed to initialize environment: {e}")

    def init(self) -> None:
        """Initialize the client environment."""
        try:
            # Check OpenVPN installation
            openvpn_path = self.vpn_manager.check_openvpn_installation()
            if self.verbose:
                self.logger.info(f"Found OpenVPN at: {openvpn_path}")

            # Create necessary directories
            for directory in [CACHE_DIR, CONFIG_DIR, DATA_DIR]:
                directory.mkdir(parents=True, exist_ok=True)
                if self.verbose:
                    self.logger.info(f"Created directory: {directory}")

            # Test API connectivity
            if not self.api_client.test_api_connectivity():
                raise ConnectionError("Failed to connect to NordVPN API")
            if self.verbose:
                self.logger.info("Successfully connected to NordVPN API")

            # Get initial IP
            initial_ip = self.vpn_manager.get_current_ip()
            if not initial_ip:
                raise ConnectionError("Failed to get initial IP")
            if self.verbose:
                self.logger.info(f"Initial IP: {initial_ip}")

            if self.verbose:
                self.logger.info("Client environment initialized successfully")
            else:
                console.print(
                    "[green]Client environment initialized successfully[/green]"
                )

        except Exception as e:
            raise ConnectionError(f"Failed to initialize client environment: {e}")

    def status(self) -> Dict[str, Union[str, bool, None]]:
        """Get current VPN connection status."""
        try:
            current_ip = self.vpn_manager.get_current_ip()
            if not current_ip:
                return {
                    "status": False,
                    "ip": "Unknown",
                    "country": "Unknown",
                    "city": "Unknown",
                    "server": None,
                }

            is_connected = self.vpn_manager.verify_connection()
            if not is_connected:
                return {
                    "status": False,
                    "ip": current_ip,
                    "country": "Unknown",
                    "city": "Unknown",
                    "server": None,
                }

            # Get location info from NordVPN API
            try:
                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers=API_HEADERS,
                    timeout=5,
                )
                response.raise_for_status()
                nord_data = response.json()
                return {
                    "status": True,
                    "ip": current_ip,
                    "country": nord_data.get("country", "Unknown"),
                    "city": nord_data.get("city", "Unknown"),
                    "server": self.vpn_manager._server,
                }
            except Exception:
                return {
                    "status": True,
                    "ip": current_ip,
                    "country": self.vpn_manager._country_name or "Unknown",
                    "city": "Unknown",
                    "server": self.vpn_manager._server,
                }

        except Exception as e:
            raise ConnectionError(f"Failed to get status: {e}")

    def go(
        self, country_code: Optional[str] = None, random_select: bool = False
    ) -> None:
        """Connect to VPN in specified country.

        Args:
            country_code: Optional country code to filter by. If None, a random country is selected.
            random_select: Whether to select a random server instead of fastest
        """
        try:
            # Get random country if none specified
            if not country_code:
                country_code = self.server_manager.get_random_country()
                if self.verbose:
                    self.logger.info(f"Selected random country: {country_code}")
                else:
                    console.print(
                        f"[cyan]Selected random country:[/cyan] {country_code}"
                    )

            # Disconnect any existing connection
            try:
                if self.verbose:
                    self.logger.info("Ensuring no existing VPN connection...")
                self.disconnect(verbose=self.verbose)
                time.sleep(2)
            except Exception as e:
                self.logger.warning(f"Error during disconnect: {e}")

            # Try to connect with retries
            max_retries = 3
            retry_count = 0

            while retry_count < max_retries:
                try:
                    if self.verbose:
                        self.logger.info("Selecting fastest server...")
                    server = self.server_manager.select_fastest_server(
                        country_code, random_select
                    )
                    if not server:
                        raise ConnectionError("Failed to select a server")

                    # Extract server info safely
                    hostname = None
                    country_name = None

                    if isinstance(server, dict):
                        hostname = server.get("hostname")
                        country_info = server.get("country", {})
                        country_name = (
                            country_info.get("name") if country_info else None
                        )
                    else:
                        hostname = str(server)

                    if not hostname:
                        raise ConnectionError("Invalid server data received")

                    country_name = country_name or country_code or "Unknown"

                    # Skip if server has already failed
                    if hostname in self._failed_servers:
                        if self.verbose:
                            self.logger.warning(
                                f"Server {hostname} previously failed, skipping"
                            )
                        raise ConnectionError("Server previously failed")

                    if self.verbose:
                        self.logger.info(f"Selected server: {hostname}")
                    else:
                        console.print(f"[cyan]Server:[/cyan] {hostname}")

                    if self.verbose:
                        self.logger.info("Setting up VPN configuration...")
                    self.vpn_manager.setup_connection(
                        hostname, self.api_client.username, self.api_client.password
                    )

                    if self.verbose:
                        self.logger.info("Establishing VPN connection...")
                    self.vpn_manager.start_openvpn()

                    # Wait for connection with timeout
                    start_time = time.time()
                    while time.time() - start_time < 10:  # 10 second timeout
                        if self.vpn_manager.verify_connection():
                            # Update connection info
                            self.vpn_manager.update_connection_info(
                                hostname, country_name
                            )

                            if self.verbose:
                                self.logger.info(f"Connected to {country_name}")
                                self.logger.info(
                                    f"VPN IP: {self.vpn_manager.get_current_ip()}"
                                )
                            else:
                                console.print(
                                    f"[green]Connected to {country_name}[/green]"
                                )
                                console.print(
                                    f"[cyan]VPN IP:[/cyan] {self.vpn_manager.get_current_ip()}"
                                )

                            return
                        time.sleep(1)

                    # Connection timeout, mark server as failed
                    self._failed_servers.add(hostname)
                    raise ConnectionError("Connection timeout")

                except Exception as e:
                    retry_count += 1
                    if retry_count < max_retries:
                        if self.verbose:
                            self.logger.warning(f"Connection failed: {e}")
                            self.logger.info("Retrying with different server...")
                        else:
                            console.print(f"[yellow]Connection failed: {e}[/yellow]")
                            console.print(
                                "[yellow]Retrying with different server...[/yellow]"
                            )
                        time.sleep(2)
                    else:
                        # Clear failed servers list after max retries
                        self._failed_servers.clear()
                        raise ConnectionError(
                            f"Failed to connect after {max_retries} attempts: {e}"
                        )

        except Exception as e:
            raise ConnectionError(f"Failed to connect: {e}")

    def disconnect(self, verbose: bool = True) -> None:
        """Disconnect from VPN."""
        try:
            self.vpn_manager.disconnect()
            if verbose:
                print("Disconnected from VPN")
        except Exception as e:
            raise ConnectionError(f"Failed to disconnect: {e}")

    def is_protected(self) -> bool:
        """Check if VPN is active."""
        status = self.status().get("status", False)
        return bool(status)
