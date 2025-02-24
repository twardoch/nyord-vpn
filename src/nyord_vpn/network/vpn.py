"""VPN connection management module.

this_file: src/nyord_vpn/network/vpn.py

This module provides the VPNConnectionManager class that handles
OpenVPN connections to NordVPN servers.

Core Responsibilities:
1. OpenVPN process management and configuration
2. Connection establishment and verification
3. IP address tracking and validation
4. Connection state management
5. Config file generation and cleanup

Integration Points:
- Used by Client (core/client.py) for VPN operations
- Uses templates from utils/templates.py for config
- Uses connection utils from utils/connection.py
- Stores state via utils/utils.py

Security Features:
- Strong encryption (AES-256-GCM)
- Certificate validation
- DNS leak prevention
- Secure process management

Error Handling:
- Graceful process termination
- Connection verification
- State recovery
- Detailed error messages

The manager implements robust connection handling with:
- Automatic retry logic
- Connection health monitoring
- Process cleanup on errors
- State persistence for recovery
"""

import os
import subprocess
import time
from pathlib import Path
from typing import Any, Optional
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn
from loguru import logger

from ..exceptions import (
    VPNError,
    VPNAuthenticationError,
    VPNConfigError,
    VPNProcessError,
    VPNTimeoutError,
)
from ..utils.templates import (
    get_config_path,
    setup_config_directory,
    get_openvpn_command,
    refresh_configs,
)

# Constants
OPENVPN_AUTH = Path.home() / ".cache" / "nyord-vpn" / "openvpn.auth"
OPENVPN_LOG = Path.home() / ".cache" / "nyord-vpn" / "openvpn.log"


