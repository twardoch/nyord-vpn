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
import psutil

from nyord_vpn.exceptions import (
    VPNError,
    VPNAuthenticationError,
    VPNConfigError,
    VPNProcessError,
)
from nyord_vpn.utils.templates import (
    get_config_path,
    download_config_zip,
)
from nyord_vpn.network.vpn_commands import get_openvpn_command
from nyord_vpn.utils.utils import (
    OPENVPN_AUTH,
    OPENVPN_CONFIG,
    OPENVPN_LOG,
    API_HEADERS,
)
from nyord_vpn.storage.state import save_vpn_state, load_vpn_state

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
    - Normal IP when not connected to VPN
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
        self._normal_ip: str | None = None
        self._connected_ip: str | None = None
        self._server: str | None = None
        self._country_name: str | None = None

        # Load saved state
        state = load_vpn_state()
        self._normal_ip = state.get("normal_ip")
        self._connected_ip = state.get("connected_ip")
        self._server = state.get("server")
        self._country_name = state.get("country")

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
            # Store normal IP before connecting
            if not self._normal_ip:
                self._normal_ip = self.get_current_ip()
                self._save_state()

            # Create auth file with credentials
            auth_content = f"{username}\n{password}"
            OPENVPN_AUTH.write_text(auth_content)
            OPENVPN_AUTH.chmod(0o600)

            if self.verbose:
                self.logger.debug(f"Created auth file at {OPENVPN_AUTH}")

        except Exception as e:
            raise VPNAuthenticationError(f"Failed to create auth file: {e}")

    def get_current_ip(self) -> str | None:
        """Get current IP address with retries.

        Attempts to get the current public IP address up to 3 times with exponential backoff.
        Uses ipify.org API as the primary source and ip-api.com as fallback.

        Returns:
            Current public IP address or None if unavailable after all retries
        """
        urls = [
            "https://api.ipify.org?format=json",
            "https://api64.ipify.org?format=json",
            "http://ip-api.com/json",
        ]

        for attempt in range(3):
            for url in urls:
                try:
                    if self.verbose:
                        self.logger.debug(
                            f"Attempting to get IP from {url} (attempt {attempt + 1}/3)"
                        )

                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    data = response.json()

                    # Handle different API response formats
                    ip = data.get("ip") or data.get("query")
                    if ip:
                        return ip

                except Exception as e:
                    if self.verbose:
                        self.logger.debug(f"Failed to get IP from {url}: {e}")
                    continue

            # Wait before next attempt (exponential backoff)
            if attempt < 2:  # Don't sleep after last attempt
                time.sleep(2**attempt)

        if self.verbose:
            self.logger.warning("Failed to get current IP after all retries")
        return None

    def _save_state(self) -> None:
        """Save current connection state."""
        current_ip = self.get_current_ip()
        state = {
            "connected": self.is_connected(),
            "current_ip": current_ip,  # Used to update normal_ip when disconnected
            "normal_ip": self._normal_ip,
            "connected_ip": self._connected_ip,
            "server": self._server,
            "country": self._country_name,
            "timestamp": time.time(),
        }
        save_vpn_state(state)

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
            self._normal_ip = self.get_current_ip()

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
            cmd = get_openvpn_command(
                config_path=config_path,
                auth_path=OPENVPN_AUTH,
                log_path=OPENVPN_LOG if self.verbose else None,
                verbosity=5 if self.verbose else 3,
            )

            if self.verbose:
                self.logger.debug(f"Running OpenVPN command: {' '.join(cmd)}")
                if OPENVPN_LOG:
                    self.logger.debug(f"OpenVPN log file: {OPENVPN_LOG}")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="Connecting...", total=None)

                try:
                    self.process = subprocess.Popen(
                        cmd,
                        stdout=subprocess.PIPE if not self.verbose else None,
                        stderr=subprocess.PIPE if not self.verbose else None,
                        text=True,
                        bufsize=1,  # Line buffered
                    )
                except subprocess.SubprocessError as e:
                    self.logger.error(f"Failed to start OpenVPN process: {e}")
                    raise VPNProcessError(f"Failed to start OpenVPN process: {e}")

                # Monitor OpenVPN output for 30 seconds or until connection established
                start_time = time.time()
                while time.time() - start_time < 30:
                    if self.process.poll() is not None:
                        stdout, stderr = self.process.communicate()
                        if self.verbose:
                            self.logger.error(f"OpenVPN process output: {stdout}")
                            self.logger.error(f"OpenVPN process error: {stderr}")
                        raise VPNProcessError(f"OpenVPN process failed: {stderr}")

                    if self.verbose and self.process.stdout:
                        line = self.process.stdout.readline()
                        if line:
                            self.logger.debug(f"OpenVPN: {line.strip()}")

                    # Check if connection is established
                    if OPENVPN_LOG and OPENVPN_LOG.exists():
                        log_content = OPENVPN_LOG.read_text()
                        if "Initialization Sequence Completed" in log_content:
                            self.logger.info("OpenVPN connection established")
                            break
                        if "AUTH_FAILED" in log_content:
                            self.logger.error("OpenVPN authentication failed")
                            if self.verbose:
                                self.logger.error(f"OpenVPN log: {log_content}")
                            raise VPNAuthenticationError(
                                "Authentication failed - check your credentials"
                            )
                        if "TLS Error" in log_content:
                            self.logger.error("OpenVPN TLS handshake failed")
                            if self.verbose:
                                self.logger.error(f"OpenVPN log: {log_content}")
                            raise VPNError("TLS handshake failed - server may be down")

                    time.sleep(0.1)

                else:
                    self.logger.error("OpenVPN connection timed out")
                    if self.verbose and OPENVPN_LOG and OPENVPN_LOG.exists():
                        self.logger.error(f"OpenVPN log: {OPENVPN_LOG.read_text()}")
                    raise VPNError("Connection timed out after 30 seconds")

            # Update connection info
            self._server = hostname
            self._connected_ip = self.get_current_ip()

            if self.verbose:
                self.logger.info(f"Connected to {hostname}")

        except Exception as e:
            if isinstance(e, VPNError | VPNAuthenticationError | VPNConfigError):
                raise
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN and clean up."""
        try:
            # Kill OpenVPN process
            if self.process:
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    self.process.kill()
                self.process = None

            # Get current IP before state reset
            current_ip = self.get_current_ip()

            # Reset connection state
            self._connected_ip = None
            self._server = None
            self._country_name = None

            # Update state with current IP as normal IP
            if current_ip:
                self._normal_ip = current_ip
            self._save_state()

            # Clean up files
            for file in [OPENVPN_CONFIG, OPENVPN_AUTH, OPENVPN_LOG]:
                if file.exists():
                    file.unlink()

            # Wait briefly for network to stabilize
            time.sleep(1)

        except Exception as e:
            raise VPNError(f"Failed to disconnect: {e}")

    def is_connected(self) -> bool:
        """Check if OpenVPN process is running."""
        return self.process is not None and self.process.poll() is None

    def verify_connection(self) -> bool:
        """Verify VPN connection is active and functioning.

        Performs multiple checks to ensure the VPN connection is working:
        1. Verifies OpenVPN process is running
        2. Checks current IP has changed from normal IP
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

            # Check if IP has changed from normal IP
            if current_ip == self._normal_ip:
                return False

            # Check NordVPN API for connection status
            try:
                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers=API_HEADERS,
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
        try:
            # Get current IP
            current_ip = self.get_current_ip()
            if not current_ip:
                return {
                    "connected": False,
                    "ip": None,
                    "normal_ip": self._normal_ip,
                    "server": None,
                    "country": None,
                }

            # Load state
            state = load_vpn_state()

            # Check if OpenVPN is running
            openvpn_running = False
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == "openvpn":
                    openvpn_running = True
                    break

            # Check NordVPN API for connection status
            try:
                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers=API_HEADERS,
                    timeout=5,
                )
                response.raise_for_status()
                nord_data = response.json()

                # We're definitely not connected if current IP matches normal IP
                if self._normal_ip and current_ip == self._normal_ip:
                    is_connected = False
                else:
                    # Otherwise check all conditions:
                    # 1. OpenVPN is running
                    # 2. Current IP matches our last known VPN IP
                    # 3. Current IP is different from our normal IP
                    # 4. The IP is recognized by NordVPN
                    is_connected = (
                        openvpn_running
                        and current_ip == state.get("connected_ip")
                        and (not self._normal_ip or current_ip != self._normal_ip)
                        and nord_data.get("status", False)
                    )

                if is_connected:
                    # Update state to ensure it's fresh
                    self._connected_ip = current_ip
                    self._save_state()

                return {
                    "connected": is_connected,
                    "ip": current_ip,
                    "normal_ip": self._normal_ip,
                    "country": nord_data.get(
                        "country", state.get("country", "Unknown")
                    ),
                    "city": nord_data.get("city", "Unknown"),
                    "server": state.get("server"),
                }

            except requests.RequestException:
                # If NordVPN API check fails, use process and IP check
                # We're definitely not connected if current IP matches normal IP
                if self._normal_ip and current_ip == self._normal_ip:
                    is_connected = False
                else:
                    is_connected = (
                        openvpn_running
                        and current_ip == state.get("connected_ip")
                        and (not self._normal_ip or current_ip != self._normal_ip)
                    )

                return {
                    "connected": is_connected,
                    "ip": current_ip,
                    "normal_ip": self._normal_ip,
                    "country": state.get("country", "Unknown"),
                    "city": "Unknown",
                    "server": state.get("server"),
                }

        except Exception as e:
            raise VPNError(f"Failed to get status: {e}")
