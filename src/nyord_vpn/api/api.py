#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pydantic", "requests", "loguru"]
# ///
# this_file: src/nyord_vpn/api/api.py

"""NordVPN API client.

This module provides a unified interface to all NordVPN API endpoints.
It aggregates functionality from both v1 and v2 API versions.
"""

from typing import cast
from loguru import logger

import v1_recommendations
import v1_technologies
import v1_groups
import v1_countries
import v2_servers

# Type aliases for clarity
ServerTuple = tuple[
    list[v2_servers.Server],
    list[v2_servers.Group],
    list[v2_servers.Service],
    list[v2_servers.Location],
    list[v2_servers.Technology],
]


class NordVPNAPI:
    """Unified NordVPN API client.

    This class provides a single interface to access all NordVPN API endpoints,
    both v1 and v2. It handles initialization of individual clients and provides
    convenience methods for common operations.
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
        self, refresh: bool = False
    ) -> list[v1_recommendations.RecommendedServer]:
        """Get recommended servers.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of recommended servers.

        """
        if self._recommended_servers is None or refresh:
            self._recommended_servers = self.recommendations.fetch_recommendations()
        return self._recommended_servers

    def get_technologies(
        self, refresh: bool = False
    ) -> list[v1_technologies.Technology]:
        """Get available VPN technologies.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of VPN technologies.

        """
        if self._technologies is None or refresh:
            self._technologies = self.technologies.fetch_technologies()
        return self._technologies

    def get_groups(self, refresh: bool = False) -> list[v1_groups.Group]:
        """Get server groups.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of server groups.

        """
        if self._groups is None or refresh:
            self._groups = self.groups.fetch_groups()
        return self._groups

    def get_countries(self, refresh: bool = False) -> list[v1_countries.Country]:
        """Get countries with server information.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            List of countries.

        """
        if self._countries is None or refresh:
            self._countries = self.countries.fetch_countries()
        return self._countries

    def get_servers(self, refresh: bool = False) -> ServerTuple:
        """Get detailed server information.

        Args:
            refresh: Whether to force refresh the cache.

        Returns:
            Tuple of (servers, groups, services, locations, technologies).

        """
        if self._servers is None or refresh:
            result = self.servers.fetch_all()
            self._servers = cast(ServerTuple, result)
        return self._servers

    def find_best_server(
        self, country_code: str | None = None, group_identifier: str | None = None
    ) -> v1_recommendations.RecommendedServer:
        """Find the best server based on load and optional filters.

        Args:
            country_code: Optional two-letter country code to filter by.
            group_identifier: Optional group identifier to filter by.

        Returns:
            The recommended server with the lowest load matching the criteria.

        Raises:
            ValueError: If no servers match the criteria.

        """
        servers = self.get_recommended_servers()

        if country_code:
            servers = [
                server
                for server in servers
                if server.locations
                and server.locations[0].country.code.upper() == country_code.upper()
            ]

        if group_identifier:
            servers = [
                server
                for server in servers
                if any(group.identifier == group_identifier for group in server.groups)
            ]

        if not servers:
            raise ValueError(
                f"No servers found matching criteria: "
                f"country_code={country_code}, group_identifier={group_identifier}"
            )

        return min(servers, key=lambda s: s.load)

    def get_server_stats(self) -> dict:
        """Get statistics about server availability.

        Returns:
            Dictionary containing various statistics about servers.

        """
        countries = self.get_countries()
        servers = self.get_servers()[0]
        groups = self.get_groups()

        return {
            "total_countries": len(countries),
            "total_servers": len(servers),
            "total_groups": len(groups),
            "servers_by_country": {
                country.code: country.server_count
                for country in sorted(
                    countries, key=lambda x: x.server_count, reverse=True
                )
            },
            "servers_by_group": {
                group.identifier: len(
                    [
                        server
                        for server in servers
                        if any(g.identifier == group.identifier for g in server.groups)
                    ]
                )
                for group in groups
            },
        }


if __name__ == "__main__":
    # Example usage
    api = NordVPNAPI()
    try:
        # Get server statistics
        stats = api.get_server_stats()
        logger.info("\nNordVPN Server Statistics:")
        logger.info(f"Total Countries: {stats['total_countries']}")
        logger.info(f"Total Servers: {stats['total_servers']}")
        logger.info(f"Total Groups: {stats['total_groups']}")

        logger.info("\nTop 5 Countries by Server Count:")
        for code, count in list(stats["servers_by_country"].items())[:5]:
            logger.info(f"{code}: {count} servers")

        logger.info("\nServers by Group:")
        for group, count in stats["servers_by_group"].items():
            logger.info(f"{group}: {count} servers")

        # Find best server example
        try:
            best_us_p2p = api.find_best_server(
                country_code="US", group_identifier="legacy_p2p"
            )
            logger.info("\nBest US P2P Server:")
            logger.info(f"Name: {best_us_p2p.name}")
            logger.info(f"Hostname: {best_us_p2p.hostname}")
            logger.info(f"Load: {best_us_p2p.load}%")
        except ValueError as e:
            logger.error(e)

    except Exception as e:
        logger.error(f"Error accessing NordVPN API: {e}")
