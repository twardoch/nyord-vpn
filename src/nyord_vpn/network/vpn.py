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
from loguru import logger
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
)
from nyord_vpn.network.vpn_commands import get_openvpn_command
from nyord_vpn.utils.utils import (
    OPENVPN_AUTH,
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
    - Public IP when not connected to VPN
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

        # IP caching
        self._cached_ip: str | None = None
        self._cached_ip_time: float = 0
        self._ip_cache_ttl: float = 3.0  # Cache IP for 3 seconds

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

        Note:
            Creates auth file with 0600 permissions for security.
            Validates credentials format before writing.

        """
        try:
            # Validate credentials
            if not username or not username.strip():
                raise VPNAuthenticationError("Username cannot be empty")
            if not password or not password.strip():
                raise VPNAuthenticationError("Password cannot be empty")

            # Ensure cache directory exists with secure permissions
            auth_dir = OPENVPN_AUTH.parent
            auth_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

            # Create auth file with credentials
            temp_auth = auth_dir / f".openvpn.auth.{os.getpid()}.tmp"
            try:
                # Write to temp file first
                temp_auth.write_text(f"{username.strip()}\n{password.strip()}")
                temp_auth.chmod(0o600)

                # Move temp file to final location (atomic operation)
                temp_auth.replace(OPENVPN_AUTH)

                if self.verbose:
                    self.logger.debug(f"Created auth file at {OPENVPN_AUTH}")

            except Exception as e:
                # Clean up temp file if it exists
                try:
                    if temp_auth.exists():
                        temp_auth.unlink()
                except Exception:
                    pass
                raise VPNAuthenticationError(f"Failed to create auth file: {e}")

            # Verify auth file permissions
            try:
                stat = OPENVPN_AUTH.stat()
                if stat.st_mode & 0o777 != 0o600:
                    OPENVPN_AUTH.chmod(0o600)
                    if self.verbose:
                        self.logger.debug("Fixed auth file permissions")
            except Exception as e:
                raise VPNAuthenticationError(
                    f"Failed to verify auth file permissions: {e}"
                )

        except Exception as e:
            if isinstance(e, VPNAuthenticationError):
                raise
            raise VPNAuthenticationError(str(e))

    def get_current_ip(self) -> str | None:
        """Get current IP address with basic verification.

        Uses two reliable services to verify the IP address:
        1. api.ipify.org (primary)
        2. ip-api.com (backup)

        Returns:
            Current public IP address or None if unavailable

        Note:
            Results are cached for 3 seconds to avoid excessive API calls.

        """
        # Check cache first
        now = time.time()
        if self._cached_ip and now - self._cached_ip_time < self._ip_cache_ttl:
            if self.verbose:
                self.logger.debug(f"Using cached IP {self._cached_ip}")
            return self._cached_ip

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
                        # Cache the result
                        self._cached_ip = ip
                        self._cached_ip_time = now
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
            # Cache the result
            self._cached_ip = most_common_ip
            self._cached_ip_time = now
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
                - Failed to disconnect existing connection

        Note:
            Will automatically disconnect any existing connection first.
            The authentication file should be at ~/.cache/nyord-vpn/openvpn.auth
            with username on first line and password on second line.

        """
        try:
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Invalid server info - missing hostname")

            # Check if we're already connected
            state = load_vpn_state()
            if state.get("connected"):
                if self.verbose:
                    self.logger.debug("Disconnecting existing VPN connection")
                try:
                    self.disconnect()
                    # Give the system a moment to clean up
                    time.sleep(0.5)
                except Exception as e:
                    # If disconnect fails, try to force cleanup
                    if self.verbose:
                        self.logger.warning(
                            f"Disconnect failed: {e}, attempting force cleanup"
                        )
                    try:
                        # Kill any existing OpenVPN processes
                        for proc in psutil.process_iter(["name", "pid"]):
                            if proc.info["name"] == "openvpn":
                                try:
                                    os.kill(proc.info["pid"], signal.SIGKILL)
                                    if self.verbose:
                                        self.logger.debug(
                                            f"Force killed OpenVPN process {proc.info['pid']}"
                                        )
                                except Exception:
                                    pass

                        # Reset instance state
                        self.process = None
                        self._server = None
                        self._country_name = None
                        self._connected_ip = None
                        self._invalidate_ip_cache()

                        # Reset state file
                        state = {
                            "connected": False,
                            "process_id": None,
                            "server": None,
                            "country": None,
                            "connected_ip": None,
                            "normal_ip": self._normal_ip,  # Keep Public IP
                            "timestamp": time.time(),
                        }
                        save_vpn_state(state)

                        # Extra delay after force cleanup
                        time.sleep(1.0)
                    except Exception as cleanup_error:
                        raise VPNError(
                            f"Failed to disconnect and cleanup: {cleanup_error}"
                        )

            # Store server info for new connection
            self._server = hostname
            self._country_name = server.get("country")

            # Ensure OpenVPN is available
            if not self.openvpn_path:
                self.openvpn_path = self.check_openvpn_installation()

            if self.verbose:
                self.logger.debug(f"Connecting to {hostname}")

            # Get OpenVPN config
            config_path = get_config_path(hostname)
            if not config_path:
                raise VPNConfigError(f"Failed to get OpenVPN config for {hostname}")

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

            try:
                self.process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,  # Line buffered
                )
            except subprocess.SubprocessError as e:
                self.logger.exception(f"Failed to start OpenVPN process: {e}")
                if self.verbose:
                    self.logger.exception(f"Command was: {' '.join(cmd)}")
                raise VPNProcessError(f"Failed to start OpenVPN process: {e}")

            # Monitor OpenVPN output for 30 seconds or until connection established
            start_time = time.time()
            connection_timeout = 30
            auth_failed = False
            tls_error = False

            while time.time() - start_time < connection_timeout:
                # Check if process died
                if self.process.poll() is not None:
                    stdout, stderr = self.process.communicate()
                    error_msg = (
                        f"OpenVPN process failed:\n"
                        f"Exit code: {self.process.returncode}\n"
                        f"Output: {stdout}\n"
                        f"Error: {stderr}"
                    )
                    self.logger.error(error_msg)
                    raise VPNProcessError(error_msg)

                # Check OpenVPN log for status
                if OPENVPN_LOG and OPENVPN_LOG.exists():
                    try:
                        log_content = OPENVPN_LOG.read_text()

                        # Check for successful connection
                        if "Initialization Sequence Completed" in log_content:
                            if self.verbose:
                                self.logger.debug("OpenVPN connection established")
                            break

                        # Check for authentication failure
                        if "AUTH_FAILED" in log_content and not auth_failed:
                            auth_failed = True
                            self.logger.error("OpenVPN authentication failed")
                            if self.verbose:
                                self.logger.error(f"OpenVPN log: {log_content}")
                                self.logger.error(
                                    "Please check your NordVPN credentials in the auth file:"
                                )
                                self.logger.error(f"  {OPENVPN_AUTH}")
                            raise VPNAuthenticationError(
                                "Authentication failed - check your credentials"
                            )

                        # Check for TLS error
                        if "TLS Error" in log_content and not tls_error:
                            tls_error = True
                            self.logger.error("OpenVPN TLS handshake failed")
                            if self.verbose:
                                self.logger.error(f"OpenVPN log: {log_content}")
                            raise VPNError("TLS handshake failed - server may be down")

                    except Exception as e:
                        self.logger.exception(f"Failed to read OpenVPN log: {e}")
                        if self.verbose:
                            self.logger.exception(f"Log path: {OPENVPN_LOG}")

                time.sleep(0.1)
            else:
                # Connection timed out
                self.logger.error("OpenVPN connection timed out")
                if self.verbose and OPENVPN_LOG and OPENVPN_LOG.exists():
                    try:
                        self.logger.error(f"OpenVPN log: {OPENVPN_LOG.read_text()}")
                        self.logger.error(f"Command was: {' '.join(cmd)}")
                    except Exception as e:
                        self.logger.exception(f"Failed to read OpenVPN log: {e}")

                # Try to clean up
                try:
                    if self.process:
                        self.process.terminate()
                        time.sleep(0.1)
                        if self.process.poll() is None:
                            self.process.kill()
                except Exception:
                    pass

                raise VPNError("Connection timed out after 30 seconds")

            # Verify connection is working
            if not self.verify_connection():
                # Try to clean up
                try:
                    if self.process:
                        self.process.terminate()
                        time.sleep(0.1)
                        if self.process.poll() is None:
                            self.process.kill()
                except Exception:
                    pass
                raise VPNError("VPN connection failed verification")

            # After process starts successfully
            if self.process and self.process.pid and self.verbose:
                self.logger.debug(
                    f"OpenVPN process started with PID {self.process.pid}"
                )

            # After successful connection, invalidate IP cache
            self._invalidate_ip_cache()

            # Update connection info and save state
            self._connected_ip = self.get_current_ip()
            self._save_state()

            if self.verbose:
                self.logger.info(
                    f"Connected to {hostname} ({self._country_name or 'Unknown country'})"
                )

        except Exception as e:
            # Clean up on any error
            try:
                if self.process:
                    self.process.terminate()
                    time.sleep(0.1)
                    if self.process.poll() is None:
                        self.process.kill()
            except Exception:
                pass

            # Reset state on error
            self.process = None
            self._server = None
            self._country_name = None
            self._connected_ip = None
            self._invalidate_ip_cache()

            # Re-raise appropriate error
            if isinstance(e, VPNError | VPNAuthenticationError | VPNConfigError):
                raise
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN and clean up.

        Performs a clean disconnection:
        1. Terminates OpenVPN process
        2. Updates connection state
        3. Records Public IP if needed
        4. Cleans up resources

        Note:
            Uses cached IP when possible and handles cleanup gracefully.

        """
        try:
            # Load state once
            state = load_vpn_state()

            # Only proceed with cleanup if we think we're connected
            if not state.get("connected"):
                if self.verbose:
                    self.logger.debug("Already disconnected")
                return

            # Try to terminate process
            process_id = state.get("process_id")
            if process_id:
                try:
                    os.kill(process_id, signal.SIGTERM)
                    if self.verbose:
                        self.logger.debug(f"Terminated OpenVPN process {process_id}")
                    # Give process a moment to terminate gracefully
                    time.sleep(0.1)
                except ProcessLookupError:
                    if self.verbose:
                        self.logger.debug(f"Process {process_id} already terminated")
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(
                            f"Failed to terminate process {process_id}: {e}"
                        )

                # Force kill if process is still running
                try:
                    if self._is_process_running(process_id):
                        os.kill(process_id, signal.SIGKILL)
                        if self.verbose:
                            self.logger.debug(
                                f"Force killed OpenVPN process {process_id}"
                            )
                except Exception:
                    pass  # Already logged warning above

            # Invalidate cache before getting current IP
            self._invalidate_ip_cache()

            # Get current IP (will use new IP after disconnect)
            current_ip = self.get_current_ip()

            # Update state with minimal writes
            new_state = {
                "connected": False,
                "process_id": None,
                "server": None,
                "country": None,
                "connected_ip": None,
                "current_ip": current_ip,
            }

            # Only update normal_ip if we don't have one or if it's changed
            if current_ip:
                if not state.get("normal_ip"):
                    new_state["normal_ip"] = current_ip
                elif state.get("normal_ip") != current_ip:
                    if self.verbose:
                        self.logger.debug(
                            f"Public IP changed: {state.get('normal_ip')} -> {current_ip}"
                        )
                    new_state["normal_ip"] = current_ip

            # Update instance state
            self.process = None
            self._server = None
            self._country_name = None
            self._connected_ip = None

            # Save state
            state.update(new_state)
            save_vpn_state(state)

            if self.verbose:
                self.logger.info(f"Disconnected from VPN. Public IP: {current_ip}")

        except Exception as e:
            if self.verbose:
                self.logger.exception(f"Error during disconnect: {e}")
            raise VPNError("Failed to disconnect from VPN") from e

    def is_connected(self) -> bool:
        """Check if OpenVPN process is running."""
        return self.process is not None and self.process.poll() is None

    def verify_connection(self) -> bool:
        """Verify VPN connection is active and functioning.

        Performs essential checks to verify the VPN connection:
        1. Verifies OpenVPN process is running
        2. Checks current IP has changed from Public IP
        3. Optional: Validates with NordVPN API

        Returns:
            bool: True if connection is verified active, False otherwise

        Note:
            Uses cached IP when possible and only performs
            essential checks needed for verification.

        """
        try:
            # Check if process is running (fastest check first)
            if not self.is_connected():
                if self.verbose:
                    self.logger.debug("OpenVPN process not running")
                return False

            # Get current IP (uses cache if available)
            current_ip = self.get_current_ip()
            if not current_ip:
                if self.verbose:
                    self.logger.debug("Could not determine current IP")
                return False

            # Check if IP has changed from Public IP
            if current_ip == self._normal_ip:
                if self.verbose:
                    self.logger.debug("Current IP matches Public IP")
                return False

            # Quick verification is good enough during connection
            # No need for additional API calls that might slow things down
            return True

        except Exception as e:
            if self.verbose:
                self.logger.debug(f"Connection verification failed: {e}")
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
            # Get current IP once and reuse it
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

            # Quick check if we're definitely not connected
            if self._normal_ip and current_ip == self._normal_ip:
                if self.verbose:
                    self.logger.debug("Current IP matches Public IP - not connected")
                return {
                    "connected": False,
                    "ip": current_ip,
                    "normal_ip": self._normal_ip,
                    "server": None,
                    "country": state.get("country", "Unknown"),
                    "city": state.get("city", "Unknown"),
                }

            # Check NordVPN API for connection status
            try:
                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers=API_HEADERS,
                    timeout=3,  # Reduced timeout since this is just for extra info
                )
                response.raise_for_status()
                nord_data = response.json()

                # Check all conditions:
                # 1. OpenVPN process is running
                # 2. Current IP matches our last known VPN IP
                # 3. Current IP is different from our Public IP
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

                # Get location info from API or state
                country = nord_data.get("country") or state.get("country")
                city = nord_data.get("city") or state.get("city")

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
        1. Checking if OpenVPN process is running (fastest check)
        2. Validating current IP differs from Public IP
        3. Updating state file if needed

        Returns:
            bool: True if connected to VPN, False otherwise

        Note:
            Uses cached IP when possible and minimizes state updates.

        """
        try:
            # Load state once
            state = load_vpn_state()

            # Check process first (fastest)
            process_id = state.get("process_id")
            if not process_id or not self._is_process_running(process_id):
                if self.verbose:
                    self.logger.debug("OpenVPN process not running")
                # Only disconnect if we think we're connected
                if state.get("connected"):
                    self.disconnect()
                return False

            # Get current IP (uses cache if available)
            current_ip = self.get_current_ip()
            if not current_ip:
                if self.verbose:
                    self.logger.warning("Could not determine current IP")
                return False

            # If we're not connected, just update Public IP if needed
            if not state.get("connected"):
                if current_ip != state.get("normal_ip"):
                    state["normal_ip"] = current_ip
                    save_vpn_state(state)
                return False

            # Compare current IP with Public IP
            normal_ip = state.get("normal_ip")
            if normal_ip == current_ip:
                if self.verbose:
                    self.logger.debug(
                        f"Current IP ({current_ip}) matches Public IP ({normal_ip})"
                    )
                self.disconnect()
                return False

            # Only update state if IP has changed
            if current_ip != state.get("connected_ip"):
                state["connected_ip"] = current_ip
                save_vpn_state(state)
                if self.verbose:
                    self.logger.debug(f"Updated connected IP to {current_ip}")

            if self.verbose:
                self.logger.debug(
                    f"Connection verified - Public IP: {normal_ip}, VPN IP: {current_ip}"
                )

            return True

        except Exception as e:
            if self.verbose:
                self.logger.exception(f"Error checking connection state: {e}")
            return False

    def _invalidate_ip_cache(self) -> None:
        """Invalidate the IP cache.

        Call this when we know the IP has changed (e.g. after connecting/disconnecting).
        """
        self._cached_ip = None
        self._cached_ip_time = 0
        if self.verbose:
            self.logger.debug("IP cache invalidated")
