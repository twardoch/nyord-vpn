"""Njord-based implementation of the VPN API."""

import asyncio
import secrets
from typing import Any

import aiohttp
import pycountry
from njord import Client

from nyord_vpn.core.exceptions import VPNError, VPNConnectionError
from nyord_vpn.data.countries import get_country_id
from nyord_vpn.api.base import BaseAPI
from nyord_vpn.utils.validation import (
    validate_country,
    validate_credentials,
    validate_hostname,
)


class NjordAPI(BaseAPI):
    """VPN API implementation using njord library."""

    RECOMMENDATIONS_URL = "https://api.nordvpn.com/v1/servers/recommendations"

    def __init__(self, username: str = "", password: str = ""):
        """Initialize NjordAPI.

        Args:
            username: Optional username (can be set via env)
            password: Optional password (can be set via env)

        Raises:
            VPNError: If credentials are invalid
        """
        # Validate credentials
        self._auth_user, self._auth_pass = validate_credentials(username, password)
        self._client = Client(user=self._auth_user, password=self._auth_pass)
        self._connected = False
        self._current_server = None
        self._loop = asyncio.get_event_loop()

    async def get_recommended_server(self, country: str) -> str:
        """Get recommended NordVPN server for a country.

        Args:
            country: Country name or code

        Returns:
            str: Server hostname

        Raises:
            VPNError: If no server is found
        """

        def handle_country_not_found(country: str) -> str:
            msg = f"Country not found: {country}"
            raise VPNError(msg)

        def handle_invalid_country(country_obj: Any) -> str:
            msg = f"Invalid country object: {country_obj}"
            raise VPNError(msg)

        def handle_unsupported_country(country: str) -> str:
            msg = f"Country not supported: {country}"
            raise VPNError(msg)

        def handle_no_servers(country: str) -> str:
            msg = f"No servers found for country: {country}"
            raise VPNError(msg)

        def handle_request_error(e: Exception) -> str:
            msg = f"Failed to get server recommendations: {e}"
            raise VPNError(msg) from e

        # Validate country
        country = validate_country(country)

        # Try exact match first
        country_obj = pycountry.countries.get(name=country)
        if not country_obj:
            # Try fuzzy search
            matches = pycountry.countries.search_fuzzy(country)
            if matches:
                country_obj = matches[0]
            else:
                return handle_country_not_found(country)

        # Get alpha_2 code safely
        alpha_2 = getattr(country_obj, "alpha_2", None)
        if not alpha_2:
            return handle_invalid_country(country_obj)

        country_id = get_country_id(alpha_2)
        if not country_id:
            return handle_unsupported_country(country)

        try:
            async with (
                aiohttp.ClientSession() as session,
                session.get(
                    self.RECOMMENDATIONS_URL,
                    params={"filters[country_id]": country_id},
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response,
            ):
                response.raise_for_status()
                servers = await response.json()

            if not servers:
                return handle_no_servers(country)

            # Use cryptographically secure random choice
            server_index = secrets.randbelow(len(servers))
            hostname = servers[server_index]["hostname"]

            # Validate hostname
            return validate_hostname(hostname)

        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            return handle_request_error(e)

    async def connect(self, country: str) -> bool:
        """Connect to VPN using njord.

        Args:
            country: Country to connect to

        Returns:
            bool: True if connection successful
        """

        def handle_vpn_error(e: VPNError) -> bool:
            # Re-raise VPN errors as-is
            raise e

        def handle_connection_error(e: Exception, context: str | None = None) -> bool:
            msg = f"Failed to connect: {context or str(e)}"
            raise VPNConnectionError(msg) from e

        try:
            # Get recommended server
            server = await self.get_recommended_server(country)

            # Run connect in thread pool
            connect_fn = self._client.connect
            await self._loop.run_in_executor(None, connect_fn)

            # Update state
            self._connected = True
            self._current_server = server

            # Get status to verify connection
            try:
                status_fn = self._client.status
                status = await self._loop.run_in_executor(None, status_fn)
                if not status or not status.get("server"):
                    return handle_connection_error(VPNError("No server in status"))
                self._current_server = validate_hostname(status["server"])
                return True
            except VPNError as e:
                return handle_vpn_error(e)
            except Exception as e:
                return handle_connection_error(e)

        except VPNError as e:
            return handle_vpn_error(e)
        except Exception as e:
            return handle_connection_error(e)

    async def disconnect(self) -> bool:
        """Disconnect from VPN using njord."""

        def handle_error(e: Exception) -> bool:
            msg = f"Failed to disconnect: {e}"
            raise VPNConnectionError(msg) from e

        try:
            # Run disconnect in thread pool
            disconnect_fn = self._client.disconnect
            result = await self._loop.run_in_executor(None, disconnect_fn)
            if not result:
                return handle_error(VPNError("Failed to disconnect"))
            self._connected = False
            self._current_server = None
            return True
        except Exception as e:
            return handle_error(e)

    async def status(self) -> dict[str, Any]:
        """Get VPN status using njord.

        Returns:
            dict: Status information
        """

        def handle_error(e: Exception) -> dict[str, Any]:
            msg = f"Failed to get status: {e}"
            raise VPNConnectionError(msg) from e

        try:
            # Run status in thread pool
            status_fn = self._client.status
            status = await self._loop.run_in_executor(None, status_fn)
            if not status:
                return handle_error(VPNError("No status returned"))
            return status
        except Exception as e:
            return handle_error(e)

    async def list_countries(self) -> list[str]:
        """Get available countries from njord."""

        def handle_error(e: Exception) -> list[str]:
            msg = f"Failed to get countries: {e}"
            raise VPNError(msg) from e

        try:
            # Run list_countries in thread pool
            list_fn = self._client.list_countries
            countries = await self._loop.run_in_executor(None, list_fn)
            if not countries:
                return handle_error(VPNError("No countries found"))
            return [str(country["name"]) for country in countries]
        except Exception as e:
            return handle_error(e)

    async def get_credentials(self) -> tuple[str, str]:
        """Get stored credentials."""
        return self._auth_user, self._auth_pass
