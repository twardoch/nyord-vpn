"""Njord-based implementation of the VPN API."""

import asyncio
import secrets
from typing import Any

import aiohttp
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

    async def _get_servers_for_country(self, country_id: str) -> list[dict[str, Any]]:
        """Get server list for a country.

        Args:
            country_id: Country ID

        Returns:
            List of server information

        Raises:
            VPNError: If request fails
        """
        try:
            async with aiohttp.ClientSession() as session, session.get(
                self.RECOMMENDATIONS_URL,
                params={"filters[country_id]": country_id},
                timeout=aiohttp.ClientTimeout(total=10),
                ssl=True,
            ) as response:
                response.raise_for_status()
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            msg = f"Failed to get server recommendations: {e}"
            raise VPNError(msg) from e

    def _select_random_server(self, servers: list[dict[str, Any]]) -> str:
        """Select a random server from the list.

        Args:
            servers: List of server information

        Returns:
            Selected server hostname

        Raises:
            VPNError: If no servers available
        """
        if not servers:
            msg = "No servers found"
            raise VPNError(msg)

        server_index = secrets.randbelow(len(servers))
        hostname = servers[server_index]["hostname"]
        return validate_hostname(hostname)

    async def get_recommended_server(self, country: str) -> str:
        """Get recommended NordVPN server for a country.

        Args:
            country: Country name or code

        Returns:
            str: Recommended server hostname

        Raises:
            VPNError: If no servers found or request fails
        """
        # Validate country and get ID
        country = validate_country(country)
        country_id = get_country_id(country)
        if not country_id:
            msg = f"Invalid country: {country}"
            raise VPNError(msg)

        # Get servers and select one
        servers = await self._get_servers_for_country(country_id)
        if not servers:
            msg = f"No servers found for country: {country}"
            raise VPNError(msg)

        return self._select_random_server(servers)

    async def connect(self, country: str) -> bool:
        """Connect to VPN in specified country.

        Args:
            country: Country name or code

        Returns:
            bool: True if connection successful

        Raises:
            VPNConnectionError: If connection fails
        """
        try:
            # Get recommended server
            await self.get_recommended_server(country)

            # Connect using njord (run in thread pool)
            connect_fn = self._client.connect
            result = await self._loop.run_in_executor(None, connect_fn)

            if result:
                self._connected = True
                # Get status (run in thread pool)
                status_fn = self._client.status
                status = await self._loop.run_in_executor(None, status_fn)
                self._current_server = status.get("server")
                return True
            return False

        except VPNError as e:
            msg = f"Failed to connect to {country}: {e}"
            raise VPNConnectionError(msg) from e
        except Exception as e:
            msg = f"Unexpected error connecting to {country}: {e}"
            raise VPNConnectionError(msg) from e

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
