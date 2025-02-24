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
            if not username or not isinstance(username, str):
                raise VPNAuthenticationError("Username must be a non-empty string")
            username = username.strip()
            if not username:
                raise VPNAuthenticationError("Username cannot be empty")

            if not password or not isinstance(password, str):
                raise VPNAuthenticationError("Password must be a non-empty string")
            password = password.strip()
            if not password:
                raise VPNAuthenticationError("Password cannot be empty")
            if len(password) < 8:
                raise VPNAuthenticationError("Password must be at least 8 characters")

            # Ensure cache directory exists with secure permissions
            auth_dir = OPENVPN_AUTH.parent
            auth_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

            # Create auth file with credentials
            temp_auth = auth_dir / f".openvpn.auth.{os.getpid()}.tmp"
            try:
                # Write to temp file first
                temp_auth.write_text(f"{username}\n{password}")
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
                raise VPNAuthenticationError(
                    f"Failed to create auth file: {e}. "
                    "Please check file permissions and disk space."
                )

            # Verify auth file permissions and contents
            try:
                stat = OPENVPN_AUTH.stat()
                if stat.st_mode & 0o777 != 0o600:
                    OPENVPN_AUTH.chmod(0o600)
                    if self.verbose:
                        self.logger.debug("Fixed auth file permissions")

                # Verify file contents
                lines = OPENVPN_AUTH.read_text().strip().split("\n")
                if len(lines) != 2:
                    raise VPNAuthenticationError(
                        "Auth file is corrupted - please run setup again"
                    )
                if lines[0].strip() != username or lines[1].strip() != password:
                    raise VPNAuthenticationError(
                        "Auth file contents don't match - please run setup again"
                    )

            except Exception as e:
                if isinstance(e, VPNAuthenticationError):
                    raise
                raise VPNAuthenticationError(
                    f"Failed to verify auth file: {e}. "
                    "Please check file permissions and try again."
                )

        except Exception as e:
            if isinstance(e, VPNAuthenticationError):
                raise
            raise VPNAuthenticationError(str(e))

    def get_current_ip(self) -> str | None:
        """Get current IP address with basic verification.

        Uses api.ipify.org as primary service with ip-api.com as backup.
        Results are cached for 30 seconds to avoid excessive API calls.

        Returns:
            Current public IP address or None if unavailable
        """
        # Check cache first
        now = time.time()
        if self._cached_ip and now - self._cached_ip_time < 30:  # 30s cache
            if self.verbose:
                self.logger.debug(f"Using cached IP {self._cached_ip}")
            return self._cached_ip

        def is_valid_ipv4(ip: str) -> bool:
            """Validate IPv4 address format."""
            try:
                parts = ip.strip().split(".")
                if len(parts) != 4:
                    return False
                return all(0 <= int(part) <= 255 for part in parts)
            except (AttributeError, TypeError, ValueError):
                return False

        # Try primary service first (up to 2 attempts)
        for attempt in range(2):
            try:
                if self.verbose:
                    self.logger.debug(f"Checking IP with api.ipify.org (attempt {attempt + 1})")
                response = requests.get("https://api.ipify.org?format=json", timeout=3)
                response.raise_for_status()
                data = response.json()
                ip = data.get("ip")
                if ip and is_valid_ipv4(ip):
                    if self.verbose:
                        self.logger.debug(f"Got valid IP {ip} from api.ipify.org")
                    self._cached_ip = ip
                    self._cached_ip_time = now
                    return ip
            except Exception as e:
                if self.verbose:
                    self.logger.debug(f"Primary IP check failed (attempt {attempt + 1}): {e}")
                if attempt < 1:  # Only sleep between attempts
                    time.sleep(0.5)

        # Try backup service (up to 2 attempts)
        for attempt in range(2):
            try:
                if self.verbose:
                    self.logger.debug(f"Checking IP with ip-api.com (attempt {attempt + 1})")
                response = requests.get("http://ip-api.com/json", timeout=3)
                response.raise_for_status()
                data = response.json()
                ip = data.get("query")
                if ip and is_valid_ipv4(ip):
                    if self.verbose:
                        self.logger.debug(f"Got valid IP {ip} from ip-api.com")
                    self._cached_ip = ip
                    self._cached_ip_time = now
                    return ip
            except Exception as e:
                if self.verbose:
                    self.logger.debug(f"Backup IP check failed (attempt {attempt + 1}): {e}")
                if attempt < 1:  # Only sleep between attempts
                    time.sleep(0.5)

        # Try one last service as final fallback
        try:
            if self.verbose:
                self.logger.debug("Checking IP with ifconfig.me (final attempt)")
            response = requests.get("https://ifconfig.me/ip", timeout=3)
            response.raise_for_status()
            ip = response.text.strip()
            if ip and is_valid_ipv4(ip):
                if self.verbose:
                    self.logger.debug(f"Got valid IP {ip} from ifconfig.me")
                self._cached_ip = ip
                self._cached_ip_time = now
                return ip
        except Exception as e:
            if self.verbose:
                self.logger.debug(f"Final IP check failed: {e}")

        if self.verbose:
            self.logger.warning("Failed to get current IP from any service")
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
        """
        try:
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Invalid server info - missing hostname")

            # Force cleanup of any existing connection
            try:
                self.disconnect()
                time.sleep(1)  # Give system time to clean up
            except Exception as e:
                if self.verbose:
                    self.logger.warning(f"Error during disconnect: {e}, attempting force cleanup")
                
                # Kill any existing OpenVPN processes
                for proc in psutil.process_iter(["name", "pid"]):
                    try:
                        if proc.info["name"] == "openvpn":
                            os.kill(proc.info["pid"], signal.SIGKILL)
                            if self.verbose:
                                self.logger.debug(f"Force killed OpenVPN process {proc.info['pid']}")
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
                time.sleep(1)  # Extra delay after force cleanup

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

            # Clear any existing log file
            if OPENVPN_LOG and OPENVPN_LOG.exists():
                try:
                    OPENVPN_LOG.unlink()
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(f"Failed to clear old log file: {e}")

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

            # Update connection info and save state
            state = {
                "connected": True,
                "process_id": self.process.pid if self.process else None,
                "server": self._server,
                "country": self._country_name,
                "timestamp": time.time(),
            }
            save_vpn_state(state)

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
        3. Cleans up resources
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

            # Update instance state
            self.process = None
            self._server = None
            self._country_name = None
            self._connected_ip = None

            # Save minimal state
            state = {
                "connected": False,
                "process_id": None,
                "server": None,
                "country": None,
                "connected_ip": None,
                "timestamp": time.time(),
            }
            save_vpn_state(state)

            if self.verbose:
                self.logger.info("Disconnected from VPN")

        except Exception as e:
            if self.verbose:
                self.logger.exception(f"Error during disconnect: {e}")
            raise VPNError("Failed to disconnect from VPN") from e

    def is_connected(self) -> bool:
        """Check if OpenVPN process is running."""
        return self.process is not None and self.process.poll() is None

    def verify_connection(self) -> bool:
        """Verify VPN connection is active and functioning.

        Verifies the OpenVPN process is running and has completed initialization.
        Checks OpenVPN logs for successful connection status.

        Returns:
            bool: True if connection is verified active, False otherwise
        """
        try:
            # Check if process is running
            if not self.is_connected():
                if self.verbose:
                    self.logger.debug("OpenVPN process not running")
                return False

            # Check OpenVPN log for connection status
            if OPENVPN_LOG and OPENVPN_LOG.exists():
                try:
                    log_content = OPENVPN_LOG.read_text()
                    if "Initialization Sequence Completed" in log_content:
                        if self.verbose:
                            self.logger.debug("OpenVPN connection verified")
                        return True
                    
                    # Check for specific failure conditions
                    if "AUTH_FAILED" in log_content:
                        raise VPNAuthenticationError("Authentication failed - check your credentials")
                    if "TLS Error" in log_content:
                        raise VPNError("TLS handshake failed - server may be down")
                        
                except Exception as e:
                    if self.verbose:
                        self.logger.debug(f"Failed to read OpenVPN log: {e}")
                    return False

            return False

        except Exception as e:
            if self.verbose:
                self.logger.debug(f"Connection verification failed: {e}")
            if isinstance(e, (VPNError, VPNAuthenticationError)):
                raise
            return False

    def status(self) -> dict[str, Any]:
        """Get current VPN connection status.

        Returns:
            dict with:
                connected (bool): True if connected to VPN
                server (str): Connected server hostname
                country (dict): Country info with code and name
                city (str): Server city location

        Raises:
            VPNError: If status check fails
        """
        try:
            # Load state once
            state = load_vpn_state()

            # Check process first (fastest)
            process_running = False
            process_id = state.get("process_id")
            if process_id:
                process_running = self._is_process_running(process_id)

            # Check OpenVPN log for connection status
            is_connected = False
            if process_running and OPENVPN_LOG and OPENVPN_LOG.exists():
                try:
                    log_content = OPENVPN_LOG.read_text()
                    is_connected = "Initialization Sequence Completed" in log_content
                except Exception as e:
                    if self.verbose:
                        self.logger.debug(f"Failed to read OpenVPN log: {e}")

            if self.verbose:
                self.logger.debug(
                    f"Connection status: process={process_running}, "
                    f"initialized={is_connected}"
                )

            return {
                "connected": is_connected,
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

        Verifies the VPN connection by checking if OpenVPN process is running
        and has completed initialization.

        Returns:
            bool: True if connected to VPN, False otherwise
        """
        try:
            # Load state once
            state = load_vpn_state()

            # Check process first
            process_id = state.get("process_id")
            if not process_id or not self._is_process_running(process_id):
                if self.verbose:
                    self.logger.debug("OpenVPN process not running")
                # Only disconnect if we think we're connected
                if state.get("connected"):
                    self.disconnect()
                return False

            # Check OpenVPN log for connection status
            if OPENVPN_LOG and OPENVPN_LOG.exists():
                try:
                    log_content = OPENVPN_LOG.read_text()
                    if "Initialization Sequence Completed" in log_content:
                        if self.verbose:
                            self.logger.debug("OpenVPN connection verified")
                        return True
                except Exception as e:
                    if self.verbose:
                        self.logger.debug(f"Failed to read OpenVPN log: {e}")

            return False

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
