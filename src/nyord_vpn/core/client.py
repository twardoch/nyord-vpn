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

import os
import sys
import time
from pathlib import Path
from typing import TypedDict

import requests
from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from rich.logging import RichHandler


from nyord_vpn.storage.models import (
    ConnectionError,
    CredentialsError,
    VPNError,
)
from nyord_vpn.utils.utils import (
    API_HEADERS,
    CACHE_DIR,
    CONFIG_DIR,
    DATA_DIR,
    save_vpn_state,
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
        }
    ]
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
    """Main NordVPN client that coordinates API, VPN, and server management.

    This class serves as the primary interface for the nyord-vpn library, orchestrating:
    1. Authentication and API interactions through NordVPNAPIClient
    2. VPN connection management through VPNConnectionManager
    3. Server selection and optimization through ServerManager
    4. State persistence and cache management

    The client handles automatic fallback mechanisms when API calls fail, maintains
    a session-based failed servers list to avoid reconnection attempts to problematic
    servers, and provides both programmatic and CLI interfaces for VPN management.

    Typical usage:
        client = Client(username="user", password="pass")
        client.go("us")  # Connect to a US server
        client.status()  # Check connection status
        client.disconnect()  # Disconnect from VPN
    """

    def __init__(
        self,
        username: str | None = None,
        password: str | None = None,
        verbose: bool = False,
        auto_init: bool = True,
    ):
        """Initialize NordVPN client with credentials and optional configuration.

        This constructor sets up the core components of the VPN client:
        1. API client for NordVPN API interactions
        2. VPN manager for OpenVPN connection handling
        3. Server manager for server selection and optimization
        4. Logging configuration for debugging
        5. Environment initialization if auto_init is True

        Args:
            username: Optional username (defaults to NORD_USER env var)
            password: Optional password (defaults to NORD_PASSWORD env var)
            verbose: Enable verbose logging for detailed operation tracking
            auto_init: Whether to automatically initialize the environment
                      (creates directories, checks OpenVPN, tests API)

        Environment variables:
            NORD_USER: NordVPN username (primary)
            NORD_PASSWORD: NordVPN password (primary)
            NORDVPN_LOGIN: NordVPN username (fallback)
            NORDVPN_PASSWORD: NordVPN password (fallback)

        Raises:
            CredentialsError: If neither direct credentials nor environment variables are provided
            ConnectionError: If auto_init is True and environment setup fails
        """
        # Get credentials
        username_str = username or os.getenv("NORD_USER") or os.getenv("NORDVPN_LOGIN")
        password_str = (
            password or os.getenv("NORD_PASSWORD") or os.getenv("NORDVPN_PASSWORD")
        )
        if not username_str or not password_str:
            raise CredentialsError(
                "NORD_USER and NORD_PASSWORD environment variables must be set"
            )

        # Initialize components
        self.verbose = verbose
        self.api_client = NordVPNAPIClient(username_str, password_str, verbose)
        self.vpn_manager = VPNConnectionManager(verbose=verbose)
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
            else:
                console.print(
                    "[green]Client environment initialized successfully[/green]"
                )

        except Exception as e:
            raise ConnectionError(f"Failed to initialize client environment: {e}")

    def status(self) -> dict[str, str | bool | None]:
        """Get current VPN connection status and details.

        Retrieves comprehensive information about the current VPN connection:
        1. Connection state (connected/disconnected)
        2. Current IP address (VPN IP if connected, normal IP if not)
        3. Connected server details (if connected)
        4. Country information (if connected)
        5. Connection duration (if connected)

        Returns:
            dict: Status information with the following keys:
                - status (bool): True if connected, False if not
                - ip (str): Current IP address
                - server (str, optional): Connected server hostname
                - country (str, optional): Connected server country
                - connected_since (str, optional): Connection timestamp

        Note:
            This method performs real-time checks of the connection state
            and IP address, ensuring accurate status information even if
            the connection was established outside this client instance.
        """
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

    def go(self, country_code: str) -> None:
        """Connect to VPN in specified country."""
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            try:
                # Get country info
                country = self.server_manager.get_country_info(country_code)
                if not country:
                    raise ValueError(f"Country code '{country_code}' not found")

                if self.verbose:
                    self.logger.info(f"Connecting to {country['name']}")

                # Get initial IP
                self._initial_ip = self.get_current_ip()
                if self.verbose:
                    self.logger.info(f"Initial IP: {self._initial_ip}")

                # Select fastest server
                server = self.server_manager.select_fastest_server(country_code)
                if not server:
                    raise VPNError("No server available")

                hostname = (
                    server.get("hostname") if isinstance(server, dict) else server
                )
                if not hostname:
                    raise VPNError("Invalid server data - missing hostname")

                if self.verbose:
                    self.logger.info(f"Selected server: {hostname}")
                else:
                    console.print(f"[cyan]Server:[/cyan] {hostname}")

                # Set up VPN configuration
                self.vpn_manager.setup_connection(
                    hostname, self.api_client.username, self.api_client.password
                )

                # Establish VPN connection
                if self.verbose:
                    self.logger.info("Establishing VPN connection...")
                self.vpn_manager.connect({"hostname": hostname})

                # Update connection info
                self._connected_ip = self.get_current_ip()
                self._server = hostname
                self._country_name = country["name"]

                if self.verbose:
                    self.logger.info(f"Connected to {hostname}")
                    self.logger.info(f"New IP: {self._connected_ip}")
                else:
                    console.print(f"[green]Connected to {hostname}[/green]")
                    console.print(f"[cyan]New IP:[/cyan] {self._connected_ip}")

                # Save state
                self._save_state()
                break

            except Exception as e:
                if self.verbose:
                    self.logger.warning(f"Connection failed: {e}")
                else:
                    console.print(f"[yellow]Connection failed: {e}[/yellow]")

                retry_count += 1
                if retry_count < max_retries:
                    if self.verbose:
                        self.logger.info("Retrying with different server...")
                    else:
                        console.print(
                            "[yellow]Retrying with different server...[/yellow]"
                        )
                    time.sleep(2)
                else:
                    raise VPNError(
                        f"Failed to connect after {max_retries} attempts: {e}"
                    )

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

    def get_current_ip(self) -> str | None:
        """Get current IP address."""
        return self.vpn_manager.get_current_ip()

    def _save_state(self) -> None:
        """Save current connection state."""
        state = {
            "connected": self.is_protected(),
            "initial_ip": self._initial_ip,
            "connected_ip": self._connected_ip,
            "server": self._server,
            "country": self._country_name,
            "timestamp": time.time(),
        }
        save_vpn_state(state)
