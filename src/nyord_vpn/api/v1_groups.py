"""NordVPN API v1 groups endpoint.

this_file: src/nyord_vpn/api/v1_groups.py

This module is deprecated and will be removed in a future version.
Please use the v2 API endpoints instead via the NordVPNAPI class.

This module provides access to the v1 groups endpoint of the NordVPN API.
It is used for legacy compatibility and as a fallback when v2 endpoints fail.
Groups represent server categories like P2P, Double VPN, etc.
"""

import warnings
from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel

from nyord_vpn.exceptions import VPNAPIError

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
GROUPS_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/servers/groups"
DEFAULT_TIMEOUT = 10  # seconds


# Display deprecation warning when the module is imported
warnings.warn(
    "The v1_groups module is deprecated and will be removed in a future version. "
    "Please use the NordVPNAPI class from nyord_vpn.api.api instead.",
    DeprecationWarning,
    stacklevel=2,
)


class GroupType(BaseModel):
    """Group type information."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str

    class Config:
        """Model configuration for validation handling."""

        extra = "ignore"  # Ignore extra fields
        protected_namespaces = ()  # Allow arbitrary attribute access


class Group(BaseModel):
    """Server group information from the v1 API."""

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


class NordVPNGroupsV1:
    """Client for the NordVPN v1 server groups API.

    This class provides methods to fetch and work with server group information
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
            "NordVPNGroupsV1 is deprecated. Use NordVPNAPI instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.timeout = timeout

    def fetch_groups(self) -> list[Group]:
        """Fetch available server groups from the v1 API.

        Returns:
            List of server groups.

        Raises:
            VPNAPIError: If the API request fails or returns invalid data.

        """
        try:
            response = requests.get(GROUPS_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [Group.model_validate(group) for group in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN server groups: {e}")
            raise VPNAPIError(
                "Failed to fetch server groups from v1 API",
                details=str(e),
                cause=e,
            )
        except (ValueError, TypeError) as e:
            logger.error(f"Failed to parse NordVPN server groups: {e}")
            raise VPNAPIError(
                "Failed to parse server groups from v1 API",
                details=str(e),
                cause=e,
            )


def get_groups_by_type(groups: list[Group], type_identifier: str) -> list[Group]:
    """Filter groups by type identifier.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

    Args:
        groups: List of groups to filter.
        type_identifier: Type identifier (e.g., 'legacy_group_category', 'regions').

    Returns:
        List of groups matching the type.

    """
    warnings.warn(
        "get_groups_by_type is deprecated. Use NordVPNAPI methods instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return [group for group in groups if group.type.identifier == type_identifier]


def get_group_by_identifier(groups: list[Group], identifier: str) -> Group:
    """Find a group by its identifier.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

    Args:
        groups: List of groups to search.
        identifier: Group identifier (e.g., 'legacy_p2p', 'europe').

    Returns:
        The matching group.

    Raises:
        ValueError: If no group matches the identifier.

    """
    warnings.warn(
        "get_group_by_identifier is deprecated. Use NordVPNAPI methods instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    for group in groups:
        if group.identifier == identifier:
            return group
    raise ValueError(f"No group found with identifier: {identifier}")
