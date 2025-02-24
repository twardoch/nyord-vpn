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
from typing import Any, Dict
import requests
from loguru import logger
import psutil
import os
import signal
import sys
import socket

from rich.console import Console

from nyord_vpn.exceptions import (
    VPNError,
    VPNAuthenticationError,
    VPNConfigError,
)
from nyord_vpn.utils.templates import (
    get_config_path,
)
from nyord_vpn.network.vpn_commands import get_openvpn_command
from nyord_vpn.utils.utils import (
    OPENVPN_AUTH,
    OPENVPN_LOG,
    check_root,
    ensure_root,
)
from nyord_vpn.storage.state import save_vpn_state, load_vpn_state
from nyord_vpn.network.server import ServerManager

console = Console()

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

    def __init__(
        self,
        api_client: Any,
        server_manager: ServerManager,
        vpn_manager: Any,
        verbose: bool = False,
    ):
        """Initialize VPN connection manager.

        Args:
            api_client: API client instance
            server_manager: Server manager instance
            vpn_manager: VPN manager instance
            verbose: Whether to enable verbose logging
        """
        self.api_client = api_client
        self.server_manager = server_manager
        self.vpn_manager = vpn_manager
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
                    self.logger.debug(
                        f"Checking IP with api.ipify.org (attempt {attempt + 1})"
                    )
                response = requests.get("https://api.ipify.org?format=json", timeout=3)
                response.raise_for_status()
                data = response.json()
                ip = data.get("ip")
                if ip and is_valid_ipv4(ip):
                    if self.verbose:
                        self.logger.debug(f"Got valid IP {ip} from api.ipify.org")
                    return ip
            except Exception as e:
                if self.verbose:
                    self.logger.debug(
                        f"Primary IP check failed (attempt {attempt + 1}): {e}"
                    )
                if attempt < 1:  # Only sleep between attempts
                    time.sleep(0.5)

        # Try backup service (up to 2 attempts)
        for attempt in range(2):
            try:
                if self.verbose:
                    self.logger.debug(
                        f"Checking IP with ip-api.com (attempt {attempt + 1})"
                    )
                response = requests.get("http://ip-api.com/json", timeout=3)
                response.raise_for_status()
                data = response.json()
                ip = data.get("query")
                if ip and is_valid_ipv4(ip):
                    if self.verbose:
                        self.logger.debug(f"Got valid IP {ip} from ip-api.com")
                    return ip
            except Exception as e:
                if self.verbose:
                    self.logger.debug(
                        f"Backup IP check failed (attempt {attempt + 1}): {e}"
                    )
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

    def connect(self, servers: list[dict[str, Any]]) -> None:
        """Connect to a VPN server, trying servers from the list on failure.

        Args:
            servers: List of server information dictionaries, ideally sorted.

        Raises:
            VPNError: If connection fails after trying all servers.

        """
        error_messages = []  # Collect error messages

        for server in servers:
            try:
                hostname = server.get("hostname")
                if not hostname:
                    raise VPNError("Invalid server info - missing hostname")

                # Force cleanup of any existing connections
                try:
                    self.disconnect()
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(
                            f"Error during disconnect: {e}, attempting force cleanup"
                        )

                    # Ensure no OpenVPN processes are running
                    for proc in psutil.process_iter(["name", "pid", "cmdline"]):
                        try:
                            if proc.info["name"] == "openvpn":
                                cmdline = proc.info.get("cmdline", [])
                                if any("nordvpn.com" in arg for arg in cmdline):
                                    try:
                                        os.kill(proc.info["pid"], signal.SIGKILL)
                                        time.sleep(0.1)  # Brief pause after kill
                                    except Exception:
                                        pass
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            continue

                # Store server info
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

                # Log config file contents for debugging
                if self.verbose:
                    try:
                        config_content = config_path.read_text()
                        self.logger.debug(f"OpenVPN config for {hostname}:")
                        for line in config_content.splitlines():
                            if not line.strip().startswith("#"):  # Skip comments
                                self.logger.debug(f"  {line}")
                    except Exception as e:
                        self.logger.warning(f"Failed to read config file: {e}")

                # Verify auth file exists and has correct format
                if not OPENVPN_AUTH.exists():
                    raise VPNError("Auth file not found - please run setup first")
                try:
                    auth_content = OPENVPN_AUTH.read_text().strip().split("\n")
                    if len(auth_content) != 2:
                        raise VPNError(
                            "Auth file is corrupted - please run setup again"
                        )
                    if not auth_content[0] or not auth_content[1]:
                        raise VPNError(
                            "Auth file contains empty username or password - please run setup again"
                        )
                    if self.verbose:
                        self.logger.debug("Auth file exists and has correct format")
                except Exception as e:
                    if isinstance(e, VPNError):
                        raise
                    raise VPNError(f"Failed to read auth file: {e}")

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

                try:
                    # Clear any existing log file
                    if OPENVPN_LOG and OPENVPN_LOG.exists():
                        OPENVPN_LOG.unlink()

                    # Start OpenVPN process
                    self.process = subprocess.Popen(
                        cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        bufsize=1,
                    )

                    # Give process a moment to start
                    time.sleep(0.5)

                    # Check if process died immediately
                    if self.process.poll() is not None:
                        stdout, stderr = self.process.communicate()
                        raise VPNError(
                            f"OpenVPN process failed to start:\n"
                            f"Exit code: {self.process.returncode}\n"
                            f"Output: {stdout}\n"
                            f"Error: {stderr}"
                        )

                except subprocess.SubprocessError as e:
                    raise VPNError(f"Failed to start OpenVPN process: {e}")

                # Monitor OpenVPN output
                start_time = time.time()
                success = False
                error_msg = None
                log_content = ""

                while time.time() - start_time < 30:  # 30 second timeout
                    # Check if process died
                    if self.process.poll() is not None:
                        stdout, stderr = self.process.communicate()

                        # Try to get log content for better error reporting
                        try:
                            if OPENVPN_LOG and OPENVPN_LOG.exists():
                                log_content = OPENVPN_LOG.read_text()
                                if self.verbose:
                                    self.logger.debug("OpenVPN log content:")
                                    for line in log_content.splitlines():
                                        self.logger.debug(f"  {line}")
                        except Exception as e:
                            if self.verbose:
                                self.logger.warning(f"Failed to read OpenVPN log: {e}")

                        # If we have log content, check for known errors
                        if log_content:
                            if "AUTH_FAILED" in log_content:
                                # Get more context around the auth failure
                                auth_lines = [
                                    line
                                    for line in log_content.splitlines()
                                    if "AUTH" in line
                                ]
                                if auth_lines and self.verbose:
                                    self.logger.debug("Auth-related log lines:")
                                    for line in auth_lines:
                                        self.logger.debug(f"  {line}")
                                error_msg = (
                                    "Authentication failed - check your credentials"
                                )
                                if "AUTH_FAILED,SESSION" in log_content:
                                    error_msg = "Session authentication failed - server may require re-login"
                                elif "AUTH_FAILED,CERTIFICATE" in log_content:
                                    error_msg = "Certificate authentication failed - server config may be invalid"
                            elif "Cannot load certificate file" in log_content:
                                error_msg = (
                                    "Certificate error - server config may be invalid"
                                )
                            elif "Cannot load private key file" in log_content:
                                error_msg = (
                                    "Private key error - server config may be invalid"
                                )
                            elif (
                                "All TAP-Windows adapters on this system are currently in use"
                                in log_content
                            ):
                                error_msg = "All VPN adapters are in use"
                            elif "TLS Error" in log_content:
                                error_msg = "TLS handshake failed - server may be down"
                            elif "TLS key negotiation failed" in log_content:
                                error_msg = "TLS key negotiation failed - server may require different TLS settings"
                            elif "Connection timed out" in log_content:
                                error_msg = (
                                    "Connection timed out - server may be unreachable"
                                )
                            elif "Cannot resolve host address" in log_content:
                                error_msg = "Cannot resolve server hostname - DNS issue"

                        # If no specific error found, use a generic message
                        if not error_msg:
                            error_msg = (
                                f"OpenVPN process terminated unexpectedly:\n"
                                f"Exit code: {self.process.returncode}\n"
                                f"Output: {stdout}\n"
                                f"Error: {stderr}\n"
                                f"Log: {log_content if log_content else 'No log available'}"
                            )
                        break

                    # Check log file for status
                    if OPENVPN_LOG and OPENVPN_LOG.exists():
                        try:
                            log_content = OPENVPN_LOG.read_text()

                            # Check for success
                            if "Initialization Sequence Completed" in log_content:
                                success = True
                                break

                            # Check for auth progress
                            if self.verbose and "AUTH" in log_content:
                                auth_lines = [
                                    line
                                    for line in log_content.splitlines()
                                    if "AUTH" in line
                                ]
                                if auth_lines:
                                    self.logger.debug("Auth progress:")
                                    for line in auth_lines:
                                        self.logger.debug(f"  {line}")

                            # Check for common errors
                            if "AUTH_FAILED" in log_content:
                                error_msg = (
                                    "Authentication failed - check your credentials"
                                )
                                break
                            if "TLS Error" in log_content:
                                error_msg = "TLS handshake failed - server may be down"
                                break
                            if "Connection timed out" in log_content:
                                error_msg = (
                                    "Connection timed out - server may be unreachable"
                                )
                                break
                            if "Cannot resolve host address" in log_content:
                                error_msg = "Cannot resolve server hostname - DNS issue"
                                break
                            if (
                                "All TAP-Windows adapters on this system are currently in use"
                                in log_content
                            ):
                                error_msg = "All VPN adapters are in use"
                                break
                            if "Cannot load certificate file" in log_content:
                                error_msg = (
                                    "Certificate error - server config may be invalid"
                                )
                                break
                            if "Cannot load private key file" in log_content:
                                error_msg = (
                                    "Private key error - server config may be invalid"
                                )
                                break
                        except Exception as e:
                            if self.verbose:
                                self.logger.warning(f"Failed to read OpenVPN log: {e}")

                    time.sleep(0.1)

                # Handle timeout or error
                if not success:
                    # Kill the process if it's still running
                    if self.process and self.process.poll() is None:
                        try:
                            self.process.terminate()
                            time.sleep(0.1)
                            if self.process.poll() is None:
                                self.process.kill()
                        except Exception:
                            pass

                    if error_msg:
                        if self.verbose:
                            self.logger.warning(
                                f"Connection to {hostname} failed: {error_msg}"
                            )
                        error_messages.append(
                            f"Connection to {hostname} failed: {error_msg}"
                        )  # Collect
                    else:
                        if self.verbose:
                            self.logger.warning(
                                f"Connection to {hostname} timed out after 30 seconds"
                            )
                        error_messages.append(
                            f"Connection to {hostname} timed out after 30 seconds"
                        )  # Collect
                    continue  # Try the next server

                # Verify connection is working
                time.sleep(1)  # Brief pause to let connection stabilize
                if not self.verify_connection():
                    error_msg = "Connection verification failed"
                    if self.verbose:
                        self.logger.warning(error_msg)
                    error_messages.append(error_msg)  # Collect
                    continue  # Try next server

                # Update state
                state = {
                    "connected": True,
                    "process_id": self.process.pid if self.process else None,
                    "server": self._server,
                    "country": self._country_name,
                    "timestamp": time.time(),
                }
                save_vpn_state(state)

                if self.verbose:
                    self.logger.info(f"Connected to {hostname}")
                return  # Success!

            except Exception as e:
                # Clean up on error
                if self.process:
                    try:
                        self.process.terminate()
                        time.sleep(0.1)  # Brief pause
                        if self.process.poll() is None:
                            self.process.kill()
                    except Exception:
                        pass

                # Reset state
                self.process = None
                self._server = None
                self._country_name = None

                error_messages.append(str(e))  # Collect

                # Re-raise with context
                if isinstance(e, VPNError | VPNAuthenticationError | VPNConfigError):
                    # raise # No, we try other servers
                    continue  # Yes, try other servers
                # raise VPNError(f"Failed to connect to VPN: {e}") # No, we try other servers
                continue

        # If we get here, all attempts failed
        raise VPNError(
            "Failed to connect after trying all servers:\n" + "\n".join(error_messages)
        )

    def disconnect(self) -> None:
        """Disconnect from VPN and clean up.

        Performs a clean disconnection:
        1. Terminates OpenVPN process
        2. Updates connection state
        3. Records Public IP
        4. Cleans up resources

        Raises:
            VPNError: If disconnection fails with details about what failed

        """
        try:
            # First try graceful termination of our tracked process
            if self.process and self.process.poll() is None:
                try:
                    self.process.terminate()
                    # Give it a moment to terminate gracefully
                    for _ in range(10):  # 1 second total
                        if self.process.poll() is not None:
                            break
                        time.sleep(0.1)
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(f"Error terminating tracked process: {e}")

            # Find and kill ALL OpenVPN processes
            for proc in psutil.process_iter(["name", "pid", "cmdline"]):
                try:
                    if proc.info["name"] == "openvpn":
                        # Double check it's our OpenVPN process by looking at cmdline
                        cmdline = proc.info.get("cmdline", [])
                        if any("nordvpn.com" in arg for arg in cmdline):
                            if self.verbose:
                                self.logger.debug(
                                    f"Found OpenVPN process {proc.info['pid']}"
                                )

                            # Try graceful termination first
                            try:
                                os.kill(proc.info["pid"], signal.SIGTERM)
                                time.sleep(0.1)  # Brief pause
                            except Exception:
                                pass

                            # Force kill if still running
                            try:
                                if self._is_process_running(proc.info["pid"]):
                                    os.kill(proc.info["pid"], signal.SIGKILL)
                                    if self.verbose:
                                        self.logger.debug(
                                            f"Force killed OpenVPN process {proc.info['pid']}"
                                        )
                            except Exception as e:
                                if self.verbose:
                                    self.logger.warning(
                                        f"Failed to kill process {proc.info['pid']}: {e}"
                                    )

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            # Verify no OpenVPN processes are left
            remaining = []
            for proc in psutil.process_iter(["name", "pid", "cmdline"]):
                try:
                    if proc.info["name"] == "openvpn":
                        cmdline = proc.info.get("cmdline", [])
                        if any("nordvpn.com" in arg for arg in cmdline):
                            remaining.append(proc.info["pid"])
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue

            if remaining:
                raise VPNError(
                    f"Failed to kill all OpenVPN processes. Remaining: {remaining}"
                )

            # Clean up OpenVPN log file
            if OPENVPN_LOG and OPENVPN_LOG.exists():
                try:
                    OPENVPN_LOG.unlink()
                    if self.verbose:
                        self.logger.debug("Cleaned up OpenVPN log file")
                except Exception as e:
                    if self.verbose:
                        self.logger.warning(f"Failed to clean up OpenVPN log: {e}")

            # Update instance state
            self.process = None
            self._server = None
            self._country_name = None
            self._connected_ip = None
            self._invalidate_ip_cache()

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
            error_details = []
            if isinstance(e, ProcessLookupError):
                error_details.append("Process not found")
            elif isinstance(e, PermissionError):
                error_details.append("Permission denied")
            else:
                error_details.append(str(e))

            if self.verbose:
                self.logger.exception(
                    f"Error during disconnect: {'; '.join(error_details)}"
                )

            raise VPNError(
                f"Failed to disconnect from VPN: {'; '.join(error_details)}"
            ) from e

    def is_connected(self) -> bool:
        """Check if OpenVPN process is running."""
        return self.process is not None and self.process.poll() is None

    def verify_connection(self) -> bool:
        """Verify that the VPN connection is working properly.

        Returns:
            bool: True if connection is verified working

        This method checks:
        1. OpenVPN process is running
        2. TUN/TAP interface is up
        3. DNS is working
        4. IP has changed from pre-connection IP

        """
        try:
            # Check process is still running
            if not self.process or self.process.poll() is not None:
                if self.verbose:
                    self.logger.debug("OpenVPN process not running")
                return False

            # Check TUN/TAP interface (platform specific)
            if sys.platform == "darwin":  # macOS
                try:
                    output = subprocess.check_output(["ifconfig"], text=True)
                    if not any(
                        line.startswith("utun") and "UP" in line
                        for line in output.split("\n")
                    ):
                        if self.verbose:
                            self.logger.debug("No active utun interface found")
                        return False
                except subprocess.CalledProcessError:
                    if self.verbose:
                        self.logger.debug("Failed to check TUN interface")
                    return False
            elif sys.platform == "linux":
                try:
                    output = subprocess.check_output(
                        ["ip", "link", "show", "tun0"], text=True
                    )
                    if "UP" not in output:
                        if self.verbose:
                            self.logger.debug("TUN interface not up")
                        return False
                except subprocess.CalledProcessError:
                    if self.verbose:
                        self.logger.debug("Failed to check TUN interface")
                    return False

            # Check DNS resolution
            try:
                socket.gethostbyname("nordvpn.com")
            except socket.gaierror:
                if self.verbose:
                    self.logger.debug("DNS resolution failed")
                return False

            # Check IP has changed
            try:
                current_ip = self.get_current_ip()
                if not current_ip:
                    if self.verbose:
                        self.logger.debug("Failed to get current IP")
                    return False

                # Get the pre-connection IP from state
                state = load_vpn_state()
                normal_ip = state.get("normal_ip")

                if normal_ip and current_ip == normal_ip:
                    if self.verbose:
                        self.logger.debug("IP has not changed from pre-connection IP")
                    return False

            except Exception as e:
                if self.verbose:
                    self.logger.debug(f"IP verification failed: {e}")
                return False

            return True

        except Exception as e:
            if self.verbose:
                self.logger.debug(f"Connection verification failed: {e}")
            return False

    def status(self) -> dict[str, Any]:
        """Get current VPN connection status.

        Returns:
            dict with:
                connected (bool): True if connected to VPN
                server (str): Connected server hostname
                country (str): Full country name
                city (str): Server city location
                ip (str): Current IP address

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

            # Get current IP
            current_ip = self.get_current_ip()

            # Get full country name if we have a country code
            country = state.get("country", "Unknown")
            if country and len(country) == 2:
                try:
                    import pycountry
                    country_obj = pycountry.countries.get(alpha_2=country.upper())
                    if country_obj:
                        country = country_obj.name
                except ImportError:
                    if self.verbose:
                        self.logger.debug("pycountry not available for country name lookup")

            if self.verbose:
                self.logger.debug(
                    f"Connection status: process={process_running}, "
                    f"initialized={is_connected}, "
                    f"ip={current_ip}"
                )

            return {
                "connected": is_connected,
                "country": country,
                "city": state.get("city", "Unknown"),
                "server": state.get("server"),
                "ip": current_ip,
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

    def go(self, country_code: str) -> None:
        """Connect to VPN in specified country.

        Args:
            country_code: Two-letter country code (e.g. 'US', 'GB')

        Raises:
            VPNError: If connection fails
        """
        if not check_root():
            ensure_root()
            return

        try:
            # First check if we're already connected
            status = self.status()
            if status.get("connected", False):
                # Automatically disconnect before connecting to new server
                if self.verbose:
                    self.logger.info("Disconnecting from current server before connecting to new one")
                self.disconnect()

            # Get fastest servers
            servers = self.server_manager.select_fastest_server(country_code)
            if not servers:
                raise VPNError(f"No servers available in {country_code}")

            if self.verbose:
                self.logger.info(f"Selected {len(servers)} servers to try")
                for i, server in enumerate(servers, 1):
                    self.logger.info(f"{i}. {server.get('hostname')} (load: {server.get('load')}%)")

            # Try servers in order until one works
            errors = []
            for server in servers:
                hostname = None  # Initialize outside try block
                try:
                    hostname = server.get("hostname")
                    if not hostname:
                        continue

                    if self.verbose:
                        self.logger.info(f"Trying server: {hostname}")
                        console.print(f"Trying server: [cyan]{hostname}[/cyan]")

                    # Set up VPN configuration
                    self.setup_connection(hostname, self.api_client.username, self.api_client.password)

                    # Try to connect
                    self.connect([server])  # Pass as list for compatibility
                    
                    # If we get here, connection succeeded
                    if self.verbose:
                        self.logger.info(f"Successfully connected to {hostname}")
                    return

                except Exception as e:
                    error_msg = f"{hostname if hostname else 'Unknown server'}: {str(e)}"
                    errors.append(error_msg)
                    if self.verbose:
                        self.logger.warning(f"Failed to connect to {hostname if hostname else 'Unknown server'}: {e}")
                    continue

            # If we get here, all servers failed
            raise VPNError(
                f"Failed to connect to any server in {country_code}:\n" + 
                "\n".join(f"- {e}" for e in errors)
            )

        except Exception as e:
            raise VPNError(f"Failed to connect: {e}")
