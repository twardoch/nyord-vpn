"""NordVPN API client for data retrieval and API interactions.

this_file: src/nyord_vpn/api/api.py

This module provides the NordVPNAPI class for interacting with NordVPN's API.
It serves as the central interface for all API operations, focusing on the v2 endpoints.

Core Responsibilities:
1. Authentication with NordVPN API (handled by underlying v2_servers client if needed)
2. Country and server information retrieval using v2 API.
3. Cache management for API responses (instance-level).
4. Location and city information lookup via v2 data.
5. API connectivity testing (implicit via successful calls).

Integration Points:
- Used by Client (core/client.py) for API operations
- Used by ServerManager (network/server.py) for server info
- Handles models defined in storage/models.py (indirectly via v2_servers models)

The client implements automatic fallback to cached data (instance-level) when
API requests fail on subsequent calls within the same instance lifetime.
"""

from typing import Any, TypeVar, cast

import requests
from loguru import logger

# Focus on v2_servers and remove v1 imports
from nyord_vpn.api import v2_servers
from nyord_vpn.exceptions import VPNAPIError

# Type aliases for clarity
# This ServerTuple now directly reflects the output of v2_servers.NordVPNServersV2.fetch_all()
ServerTuple = tuple[
    list[v2_servers.Server],
    list[v2_servers.Group],
    list[v2_servers.Service],
    list[v2_servers.Location],
    list[v2_servers.Technology],
]

T = TypeVar("T")


