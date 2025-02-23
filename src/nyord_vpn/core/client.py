"""Main VPN client implementation."""

from pathlib import Path
from types import TracebackType
from typing import Any, NoReturn

from loguru import logger

from nyord_vpn.api.njord import NjordVPNClient
from nyord_vpn.api.legacy import LegacyVPNClient
from nyord_vpn.core.base import BaseVPNClient
from nyord_vpn.core.exceptions import VPNError, VPNConnectionError


def _raise_connection_error(error: Exception, country: str) -> NoReturn:
    msg = f"Failed to connect to {country}: {error}"
    raise VPNConnectionError(msg) from error


def _raise_disconnect_error(error: Exception) -> NoReturn:
    msg = f"Failed to disconnect: {error}"
    raise VPNConnectionError(msg) from error


def _raise_status_error(error: Exception) -> NoReturn:
    msg = f"Failed to get status: {error}"
    raise VPNConnectionError(msg) from error


def _raise_countries_error(error: Exception) -> NoReturn:
    msg = f"Failed to list countries: {error}"
    raise VPNConnectionError(msg) from error


class VPNClient:
    """Main VPN client that manages connection and APIs."""

    def __init__(self, use_legacy_api: bool = False) -> None:
        """Initialize VPN client.

        Args:
            use_legacy_api: Whether to use legacy API only

        Note:
            Credentials must be provided via NORD_USER and NORD_PASSWORD environment variables.
        """
        # Initialize APIs
        if use_legacy_api:
            # Use only legacy API
            self.primary_api = LegacyVPNClient()
            self.fallback_api = None
        else:
            # Use njord API with legacy fallback
            self.primary_api = NjordVPNClient()
            self.fallback_api = LegacyVPNClient()

        logger.debug(
            f"Initialized VPN client with {'legacy' if use_legacy_api else 'njord'} API"
        )

        # Setup API methods
        if self.fallback_api:
            # Use fallback if available
            self._connect = self._with_fallback(
                self.primary_api.connect,
                self.fallback_api.connect,
            )
            self._disconnect = self._with_fallback(
                self.primary_api.disconnect,
                self.fallback_api.disconnect,
            )
            self._status = self._with_fallback(
                self.primary_api.status,
                self.fallback_api.status,
            )
            self._list_countries = self._with_fallback(
                self.primary_api.list_countries,
                self.fallback_api.list_countries,
            )
        else:
            # Use primary API directly
            self._connect = self.primary_api.connect
            self._disconnect = self.primary_api.disconnect
            self._status = self.primary_api.status
            self._list_countries = self.primary_api.list_countries

    def _with_fallback(self, primary_func, fallback_func):
        """Wrap a function with fallback support."""

        def wrapper(*args, **kwargs):
            try:
                return primary_func(*args, **kwargs)
            except Exception as e:
                if self.fallback_api:
                    return fallback_func(*args, **kwargs)
                raise e

        return wrapper

    def connect(self, country: str | None = None) -> bool:
        """Connect to VPN.

        Args:
            country: Optional country to connect to

        Returns:
            bool: True if connection successful

        Raises:
            VPNConnectionError: If connection fails
        """
        try:
            return self._connect(country)
        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    def disconnect(self) -> bool:
        """Disconnect from VPN.

        Returns:
            bool: True if disconnection successful

        Raises:
            VPNConnectionError: If disconnection fails
        """
        try:
            return self._disconnect()
        except Exception as e:
            msg = "Failed to disconnect"
            raise VPNConnectionError(msg) from e

    def status(self) -> dict[str, Any]:
        """Get current VPN connection status.

        Returns:
            dict: Status information including:
                - connected (bool): Whether connected
                - country (str): Connected country if any
                - ip (str): Current IP address
                - server (str): Connected server if any
        """
        try:
            status = self._status()
            # Ensure consistent status format
            return {
                "connected": bool(status.get("connected", False)),
                "country": str(status.get("country", "")),
                "ip": str(status.get("ip", "")),
                "server": str(status.get("server", "")) if status.get("server") else "",
            }
        except Exception as e:
            msg = "Failed to get status"
            raise VPNConnectionError(msg) from e

    def list_countries(self) -> list[dict[str, Any]]:
        """Get list of available countries.

        Returns:
            list: List of countries with name and code
        """
        try:
            return self._list_countries()
        except Exception as e:
            msg = "Failed to list countries"
            raise VPNConnectionError(msg) from e
