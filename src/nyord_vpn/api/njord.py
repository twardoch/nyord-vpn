"""Njord-based implementation of the VPN API."""

import asyncio
import secrets
from typing import Any

import aiohttp
import pycountry
from njord import Client

from nyord_vpn.core.exceptions import VPNError, VPNConnectionError, VPNStatusError
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
                msg = f"Country not found: {country}"
                raise VPNError(msg)

        # Get alpha_2 code safely
        alpha_2 = getattr(country_obj, "alpha_2", None)
        if not alpha_2:
            msg = f"Invalid country object: {country_obj}"
            raise VPNError(msg)

        country_id = get_country_id(alpha_2)
        if not country_id:
            msg = f"Country not supported: {country}"
            raise VPNError(msg)

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
                msg = f"No servers found for country: {country}"
                raise VPNError(msg)

            # Use cryptographically secure random choice
            server_index = secrets.randbelow(len(servers))
            hostname = servers[server_index]["hostname"]

            # Validate hostname
            return validate_hostname(hostname)

        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            msg = f"Failed to get server recommendations: {e}"
            raise VPNError(msg) from e

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
            # Validate country
            country = validate_country(country)

            # Get recommended server (we don't use this directly since njord
            # has its own server selection logic)
            await self.get_recommended_server(country)

            # Connect using njord (run in thread pool)
            connect_fn = self._client.connect
            result = await self._loop.run_in_executor(None, connect_fn)
            self._connected = bool(result)

            if self._connected:
                # Get status (run in thread pool)
                status_fn = self._client.status
                status = await self._loop.run_in_executor(None, status_fn)
                server = status.get("server")
                if server:
                    self._current_server = validate_hostname(server)

            return self._connected

        except VPNError:
            # Re-raise VPN errors as-is
            raise
        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    async def disconnect(self) -> bool:
        """Disconnect from VPN using njord."""
        try:
            # Run disconnect in thread pool
            disconnect_fn = self._client.disconnect
            await self._loop.run_in_executor(None, disconnect_fn)
            self._connected = False
            self._current_server = None
            return True

        except Exception as e:
            msg = f"Failed to disconnect: {e}"
            raise VPNConnectionError(msg) from e

    async def status(self) -> dict[str, Any]:
        """Get VPN connection status."""
        try:
            # Run status check in thread pool
            status_fn = self._client.status
            status = await self._loop.run_in_executor(None, status_fn)
            return {
                "connected": self._connected,
                "country": str(status.get("country", "")),
                "ip": str(status.get("ip", "")),
                "server": str(self._current_server) if self._current_server else "",
            }

        except Exception as e:
            msg = f"Failed to get status: {e}"
            raise VPNStatusError(msg) from e

    async def list_countries(self) -> list[str]:
        """Get available countries from njord."""
        try:
            # Run list_countries in thread pool
            list_fn = self._client.list_countries
            countries = await self._loop.run_in_executor(None, list_fn)
            return [str(country["name"]) for country in countries]

        except Exception as e:
            msg = f"Failed to get countries: {e}"
            raise VPNError(msg) from e

    async def get_credentials(self) -> tuple[str, str]:
        """Get stored credentials."""
        return self._auth_user, self._auth_pass
