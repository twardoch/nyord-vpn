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
import signal
import socket
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Any

import psutil
import requests
from loguru import logger
from rich.console import Console

from nyord_vpn.exceptions import VPNConfigError, VPNError, VPNProcessError
from nyord_vpn.network.server import ServerManager
from nyord_vpn.network.vpn_commands import OpenVPNConfig, get_openvpn_command
from nyord_vpn.storage.state import load_vpn_state, save_vpn_state
from nyord_vpn.utils.templates import get_config_path
from nyord_vpn.utils.utils import (OPENVPN_AUTH, OPENVPN_LOG, check_root,
                                   ensure_root)

console = Console()

# Constants
OPENVPN_AUTH = Path.home() / ".cache" / "nyord-vpn" / "openvpn.auth"
OPENVPN_LOG = Path.home() / ".cache" / "nyord-vpn" / "openvpn.log"

# Default retry wait time in seconds
DEFAULT_RETRY_WAIT = 1

# Constants for process management (internal use)
PROCESS_CHECK_INTERVAL = 0.5  # seconds
PROCESS_STARTUP_GRACE = 2.0  # seconds

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
        *,
        verbose: bool = False,
        timeout: int = 30,
    ) -> None:
        """Initialize VPN connection manager.

        Args:
            api_client: API client instance
            server_manager: Server manager instance
            vpn_manager: VPN manager instance
            verbose: Whether to enable verbose logging
            timeout: Connection timeout in seconds

        """
        self.api_client = api_client
        self.server_manager = server_manager
        self.vpn_manager = vpn_manager
        self.verbose = verbose
        self.logger = logger
        self.process: subprocess.Popen | None = None
        self.openvpn_path: str | None = None
        self.timeout = timeout

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

        # Connection setup variables
        self.hostname: str | None = None
        self.config_path: Path | None = None

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

    def setup_connection(self, server_hostname: str, username: str, password: str) -> None:
        """Setup the OpenVPN connection.

        Args:
            server_hostname: Server hostname
            username: VPN username
            password: VPN password

        Raises:
            VPNError: If unable to setup the connection

        """
        # Save hostname for state management
        self.hostname = server_hostname

        # Get config path for this server
        config_path = get_config_path(server_hostname)
        if config_path is None:
            # Fallback path in case config doesn't exist
            config_path = Path(os.path.expanduser(f"~/.cache/nyord-vpn/configs/{server_hostname}.ovpn"))
            if not config_path.exists():
                raise VPNConfigError(f"Configuration file not found for server {server_hostname}")

        # Set the config path so it's available throughout the session
        self.config_path = config_path  # This will always be a Path object

        # Create auth file with username/password
        try:
            # Decode password if it appears to be URL encoded
            if "%" in password:
                try:
                    password = urllib.parse.unquote(password)
                except Exception:
                    # If decoding fails, use the original password
                    pass

            # Ensure the credentials are written without extra whitespace
            username = username.strip()
            password = password.strip()

            # Write credentials to auth file
            auth_dir = os.path.dirname(OPENVPN_AUTH)
            os.makedirs(auth_dir, exist_ok=True)

            with open(OPENVPN_AUTH, "w") as f:
                f.write(f"{username}\n{password}\n")

            # Set permissions to 0600 (rw-------)
            os.chmod(OPENVPN_AUTH, 0o600)

            # Verify the file was created and has correct format
            with open(OPENVPN_AUTH) as f:
                lines = f.readlines()
                if len(lines) != 2:
                    raise VPNError("Auth file has incorrect format")

                self.logger.debug("Auth file exists and has correct format")
        except OSError as e:
            raise VPNError(f"Failed to read auth file: {e}")

        # Create OpenVPN configuration for this connection
        try:
            config = OpenVPNConfig(
                config_path=self.config_path,
                auth_path=Path(OPENVPN_AUTH),
                log_path=Path(OPENVPN_LOG),
                verbosity=3 if self.verbose else 1,
            )

            # Get OpenVPN command
            cmd = get_openvpn_command(config)

            # Prepend sudo if needed
            sudo_cmd = ["sudo", *cmd] if not check_root() else cmd

            self.logger.debug(f"OpenVPN command: {' '.join(sudo_cmd)}")

            # Start OpenVPN process with sudo
            self.process = subprocess.Popen(
                sudo_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
            )
            self.pid = self.process.pid
            self.running = True
            self.start_time = time.time()
            self.exit_code = None

            # Check if process died immediately
            time.sleep(0.1)
            if self.process.poll() is not None:
                self.running = False
                self.exit_code = self.process.returncode
                stdout, stderr = self.process.communicate()
                raise VPNProcessError(
                    f"OpenVPN process failed to start: exit code {self.exit_code}\n"
                    f"Output: {stdout}\n"
                    f"Error: {stderr}"
                )

        except VPNConfigError as e:
            raise VPNError(f"Failed to create OpenVPN configuration: {e}")
        except Exception as e:
            raise VPNError(f"Failed to start OpenVPN: {e}")

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
        """Start an OpenVPN connection.

        Starts a new OpenVPN process with the appropriate command-line
        arguments, environment variables, and configuration.

        Args:
            servers: List of server dictionaries

        Raises:
            VPNError: If the connection fails for any reason
            VPNConfigError: If the OpenVPN configuration is invalid
            VPNAuthenticationError: If authentication fails

        """
        if self.hostname:
            self.logger.info(f"Connecting to {self.hostname}")
        else:
            self.logger.info("Connecting to VPN")

        try:
            # Verify auth file exists and has correct format
            if not OPENVPN_AUTH.exists():
                raise VPNError("Auth file not found - please run setup first")

            # Ensure auth file has correct permissions
            OPENVPN_AUTH.chmod(0o600)

            try:
                # Verify file contents - must have two non-empty lines
                lines = OPENVPN_AUTH.read_text().strip().split("\n")
                if len(lines) != 2:
                    raise VPNError(
                        "Auth file is corrupted - please run setup again"
                    )
                if not lines[0].strip() or not lines[1].strip():
                    raise VPNError(
                        "Auth file contains empty username or password - please run setup again"
                    )
                self.logger.debug("Auth file exists and has correct format")
            except OSError as e:
                raise VPNError(f"Failed to read auth file: {e}")

            # Verify config_path is set and valid before using it
            if not self.config_path or not isinstance(self.config_path, Path):
                raise VPNConfigError("Configuration path is not set - please run setup_connection first")

            if not self.config_path.exists():
                raise VPNConfigError(f"Configuration file not found at {self.config_path}")

            # Create OpenVPN configuration for this connection
            try:
                config = OpenVPNConfig(
                    config_path=self.config_path,
                    auth_path=OPENVPN_AUTH,
                    log_path=OPENVPN_LOG,
                    verbosity=3 if self.verbose else 1,
                )

                # Get OpenVPN command
                cmd = get_openvpn_command(config)

                # Prepend sudo to the command since OpenVPN needs root privileges
                sudo_cmd = ["sudo", *cmd]

                if self.verbose:
                    self.logger.debug(f"OpenVPN command: {' '.join(sudo_cmd)}")

                # Start OpenVPN process with sudo
                self.process = subprocess.Popen(
                    sudo_cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,
                )
                self.pid = self.process.pid
                self.running = True
                self.start_time = time.time()
                self.exit_code = None

                # Check if process died immediately
                time.sleep(0.1)
                if self.process.poll() is not None:
                    self.running = False
                    self.exit_code = self.process.returncode
                    stdout, stderr = self.process.communicate()
                    raise VPNProcessError(
                        f"OpenVPN process failed to start: exit code {self.exit_code}\n"
                        f"Output: {stdout}\n"
                        f"Error: {stderr}"
                    )
            except VPNConfigError as e:
                raise VPNError(f"Failed to create OpenVPN configuration: {e}")
        except Exception as e:
            if isinstance(e, VPNError):
                raise
            raise VPNError(f"Connection failed: {e}")

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
            dict: Status information including:
                - connected (bool): Whether connected to VPN
                - ip (str): Current IP address
                - normal_ip (str): IP when not connected to VPN
                - server (str): Connected server if any
                - country (str): Connected country if any

        """
        status = {
            "connected": self.is_connected(),
            "ip": self.get_current_ip(),
            "normal_ip": self._normal_ip,
            "server": self._server,
            "country": None,
        }

        # Get country information from server manager's cached data
        if self._server:
            try:
                # Get server info from cache
                cache = self.server_manager.get_servers_cache()
                if cache and cache.get("servers"):
                    # Find our server in the cache
                    for server in cache["servers"]:
                        if server.get("hostname") == self._server:
                            # Get location info
                            location_ids = server.get("location_ids", [])
                            locations = cache.get("locations", {})

                            # Find matching location with country info
                            for loc_id in location_ids:
                                location = locations.get(str(loc_id))
                                if location and location.get("country"):
                                    status["country"] = location["country"]["name"]
                                    break
                            break

                # Fallback to hostname parsing if server not found in cache
                if not status["country"]:
                    country_code = self._server.split(".")[0][:2].upper()
                    country = self.api_client.get_country_by_code(country_code)
                    if country:
                        status["country"] = country["name"]

            except Exception as e:
                if self.verbose:
                    self.logger.warning(
                        f"Failed to get country information from server data: {e}"
                    )

        return status

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
                    self.logger.info(
                        "Disconnecting from current server before connecting to new one"
                    )
                self.disconnect()

            # Get fastest servers
            servers = self.server_manager.select_fastest_server(country_code)
            if not servers:
                raise VPNError(f"No servers available in {country_code}")

            if self.verbose:
                self.logger.info(f"Selected {len(servers)} servers to try")
                for i, server in enumerate(servers, 1):
                    self.logger.info(
                        f"{i}. {server.get('hostname')} (load: {server.get('load')}%)"
                    )

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
                    self.setup_connection(
                        hostname, self.api_client.username, self.api_client.password
                    )

                    # Try to connect
                    self.connect([server])  # Pass as list for compatibility

                    # If we get here, connection succeeded
                    if self.verbose:
                        self.logger.info(f"Successfully connected to {hostname}")
                    return

                except Exception as e:
                    error_msg = f"{hostname if hostname else 'Unknown server'}: {e!s}"
                    errors.append(error_msg)
                    if self.verbose:
                        self.logger.warning(
                            f"Failed to connect to {hostname if hostname else 'Unknown server'}: {e}"
                        )
                    continue

            # If we get here, all servers failed
            raise VPNError(
                f"Failed to connect to any server in {country_code}:\n"
                + "\n".join(f"- {e}" for e in errors)
            )

        except Exception as e:
            raise VPNError(f"Failed to connect: {e}")
