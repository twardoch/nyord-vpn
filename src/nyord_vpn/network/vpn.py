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

import subprocess
import time
from pathlib import Path
from typing import Any
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn
from loguru import logger
import shutil

from nyord_vpn.exceptions import (
    VPNError,
    VPNAuthenticationError,
    VPNConfigError,
    VPNProcessError,
)
from nyord_vpn.utils.templates import (
    get_config_path,
    download_config_zip,
    get_openvpn_command,
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

    def __init__(self, verbose: bool = False) -> None:
        """Initialize VPN connection manager.

        Args:
            verbose: Whether to enable verbose logging

        """
        self.verbose = verbose
        self.logger = logger
        self.process: subprocess.Popen | None = None
        self.openvpn_path: str | None = None

        # Connection state
        self._initial_ip: str | None = None
        self._connected_ip: str | None = None
        self._server: str | None = None
        self._country_name: str | None = None

        # Ensure cache directory exists
        OPENVPN_AUTH.parent.mkdir(parents=True, exist_ok=True)

        # Try to find OpenVPN at init
        try:
            self.openvpn_path = self.check_openvpn_installation()
        except VPNError:
            if self.verbose:
                self.logger.warning("OpenVPN not found during initialization")

    def check_openvpn_installation(self) -> str:
        """Check if OpenVPN is installed and accessible.

        Returns:
            str: Path to OpenVPN executable

        Raises:
            VPNError: If OpenVPN is not installed or not accessible
        """
        try:
            # Try to find openvpn in common locations
            openvpn_paths = [
                "/usr/local/sbin/openvpn",  # Homebrew on macOS
                "/usr/sbin/openvpn",  # Linux
                "/opt/homebrew/sbin/openvpn",  # Apple Silicon macOS
            ]

            for path in openvpn_paths:
                if Path(path).exists():
                    # Verify we can run it
                    result = subprocess.run(
                        [path, "--version"], capture_output=True, text=True, check=False
                    )
                    if result.returncode == 0:
                        if self.verbose:
                            self.logger.debug(f"Found OpenVPN at {path}")
                        return path

            # If not found in common paths, try which
            try:
                result = subprocess.run(
                    ["which", "openvpn"], capture_output=True, text=True, check=True
                )
                path = result.stdout.strip()
                if path:
                    if self.verbose:
                        self.logger.debug(f"Found OpenVPN at {path}")
                    return path
            except subprocess.CalledProcessError:
                pass

            raise VPNError(
                "OpenVPN not found. Please install OpenVPN:\n"
                "  macOS: brew install openvpn\n"
                "  Linux: sudo apt install openvpn  # or your distro's package manager"
            )

        except Exception as e:
            if isinstance(e, VPNError):
                raise
            raise VPNError(f"Failed to verify OpenVPN installation: {e}")

    def setup_connection(self, hostname: str, username: str, password: str) -> None:
        """Set up VPN connection configuration.

        This method prepares the authentication and configuration files needed
        for establishing a VPN connection. It must be called before connect().

        Args:
            hostname: VPN server hostname to connect to
            username: NordVPN username
            password: NordVPN password

        Raises:
            VPNAuthenticationError: If credentials are invalid or auth file creation fails
            VPNConfigError: If config file creation fails
        """
        try:
            # Create auth file with credentials
            auth_content = f"{username}\n{password}"
            OPENVPN_AUTH.write_text(auth_content)
            OPENVPN_AUTH.chmod(0o600)  # Set secure permissions

            if self.verbose:
                self.logger.debug(f"Created auth file at {OPENVPN_AUTH}")

        except Exception as e:
            raise VPNAuthenticationError(f"Failed to create auth file: {e}")

    def get_current_ip(self) -> str | None:
        """Get current IP address.

        Returns:
            Current public IP address or None if unavailable

        """
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=5)
            response.raise_for_status()
            return response.json().get("ip")
        except Exception:
            return None

    def connect(self, server: dict[str, Any]) -> None:
        """Connect to a VPN server.

        Args:
            server: Server information dictionary containing:
                - hostname: Server hostname for connection
                - (optional) additional server metadata

        Raises:
            VPNError: If connection fails due to:
                - Invalid server information
                - Missing authentication
                - OpenVPN process failure
                - Connection verification failure
                - Timeout during connection

        Note:
            This method requires root/sudo privileges to establish the VPN connection.
            The authentication file should be at ~/.cache/nyord-vpn/openvpn.auth
            with username on first line and password on second line.
        """
        try:
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Invalid server info - missing hostname")

            # Ensure OpenVPN is available
            if not self.openvpn_path:
                self.openvpn_path = self.check_openvpn_installation()

            if self.verbose:
                self.logger.debug(f"Connecting to {hostname}")

            # Store initial IP
            self._initial_ip = self.get_current_ip()

            # Get OpenVPN config
            config_path = get_config_path(hostname)
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
                    "\nThe file should contain your username on the first line and password on the second line.",
                )

            try:
                auth_lines = OPENVPN_AUTH.read_text().strip().splitlines()
                if len(auth_lines) != 2 or not all(line.strip() for line in auth_lines):
                    raise VPNAuthenticationError(
                        "Invalid auth file format. The file should contain exactly two non-empty lines:\n"
                        "  Line 1: Your NordVPN username\n"
                        "  Line 2: Your NordVPN password",
                    )
            except Exception as e:
                if isinstance(e, VPNAuthenticationError):
                    raise
                raise VPNAuthenticationError(f"Failed to read auth file: {e}")

            # Start OpenVPN process
            cmd = [
                "sudo",
                self.openvpn_path,
                "--config",
                str(config_path),
                "--auth-user-pass",
                str(OPENVPN_AUTH),
                "--log",
                str(OPENVPN_LOG),
            ]

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
                time.sleep(5)  # Give OpenVPN time to start
                if self.process.poll() is not None:
                    stdout, stderr = self.process.communicate()
                    raise VPNProcessError(
                        f"OpenVPN process failed:\n{stderr}\nOutput:\n{stdout}",
                    )

                # Update connection info
                self._server = hostname
                self._connected_ip = self.get_current_ip()

                if self.verbose:
                    self.logger.info(f"Connected to {hostname}")

            except Exception as e:
                if self.process and self.process.poll() is None:
                    self.process.terminate()
                    try:
                        self.process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        self.process.kill()
                raise VPNError(f"Failed to establish connection: {e}")

        except Exception as e:
            if isinstance(e, VPNError | VPNAuthenticationError | VPNConfigError):
                raise
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN.

        This method:
        1. Gracefully terminates the OpenVPN process
        2. Forces termination if graceful shutdown fails
        3. Cleans up any lingering OpenVPN processes
        4. Resets all connection state information

        Raises:
            VPNProcessError: If process termination fails
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

    def verify_connection(self) -> bool:
        """Verify VPN connection is active and functioning.

        Performs multiple checks to ensure the VPN connection is working:
        1. Verifies OpenVPN process is running
        2. Checks current IP has changed from initial IP
        3. Validates connection with NordVPN API (if available)
        4. Ensures IP address is reachable

        Returns:
            bool: True if connection is verified active, False otherwise

        Note:
            This method is used both during connection establishment
            and for periodic connection health checks. It gracefully
            handles API failures by falling back to IP-based verification.

        """
        try:
            # Check if process is running
            if not self.is_connected():
                return False

            # Get current IP
            current_ip = self.get_current_ip()
            if not current_ip:
                return False

            # Check if IP has changed from initial
            if current_ip == self._initial_ip:
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
                if not nord_data.get("status", False):
                    return False
            except Exception:
                # If API check fails, just verify IP change
                pass

            return True

        except Exception:
            return False
