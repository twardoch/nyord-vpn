#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pydantic", "requests", "loguru"]
# ///
# this_file: src/nyord_vpn/api/v1-groups.py

"""NordVPN API v1 server groups client.

This module provides a clean interface to the NordVPN v1 server groups API endpoint.
The v1 groups API provides information about different server categories and types.
"""

from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
GROUPS_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/servers/groups"
DEFAULT_TIMEOUT = 10  # seconds


class GroupType(BaseModel):
    """Group type information."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str


class Group(BaseModel):
    """Server group information from the v1 API."""

    id: int
    created_at: datetime
    updated_at: datetime
    title: str
    identifier: str
    type: GroupType


class NordVPNGroupsV1:
    """Client for the NordVPN v1 server groups API.

    This class provides methods to fetch and work with server group information
    from the NordVPN v1 API.
    """

    def __init__(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        self.timeout = timeout

    def fetch_groups(self) -> list[Group]:
        """Fetch available server groups from the v1 API.

        Returns:
            List of server groups.

        Raises:
            requests.exceptions.RequestException: If the API request fails.

        """
        try:
            response = requests.get(GROUPS_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [Group.model_validate(group) for group in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN server groups: {e}")
            raise


def get_groups_by_type(groups: list[Group], type_identifier: str) -> list[Group]:
    """Filter groups by type identifier.

    Args:
        groups: List of groups to filter.
        type_identifier: Type identifier (e.g., 'legacy_group_category', 'regions').

    Returns:
        List of groups matching the type.

    """
    return [group for group in groups if group.type.identifier == type_identifier]


def get_group_by_identifier(groups: list[Group], identifier: str) -> Group:
    """Find a group by its identifier.

    Args:
        groups: List of groups to search.
        identifier: Group identifier (e.g., 'legacy_p2p', 'europe').

    Returns:
        The matching group.

    Raises:
        ValueError: If no group matches the identifier.

    """
    for group in groups:
        if group.identifier == identifier:
            return group
    raise ValueError(f"No group found with identifier: {identifier}")


if __name__ == "__main__":
    # Example usage
    client = NordVPNGroupsV1()
    try:
        groups = client.fetch_groups()

        # Print all available groups by type
        logger.info("Server groups by type:")
        for type_id in {group.type.identifier for group in groups}:
            type_groups = get_groups_by_type(groups, type_id)
            logger.info(f"\n{type_groups[0].type.title}:")
            for group in type_groups:
                logger.info(f"- {group.title} ({group.identifier})")

        # Example: Find specific group
        try:
            p2p_group = get_group_by_identifier(groups, "legacy_p2p")
            logger.info("\nP2P group details:")
            logger.info(f"Title: {p2p_group.title}")
            logger.info(f"Type: {p2p_group.type.title}")
            logger.info(f"Added: {p2p_group.created_at}")
        except ValueError as e:
            logger.error(e)

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch groups: {e}")
