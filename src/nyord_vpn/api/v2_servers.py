"""NordVPN API v2 servers endpoint.

this_file: src/nyord_vpn/api/v2_servers.py

This module provides access to the v2 servers endpoint of the NordVPN API.
It is the preferred interface for server information and should be used
instead of the v1 endpoints whenever possible.

The v2 servers API provides comprehensive information about available servers:
- Server locations and capabilities
- Current load and status
- Supported protocols and features
- Geographic information
"""

from datetime import datetime
from typing import Any, TypeVar, cast

from loguru import logger
import requests
from pydantic import BaseModel, TypeAdapter

from nyord_vpn.exceptions import VPNAPIError

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
SERVERS_V2_ENDPOINT = f"{NORDVPN_API_BASE}/v2/servers"
DEFAULT_TIMEOUT = 10  # seconds

# Type variables for type hints
T = TypeVar("T")


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
    name: str | None = None
    identifier: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    status: str | None = None
    metadata: list[TechnologyMetadata] | None = None

    class Config:
        """Model configuration for validation handling."""

        extra = "ignore"  # Ignore extra fields
        protected_namespaces = ()  # Allow arbitrary attribute access


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

    class Config:
        """Model configuration for validation handling."""

        extra = "ignore"  # Ignore extra fields
        protected_namespaces = ()  # Allow arbitrary attribute access


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

    Attributes:
        id: Unique identifier for the server
        created_at: When the server was first added
        updated_at: When the server was last updated
        name: Human-readable name of the server
        station: Server hostname
        ipv6_station: IPv6 hostname (if available)
        hostname: Full hostname of the server
        status: Current server status (e.g., "online", "maintenance")
        load: Current server load percentage (0-100)
        ips: List of IP addresses associated with this server
        specifications: Technical specifications of the server
        technologies: VPN technologies supported by this server
        groups: Server groups this server belongs to
        services: Services provided by this server
        locations: Geographic locations of this server

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
    group_ids: list[int] | None = None
    service_ids: list[int] | None = None
    location_ids: list[int] | None = None


class NordVPNServersV2:
    """Client for the NordVPN v2 servers API.

    This class provides methods to fetch and work with server information from
    the NordVPN v2 API. The v2 API provides a normalized data structure where
    server information and related data are separated to avoid redundancy.

    Attributes:
        timeout: Request timeout in seconds for API calls

    """

    def __init__(self, *, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        self.timeout = timeout
        self._type_adapters: dict[str, TypeAdapter] = {
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

        This method retrieves the full dataset from the v2 servers API and
        processes it into a structured format. It establishes relationships
        between servers and their related entities.

        Returns:
            A tuple containing lists of (servers, groups, services, locations, technologies).

        Raises:
            VPNAPIError: If the API request fails or returns invalid data.

        """
        try:
            response = requests.get(SERVERS_V2_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            # Parse each component using its type adapter
            parsed_data: dict[str, list[Any]] = {}
            for key, adapter in self._type_adapters.items():
                try:
                    parsed_data[key] = adapter.validate_python(data[key])
                except (KeyError, ValueError, TypeError) as err:
                    logger.error(f"Failed to parse {key} data: {err}")
                    raise VPNAPIError(
                        f"Failed to parse {key} data from v2 API",
                        details=str(err),
                        cause=err,
                    ) from err

            # Create lookup maps for efficient linking
            relationship_maps = {
                "groups": {group.id: group for group in parsed_data["groups"]},
                "services": {
                    service.id: service for service in parsed_data["services"]
                },
                "locations": {
                    location.id: location for location in parsed_data["locations"]
                },
            }

            # Link related objects to servers
            for server in parsed_data["servers"]:
                self._link_server_relations(server, relationship_maps)

            return (
                cast(list[Server], parsed_data["servers"]),
                cast(list[Group], parsed_data["groups"]),
                cast(list[Service], parsed_data["services"]),
                cast(list[Location], parsed_data["locations"]),
                cast(list[Technology], parsed_data["technologies"]),
            )

        except requests.exceptions.RequestException as error:
            logger.error(f"Failed to fetch NordVPN server data: {error}")
            raise VPNAPIError(
                "Failed to fetch server data from v2 API",
                details=str(error),
                cause=error,
            ) from error

    def _link_server_relations(
        self, server: Server, relationship_maps: dict[str, dict[int, Any]]
    ) -> None:
        """Link related objects (groups, services, locations) to a server.

        This method establishes the relationships between a server and its
        related entities by replacing the ID references with actual objects.

        Args:
            server: The server object to update with relationship links.
            relationship_maps: Dictionary containing the lookup maps for related objects.

        """
        # Link groups
        server.groups = [
            relationship_maps["groups"][group_id]
            for group_id in getattr(server, "group_ids", []) or []
            if group_id in relationship_maps["groups"]
        ]

        # Link services
        server.services = [
            relationship_maps["services"][service_id]
            for service_id in getattr(server, "service_ids", []) or []
            if service_id in relationship_maps["services"]
        ]

        # Link locations
        server.locations = [
            relationship_maps["locations"][location_id]
            for location_id in getattr(server, "location_ids", []) or []
            if location_id in relationship_maps["locations"]
        ]

        # Clean up ID lists
        for attr in ["group_ids", "service_ids", "location_ids"]:
            if hasattr(server, attr):
                delattr(server, attr)


def get_servers_by_country(servers: list[Server], country_code: str) -> list[Server]:
    """Filter servers by country code.

    This function filters a list of servers to include only those located
    in the specified country.

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

    This function filters a list of servers to include only those belonging
    to the specified group.

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
