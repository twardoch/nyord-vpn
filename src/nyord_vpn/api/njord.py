"""Njord-based implementation of the VPN API."""


from njord import Client

from nyord_vpn.core.exceptions import VPNError, VPNConnectionError, VPNStatusError
from nyord_vpn.api.base import BaseAPI


class NjordAPI(BaseAPI):
    """VPN API implementation using njord library."""

    def __init__(self, username: str = "", password: str = ""):
        """Initialize NjordAPI.

        Args:
            username: Optional username (can be set via env)
            password: Optional password (can be set via env)
        """
        self._client = Client(user=username, password=password)
        self._connected = False
        self._current_server = None

    async def connect(self, country: str) -> bool:
        """Connect to VPN using njord."""
        try:
            result = await self._client.connect()
            self._connected = result
            if result:
                status = await self._client.status()
                self._current_server = status.get("server")
            return result
        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    async def disconnect(self) -> bool:
        """Disconnect from VPN using njord."""
        try:
            self._client.disconnect()
            self._connected = False
            self._current_server = None
            return True
        except Exception as e:
            msg = f"Failed to disconnect: {e}"
            raise VPNConnectionError(msg) from e

    async def status(self) -> dict[str, any]:
        """Get VPN connection status."""
        try:
            status = await self._client.status()
            return {
                "connected": self._connected,
                "country": status.get("country", ""),
                "ip": status.get("ip", ""),
                "server": self._current_server,
            }
        except Exception as e:
            msg = f"Failed to get status: {e}"
            raise VPNStatusError(msg) from e

    async def list_countries(self) -> list[str]:
        """Get available countries from njord."""
        try:
            countries = await self._client.list_countries()
            return [country["name"] for country in countries]
        except Exception as e:
            msg = f"Failed to get countries: {e}"
            raise VPNError(msg) from e

    async def get_credentials(self) -> tuple[str, str]:
        """Get stored credentials."""
        return self._client.auth_user, self._client.auth_password
