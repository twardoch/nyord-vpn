"""Main VPN client implementation."""

from pathlib import Path

from nyord_vpn.api.njord import NjordAPI
from nyord_vpn.api.legacy import LegacyAPI
from nyord_vpn.utils.retry import with_fallback, with_retry
from nyord_vpn.utils.log_utils import (
    log_operation,
    log_success,
    log_error,
    setup_logging,
)
from nyord_vpn.core.config import load_config
from nyord_vpn.core.exceptions import VPNError, VPNConnectionError


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
        self.logger = setup_logging(log_file=log_file)

        # Load config
        self.config = load_config(config_file)
        if username:
            self.config.username = username
        if password:
            self.config.password = password

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
            self.primary_api.connect, self.fallback_api.connect
        )
        self._disconnect = with_fallback(
            self.primary_api.disconnect, self.fallback_api.disconnect
        )
        self._status = with_fallback(self.primary_api.status, self.fallback_api.status)
        self._list_countries = with_fallback(
            self.primary_api.list_countries, self.fallback_api.list_countries
        )

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.disconnect()

    @with_retry()
    async def connect(self, country: str | None = None) -> bool:
        """Connect to VPN.

        Args:
            country: Optional country to connect to

        Returns:
            bool: True if connection successful

        Raises:
            VPNConnectionError: If connection fails
        """
        country = country or self.config.default_country
        log_operation(f"Connecting to VPN in {country}")

        try:
            result = await self._connect(country)
            if result:
                log_success("Connected successfully")
            else:
                log_error("Connection failed")
            return result
        except Exception as e:
            log_error(f"Connection failed: {e}")
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    @with_retry()
    async def disconnect(self) -> bool:
        """Disconnect from VPN.

        Returns:
            bool: True if disconnection successful

        Raises:
            VPNConnectionError: If disconnection fails
        """
        log_operation("Disconnecting from VPN")

        try:
            result = await self._disconnect()
            if result:
                log_success("Disconnected successfully")
            else:
                log_error("Disconnection failed")
            return result
        except Exception as e:
            log_error(f"Disconnection failed: {e}")
            msg = f"Failed to disconnect: {e}"
            raise VPNConnectionError(msg) from e

    @with_retry()
    async def status(self) -> dict:
        """Get VPN status.

        Returns:
            dict: Status information

        Raises:
            VPNError: If status check fails
        """
        try:
            return await self._status()
        except Exception as e:
            log_error(f"Failed to get status: {e}")
            msg = f"Failed to get status: {e}"
            raise VPNError(msg) from e

    @with_retry()
    async def list_countries(self) -> list[str]:
        """Get available countries.

        Returns:
            list[str]: List of country names

        Raises:
            VPNError: If country list fetch fails
        """
        try:
            return await self._list_countries()
        except Exception as e:
            log_error(f"Failed to get countries: {e}")
            msg = f"Failed to get countries: {e}"
            raise VPNError(msg) from e
