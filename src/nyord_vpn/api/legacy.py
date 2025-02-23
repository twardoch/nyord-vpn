"""Legacy VPN API implementation based on shell script."""

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any

import requests
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from nyord_vpn.core.base import BaseVPNClient, VPNStatus
from nyord_vpn.core.exceptions import VPNConfigError, VPNConnectionError, VPNServerError

# Country ID mapping from shell script
COUNTRY_IDS = {
    "albania": 2,
    "algeria": 3,
    "andorra": 5,
    "argentina": 10,
    "armenia": 11,
    "australia": 13,
    "austria": 14,
    # ... more countries to be added
    "united_states": 228,
    "united_kingdom": 227,
}


class LegacyVPNClient(BaseVPNClient):
    """Legacy VPN client implementation."""

    CONFIGS_DIR = Path("/etc/nordvpn_file")
    CONFIGS_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"

    def __init__(self) -> None:
        """Initialize legacy VPN client."""
        super().__init__()
        self._openvpn_pid: int | None = None
        self._current_server: str | None = None
        self._ensure_openvpn()

    def _ensure_openvpn(self) -> None:
        """Ensure OpenVPN is installed."""
        try:
            subprocess.run(["openvpn", "--version"], check=True, capture_output=True)
        except (subprocess.SubprocessError, FileNotFoundError) as e:
            msg = "OpenVPN not found. Install with: brew install openvpn"
            raise VPNConfigError(
                msg
            ) from e

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def _get_server(self, country: str | None = None) -> str:
        """Get recommended server for country.

        Args:
            country: Optional country name or code

        Returns:
            str: Server hostname

        Raises:
            VPNServerError: If server cannot be found
        """
        try:
            # Prepare country filter
            country_id = ""
            if country:
                country = country.lower().replace(" ", "_")
                country_id = COUNTRY_IDS.get(country, "")

            # Get server recommendation
            url = "https://nordvpn.com/wp-admin/admin-ajax.php"
            params = {
                "action": "servers_recommendations",
                "filters": json.dumps({"country_id": country_id})
                if country_id
                else "{}",
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            # Get first TCP server
            for server in data:
                hostname = server.get("hostname")
                if hostname:
                    return f"{hostname}.tcp"

            msg = "No suitable servers found"
            raise VPNServerError(msg)
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            msg = "Failed to get server recommendations"
            raise VPNServerError(msg) from e

    def _ensure_configs(self) -> None:
        """Ensure OpenVPN configs are downloaded and cached."""
        if not self.CONFIGS_DIR.exists():
            logger.info("Downloading OpenVPN configurations...")
            try:
                # Create configs directory
                self.CONFIGS_DIR.mkdir(parents=True, exist_ok=True)

                # Download and extract configs
                response = requests.get(self.CONFIGS_URL)
                response.raise_for_status()
                zip_path = self.CONFIGS_DIR / "ovpn.zip"
                zip_path.write_bytes(response.content)

                # Extract TCP configs only
                subprocess.run(
                    [
                        "unzip",
                        "-qq",
                        str(zip_path),
                        "ovpn_tcp/*",
                        "-d",
                        str(self.CONFIGS_DIR),
                    ],
                    check=True,
                )

                # Cleanup
                zip_path.unlink()
                logger.info("OpenVPN configurations downloaded and extracted")
            except Exception as e:
                msg = "Failed to download OpenVPN configurations"
                raise VPNConfigError(msg) from e

    def connect(self, country: str | None = None) -> bool:
        """Connect to VPN using legacy implementation."""
        try:
            # Disconnect if connected
            self.disconnect()

            # Get server and ensure configs
            server = self._get_server(country)
            self._ensure_configs()

            # Create temp auth file
            auth_file = Path(tempfile.mkstemp(prefix="nordvpn_", suffix=".auth")[1])
            auth_file.write_text(f"{self.username}\n{self.password}")
            auth_file.chmod(0o600)

            try:
                # Start OpenVPN
                config_file = self.CONFIGS_DIR / "ovpn_tcp" / server
                if not config_file.exists():
                    msg = f"Config file not found: {config_file}"
                    raise VPNConfigError(msg)

                process = subprocess.Popen(
                    [
                        "sudo",
                        "openvpn",
                        "--config",
                        str(config_file),
                        "--auth-user-pass",
                        str(auth_file),
                        "--daemon",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                self._openvpn_pid = process.pid
                self._current_server = server

                # Wait for connection
                logger.info(f"Connecting to {server}...")
                return True
            finally:
                # Cleanup auth file
                auth_file.unlink()
        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    def disconnect(self) -> bool:
        """Disconnect from VPN."""
        try:
            if self._openvpn_pid:
                subprocess.run(["sudo", "kill", str(self._openvpn_pid)], check=True)
                self._openvpn_pid = None
                self._current_server = None
            subprocess.run(["sudo", "pkill", "openvpn"], check=True)
            return True
        except subprocess.SubprocessError as e:
            msg = "Failed to disconnect"
            raise VPNConnectionError(msg) from e

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def protected(self) -> bool:
        """Check if VPN is active."""
        try:
            response = requests.get("https://ipinfo.io/json")
            response.raise_for_status()
            data = response.json()
            return "nordvpn.com" in data.get("org", "").lower()
        except Exception:
            return False

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def status(self) -> VPNStatus:
        """Get VPN status."""
        try:
            response = requests.get("https://ipinfo.io/json")
            response.raise_for_status()
            data = response.json()
            return VPNStatus(
                connected=self.protected(),
                ip=data.get("ip", ""),
                country=data.get("country", ""),
                server=self._current_server or "",
            )
        except Exception as e:
            msg = "Failed to get status"
            raise VPNConnectionError(msg) from e

    def list_countries(self) -> list[dict[str, Any]]:
        """Get list of available countries."""
        return [
            {"name": name.replace("_", " ").title(), "code": code}
            for name, code in COUNTRY_IDS.items()
        ]
