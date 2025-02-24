"""NordVPN API v1 recommendations endpoint.

this_file: src/nyord_vpn/api/v1_recommendations.py

This module is deprecated and will be removed in a future version.
Please use the v2 API endpoints instead via the NordVPNAPI class.

This module provides access to the v1 recommendations endpoint of the NordVPN API.
It is used for legacy compatibility and as a fallback when v2 endpoints fail.
The recommendations API suggests optimal servers based on load and location.
"""

import warnings
from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel

from nyord_vpn.exceptions import VPNAPIError

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
RECOMMENDATIONS_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/servers/recommendations"
DEFAULT_TIMEOUT = 10  # seconds


# Display deprecation warning when the module is imported
warnings.warn(
    "The v1_recommendations module is deprecated and will be removed in a future version. "
    "Please use the NordVPNAPI class from nyord_vpn.api.api instead.",
    DeprecationWarning,
    stacklevel=2,
)


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

    Note:
        This class is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class from nyord_vpn.api.api instead.

    """

    def __init__(self, *, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        warnings.warn(
            "NordVPNRecommendationsV1 is deprecated. Use NordVPNAPI instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.timeout = timeout

    def fetch_recommendations(self) -> list[RecommendedServer]:
        """Fetch recommended servers from the v1 API.

        Returns:
            List of recommended servers.

        Raises:
            VPNAPIError: If the API request fails or returns invalid data.

        """
        try:
            response = requests.get(RECOMMENDATIONS_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [RecommendedServer.model_validate(server) for server in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN server recommendations: {e}")
            raise VPNAPIError(
                "Failed to fetch recommended servers from v1 API",
                details=str(e),
                cause=e,
            )
        except (ValueError, TypeError) as e:
            logger.error(f"Failed to parse NordVPN server recommendations: {e}")
            raise VPNAPIError(
                "Failed to parse recommended servers from v1 API",
                details=str(e),
                cause=e,
            )


def get_recommendations_by_country(
    servers: list[RecommendedServer], country_code: str
) -> list[RecommendedServer]:
    """Filter recommended servers by country code.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI.find_best_server method instead.

    Args:
        servers: List of servers to filter.
        country_code: Two-letter country code (e.g., 'US', 'DE').

    Returns:
        List of recommended servers in the specified country.

    """
    warnings.warn(
        "get_recommendations_by_country is deprecated. Use NordVPNAPI.find_best_server instead.",
        DeprecationWarning,
        stacklevel=2,
    )
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

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI.find_best_server method instead.

    Args:
        servers: List of servers to filter.
        group_identifier: Group identifier (e.g., 'legacy_p2p').

    Returns:
        List of recommended servers in the specified group.

    """
    warnings.warn(
        "get_recommendations_by_group is deprecated. Use NordVPNAPI.find_best_server instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return [
        server
        for server in servers
        if any(group.identifier == group_identifier for group in server.groups)
    ]