class NordVPNAPI:
    """Unified NordVPN API client, focused on v2 API.

    This class provides a single interface to access NordVPN API endpoints,
    primarily leveraging the v2 servers API.

    Attributes:
        timeout: Request timeout in seconds for all API calls.
        servers: Client for v2 servers API.
    """

    def __init__(self, timeout: int = 10) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds for all API calls.
        """
        self.timeout = timeout
        self.servers = v2_servers.NordVPNServersV2(timeout=timeout)

        # Cache for API responses (specifically for the comprehensive v2 server data)
        self._servers_cache: ServerTuple | None = None # Renamed for clarity

    def get_servers(self, *, refresh: bool = False) -> ServerTuple:
        """Get detailed server information using the v2 API.

        This method uses the v2 API to fetch comprehensive server information,
        including groups, services, locations, and technologies.
        Results are cached within the instance.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            Tuple of (servers, groups, services, locations, technologies).

        Raises:
            VPNAPIError: If the API request fails and no cached data is available.
        """
        if self._servers_cache is None or refresh:
            try:
                # fetch_all() from v2_servers.py returns the tuple directly
                result = self.servers.fetch_all()
                self._servers_cache = result # Already in ServerTuple format
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch servers from v2 API: {e}")
                if self._servers_cache is None: # Only raise if we have no cached data at all
                    raise VPNAPIError("Failed to fetch servers from v2 API") from e
            except VPNAPIError as e: # Catch VPNAPIError from fetch_all if parsing fails
                logger.error(f"Error processing server data from v2 API: {e}")
                if self._servers_cache is None:
                    raise # Re-raise if no cache

        if self._servers_cache is None:
            # This case should ideally be covered by the error handling above,
            # but as a safeguard:
            raise VPNAPIError("Server data could not be retrieved and no cache is available.")

        return self._servers_cache

    def _filter_servers_v2(
        self,
        servers_list: list[v2_servers.Server],
        country_code: str | None,
        group_identifier: str | None,
        technology_identifier: str | None,
    ) -> list[v2_servers.Server]:
        """Helper to filter v2 servers."""
        filtered = servers_list
        if country_code:
            filtered = [
                s
                for s in filtered
                if s.locations
                and any(
                    loc.country.code.upper() == country_code.upper()
                    for loc in s.locations
                )
            ]
        if group_identifier:
            filtered = [
                s
                for s in filtered
                if any(g.identifier == group_identifier for g in s.groups)
            ]
        if technology_identifier:
            filtered = [
                s
                for s in filtered
                if any(t.identifier == technology_identifier for t in s.technologies)
            ]
        return filtered

    def find_best_server(
        self,
        country_code: str | None = None,
        group_identifier: str | None = None,
        technology_identifier: str | None = None,
    ) -> v2_servers.Server:
        """Find the best server based on load and optional filters, using v2 API.

        Args:
            country_code: Two-letter country code (e.g., 'US').
            group_identifier: Group identifier (e.g., 'legacy_p2p').
            technology_identifier: Technology identifier (e.g., 'openvpn_udp').

        Returns:
            A v2_servers.Server object representing the best server.

        Raises:
            VPNAPIError: If no suitable server is found or API request fails.
        """
        try:
            # The first element of the tuple returned by get_servers() is the list of servers.
            all_v2_servers = self.get_servers(refresh=False)[0] # Use cached data if available for filtering

            filtered_v2_servers = self._filter_servers_v2(
                all_v2_servers, country_code, group_identifier, technology_identifier
            )

            if not filtered_v2_servers:
                criteria_parts = []
                if country_code: criteria_parts.append(f"country={country_code}")
                if group_identifier: criteria_parts.append(f"group={group_identifier}")
                if technology_identifier: criteria_parts.append(f"tech={technology_identifier}")
                criteria_str = ", ".join(criteria_parts) if criteria_parts else "any criteria"
                raise VPNAPIError(f"No v2 servers found matching: {criteria_str}")

            # Return the server with the minimum load
            return min(filtered_v2_servers, key=lambda s: s.load)

        except VPNAPIError: # Re-raise VPNAPIError if it's from get_servers or filtering
            raise
        except requests.exceptions.RequestException as e: # Catch potential errors from get_servers if refresh was forced
            logger.error(f"API request failed during find_best_server: {e}")
            raise VPNAPIError(f"Failed to find suitable server due to API error: {e}") from e
        except Exception as e: # Catch other unexpected errors
            logger.error(f"Unexpected error in find_best_server: {e}")
            raise VPNAPIError(f"Unexpected error finding best server: {e}") from e


    def get_server_stats(self, refresh_cache: bool = False) -> dict[str, Any]:
        """Get statistics about server availability using v2 API data.

        Args:
            refresh_cache: Whether to force a refresh of the server data cache.

        Returns:
            Dictionary containing various statistics about servers.

        Raises:
            VPNAPIError: If API requests fail and no statistics can be generated.
        """
        try:
            # Use the v2 API data
            servers, groups, _, locations, _ = self.get_servers(refresh=refresh_cache)

            # Create a map of country codes to countries
            countries_by_code: dict[str, v2_servers.Country] = {}
            for location_obj in locations: # Iterate over Location objects
                if location_obj.country and location_obj.country.code:
                    country_code = location_obj.country.code.upper()
                    if country_code not in countries_by_code:
                        countries_by_code[country_code] = location_obj.country

            # Count servers by country
            servers_by_country: dict[str, int] = {}
            for server_obj in servers: # Iterate over Server objects
                if not server_obj.locations:
                    continue
                for location_obj in server_obj.locations:
                    if location_obj.country and location_obj.country.code:
                        country_code = location_obj.country.code.upper()
                        servers_by_country[country_code] = servers_by_country.get(country_code, 0) + 1

            # Count servers by group
            servers_by_group: dict[str, int] = {}
            for group_obj in groups: # Iterate over Group objects
                if group_obj.identifier:
                    servers_by_group[group_obj.identifier] = len(
                        [
                            server_obj
                            for server_obj in servers # Iterate over Server objects
                            if any(g.identifier == group_obj.identifier for g in server_obj.groups)
                        ]
                    )

            return {
                "total_countries": len(countries_by_code),
                "total_servers": len(servers),
                "total_groups": len(groups),
                "servers_by_country": dict(
                    sorted(servers_by_country.items(), key=lambda item: item[1], reverse=True)
                ),
                "servers_by_group": servers_by_group,
            }

        except (VPNAPIError, requests.exceptions.RequestException) as e:
            logger.error(f"Failed to generate server statistics using v2 API: {e}")
            raise VPNAPIError(
                "Failed to generate server statistics using v2 API"
            ) from e

    def get_all_countries_from_v2(self, refresh_cache: bool = False) -> list[dict[str, str]]:
        """
        Retrieves a list of unique countries from the v2 server data.

        Args:
            refresh_cache: Whether to force a refresh of the server data cache.

        Returns:
            A list of dictionaries, where each dictionary represents a country
            and contains 'name' and 'code'.

        Raises:
            VPNAPIError: If server data cannot be fetched.
        """
        try:
            _, _, _, locations_data, _ = self.get_servers(refresh=refresh_cache)

            countries_set: set[tuple[str, str]] = set() # Use a set of tuples to store unique (name, code)
            for loc in locations_data:
                if loc.country and loc.country.name and loc.country.code:
                    countries_set.add((loc.country.name, loc.country.code.upper()))

            # Convert set of tuples to list of dicts
            return [{"name": name, "code": code} for name, code in sorted(list(countries_set))]

        except VPNAPIError:
            raise # Re-raise if get_servers fails
        except Exception as e:
            logger.error(f"Unexpected error extracting countries from v2 data: {e}")
            raise VPNAPIError("Failed to extract countries from v2 server data") from e
