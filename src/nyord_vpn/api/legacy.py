"""Legacy VPN API implementation."""

from typing import TypedDict, Any
import shutil
import subprocess
import requests

from nyord_vpn.api.base import BaseAPI


class ServerInfo(TypedDict):
    name: str
    id: str


class CountryInfo(TypedDict):
    name: str
    id: str


class LegacyAPI(BaseAPI):
    """Legacy NordVPN API implementation."""

    def __init__(self, username: str, password: str):
        """Initialize the API with NordVPN credentials.

        Args:
            username: NordVPN username
            password: NordVPN password
        """
        self.username = username
        self.password = password

        # Check if nordvpn command exists
        nordvpn_path = shutil.which("nordvpn")
        if not nordvpn_path:
            msg = "nordvpn command not found in PATH"
            raise RuntimeError(msg)
        self.nordvpn_path = nordvpn_path

    async def _get_servers(self, country: str) -> list[ServerInfo]:
        """Get list of servers for a country.

        Args:
            country: Country name or code

        Returns:
            List of server information
        """
        try:
            response = requests.get(
                f"https://api.nordvpn.com/v1/servers/{country}", timeout=10
            )
            response.raise_for_status()
            servers = response.json()
            return [{"name": s["name"], "id": s["id"]} for s in servers]
        except Exception as e:
            msg = "Failed to get server list"
            raise RuntimeError(msg) from e

    async def connect(self, country: str | None = None) -> bool:
        """Connect to NordVPN.

        Args:
            country: Optional country to connect to

        Returns:
            True if connection successful
        """
        cmd = [self.nordvpn_path, "connect"]
        if country:
            cmd.append(country)

        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=30)
            return True
        except subprocess.CalledProcessError as e:
            msg = "Failed to connect"
            raise RuntimeError(msg) from e
        except subprocess.TimeoutExpired as e:
            msg = "Connection timed out after 30 seconds"
            raise RuntimeError(msg) from e

    async def disconnect(self) -> bool:
        """Disconnect from NordVPN.

        Returns:
            True if disconnection successful
        """
        try:
            subprocess.run(
                [self.nordvpn_path, "disconnect"],
                check=True,
                capture_output=True,
                timeout=10,
            )
            return True
        except subprocess.CalledProcessError as e:
            msg = "Failed to disconnect"
            raise RuntimeError(msg) from e
        except subprocess.TimeoutExpired as e:
            msg = "Disconnect timed out after 10 seconds"
            raise RuntimeError(msg) from e

    async def status(self) -> dict[str, Any]:
        """Get current connection status.

        Returns:
            Dictionary with status information
        """
        try:
            # Get current IP
            ip_response = requests.get(
                "https://api.nordvpn.com/v1/helpers/ip", timeout=10
            )
            ip_response.raise_for_status()
            ip_info = ip_response.json()

            # Get connection status
            status = subprocess.run(
                [self.nordvpn_path, "status"],
                capture_output=True,
                check=True,
                timeout=10,
            )

            return {
                "ip": ip_info.get("ip"),
                "country": ip_info.get("country"),
                "status": status.stdout.decode(),
            }
        except (subprocess.CalledProcessError, requests.RequestException) as e:
            msg = "Failed to get status"
            raise RuntimeError(msg) from e

    async def list_countries(self) -> list[str]:
        """Get list of available countries.

        Returns:
            List of country names
        """
        try:
            response = requests.get(
                "https://api.nordvpn.com/v1/servers/countries", timeout=10
            )
            response.raise_for_status()
            countries: list[CountryInfo] = response.json()
            return [c["name"] for c in countries]
        except requests.RequestException as e:
            msg = "Failed to get country list"
            raise RuntimeError(msg) from e

    async def get_credentials(self) -> tuple[str, str]:
        """Get stored credentials.

        Returns:
            Tuple of (username, password)
        """
        return self.username, self.password
