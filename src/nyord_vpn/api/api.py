"""NordVPN API client for data retrieval and API interactions.

this_file: src/nyord_vpn/api/api.py

This module provides the NordVPNAPI class for interacting with NordVPN's API.
It serves as the central interface for all API operations, coordinating between
v1 and v2 endpoints with automatic fallback support.

Core Responsibilities:
1. Authentication with NordVPN API
2. Country and server information retrieval
3. Cache management for API responses
4. Location and city information lookup
5. API connectivity testing

Integration Points:
- Used by Client (core/client.py) for API operations
- Used by ServerManager (network/server.py) for server info
- Interacts with cache system in utils/utils.py
- Handles models defined in storage/models.py

The client implements automatic fallback to cached data when
API requests fail, and provides both raw and formatted data
access methods. This ensures continuous operation even during
API outages or rate limiting.
"""

import warnings
from typing import Any, TypeVar, cast

import requests
from loguru import logger

from nyord_vpn.api import (
    v1_countries,
    v1_groups,
    v1_recommendations,
    v1_technologies,
    v2_servers,
)
from nyord_vpn.exceptions import VPNAPIError

# Type aliases for clarity
ServerTuple = tuple[
    list[v2_servers.Server],
    list[v2_servers.Group],
    list[v2_servers.Service],
    list[v2_servers.Location],
    list[v2_servers.Technology],
]

T = TypeVar("T")


