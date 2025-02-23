"""VPN connection manager for NordVPN."""

import os
import subprocess
import time
from pathlib import Path
from typing import Optional, Dict, Any
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn
from loguru import logger

from .exceptions import VPNError
from .utils import API_HEADERS


class VPNConnectionManager:
    """Manages VPN connections using OpenVPN."""

    def __init__(
        self, openvpn_path: str = "/usr/local/sbin/openvpn", verbose: bool = False
    ):
        """Initialize VPN connection manager.

        Args:
            openvpn_path: Path to OpenVPN executable
            verbose: Whether to enable verbose logging
        """
        self.openvpn_path = openvpn_path
        self.logger = logger
        self.verbose = verbose
        self.auth_file = None
        self.config_file = None
        self.process: Optional[subprocess.Popen] = None
        self.config_dir = Path(os.path.expanduser("~/.config/nyord-vpn/configs"))
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Connection state
        self._initial_ip: Optional[str] = None
        self._connected_ip: Optional[str] = None
        self._server: Optional[str] = None
        self._country_name: Optional[str] = None

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

    def connect(self, server: Dict[str, Any]) -> None:
        """Connect to a VPN server.

        Args:
            server: Server info dictionary

        Raises:
            VPNError: If connection fails
        """
        try:
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Invalid server info - missing hostname")

            if self.verbose:
                self.logger.debug(f"Connecting to {hostname}")

            # Store initial IP
            self._initial_ip = self.get_current_ip()

            # Generate OpenVPN config
            config_path = self._generate_config(hostname)

            # Start OpenVPN process
            cmd = [
                "sudo",
                "openvpn",
                "--config",
                str(config_path),
                "--auth-user-pass",
                str(self.auth_file),
            ]

            if self.verbose:
                self.logger.debug(f"Running OpenVPN command: {' '.join(cmd)}")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="Connecting...", total=None)
                self.process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

            # Wait for initial connection
            time.sleep(5)
            if self.process.poll() is not None:
                stdout, stderr = self.process.communicate()
                raise VPNError(f"OpenVPN process failed: {stderr}\nOutput: {stdout}")

            # Verify connection
            if not self.verify_connection():
                raise VPNError("Failed to establish VPN connection")

            # Update connection info
            self._server = hostname
            self._connected_ip = self.get_current_ip()

            if self.verbose:
                self.logger.info(f"Connected to {hostname}")

        except Exception as e:
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN."""
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

        # Reset connection state
        self._initial_ip = None
        self._connected_ip = None
        self._server = None
        self._country_name = None

    def verify_connection(self) -> bool:
        """Verify VPN connection is active."""
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

    def _generate_config(self, hostname: str) -> Path:
        """Generate OpenVPN config file for server.

        Args:
            hostname: Server hostname

        Returns:
            Path: Path to generated config file
        """
        config_path = self.config_dir / f"{hostname}.ovpn"

        # Basic OpenVPN config
        config = f"""client
dev tun
proto tcp
remote {hostname} 443
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
comp-lzo
verb 3
"""

        config_path.write_text(config)
        return config_path

    def is_connected(self) -> bool:
        """Check if VPN is currently connected.

        Returns:
            bool: True if connected
        """
        return self.process is not None and self.process.poll() is None

    def update_connection_info(self, server_hostname: str, country_name: str) -> None:
        """Update connection information."""
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
        """
        # Generate OpenVPN config
        self.config_file = self._generate_config(server_hostname)

        # Create auth file
        self.auth_file = self.config_dir / "auth.txt"
        self.auth_file.write_text(f"{username}\n{password}")
        self.auth_file.chmod(0o600)

    def start_openvpn(self) -> None:
        """Start OpenVPN process with the current configuration."""
        if not self.config_file or not self.auth_file:
            raise VPNError("VPN not configured. Call setup_connection first.")

        if not self.config_file.exists():
            raise VPNError(f"OpenVPN config file not found: {self.config_file}")

        if not self.auth_file.exists():
            raise VPNError(f"OpenVPN auth file not found: {self.auth_file}")

        cmd = [
            self.openvpn_path,
            "--config",
            str(self.config_file),
            "--auth-user-pass",
            str(self.auth_file),
            "--daemon",  # Run in background
            "--script-security",
            "2",  # Allow running up/down scripts
            "--verb",
            "3",  # Verbose logging
        ]

        try:
            subprocess.run(cmd, check=True)
            self.logger.info("OpenVPN process started")
        except subprocess.CalledProcessError as e:
            raise VPNError(f"Failed to start OpenVPN: {e}")
