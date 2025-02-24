#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pydantic", "requests", "loguru"]
# ///
# this_file: src/nyord_vpn/api/v1-recommendations.py

"""NordVPN API v1 server recommendations client.

This module provides a clean interface to the NordVPN v1 server recommendations API endpoint.
The v1 recommendations API provides a list of recommended servers based on current load and status.
"""

from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
RECOMMENDATIONS_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/servers/recommendations"
DEFAULT_TIMEOUT = 10  # seconds


class City(BaseModel):
    """City location information."""

    id: int
    name: str
    latitude: float
    longitude: float
    dns_name: str
    hub_score: int


class Country(BaseModel):
    """Country information."""

    id: int
    name: str
    code: str
    city: City


class Location(BaseModel):
    """Geographical location information."""

    id: int
    created_at: datetime
    updated_at: datetime
    latitude: float
    longitude: float
    country: Country


class Service(BaseModel):
    """Service provided by the server."""

    id: int
    name: str
    identifier: str
    created_at: datetime
    updated_at: datetime


class TechnologyMetadata(BaseModel):
    """Technology metadata."""

    name: str
    value: str


class TechnologyPivot(BaseModel):
    """Technology pivot information."""

    technology_id: int
    server_id: int
    status: str


class Technology(BaseModel):
    """VPN technology information."""

    id: int
    name: str
    identifier: str
    created_at: datetime
    updated_at: datetime
    metadata: list[TechnologyMetadata] | None = []
    pivot: TechnologyPivot


class GroupType(BaseModel):
    """Group type information."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str


class Group(BaseModel):
    """Server group information."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str
    type: GroupType


class SpecificationValue(BaseModel):
    """Specification value."""

    id: int
    value: str


class Specification(BaseModel):
    """Server specification."""

    id: int
    title: str
    identifier: str
    values: list[SpecificationValue]


class IP(BaseModel):
    """IP address information."""

    id: int
    ip: str
    version: int


class ServerIP(BaseModel):
    """Server IP configuration."""

    id: int
    created_at: datetime
    updated_at: datetime
    server_id: int
    ip_id: int
    type: str
    ip: IP


class RecommendedServer(BaseModel):
    """Recommended server information from the v1 API."""

    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    station: str
    ipv6_station: str = ""
    hostname: str
    load: int
    status: str
    locations: list[Location]
    services: list[Service]
    technologies: list[Technology]
    groups: list[Group]
    specifications: list[Specification]
    ips: list[ServerIP]


class NordVPNRecommendationsV1:
    """Client for the NordVPN v1 server recommendations API.

    This class provides methods to fetch and work with recommended server information
    from the NordVPN v1 API.
    """

    def __init__(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        self.timeout = timeout

    def fetch_recommendations(self) -> list[RecommendedServer]:
        """Fetch recommended servers from the v1 API.

        Returns:
            List of recommended servers.

        Raises:
            requests.exceptions.RequestException: If the API request fails.

        """
        try:
            response = requests.get(RECOMMENDATIONS_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [RecommendedServer.model_validate(server) for server in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN server recommendations: {e}")
            raise


def get_recommendations_by_country(
    servers: list[RecommendedServer], country_code: str
) -> list[RecommendedServer]:
    """Filter recommended servers by country code.

    Args:
        servers: List of servers to filter.
        country_code: Two-letter country code (e.g., 'US', 'DE').

    Returns:
        List of recommended servers in the specified country.

    """
    return [
        server
        for server in servers
        if server.locations
        and server.locations[0].country.code.upper() == country_code.upper()
    ]


def get_recommendations_by_group(
    servers: list[RecommendedServer], group_identifier: str
) -> list[RecommendedServer]:
    """Filter recommended servers by group identifier.

    Args:
        servers: List of servers to filter.
        group_identifier: Group identifier (e.g., 'legacy_p2p').

    Returns:
        List of recommended servers in the specified group.

    """
    return [
        server
        for server in servers
        if any(group.identifier == group_identifier for group in server.groups)
    ]


if __name__ == "__main__":
    # Example usage
    client = NordVPNRecommendationsV1()
    try:
        recommended_servers = client.fetch_recommendations()

        # Print some server information
        for server in recommended_servers[:5]:  # First 5 servers
            logger.info(
                f"Server: {server.name} ({server.hostname}) - Load: {server.load}%"
            )
            if server.locations:
                loc = server.locations[0]
                logger.info(f"  Location: {loc.country.name}, {loc.country.city.name}")
            if server.groups:
                logger.info(
                    f"  Groups: {', '.join(group.title for group in server.groups)}"
                )
            if server.services:
                logger.info(
                    f"  Services: {', '.join(service.name for service in server.services)}"
                )
            logger.info("---")

        # Example: Find US servers
        us_servers = get_recommendations_by_country(recommended_servers, "US")
        logger.info(f"\nNumber of US recommended servers: {len(us_servers)}")

        # Example: Find P2P servers
        p2p_servers = get_recommendations_by_group(recommended_servers, "legacy_p2p")
        logger.info(f"\nNumber of recommended P2P servers: {len(p2p_servers)}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch server recommendations: {e}")