class NordVPNAPI:
    """Unified NordVPN API client.

    This class provides a single interface to access all NordVPN API endpoints,
    both v1 and v2. It handles initialization of individual clients and provides
    convenience methods for common operations.

    Attributes:
        timeout: Request timeout in seconds for all API calls.
        recommendations: Client for v1 recommendations API (deprecated).
        technologies: Client for v1 technologies API (deprecated).
        groups: Client for v1 groups API (deprecated).
        countries: Client for v1 countries API (deprecated).
        servers: Client for v2 servers API (preferred).

    """

    def __init__(self, timeout: int = 10) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds for all API calls.

        """
        self.timeout = timeout

        # Initialize individual clients
        self.recommendations = v1_recommendations.NordVPNRecommendationsV1(
            timeout=timeout
        )
        self.technologies = v1_technologies.NordVPNTechnologiesV1(timeout=timeout)
        self.groups = v1_groups.NordVPNGroupsV1(timeout=timeout)
        self.countries = v1_countries.NordVPNCountriesV1(timeout=timeout)
        self.servers = v2_servers.NordVPNServersV2(timeout=timeout)

        # Cache for API responses
        self._recommended_servers: list[v1_recommendations.RecommendedServer] | None = (
            None
        )
        self._technologies: list[v1_technologies.Technology] | None = None
        self._groups: list[v1_groups.Group] | None = None
        self._countries: list[v1_countries.Country] | None = None
        self._servers: ServerTuple | None = None

    def get_recommended_servers(
        self, *, refresh: bool = False
    ) -> list[v1_recommendations.RecommendedServer]:
        """Get recommended servers.

        This method is deprecated and uses the v1 API. Consider using find_best_server
        or get_servers instead, which use the v2 API.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of recommended servers.

        """
        warnings.warn(
            "get_recommended_servers is deprecated and uses the v1 API. "
            "Consider using find_best_server or get_servers instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self._recommended_servers is None or refresh:
            try:
                self._recommended_servers = self.recommendations.fetch_recommendations()
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch recommended servers: {e}")
                if self._recommended_servers is None:
                    # Only raise if we don't have cached data
                    raise VPNAPIError("Failed to fetch recommended servers") from e

        return self._recommended_servers

    def get_technologies(
        self, *, refresh: bool = False
    ) -> list[v1_technologies.Technology]:
        """Get available VPN technologies.

        This method is deprecated and uses the v1 API. Consider using get_servers
        instead, which uses the v2 API and includes technology information.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of VPN technologies.

        """
        warnings.warn(
            "get_technologies is deprecated and uses the v1 API. "
            "Consider using get_servers instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self._technologies is None or refresh:
            try:
                self._technologies = self.technologies.fetch_technologies()
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch technologies: {e}")
                if self._technologies is None:
                    # Only raise if we don't have cached data
                    raise VPNAPIError("Failed to fetch technologies") from e

        return self._technologies

    def get_groups(self, *, refresh: bool = False) -> list[v1_groups.Group]:
        """Get server groups.

        This method is deprecated and uses the v1 API. Consider using get_servers
        instead, which uses the v2 API and includes group information.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of server groups.

        """
        warnings.warn(
            "get_groups is deprecated and uses the v1 API. "
            "Consider using get_servers instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self._groups is None or refresh:
            try:
                self._groups = self.groups.fetch_groups()
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch groups: {e}")
                if self._groups is None:
                    # Only raise if we don't have cached data
                    raise VPNAPIError("Failed to fetch groups") from e

        return self._groups

    def get_countries(self, *, refresh: bool = False) -> list[v1_countries.Country]:
        """Get countries with server information.

        This method is deprecated and uses the v1 API. Consider using get_servers
        instead, which uses the v2 API and includes country information.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of countries.

        """
        warnings.warn(
            "get_countries is deprecated and uses the v1 API. "
            "Consider using get_servers instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self._countries is None or refresh:
            try:
                self._countries = self.countries.fetch_countries()
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch countries: {e}")
                if self._countries is None:
                    # Only raise if we don't have cached data
                    raise VPNAPIError("Failed to fetch countries") from e

        return self._countries

    def get_servers(self, *, refresh: bool = False) -> ServerTuple:
        """Get detailed server information.

        This method uses the v2 API to fetch comprehensive server information,
        including groups, services, locations, and technologies.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            Tuple of (servers, groups, services, locations, technologies).

        Raises:
            VPNAPIError: If the API request fails and no cached data is available.

        """
        if self._servers is None or refresh:
            try:
                result = self.servers.fetch_all()
                self._servers = cast("ServerTuple", result)
            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to fetch servers: {e}")
                if self._servers is None:
                    # Only raise if we don't have cached data
                    raise VPNAPIError("Failed to fetch servers") from e

        return self._servers

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

    def _filter_servers_v1(
        self,
        servers_list: list[v1_recommendations.RecommendedServer],
        country_code: str | None,
        group_identifier: str | None,
        technology_identifier: str | None,
    ) -> list[v1_recommendations.RecommendedServer]:
        """Helper to filter v1 servers."""
        filtered = servers_list
        if country_code:
            filtered = [
                s
                for s in filtered
                if s.locations and s.locations[0].country.code.upper() == country_code.upper()
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
        *,
        use_v2: bool = True,
    ) -> v1_recommendations.RecommendedServer | v2_servers.Server:
        """Find the best server based on load and optional filters."""
        if use_v2:
            try:
                all_v2_servers = self.get_servers()[0]
                filtered_v2_servers = self._filter_servers_v2(
                    all_v2_servers, country_code, group_identifier, technology_identifier
                )
                if filtered_v2_servers:
                    return min(filtered_v2_servers, key=lambda s: s.load)
                logger.warning(
                    "No v2 servers matched criteria (country=%s, group=%s, tech=%s). Falling back to v1.",
                    country_code,
                    group_identifier,
                    technology_identifier,
                )
            except (requests.exceptions.RequestException, VPNAPIError) as e:
                logger.warning(f"v2 API failed: {e}. Falling back to v1.")

        # Fallback to v1 API
        try:
            all_v1_servers = self.get_recommended_servers()
            filtered_v1_servers = self._filter_servers_v1(
                all_v1_servers, country_code, group_identifier, technology_identifier
            )
            if not filtered_v1_servers:
                criteria_parts = []
                if country_code:
                    criteria_parts.append(f"country={country_code}")
                if group_identifier:
                    criteria_parts.append(f"group={group_identifier}")
                if technology_identifier:
                    criteria_parts.append(f"tech={technology_identifier}")
                criteria_str = ", ".join(criteria_parts) if criteria_parts else "any"
                raise ValueError(f"No v1 servers found matching criteria: {criteria_str}")
            return min(filtered_v1_servers, key=lambda s: s.load)
        except (requests.exceptions.RequestException, VPNAPIError, ValueError) as e:
            # If ValueError came from _filter_servers_v1 not finding servers,
            # or API errors from get_recommended_servers
            raise VPNAPIError(f"Failed to find suitable server via v1/v2 APIs: {e}") from e


    def get_server_stats(self) -> dict[str, Any]:
        """Get statistics about server availability.

        This method combines data from both v1 and v2 APIs to provide
        comprehensive statistics about available servers.

        Returns:
            Dictionary containing various statistics about servers.

        Raises:
            VPNAPIError: If API requests fail and no statistics can be generated.

        """
        try:
            # Try v2 API first
            servers, groups, _, locations, _ = self.get_servers()

            # Create a map of country codes to countries
            countries_by_code = {}
            for location in locations:
                country_code = location.country.code
                if country_code not in countries_by_code:
                    countries_by_code[country_code] = location.country

            # Count servers by country
            servers_by_country = {}
            for server in servers:
                if not server.locations:
                    continue

                for location in server.locations:
                    country_code = location.country.code
                    if country_code not in servers_by_country:
                        servers_by_country[country_code] = 0
                    servers_by_country[country_code] += 1

            # Count servers by group
            servers_by_group = {}
            for group in groups:
                servers_by_group[group.identifier] = len(
                    [
                        server
                        for server in servers
                        if any(g.identifier == group.identifier for g in server.groups)
                    ]
                )

            return {
                "total_countries": len(countries_by_code),
                "total_servers": len(servers),
                "total_groups": len(groups),
                "servers_by_country": dict(
                    sorted(servers_by_country.items(), key=lambda x: x[1], reverse=True)
                ),
                "servers_by_group": servers_by_group,
            }

        except (VPNAPIError, requests.exceptions.RequestException) as e:
            # Fall back to v1 API
            logger.warning(f"Failed to generate stats from v2 API, trying v1: {e}")

            try:
                countries = self.get_countries()
                v1_groups = self.get_groups()

                return {
                    "total_countries": len(countries),
                    "total_servers": sum(country.server_count for country in countries),
                    "total_groups": len(v1_groups),
                    "servers_by_country": {
                        country.code: country.server_count
                        for country in sorted(
                            countries, key=lambda x: x.server_count, reverse=True
                        )
                    },
                    # We don't have accurate group data from v1 API
                    "servers_by_group": {group.identifier: 0 for group in v1_groups},
                }
            except (VPNAPIError, requests.exceptions.RequestException) as e2:
                raise VPNAPIError(
                    "Failed to generate server statistics using v1/v2 APIs"
                ) from e2
