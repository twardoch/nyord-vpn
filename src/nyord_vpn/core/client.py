"""Main NordVPN client implementation.

this_file: src/nyord_vpn/core/client.py

This module contains the main Client class that coordinates all VPN operations.
It serves as the primary entry point for both CLI and library usage, orchestrating:

Components:
- API interactions via NordVPNAPI (api/api.py) for authentication and server info
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
from typing import Any, TypedDict

from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from rich.logging import RichHandler

from nyord_vpn.api.api import NordVPNAPI
from nyord_vpn.exceptions import VPNConnectionError, VPNError
from nyord_vpn.network.server import ServerManager
from nyord_vpn.network.vpn import VPNConnectionManager
# DATA_DIR is no longer used here or created by init()
from nyord_vpn.utils.utils import CACHE_DIR, CONFIG_DIR, save_vpn_state

load_dotenv()


# Update logger configuration to respect verbose flag
def configure_logging(verbose: bool = False) -> None:
    """Configure logging based on verbose mode."""
    # Set default level to WARNING when not in verbose mode
    log_level = "DEBUG" if verbose else "WARNING"

    # Configure loguru logger
    logger.remove()  # Remove default handler
    logger.add(
        sys.stderr,
        level=log_level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )


# Default logger configuration
logger.configure(
    handlers=[
        {
            "sink": RichHandler(),
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            "level": "WARNING",  # Default to WARNING level
        },
    ],
)


# Constants
PACKAGE_DIR = Path(__file__).parent
# CACHE_FILE = DATA_DIR / "countries.json" # No longer needed

# Rich console for pretty output
console = Console()


# Store cache in the package directory
# COUNTRIES_CACHE = PACKAGE_DIR / "data" / "countries.json" # No longer needed


# Obsolete TypedDicts removed as FALLBACK_DATA and associated logic are gone.
# class City(TypedDict):
#     """City information from NordVPN API."""
#
#     dns_name: str
#     hub_score: int
#     id: int
#     latitude: float
#     longitude: float
#     name: str
#     serverCount: int
#
#
# class Country(TypedDict):
#     """Country information from NordVPN API."""
#
#     cities: list[City]
#     code: str
#     id: int
#     name: str
#     serverCount: int
#
#
# class CountryCache(TypedDict):
#     """Cache file structure."""
#
#     countries: list[Country]
#     last_updated: str


# Fallback country list in case API is unreachable
# FALLBACK_DATA: CountryCache = { ... } # Removed

# Cache expiry in seconds (24 hours)
# CACHE_EXPIRY = 24 * 60 * 60 # This might be related to the removed COUNTRIES_CACHE


class Client:
    """Main NordVPN client that coordinates API, VPN, and server management.

    This class provides the high-level interface for:
    1. Managing VPN connections
    2. Server selection and optimization
    3. Connection status monitoring
    4. User feedback and logging
    """

    def __init__(
        self,
        username_str: str | None = None,
        password_str: str | None = None,
        *,
        verbose: bool = False,
    ) -> None:
        """Initialize Client with credentials.

        Args:
            username_str: NordVPN username or None to use environment variable
            password_str: NordVPN password or None to use environment variable
            verbose: Whether to enable verbose logging (default: False)

        Raises:
            VPNError: If credentials are not available

        """
        # Store verbose flag first
        self.verbose = verbose

        # Configure logging based on verbose flag right away
        configure_logging(verbose)

        # Setup logger
        self.logger = logger

        if self.verbose:
            self.logger.info("Initializing NordVPN client...")

        # Get credentials from parameters or environment
        self.username = (
            username_str or os.getenv("NORD_USER") or os.getenv("NORDVPN_LOGIN")
        )
        self.password = (
            password_str or os.getenv("NORD_PASSWORD") or os.getenv("NORDVPN_PASSWORD")
        )

        if not self.username or not self.password:
            raise VPNError(
                "Missing VPN credentials. "
                "Please provide username and password or set NORD_USER and NORD_PASSWORD environment variables."
            )

        # Initialize components in the correct order
        self.api_client = NordVPNAPI(timeout=10)
        self.server_manager = ServerManager(self.api_client)
        self.vpn_manager = VPNConnectionManager( # Instantiation of VPNConnectionManager
            api_client=self.api_client,         # Pass the API client
            server_manager=self.server_manager, # Pass the ServerManager
            # vpn_manager=self, # This argument is now removed from VPNConnectionManager's __init__
            verbose=verbose                     # Pass the verbose flag
        )

        # Set up VPN credentials
        try:
            self.vpn_manager.setup_connection("", self.username, self.password)
        except VPNError as e:
            if "hostname" in str(e).lower():
                # Ignore hostname error since we'll set it later
                pass
            else:
                raise

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
            country_code: Two-letter country code (e.g. 'US', 'GB')

        Raises:
            VPNError: If connection fails

        """
        try:
            # First check if we're already connected
            status = self.status()
            if status.get("connected", False):
                # VPN manager will handle disconnection automatically
                if self.verbose:
                    self.logger.info(
                        "Already connected, will disconnect before connecting to new server"
                    )

            # Select fastest servers
            servers = self.server_manager.select_fastest_server(country_code)
            if not servers:
                raise VPNError(f"No servers available in {country_code}")

            # Take the first (fastest) server
            server = servers[0]
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Selected server has no hostname")

            if self.verbose:
                self.logger.info(f"Selected server: {hostname}")
                console.print(f"Selected server: [cyan]{hostname}[/cyan]")

            # Set up VPN configuration
            if not self.username or not self.password:
                raise VPNError("Missing VPN credentials")
            self.vpn_manager.setup_connection(hostname, self.username, self.password)

            # Connect to VPN
            if self.verbose:
                self.logger.info("Establishing VPN connection...")
                console.print("Establishing VPN connection...")

            # Connect and wait for result
            self.vpn_manager.connect(servers)  # Pass all servers to try in order

            # Get status for display
            status = self.status()

            # Output based on verbose mode
            if self.verbose:
                console.print("[green]Successfully connected to VPN[/green]")
                console.print(f"Private IP: [cyan]{status.get('ip', 'Unknown')}[/cyan]")
                console.print(
                    f"Country: [cyan]{status.get('country', 'Unknown')}[/cyan]"
                )
                console.print(f"Server: [cyan]{status.get('server', 'Unknown')}[/cyan]")
            else:
                console.print(self._format_minimal_output(status))

        except Exception as e:
            raise VPNError(f"Failed to connect: {e}")

    def bye(self) -> None:
        """Disconnect from the VPN."""
        if self.verbose:
            logger.info("Checking current connection status...")

        try:
            status = self.vpn_manager.status()
            if status["connected"]:
                self.vpn_manager.disconnect()
            elif self.verbose:
                logger.info("No active VPN connection found")
        except VPNError as e:
            logger.error(f"Error during disconnect: {e}")
            return

        # Get current IP before disconnecting
        current_ip = self.vpn_manager.get_current_ip()
        if self.verbose:
            self.logger.info("Checking current connection status...")

        # Disconnect if connected
        if self.vpn_manager.is_connected():
            if self.verbose:
                self.logger.info("Disconnecting from VPN...")
            self.vpn_manager.disconnect()
            if self.verbose:
                console.print("[green]Disconnected from VPN[/green]")
        elif self.verbose:
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

        # Final status output
        status = self.status()
        if self.verbose:
            if public_ip:
                console.print(f"Public IP: [cyan]{public_ip}[/cyan]")
            else:
                console.print("[yellow]Could not determine IP[/yellow]")
        else:
            console.print(self._format_minimal_output(status))

    def info(self) -> None:
        """Display current VPN status."""
        try:
            status = self.status()
            if self.verbose:
                if status.get("connected", False):
                    console.print("[green]VPN Status: Connected[/green]")
                    console.print(
                        f"Private IP: [cyan]{status.get('ip', 'Unknown')}[/cyan]"
                    )
                    console.print(
                        f"Country: [cyan]{status.get('country', 'Unknown')}[/cyan]"
                    )
                    console.print(
                        f"Server: [cyan]{status.get('server', 'Unknown')}[/cyan]"
                    )
                else:
                    console.print("[yellow]VPN Status: Not Connected[/yellow]")
                    console.print(
                        f"Public IP: [cyan]{status.get('ip', 'Unknown')}[/cyan]"
                    )
            else:
                console.print(self._format_minimal_output(status))
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
            VPNConnectionError: If any initialization step fails (OpenVPN missing,
                               directory creation fails, API unreachable, etc.)

        """
        try:
            # Create necessary directories
            # DATA_DIR creation removed as its primary use (static countries.json) is gone.
            # CONFIG_DIR is created by utils.utils.py upon import if not existing.
            # CACHE_DIR is also created by utils.utils.py.
            # Explicit creation here ensures they exist with client's knowledge.
            for directory in [CACHE_DIR, CONFIG_DIR]: # Only CACHE_DIR and CONFIG_DIR
                directory.mkdir(parents=True, exist_ok=True)

            # Test API connectivity using a v2 method
            try:
                # Use get_servers with refresh to actively test the API
                # We don't need the result here, just that it doesn't raise an error.
                self.api_client.get_servers(refresh=True)
                if self.verbose:
                    self.logger.info("Successfully connected to NordVPN API.")
            except Exception as e:
                self.logger.error(f"Failed to connect to NordVPN API: {e}")
                raise VPNConnectionError("Failed to connect to NordVPN API") from e

            # Get initial IP for comparison
            try:
                self.get_current_ip()
            except Exception as e:
                raise VPNConnectionError("Failed to get initial IP") from e

        except Exception as e:
            if isinstance(e, VPNConnectionError):
                raise
            raise VPNConnectionError(f"Failed to initialize client environment: {e}")

    def get_current_ip(self) -> str | None:
        """Get current IP address."""
        return self.vpn_manager.get_current_ip()

    def list_countries(self) -> None:
        """List all available countries from the NordVPN API."""
        try:
            countries = self.api_client.get_all_countries_from_v2(refresh_cache=False)
            if not countries:
                console.print("[yellow]No countries found or API error.[/yellow]")
                return

            console.print("[green]Available countries:[/green]")
            for country_info in countries:
                console.print(f"  - {country_info['name']} ({country_info['code']})")
        except VPNAPIError as e:
            console.print(f"[red]Error fetching countries:[/red] {e}")
        except Exception as e:
            console.print(f"[red]An unexpected error occurred:[/red] {e}")

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

    def _format_minimal_output(self, status: dict) -> str:
        """Format minimal output string based on connection status.

        Args:
            status: The VPN status dictionary from self.status()

        Returns:
            str: Formatted string in the format "IPADDRESS: VPNSERVERNAME" or "IPADDRESS: -"

        """
        ip_address = status.get("ip", "Unknown")
        server_name = status.get("server", "-")

        if status.get("connected", False):
            return f"{ip_address}: {server_name}"
        return f"{ip_address}: -"
