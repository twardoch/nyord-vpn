"""NordVPN API v1 technologies endpoint.

this_file: src/nyord_vpn/api/v1_technologies.py

This module is deprecated and will be removed in a future version.
Please use the v2 API endpoints instead via the NordVPNAPI class.

This module provides access to the v1 technologies endpoint of the NordVPN API.
It is used for legacy compatibility and as a fallback when v2 endpoints fail.
The technologies API provides information about available VPN protocols and features.
"""

import warnings
from datetime import datetime
from loguru import logger
import requests
from pydantic import BaseModel

from nyord_vpn.exceptions import VPNAPIError

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
TECHNOLOGIES_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/technologies"
DEFAULT_TIMEOUT = 10  # seconds


# Display deprecation warning when the module is imported
warnings.warn(
    "The v1_technologies module is deprecated and will be removed in a future version. "
    "Please use the NordVPNAPI class from nyord_vpn.api.api instead.",
    DeprecationWarning,
    stacklevel=2,
)


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
            "NordVPNTechnologiesV1 is deprecated. Use NordVPNAPI instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.timeout = timeout

    def fetch_technologies(self) -> list[Technology]:
        """Fetch available VPN technologies from the v1 API.

        Returns:
            List of VPN technologies.

        Raises:
            VPNAPIError: If the API request fails or returns invalid data.

        """
        try:
            response = requests.get(TECHNOLOGIES_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [Technology.model_validate(tech) for tech in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN technologies: {e}")
            raise VPNAPIError(
                "Failed to fetch technologies from v1 API",
                details=str(e),
                cause=e,
            )
        except (ValueError, TypeError) as e:
            logger.error(f"Failed to parse NordVPN technologies: {e}")
            raise VPNAPIError(
                "Failed to parse technologies from v1 API",
                details=str(e),
                cause=e,
            )


def get_technology_by_identifier(
    technologies: list[Technology], identifier: str
) -> Technology:
    """Find a technology by its identifier.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

    Args:
        technologies: List of technologies to search.
        identifier: Technology identifier (e.g., 'wireguard_udp').

    Returns:
        The matching technology.

    Raises:
        ValueError: If no technology matches the identifier.

    """
    warnings.warn(
        "get_technology_by_identifier is deprecated. Use NordVPNAPI methods instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    for tech in technologies:
        if tech.identifier == identifier:
            return tech
    raise ValueError(f"No technology found with identifier: {identifier}")
