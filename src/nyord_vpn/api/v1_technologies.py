#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pydantic", "requests", "loguru"]
# ///
# this_file: src/nyord_vpn/api/v1-technologies.py

"""NordVPN API v1 technologies client.

This module provides a clean interface to the NordVPN v1 technologies API endpoint.
The v1 technologies API provides information about available VPN technologies and protocols.
"""

from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
TECHNOLOGIES_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/technologies"
DEFAULT_TIMEOUT = 10  # seconds


class Technology(BaseModel):
    """VPN technology information from the v1 API."""

    id: int
    name: str
    identifier: str
    internal_identifier: str
    created_at: datetime
    updated_at: datetime


class NordVPNTechnologiesV1:
    """Client for the NordVPN v1 technologies API.

    This class provides methods to fetch and work with VPN technology information
    from the NordVPN v1 API.
    """

    def __init__(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        self.timeout = timeout

    def fetch_technologies(self) -> list[Technology]:
        """Fetch available VPN technologies from the v1 API.

        Returns:
            List of VPN technologies.

        Raises:
            requests.exceptions.RequestException: If the API request fails.

        """
        try:
            response = requests.get(TECHNOLOGIES_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [Technology.model_validate(tech) for tech in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN technologies: {e}")
            raise


def get_technology_by_identifier(
    technologies: list[Technology], identifier: str
) -> Technology:
    """Find a technology by its identifier.

    Args:
        technologies: List of technologies to search.
        identifier: Technology identifier (e.g., 'wireguard_udp').

    Returns:
        The matching technology.

    Raises:
        ValueError: If no technology matches the identifier.

    """
    for tech in technologies:
        if tech.identifier == identifier:
            return tech
    raise ValueError(f"No technology found with identifier: {identifier}")


if __name__ == "__main__":
    # Example usage
    client = NordVPNTechnologiesV1()
    try:
        technologies = client.fetch_technologies()

        # Print all available technologies
        logger.info("Available VPN technologies:")
        for tech in technologies:
            logger.info(f"- {tech.name} ({tech.identifier})")
            logger.info(f"  Internal ID: {tech.internal_identifier}")
            logger.info(f"  Added: {tech.created_at}")
            logger.info("---")

        # Example: Find specific technology
        try:
            wireguard = get_technology_by_identifier(technologies, "wireguard_udp")
            logger.info("\nWireGuard details:")
            logger.info(f"Name: {wireguard.name}")
            logger.info(f"Internal identifier: {wireguard.internal_identifier}")
            logger.info(f"Added: {wireguard.created_at}")
        except ValueError as e:
            logger.error(e)

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch technologies: {e}")