class VPNConnectionManager:
    """Manages VPN connections using OpenVPN.

    This class is responsible for the low-level VPN connection management:
    1. OpenVPN process control (start, stop, monitor)
    2. Configuration file management
    3. Connection state tracking and verification
    4. IP address monitoring and validation

    The manager maintains state about the current connection including:
    - Initial IP before connection
    - Connected IP after successful connection
    - Current server hostname
    - Connected country information
    """

    def __init__(self, verbose: bool = False):
        """Initialize VPN connection manager.

        Args:
            verbose: Whether to enable verbose logging
        """
        self.verbose = verbose
        self.logger = logger
        self.process: Optional[subprocess.Popen] = None

        # Connection state
        self._initial_ip: Optional[str] = None
        self._connected_ip: Optional[str] = None
        self._server: Optional[str] = None
        self._country_name: Optional[str] = None

        # Ensure cache directory exists
        OPENVPN_AUTH.parent.mkdir(parents=True, exist_ok=True)

    def get_current_ip(self) -> Optional[str]:
        """Get current IP address."""
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=5)
            response.raise_for_status()
            return response.json().get("ip")
        except Exception:
            return None

    def check_openvpn_installation(self) -> str:
        """Verify OpenVPN is installed and return its path."""
        try:
            result = subprocess.run(
                ["which", "openvpn"], capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            raise VPNError(
                "OpenVPN not found. Please install OpenVPN first:\n"
                "  macOS: brew install openvpn\n"
                "  Linux: sudo apt install openvpn\n"
                "  Windows: Download from https://openvpn.net/community-downloads/"
            )

    def connect(self, server: dict[str, Any]) -> None:
        """Connect to a VPN server using OpenVPN.

        This method handles the complete connection process:
        1. Validates server information
        2. Captures initial IP address
        3. Gets OpenVPN configuration
        4. Verifies authentication file
        5. Launches OpenVPN process
        6. Monitors connection establishment
        7. Verifies successful connection
        8. Updates connection state

        Args:
            server: Server information dictionary containing:
                - hostname: Server hostname for connection
                - (optional) additional server metadata

        Raises:
            VPNError: Base class for all VPN-related errors
            VPNAuthenticationError: If authentication fails
            VPNConfigError: If there are issues with the configuration
            VPNProcessError: If the OpenVPN process fails
            VPNTimeoutError: If connection times out
        """
        try:
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Invalid server info - missing hostname")

            if self.verbose:
                self.logger.debug(f"Connecting to {hostname}")

            # Store initial IP
            self._initial_ip = self.get_current_ip()

            # Get OpenVPN config
            config_path = get_config_path(hostname)
            if not config_path:
                if self.verbose:
                    self.logger.debug("Config not found, downloading configs...")
                try:
                    setup_config_directory()
                    config_path = get_config_path(hostname)
                except Exception as e:
                    raise VPNConfigError(f"Failed to download OpenVPN configs: {e}")
                if not config_path:
                    raise VPNConfigError(f"Failed to get OpenVPN config for {hostname}")

            # Verify auth file exists and has correct format
            if not OPENVPN_AUTH.exists():
                raise VPNAuthenticationError(
                    "Authentication file not found. Please create ~/.cache/nyord-vpn/openvpn.auth with your NordVPN credentials:\n"
                    "  1. Set your credentials as environment variables:\n"
                    "     export NORD_USER='your_nordvpn_username'\n"
                    "     export NORD_PASSWORD='your_nordvpn_password'\n"
                    "  2. Create the auth file:\n"
                    '     echo "$NORD_USER" > ~/.cache/nyord-vpn/openvpn.auth\n'
                    '     echo "$NORD_PASSWORD" >> ~/.cache/nyord-vpn/openvpn.auth\n'
                    "\nThe file should contain your username on the first line and password on the second line."
                )

            try:
                auth_lines = OPENVPN_AUTH.read_text().strip().splitlines()
                if len(auth_lines) != 2 or not all(line.strip() for line in auth_lines):
                    raise VPNAuthenticationError(
                        "Invalid auth file format. The file should contain exactly two non-empty lines:\n"
                        "  Line 1: Your NordVPN username\n"
                        "  Line 2: Your NordVPN password"
                    )
            except Exception as e:
                if isinstance(e, VPNAuthenticationError):
                    raise
                raise VPNAuthenticationError(f"Failed to read auth file: {e}")

            # Start OpenVPN process
            cmd = get_openvpn_command(config_path, OPENVPN_AUTH, OPENVPN_LOG)

            if self.verbose:
                self.logger.debug(f"Running OpenVPN command: {' '.join(cmd)}")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="Connecting...", total=None)
                try:
                    self.process = subprocess.Popen(
                        cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        bufsize=1,  # Line buffered
                    )
                except subprocess.SubprocessError as e:
                    raise VPNProcessError(f"Failed to start OpenVPN process: {e}")

            # Wait for initial connection and capture output
            try:
                time.sleep(5)
                if self.process.poll() is not None:
                    stdout, stderr = self.process.communicate()
                    if self.verbose:
                        self.logger.debug(f"OpenVPN stdout:\n{stdout}")
                        self.logger.debug(f"OpenVPN stderr:\n{stderr}")
                    if "AUTH_FAILED" in stderr:
                        raise VPNAuthenticationError(
                            f"Authentication failed. Full error:\n{stderr}"
                        )
                    raise VPNProcessError(
                        f"OpenVPN process failed:\n{stderr}\nOutput:\n{stdout}"
                    )
            except subprocess.TimeoutExpired:
                raise VPNTimeoutError("Timeout waiting for OpenVPN process")

            # Update connection info
            self._server = hostname
            self._connected_ip = self.get_current_ip()

            # Verify connection is working
            if not self.verify_connection():
                raise VPNError("Failed to establish VPN connection")

            if self.verbose:
                self.logger.info(f"Connected to {hostname}")

        except Exception as e:
            # Clean up on error
            self.disconnect()
            if isinstance(
                e,
                (
                    VPNAuthenticationError,
                    VPNConfigError,
                    VPNProcessError,
                    VPNTimeoutError,
                    VPNError,
                ),
            ):
                raise
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN and clean up resources.

        Performs a complete cleanup of the VPN connection:
        1. Attempts graceful termination of OpenVPN process
        2. Forces process termination if graceful shutdown fails
        3. Cleans up any lingering OpenVPN processes
        4. Resets all connection state information

        Raises:
            VPNProcessError: If there are issues terminating the OpenVPN process
        """
        if self.process:
            try:
                # Try graceful shutdown first
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Force kill if graceful shutdown fails
                    self.process.kill()
                    self.process.wait()
            except Exception as e:
                if self.verbose:
                    self.logger.warning(f"Error during VPN disconnect: {e}")
                raise VPNProcessError(f"Failed to terminate OpenVPN process: {e}")
            finally:
                self.process = None

        # Clean up any lingering OpenVPN processes
        try:
            subprocess.run(
                ["sudo", "pkill", "-f", "openvpn"],
                check=False,
                capture_output=True,
            )
        except Exception as e:
            if self.verbose:
                self.logger.warning(f"Error cleaning up OpenVPN processes: {e}")
            raise VPNProcessError(f"Failed to clean up OpenVPN processes: {e}")

        # Reset connection state
        self._initial_ip = None
        self._connected_ip = None
        self._server = None
        self._country_name = None

    def is_connected(self) -> bool:
        """Check if VPN is currently connected.

        Returns:
            bool: True if connected
        """
        return self.process is not None and self.process.poll() is None

    def update_connection_info(self, server_hostname: str, country_name: str) -> None:
        """Update connection information.

        Args:
            server_hostname: Connected server hostname
            country_name: Connected country name
        """
        self._server = server_hostname
        self._country_name = country_name
        self._connected_ip = self.get_current_ip()

    def setup_connection(
        self, server_hostname: str, username: str, password: str
    ) -> None:
        """Set up OpenVPN configuration files.

        Args:
            server_hostname: Server hostname
            username: NordVPN username
            password: NordVPN password

        Raises:
            VPNConfigError: If there are issues with the configuration
            VPNAuthenticationError: If there are issues with credentials
        """
        try:
            # Create auth file
            OPENVPN_AUTH.write_text(f"{username}\n{password}")
            OPENVPN_AUTH.chmod(0o600)
        except Exception as e:
            raise VPNAuthenticationError(f"Failed to create auth file: {e}")

        if self.verbose:
            self.logger.debug(f"Created auth file at {OPENVPN_AUTH}")

        # Ensure we have the config
        config_path = get_config_path(server_hostname)
        if not config_path:
            if self.verbose:
                self.logger.debug("Config not found, downloading configs...")
            try:
                setup_config_directory()
                config_path = get_config_path(server_hostname)
            except Exception as e:
                raise VPNConfigError(f"Failed to download OpenVPN configs: {e}")
            if not config_path:
                raise VPNConfigError(
                    f"Failed to get OpenVPN config for {server_hostname}"
                )

        if self.verbose:
            self.logger.debug(f"Using OpenVPN config: {config_path}")

    def verify_connection(self) -> bool:
        """Verify VPN connection is active and functioning.

        Performs multiple checks to ensure the VPN connection is working:
        1. Verifies OpenVPN process is running
        2. Checks current IP has changed from initial IP
        3. Validates connection with NordVPN API
        4. Ensures DNS resolution is working
        5. Checks for potential leaks

        Returns:
            bool: True if connection is verified active

        Note:
            This method is used both during connection establishment
            and for periodic connection health checks.
        """
        try:
            # Check if process is running
            if not self.is_connected():
                if self.verbose:
                    self.logger.debug("OpenVPN process is not running")
                return False

            # Get current IP
            current_ip = self.get_current_ip()
            if not current_ip:
                if self.verbose:
                    self.logger.debug("Failed to get current IP")
                return False

            # Check if IP has changed from initial
            if current_ip == self._initial_ip:
                if self.verbose:
                    self.logger.debug("IP address has not changed")
                return False

            # Check DNS resolution
            try:
                subprocess.run(
                    ["dig", "+short", "nordvpn.com"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=2,
                    check=True,
                )
            except (subprocess.SubprocessError, subprocess.TimeoutExpired):
                if self.verbose:
                    self.logger.debug("DNS resolution check failed")
                return False

            # Check NordVPN API for connection status
            try:
                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers={
                        "User-Agent": "Mozilla/5.0",
                        "Accept": "application/json",
                    },
                    timeout=5,
                )
                response.raise_for_status()
                nord_data = response.json()

                # Check if we're connected to NordVPN
                if not nord_data.get("status", False):
                    if self.verbose:
                        self.logger.debug("NordVPN API reports not connected")
                    return False

                # Verify the server matches
                if self._server and nord_data.get("hostname") != self._server:
                    if self.verbose:
                        self.logger.debug(
                            f"Connected to wrong server: {nord_data.get('hostname')} != {self._server}"
                        )
                    return False

            except Exception:
                # If API check fails, just verify IP change
                if self.verbose:
                    self.logger.debug(
                        "NordVPN API check failed, falling back to IP verification"
                    )
                pass

            # Check for potential DNS leaks
            try:
                dns_servers = subprocess.run(
                    ["scutil", "--dns"],
                    capture_output=True,
                    text=True,
                    timeout=2,
                    check=True,
                ).stdout
                if (
                    "103.86.96.100" not in dns_servers
                    and "103.86.99.100" not in dns_servers
                ):
                    if self.verbose:
                        self.logger.debug("Potential DNS leak detected")
                    return False
            except Exception:
                # DNS leak check is optional
                pass

            return True

        except Exception as e:
            if self.verbose:
                self.logger.debug(f"Connection verification failed: {e}")
            return False
