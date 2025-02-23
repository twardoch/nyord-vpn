"""VPN connection manager for OpenVPN processes and connection state."""

import subprocess
import time
from pathlib import Path
from typing import Optional, Dict
import requests
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console

from .models import ConnectionError, DisconnectionError
from .utils import OPENVPN_CONFIG, OPENVPN_AUTH, OPENVPN_LOG
from ._templates import OPENVPN_TEMPLATE
from .connection_helpers import is_openvpn_running, compute_connection_status
from .state_manager import save_vpn_state, load_vpn_state

console = Console()


class VPNConnectionManager:
    """Manages VPN connections and OpenVPN processes."""

    def __init__(self, verbose: bool = False):
        """Initialize connection manager."""
        self.verbose = verbose
        self._initial_ip: Optional[str] = None
        self._connected_ip: Optional[str] = None
        self._server: Optional[str] = None
        self._country_name: Optional[str] = None
        self._load_state()

    def _load_state(self) -> None:
        """Load saved connection state."""
        state = load_vpn_state()
        self._initial_ip = state.get("initial_ip")
        self._connected_ip = state.get("connected_ip")
        self._server = state.get("server")
        self._country_name = state.get("country")

    def _save_state(self, is_connected: bool = False) -> None:
        """Save current connection state."""
        state = {
            "connected": is_connected,
            "initial_ip": self._initial_ip,
            "connected_ip": self._connected_ip,
            "server": self._server,
            "country": self._country_name,
            "timestamp": time.time(),
        }
        save_vpn_state(state)

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
            raise ConnectionError(
                "OpenVPN not found. Please install OpenVPN first:\n"
                "  macOS: brew install openvpn\n"
                "  Linux: sudo apt install openvpn\n"
                "  Windows: Download from https://openvpn.net/community-downloads/"
            )

    def setup_connection(
        self, server_hostname: str, username: str, password: str
    ) -> None:
        """Set up OpenVPN configuration files."""
        # Create OpenVPN config
        config = OPENVPN_TEMPLATE.format(server=server_hostname)
        OPENVPN_CONFIG.write_text(config)
        OPENVPN_CONFIG.chmod(0o600)

        # Create auth file
        OPENVPN_AUTH.write_text(f"{username}\n{password}")
        OPENVPN_AUTH.chmod(0o600)

    def start_openvpn(self) -> None:
        """Start OpenVPN process."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Connecting...", total=None)
            subprocess.Popen(
                [
                    "sudo",
                    "openvpn",
                    "--config",
                    str(OPENVPN_CONFIG),
                    "--auth-user-pass",
                    str(OPENVPN_AUTH),
                    "--daemon",
                    "--log",
                    str(OPENVPN_LOG),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

    def verify_connection(self) -> bool:
        """Verify VPN connection is active."""
        try:
            current_ip = self.get_current_ip()
            if not current_ip:
                return False

            state = load_vpn_state()
            initial_ip = state.get("initial_ip")
            connected_ip = state.get("connected_ip")
            openvpn_running = is_openvpn_running()

            # Check NordVPN API for connection status
            try:
                from .utils import API_HEADERS

                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers=API_HEADERS,
                    timeout=5,
                )
                response.raise_for_status()
                nord_data = response.json()
                nord_status = nord_data.get("status", False)
            except requests.RequestException:
                nord_status = None

            return compute_connection_status(
                current_ip,
                initial_ip,
                connected_ip,
                openvpn_running,
                nord_status=nord_status,
            )
        except Exception:
            return False

    def cleanup(self) -> None:
        """Clean up connection files."""
        for file in [OPENVPN_CONFIG, OPENVPN_AUTH, OPENVPN_LOG]:
            if file.exists():
                file.unlink()

    def disconnect(self) -> None:
        """Disconnect VPN and clean up."""
        try:
            # Kill all OpenVPN processes
            for proc in subprocess.check_output(["pgrep", "openvpn"]).split():
                subprocess.run(["sudo", "kill", proc.decode()], check=True)

            # Wait for processes to terminate
            time.sleep(1)

            # Verify all processes are terminated
            if is_openvpn_running():
                raise DisconnectionError("Failed to terminate all OpenVPN processes")

            # Reset and save state
            self._initial_ip = None
            self._connected_ip = None
            self._server = None
            self._country_name = None
            self._save_state(is_connected=False)

            # Clean up files
            self.cleanup()

        except subprocess.CalledProcessError:
            # No OpenVPN processes found
            pass
        except Exception as e:
            raise DisconnectionError(f"Error during disconnect: {e}")

    def update_connection_info(self, server_hostname: str, country_name: str) -> None:
        """Update connection information."""
        self._server = server_hostname
        self._country_name = country_name
        self._connected_ip = self.get_current_ip()
        self._save_state(is_connected=True)
