"""Main NordVPN client implementation.

this_file: src/nyord_vpn/core/client.py

This module contains the main Client class that coordinates all VPN operations.
It serves as the primary entry point for both CLI and library usage, orchestrating:

Components:
- API interactions via NordVPNAPIClient (core/api.py) for authentication and server info
- VPN connections via VPNConnectionManager (network/vpn.py) for OpenVPN management
- Server selection via ServerManager (network/server.py) for optimal server choice
- State persistence via utils/utils.py for connection recovery

The client implements automatic fallback mechanisms and retry logic to handle:
1. API failures (falls back to cached data)
2. Connection failures (retries with different servers)
3. State management (persists and recovers connection state)
4. Error handling (provides detailed error messages and recovery steps)

Used by:
- CLI interface in __main__.py for command-line operations
- Python applications importing the Client class directly
- Internal test suite for integration testing

Example usage:
    from nyord_vpn import Client

    client = Client(username="user", password="pass")
    client.go("us")  # Connect to US server
    client.status()  # Check connection status
    client.disconnect()  # Disconnect from VPN
"""

import time
import os
from pathlib import Path
from typing import TypedDict, Any
import json

from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from rich.logging import RichHandler

from nyord_vpn.storage.models import (
    ConnectionError,
    VPNError,
    ServerError,
)
from nyord_vpn.utils.utils import (
    CACHE_DIR,
    CONFIG_DIR,
    DATA_DIR,
    save_vpn_state,
    check_root,
    ensure_root,
)
from nyord_vpn.network.server import ServerManager
from nyord_vpn.core.api import NordVPNAPIClient
from nyord_vpn.network.vpn import VPNConnectionManager

load_dotenv()
logger.configure(
    handlers=[
        {
            "sink": RichHandler(),
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        },
    ],
)


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

    cities: list[City]
    code: str
    id: int
    name: str
    serverCount: int


