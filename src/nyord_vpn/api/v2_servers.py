#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pydantic", "requests", "loguru"]
# ///
# this_file: src/nyord_vpn/api/v2-servers.py

"""NordVPN API v2 server information client.

This module provides a clean interface to the NordVPN v2 servers API endpoint.
The v2 API provides a normalized data structure where server information and related
data (groups, services, locations, technologies) are separated to avoid redundancy.
"""

from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel, TypeAdapter

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
SERVERS_V2_ENDPOINT = f"{NORDVPN_API_BASE}/v2/servers"
DEFAULT_TIMEOUT = 10  # seconds


class TechnologyMetadata(BaseModel):
    """Metadata associated with a technology.

    For example, a technology might have metadata about its public key or other
    configuration parameters.
    """

    name: str
    value: str


class Technology(BaseModel):
    """A VPN technology supported by NordVPN servers.

    Technologies represent different VPN protocols and configurations available
    on the servers (e.g., OpenVPN, IKEv2, etc.).
    """

    id: int
    name: str
    identifier: str
    created_at: datetime
    updated_at: datetime
    status: str | None = None
    metadata: list[TechnologyMetadata] | None = None


class IP(BaseModel):
    """IP address information for a server."""

    id: int
    ip: str
    version: int


class ServerIP(BaseModel):
    """Detailed IP configuration for a server including type and metadata."""

    id: int
    created_at: datetime
    updated_at: datetime
    server_id: int
    ip_id: int
    type: str
    ip: IP


class SpecificationValue(BaseModel):
    """Value for a server specification."""

    id: int
    value: str


class Specification(BaseModel):
    """Technical specification of a server capability."""

    id: int
    title: str
    identifier: str
    values: list[SpecificationValue]


class GroupType(BaseModel):
    """Type classification for server groups."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str


class Group(BaseModel):
    """Server group information (e.g., P2P, Standard VPN, etc.)."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str
    type: GroupType


class Service(BaseModel):
    """Service provided by the server."""

    id: int
    name: str
    identifier: str
    created_at: datetime
    updated_at: datetime


class City(BaseModel):
    """City location information for a server."""

    id: int
    name: str
    latitude: float
    longitude: float
    dns_name: str
    hub_score: int


class Country(BaseModel):
    """Country information including its primary city."""

    id: int
    name: str
    code: str
    city: City


class Location(BaseModel):
    """Geographical location information for a server."""

    id: int
    created_at: datetime
    updated_at: datetime
    latitude: float
    longitude: float
    country: Country


class Server(BaseModel):
    """NordVPN server information.

    This model represents a complete server entry from the v2 API, including
    all its relationships to other entities like locations, groups, and services.
    """

    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    station: str
    ipv6_station: str
    hostname: str
    status: str
    load: int
    ips: list[ServerIP]
    specifications: list[Specification]
    technologies: list[Technology]
    groups: list[Group] = []
    services: list[Service] = []
    locations: list[Location] = []


class NordVPNServersV2:
    """Client for the NordVPN v2 servers API.

    This class provides methods to fetch and work with server information from
    the NordVPN v2 API. The v2 API provides a normalized data structure where
    server information and related data are separated to avoid redundancy.
    """

    def __init__(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        self.timeout = timeout
        self._type_adapters = {
            "servers": TypeAdapter(list[Server]),
            "groups": TypeAdapter(list[Group]),
            "services": TypeAdapter(list[Service]),
            "locations": TypeAdapter(list[Location]),
            "technologies": TypeAdapter(list[Technology]),
        }

    def fetch_all(
        self,
    ) -> tuple[
        list[Server], list[Group], list[Service], list[Location], list[Technology]
    ]:
        """Fetch and parse all server data from the v2 API.

        Returns:
            A tuple containing lists of (servers, groups, services, locations, technologies).

        Raises:
            requests.exceptions.RequestException: If the API request fails.

        """
        try:
            response = requests.get(SERVERS_V2_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            # Parse each component using its type adapter
            parsed_data = {
                key: self._type_adapters[key].validate_python(data[key])
                for key in self._type_adapters
            }

            # Create lookup maps for efficient linking
            maps = {
                "groups": {g.id: g for g in parsed_data["groups"]},
                "services": {s.id: s for s in parsed_data["services"]},
                "locations": {l.id: l for l in parsed_data["locations"]},
            }

            # Link related objects to servers
            for server in parsed_data["servers"]:
                self._link_server_relations(server, maps)

            return (
                parsed_data["servers"],
                parsed_data["groups"],
                parsed_data["services"],
                parsed_data["locations"],
                parsed_data["technologies"],
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN server data: {e}")
            raise

    def _link_server_relations(self, server: Server, maps: dict) -> None:
        """Link related objects (groups, services, locations) to a server.

        Args:
            server: The server object to update.
            maps: Dictionary containing the lookup maps for related objects.

        """
        # Link groups
        server.groups = [
            maps["groups"][group_id]
            for group_id in getattr(server, "group_ids", [])
            if group_id in maps["groups"]
        ]

        # Link services
        server.services = [
            maps["services"][service_id]
            for service_id in getattr(server, "service_ids", [])
            if service_id in maps["services"]
        ]

        # Link locations
        server.locations = [
            maps["locations"][location_id]
            for location_id in getattr(server, "location_ids", [])
            if location_id in maps["locations"]
        ]

        # Clean up ID lists
        for attr in ["group_ids", "service_ids", "location_ids"]:
            if hasattr(server, attr):
                delattr(server, attr)


def get_servers_by_country(servers: list[Server], country_code: str) -> list[Server]:
    """Filter servers by country code.

    Args:
        servers: List of servers to filter.
        country_code: Two-letter country code (e.g., 'US', 'DE').

    Returns:
        List of servers in the specified country.

    """
    return [
        server
        for server in servers
        if server.locations
        and server.locations[0].country.code.upper() == country_code.upper()
    ]


def get_servers_by_group(servers: list[Server], group_identifier: str) -> list[Server]:
    """Filter servers by group identifier.

    Args:
        servers: List of servers to filter.
        group_identifier: Group identifier (e.g., 'legacy_p2p').

    Returns:
        List of servers in the specified group.

    """
    return [
        server
        for server in servers
        if any(group.identifier == group_identifier for group in server.groups)
    ]


if __name__ == "__main__":
    # Example usage
    client = NordVPNServersV2()
    try:
        servers, groups, services, locations, technologies = client.fetch_all()

        # Print some server information
        for server in servers[:5]:  # First 5 servers
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
        us_servers = get_servers_by_country(servers, "US")
        logger.info(f"\nNumber of US servers: {len(us_servers)}")

        # Example: Find P2P servers
        p2p_servers = get_servers_by_group(servers, "legacy_p2p")
        logger.info(f"\nNumber of P2P servers: {len(p2p_servers)}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch server data: {e}")
