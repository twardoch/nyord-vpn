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
from nyord_vpn.core.config import VPNConfig
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
        if config_file:
            self.config = VPNConfig.from_file(config_file)
        else:
            self.config = VPNConfig.from_env()

        # Override with explicit credentials if provided
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

    @classmethod
    def from_file(
        cls,
        config_file: Path,
        username: str | None = None,
        password: str | None = None,
        log_file: Path | None = None,
    ) -> "VPNClient":
        """Create a VPNClient instance from a configuration file.

        Args:
            config_file: Path to the configuration file
            username: Optional username (overrides config)
            password: Optional password (overrides config)
            log_file: Optional path to log file

        Returns:
            VPNClient: A new VPNClient instance
        """
        return cls(
            config_file=config_file,
            username=username,
            password=password,
            log_file=log_file,
        )

    @classmethod
    def from_env(
        cls,
        username: str | None = None,
        password: str | None = None,
        log_file: Path | None = None,
    ) -> "VPNClient":
        """Create a VPNClient instance from environment variables.

        Args:
            username: Optional username (overrides env)
            password: Optional password (overrides env)
            log_file: Optional path to log file

        Returns:
            VPNClient: A new VPNClient instance
        """
        return cls(
            username=username,
            password=password,
            log_file=log_file,
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
        if exc_type is None:
            await self.disconnect()

    def is_connected(self) -> bool:
        """Check if VPN is connected."""
        try:
            status = self._status()
            if isinstance(status, dict):
                return bool(status.get("connected", False))
            return False
        except VPNError:
            return False

    async def connect(self, country: str | None = None) -> bool:
        """Connect to VPN.

        Args:
            country: Optional country to connect to (defaults to config)

        Returns:
            bool: True if connection successful

        Raises:
            VPNConnectionError: If connection fails
        """
        target_country = country or self.config.default_country
        try:
            return await self._connect(target_country)
        except Exception as e:
            _raise_connection_error(e, target_country)

    async def disconnect(self) -> bool:
        """Disconnect from VPN.

        Returns:
            bool: True if disconnection successful

        Raises:
            VPNConnectionError: If disconnection fails
        """
        return await self._disconnect()

    @with_retry()
    async def status(self) -> dict[str, Any]:
        """Get current VPN connection status.

        Returns:
            dict: Status information including:
                - connected (bool): Whether connected
                - country (str): Connected country if any
                - ip (str): Current IP address
                - server (str): Connected server if any
        """
        return await self._status()

    @with_retry()
    async def list_countries(self) -> list[str]:
        """Get list of available countries.

        Returns:
            list[str]: List of country names
        """
        return await self._list_countries()
