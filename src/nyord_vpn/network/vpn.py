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
import os
import signal

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
        """Get current IP address with basic verification.

        Uses two reliable services to verify the IP address:
        1. api.ipify.org (primary)
        2. ip-api.com (backup)

        Returns:
            Current public IP address or None if unavailable
        """
        urls = [
            "https://api.ipify.org?format=json",  # Most reliable, fastest
            "http://ip-api.com/json",  # Good backup with location info
        ]

        def is_valid_ipv4(ip: str) -> bool:
            """Validate IPv4 address format."""
            try:
                parts = ip.strip().split(".")
                if len(parts) != 4:
                    return False
                return all(0 <= int(part) <= 255 for part in parts)
            except (AttributeError, TypeError, ValueError):
                return False

        # Track IP addresses seen
        ip_counts: dict[str, int] = {}

        # Try each service once with a short timeout
        for url in urls:
            try:
                if self.verbose:
                    self.logger.debug(f"Checking IP with {url}")

                response = requests.get(url, timeout=3)
                response.raise_for_status()

                # Handle different API response formats
                if url.endswith("json"):
                    try:
                        data = response.json()
                        ip = data.get("ip") or data.get("query")
                    except requests.exceptions.JSONDecodeError:
                        continue
                else:
                    ip = response.text.strip()

                # Validate and count IP
                if ip and is_valid_ipv4(ip):
                    if self.verbose:
                        self.logger.debug(f"Got valid IP {ip} from {url}")
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1

                    # Return immediately if both services agree
                    if ip_counts[ip] >= 2:
                        if self.verbose:
                            self.logger.debug(
                                f"IP {ip} confirmed by {ip_counts[ip]} services"
                            )
                        return ip

            except Exception as e:
                if self.verbose:
                    self.logger.debug(f"Failed to get IP from {url}: {e}")
                continue

        # If we got at least one valid IP, use it
        if ip_counts:
            most_common_ip = max(ip_counts.items(), key=lambda x: x[1])[0]
            if self.verbose:
                self.logger.debug(
                    f"Using IP {most_common_ip} (seen {ip_counts[most_common_ip]} times)"
                )
            return most_common_ip

        if self.verbose:
            self.logger.warning("Failed to get current IP")
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
            "process_id": self.process.pid if self.process else None,
            "timestamp": time.time(),
        }
        save_vpn_state(state)
        if self.verbose:
            self.logger.debug(
                f"Saved state: connected={state['connected']}, "
                f"server={state['server']}, country={state['country']}"
            )

    def connect(self, server: dict[str, Any]) -> None:
        """Connect to a VPN server.

        Args:
            server: Server information dictionary containing:
                - hostname: Server hostname for connection
                - country: Server country name
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

            # Store server info
            self._server = hostname
            self._country_name = server.get("country")

            # Store initial IP if not set
            if not self._normal_ip:
                self._normal_ip = self.get_current_ip()
                self._save_state()

            # Ensure OpenVPN is available
            if not self.openvpn_path:
                self.openvpn_path = self.check_openvpn_installation()

            if self.verbose:
                self.logger.debug(f"Connecting to {hostname}")

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
                self.logger.debug("Running OpenVPN command:")
                self.logger.debug(" ".join(cmd))
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
                        stdout=subprocess.PIPE,  # Always capture output for error handling
                        stderr=subprocess.PIPE,  # Always capture errors
                        text=True,
                        bufsize=1,  # Line buffered
                    )
                except subprocess.SubprocessError as e:
                    self.logger.error(f"Failed to start OpenVPN process: {e}")
                    if self.verbose:
                        self.logger.error(f"Command was: {' '.join(cmd)}")
                        self.logger.error(f"Error: {e}")
                    raise VPNProcessError(f"Failed to start OpenVPN process: {e}")

                # Monitor OpenVPN output for 30 seconds or until connection established
                start_time = time.time()
                while time.time() - start_time < 30:
                    if self.process.poll() is not None:
                        stdout, stderr = self.process.communicate()
                        error_msg = (
                            f"OpenVPN process failed:\n"
                            f"Command: {' '.join(cmd)}\n"
                            f"Exit code: {self.process.returncode}\n"
                            f"Output: {stdout}\n"
                            f"Error: {stderr}"
                        )
                        self.logger.error(error_msg)
                        raise VPNProcessError(error_msg)

                    # Always read output for logging
                    if self.process.stdout:
                        while True:
                            line = self.process.stdout.readline()
                            if not line:
                                break
                            line = line.strip()
                            if line:
                                if self.verbose:
                                    self.logger.debug(f"OpenVPN: {line}")
                                # Check for critical errors in output
                                if "ERROR:" in line:
                                    self.logger.error(f"OpenVPN error: {line}")
                                    if "Cannot resolve host address" in line:
                                        raise VPNError(
                                            f"Failed to resolve server: {line}"
                                        )
                                    if "TLS key negotiation failed" in line:
                                        raise VPNError(
                                            "Failed to establish secure connection"
                                        )

                    # Check if connection is established
                    if OPENVPN_LOG and OPENVPN_LOG.exists():
                        try:
                            log_content = OPENVPN_LOG.read_text()
                            if "Initialization Sequence Completed" in log_content:
                                self.logger.info("OpenVPN connection established")
                                break
                            if "AUTH_FAILED" in log_content:
                                self.logger.error("OpenVPN authentication failed")
                                if self.verbose:
                                    self.logger.error(f"OpenVPN log: {log_content}")
                                    self.logger.error(
                                        "Please check your NordVPN credentials in the auth file:"
                                    )
                                    self.logger.error(f"  {OPENVPN_AUTH}")
                                    self.logger.error("The file should contain:")
                                    self.logger.error("  Line 1: Your NordVPN username")
                                    self.logger.error("  Line 2: Your NordVPN password")
                                raise VPNAuthenticationError(
                                    "Authentication failed - check your credentials"
                                )
                            if "TLS Error" in log_content:
                                self.logger.error("OpenVPN TLS handshake failed")
                                if self.verbose:
                                    self.logger.error(f"OpenVPN log: {log_content}")
                                raise VPNError(
                                    "TLS handshake failed - server may be down"
                                )
                        except Exception as e:
                            self.logger.error(f"Failed to read OpenVPN log: {e}")
                            if self.verbose:
                                self.logger.error(f"Log path: {OPENVPN_LOG}")

                    time.sleep(0.1)

                else:
                    self.logger.error("OpenVPN connection timed out")
                    if self.verbose and OPENVPN_LOG and OPENVPN_LOG.exists():
                        try:
                            self.logger.error(f"OpenVPN log: {OPENVPN_LOG.read_text()}")
                            self.logger.error(f"Command was: {' '.join(cmd)}")
                        except Exception as e:
                            self.logger.error(f"Failed to read OpenVPN log: {e}")
                    raise VPNError("Connection timed out after 30 seconds")

            # Verify connection is working
            if not self.verify_connection():
                raise VPNError("VPN connection failed verification")

            # After process starts successfully
            if self.process and self.process.pid:
                if self.verbose:
                    self.logger.debug(
                        f"OpenVPN process started with PID {self.process.pid}"
                    )

            # Update connection info and save state
            self._connected_ip = self.get_current_ip()
            self._save_state()

            if self.verbose:
                self.logger.info(
                    f"Connected to {hostname} ({self._country_name or 'Unknown country'})"
                )

        except Exception as e:
            if isinstance(e, (VPNError, VPNAuthenticationError, VPNConfigError)):
                raise
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN and clean up.

        Performs a clean disconnection:
        1. Terminates OpenVPN process
        2. Updates connection state
        3. Records normal IP
        4. Cleans up resources
        """
        try:
            state = load_vpn_state()
            process_id = state.get("process_id")

            if process_id:
                try:
                    os.kill(process_id, signal.SIGTERM)
                    if self.verbose:
                        self.logger.debug(f"Terminated OpenVPN process {process_id}")
                except ProcessLookupError:
                    if self.verbose:
                        self.logger.debug(f"Process {process_id} already terminated")
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(
                            f"Failed to terminate process {process_id}: {e}"
                        )

            # Get current IP for accurate state
            current_ip = self.get_current_ip()

            # Update state
            state.update(
                {
                    "connected": False,
                    "process_id": None,
                    "server": None,
                    "country": None,
                    "connected_ip": None,
                    "current_ip": current_ip,
                }
            )

            # If we have a current IP and no normal_ip, update it
            if current_ip and not state.get("normal_ip"):
                state["normal_ip"] = current_ip

            save_vpn_state(state)

            if self.verbose:
                self.logger.info(
                    f"Disconnected from VPN. Normal IP: {state.get('normal_ip')}"
                )

        except Exception as e:
            if self.verbose:
                self.logger.error(f"Error during disconnect: {e}")
            raise VPNError("Failed to disconnect from VPN") from e

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
                - city (str): Connected city if known
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
                    "city": None,
                }

            # Load state
            state = load_vpn_state()
            stored_pid = state.get("process_id")

            # Check if our specific OpenVPN process is running
            process_running = False
            if stored_pid:
                process_running = self._is_process_running(stored_pid)
                if self.verbose and not process_running:
                    self.logger.debug(
                        f"Stored OpenVPN process {stored_pid} not running"
                    )

            # Fallback to checking for any OpenVPN process
            if not process_running:
                for proc in psutil.process_iter(["name", "pid"]):
                    if proc.info["name"] == "openvpn":
                        process_running = True
                        if self.verbose:
                            self.logger.debug(
                                f"Found OpenVPN process {proc.info['pid']}"
                            )
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

                # Determine connection status
                if self._normal_ip and current_ip == self._normal_ip:
                    is_connected = False
                    if self.verbose:
                        self.logger.debug(
                            "Current IP matches normal IP - not connected"
                        )
                else:
                    # Check all conditions:
                    # 1. OpenVPN process is running
                    # 2. Current IP matches our last known VPN IP
                    # 3. Current IP is different from our normal IP
                    # 4. The IP is recognized by NordVPN
                    is_connected = (
                        process_running
                        and current_ip == state.get("connected_ip")
                        and (not self._normal_ip or current_ip != self._normal_ip)
                        and nord_data.get("status", False)
                    )
                    if self.verbose:
                        self.logger.debug(
                            f"Connection status: process={process_running}, "
                            f"ip_match={current_ip == state.get('connected_ip')}, "
                            f"ip_changed={not self._normal_ip or current_ip != self._normal_ip}, "
                            f"nord_status={nord_data.get('status', False)}"
                        )

                if is_connected:
                    # Update state to ensure it's fresh
                    self._connected_ip = current_ip
                    self._save_state()

                # Get location info
                country = nord_data.get("country")
                city = nord_data.get("city")

                # If API doesn't provide location, use stored values
                if not country:
                    country = state.get("country")
                    if self.verbose and country:
                        self.logger.debug(f"Using stored country: {country}")
                if not city:
                    city = state.get("city", "Unknown")
                    if self.verbose and city != "Unknown":
                        self.logger.debug(f"Using stored city: {city}")

                return {
                    "connected": is_connected,
                    "ip": current_ip,
                    "normal_ip": self._normal_ip,
                    "country": country or "Unknown",
                    "city": city or "Unknown",
                    "server": state.get("server"),
                }

            except requests.RequestException as e:
                if self.verbose:
                    self.logger.debug(f"NordVPN API check failed: {e}")

                # If API check fails, use process and IP check
                if self._normal_ip and current_ip == self._normal_ip:
                    is_connected = False
                else:
                    is_connected = (
                        process_running
                        and current_ip == state.get("connected_ip")
                        and (not self._normal_ip or current_ip != self._normal_ip)
                    )

                return {
                    "connected": is_connected,
                    "ip": current_ip,
                    "normal_ip": self._normal_ip,
                    "country": state.get("country", "Unknown"),
                    "city": state.get("city", "Unknown"),
                    "server": state.get("server"),
                }

        except Exception as e:
            raise VPNError(f"Failed to get status: {e}")

    def _is_process_running(self, process_id: int) -> bool:
        """Check if a process is running by its PID.

        Args:
            process_id: Process ID to check

        Returns:
            bool: True if running, False if not
        """
        try:
            os.kill(process_id, 0)
            return True
        except OSError:
            return False
        except Exception as e:
            if self.verbose:
                self.logger.debug(f"Error checking process {process_id}: {e}")
            return False

    def check_connection_state(self) -> bool:
        """Check current VPN connection state.

        Verifies the VPN connection by:
        1. Checking if OpenVPN process is running
        2. Validating current IP differs from normal IP
        3. Ensuring connection is established
        4. Updating state file with accurate IPs

        Returns:
            bool: True if connected to VPN, False otherwise
        """
        try:
            state = load_vpn_state()
            current_ip = self.get_current_ip()

            if not current_ip:
                if self.verbose:
                    self.logger.warning("Could not determine current IP")
                return False

            # If we're not connected, update the normal IP
            if not state.get("connected"):
                state["normal_ip"] = current_ip
                save_vpn_state(state)
                return False

            # Check if OpenVPN process is running
            process_id = state.get("process_id")
            if not process_id or not self._is_process_running(process_id):
                if self.verbose:
                    self.logger.debug("OpenVPN process not running")
                self.disconnect()
                return False

            # Compare current IP with normal IP
            normal_ip = state.get("normal_ip")
            if normal_ip == current_ip:
                if self.verbose:
                    self.logger.debug(
                        f"Current IP ({current_ip}) matches normal IP ({normal_ip})"
                    )
                self.disconnect()
                return False

            # Update state with current IP
            state["connected_ip"] = current_ip
            save_vpn_state(state)

            if self.verbose:
                self.logger.debug(
                    f"Connection verified - Normal IP: {normal_ip}, VPN IP: {current_ip}"
                )

            return True

        except Exception as e:
            if self.verbose:
                self.logger.error(f"Error checking connection state: {e}")
            return False