class CountryCache(TypedDict):
    """Cache file structure."""

    countries: list[Country]
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
                },
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
                },
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
                },
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
    """Main NordVPN client that coordinates API, VPN, and server management.

    This class provides the high-level interface for:
    1. Managing VPN connections
    2. Server selection and optimization
    3. Connection status monitoring
    4. User feedback and logging
    """

    def __init__(self, username_str: str | None = None, password_str: str | None = None, verbose: bool = False) -> None:
        """Initialize NordVPN client.

        Args:
            username_str: NordVPN username (optional if NORDVPN_USERNAME env var is set)
            password_str: NordVPN password (optional if NORDVPN_PASSWORD env var is set)
            verbose: Whether to enable verbose output

        Raises:
            VPNError: If credentials are not available
        """
        self.verbose = verbose
        self.logger = logger

        # Get credentials from env vars if not provided
        self.username = username_str or os.environ.get("NORDVPN_USERNAME")
        self.password = password_str or os.environ.get("NORDVPN_PASSWORD")
        
        if not self.username or not self.password:
            raise VPNError(
                "No VPN credentials available. Please set NORDVPN_USERNAME and NORDVPN_PASSWORD environment variables."
            )

        self.api_client = NordVPNAPIClient(self.username, self.password, verbose)
        self.vpn_manager = VPNConnectionManager(verbose=verbose)
        self.server_manager = ServerManager(self.api_client)

    def is_protected(self) -> bool:
        """Check if VPN is active."""
        status = self.status()
        return status.get("connected", False)

    def status(self) -> dict[str, Any]:
        """Get current VPN status.

        Returns:
            dict: Status information including:
                - connected (bool): Whether connected to VPN
                - ip (str): Current IP address
                - normal_ip (str): IP when not connected to VPN
                - server (str): Connected server if any
                - country (str): Connected country if any

        """
        return self.vpn_manager.status()

    def go(self, country_code: str) -> None:
        """Connect to VPN in specified country.

        Args:
            country_code: Two-letter country code (e.g. 'us', 'de')

        Raises:
            VPNError: If connection fails
        """
        try:
            # Check if already connected
            status = self.status()
            if status.get("connected", False):
                self.logger.info("Already connected to VPN, disconnecting first...")
                self.bye()

            # Try up to 3 servers in the country
            last_error = None
            tried_servers = set()
            hostname = None
            
            for _ in range(3):
                try:
                    # Get a server we haven't tried yet
                    server = self.server_manager.select_fastest_server(
                        country_code,
                        exclude_servers=tried_servers
                    )
                    if not server:
                        raise VPNError(f"No more servers available in {country_code}")

                    hostname = server.get("hostname")
                    if not hostname:
                        raise VPNError("Selected server has no hostname")
                        
                    tried_servers.add(hostname)
                    self.logger.info(f"Selected server: {hostname}")
                    self.vpn_manager.connect(server)
                    return  # Success!
                except VPNError as e:
                    last_error = e
                    if hostname:
                        self.logger.debug(f"Failed to connect to {hostname}: {e}")
                    continue  # Try next server

            # If we get here, all attempts failed
            raise VPNError(f"Failed to connect to any server in {country_code}: {last_error}")

        except Exception as e:
            if isinstance(e, VPNError):
                raise
            raise VPNError(f"Failed to connect to VPN: {e}")

    def bye(self) -> None:
        """Disconnect from VPN and show status.

        Disconnects from any active VPN connection and displays
        the current connection status including the public IP.

        Raises:
            VPNError: If disconnection fails
        """
        try:
            # Get current IP before disconnecting
            current_ip = self.vpn_manager.get_current_ip()
            if self.verbose:
                self.logger.info("Checking current connection status...")

            # Disconnect if connected
            if self.vpn_manager.is_connected():
                if self.verbose:
                    self.logger.info("Disconnecting from VPN...")
                self.vpn_manager.disconnect()
                console.print("[green]Disconnected from VPN[/green]")
            else:
                if self.verbose:
                    self.logger.info("No active VPN connection found")
                console.print("[yellow]Not connected to VPN[/yellow]")

            # Get fresh IP after disconnecting and save state
            public_ip = self.vpn_manager.get_current_ip()
            if not public_ip and current_ip:
                public_ip = current_ip  # Use pre-disconnect IP if available
            
            # Save state with current IP after disconnection
            state = {
                "connected": False,
                "current_ip": public_ip,  # This will update normal_ip in state
                "server": None,
                "country": None,
                "timestamp": time.time(),
            }
            save_vpn_state(state)
            
            if public_ip:
                console.print(f"Public IP: [cyan]{public_ip}[/cyan]")
            else:
                console.print("[yellow]Could not determine IP[/yellow]")

        except Exception as e:
            self.logger.error(f"Failed to disconnect: {e}")
            raise VPNError(f"Failed to disconnect: {e}")

    def info(self) -> None:
        """Display current VPN status."""
        try:
            status = self.status()
            if status.get("connected", False):
                console.print("[green]VPN Status: Connected[/green]")
                console.print(f"Current IP: [cyan]{status.get('ip', 'Unknown')}[/cyan]")
                console.print(
                    f"Country: [cyan]{status.get('country', 'Unknown')}[/cyan]"
                )
                console.print(f"Server: [cyan]{status.get('server', 'Unknown')}[/cyan]")
            else:
                console.print("[yellow]VPN Status: Not Connected[/yellow]")
                console.print(
                    f"Public IP: [cyan]{status.get('normal_ip', 'Unknown')}[/cyan]"
                )
        except Exception as e:
            raise VPNError(f"Failed to get status: {e}")

    def init(self) -> None:
        """Initialize the client environment and verify all dependencies.

        This method performs essential setup tasks:
        1. Verifies OpenVPN installation and accessibility
        2. Creates necessary directory structure for configs and cache
        3. Tests API connectivity to ensure account access
        4. Captures initial IP address for connection verification
        5. Sets up logging based on verbosity level

        The initialization process ensures all components required for
        VPN operation are available and properly configured before
        attempting any connections.

        Raises:
            ConnectionError: If any initialization step fails (OpenVPN missing,
                           directory creation fails, API unreachable, etc.)

        """
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

        except Exception as e:
            raise ConnectionError(f"Failed to initialize client environment: {e}")

    def get_current_ip(self) -> str | None:
        """Get current IP address."""
        return self.vpn_manager.get_current_ip()

    def _save_state(self) -> None:
        """Save current connection state."""
        state = {
            "connected": self.is_protected(),
            "initial_ip": self.get_current_ip(),
            "connected_ip": self.get_current_ip(),
            "server": self.status().get("server", "Unknown"),
            "country": self.status().get("country", "Unknown"),
            "timestamp": time.time(),
        }
        save_vpn_state(state)
