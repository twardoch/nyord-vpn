"""Main VPN client implementation."""

from pathlib import Path
from types import TracebackType
from typing import Any, NoReturn

from pydantic import SecretStr

from nyord_vpn.api.njord import NjordAPI
from nyord_vpn.api.legacy import LegacyAPI
from nyord_vpn.utils.retry import with_fallback, with_retry
from nyord_vpn.utils.log_utils import (
    LogConfig,
    setup_logging,
)
from nyord_vpn.core.config import load_config
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

    def __init__(
        self,
        config_file: Path | None = None,
        username: str | None = None,
        password: str | None = None,
        log_file: Path | None = None,
    ):
        """Initialize VPN client.

        Args:
            config_file: Optional path to config file
            username: Optional username (overrides config)
            password: Optional password (overrides config)
            log_file: Optional path to log file
        """
        # Setup logging
        log_config = LogConfig(log_file=log_file) if log_file else None
        self.logger = setup_logging(log_config)

        # Load config
        self.config = load_config(config_file)
        if username:
            self.config.username = username
        if password:
            self.config.password = SecretStr(password)

        # Initialize APIs
        self.primary_api = NjordAPI(
            username=self.config.username,
            password=self.config.password.get_secret_value(),
        )
        self.fallback_api = LegacyAPI(
            username=self.config.username,
            password=self.config.password.get_secret_value(),
        )

        # Setup API methods with fallback
        self._connect = with_fallback(
            self.primary_api.connect,
            self.fallback_api.connect,
        )
        self._disconnect = with_fallback(
            self.primary_api.disconnect,
            self.fallback_api.disconnect,
        )
        self._status = with_fallback(
            self.primary_api.status,
            self.fallback_api.status,
        )
        self._list_countries = with_fallback(
            self.primary_api.list_countries,
            self.fallback_api.list_countries,
        )

    async def __aenter__(self) -> "VPNClient":
        """Async context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Async context manager exit."""
        await self.disconnect()

    def _raise_connection_error(
        self, error: Exception, server: str | None = None
    ) -> None:
        """Raise a VPNConnectionError with a descriptive message."""
        msg = "Error connecting to VPN"
        if server:
            msg = f"{msg} server {server}"
        msg = f"{msg}: {error}"
        raise VPNConnectionError(msg) from error

    def _raise_disconnect_error(self, error: Exception) -> None:
        """Raise a VPNConnectionError with a descriptive message."""
        msg = f"Error disconnecting from VPN: {error}"
        raise VPNConnectionError(msg) from error

    def _raise_status_error(self, error: Exception) -> None:
        """Raise a VPNError with a descriptive message."""
        msg = f"Error getting VPN status: {error}"
        raise VPNError(msg) from error

    def _raise_countries_error(self, error: Exception) -> None:
        """Raise a VPNError with a descriptive message."""
        msg = f"Error getting list of countries: {error}"
        raise VPNError(msg) from error

    @with_retry()
    async def connect(self) -> bool:
        """Connect to the VPN."""
        try:
            if not await self._connect():
                msg = "Failed to connect to VPN"
                raise VPNConnectionError(msg)
            return True
        except Exception as e:
            msg = f"Failed to connect to VPN: {e}"
            raise VPNConnectionError(msg) from e

    @with_retry()
    async def disconnect(self) -> bool:
        """Disconnect from the VPN."""
        try:
            if not await self._disconnect():
                msg = "Failed to disconnect from VPN"
                raise VPNError(msg)
            return True
        except Exception as e:
            msg = f"Failed to disconnect from VPN: {e}"
            raise VPNError(msg) from e

    @with_retry()
    async def status(self) -> dict[str, Any]:
        """Get the current VPN status."""
        try:
            status = await self._status()
            if not status:
                msg = "Failed to get VPN status"
                raise VPNError(msg)
            return status
        except Exception as e:
            msg = f"Failed to get VPN status: {e}"
            raise VPNError(msg) from e

    @with_retry()
    async def list_countries(self) -> list[str]:
        """List available countries."""
        try:
            countries = await self._list_countries()
            if not countries:
                msg = "Failed to get country list"
                raise VPNError(msg)
            return countries
        except Exception as e:
            msg = f"Failed to get country list: {e}"
            raise VPNError(msg) from e
