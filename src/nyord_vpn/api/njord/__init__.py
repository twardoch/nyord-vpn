"""
njord

"""

__version__ = "0.0.2"
__author__ = "admjs"

from typing import Any

from loguru import logger

from .client import Client
from nyord_vpn.core.base import BaseVPNClient, VPNStatus
from nyord_vpn.core.exceptions import VPNConnectionError, VPNServerError


class NjordVPNClient(BaseVPNClient):
    """Njord VPN client implementation."""

    def __init__(self) -> None:
        """Initialize njord VPN client."""
        super().__init__()
        self._client = Client(user=self.username, password=self.password)
        self._current_server: str | None = None
        logger.debug("Initialized njord VPN client")

    def connect(self, country: str | None = None) -> bool:
        """Connect to VPN using njord."""
        try:
            # Get server info
            if country:
                server_info = self._client.fetch_server_info()
                if not server_info:
                    msg = "No servers found"
                    raise VPNServerError(msg)
                hostname, _ = server_info
                self._current_server = hostname

            # Connect
            result = self._client.connect()
            if not result:
                msg = "Failed to connect"
                raise VPNConnectionError(msg)

            logger.info(f"Connected to {self._current_server or 'VPN'}")
            return True
        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    def disconnect(self) -> bool:
        """Disconnect from VPN."""
        try:
            self._client.disconnect()
            self._current_server = None
            return True
        except Exception as e:
            msg = "Failed to disconnect"
            raise VPNConnectionError(msg) from e

    def protected(self) -> bool:
        """Check if VPN is active."""
        try:
            return self._client.is_protected()
        except Exception:
            return False

    def status(self) -> VPNStatus:
        """Get VPN status."""
        try:
            status = self._client.status()
            return VPNStatus(
                connected=self.protected(),
                ip=status.get("ip", ""),
                country=status.get("country", ""),
                server=self._current_server or "",
            )
        except Exception as e:
            msg = "Failed to get status"
            raise VPNConnectionError(msg) from e

    def list_countries(self) -> list[dict[str, Any]]:
        """Get list of available countries."""
        try:
            countries = self._client.list_countries()
            return [
                {"name": country.get("name", ""), "code": str(country.get("id", ""))}
                for country in countries
            ]
        except Exception as e:
            msg = "Failed to get country list"
            raise VPNServerError(msg) from e


__all__ = ["Client", "NjordVPNClient"]
