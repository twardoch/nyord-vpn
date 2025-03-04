"""NordVPN API v1 countries endpoint.

this_file: src/nyord_vpn/api/v1_countries.py

This module is deprecated and will be removed in a future version.
Please use the v2 API endpoints instead via the NordVPNAPI class.

This module provides access to the v1 countries endpoint of the NordVPN API.
It is used for legacy compatibility and as a fallback when v2 endpoints fail.
"""

import warnings

import requests
from loguru import logger
from pydantic import BaseModel

from nyord_vpn.exceptions import VPNAPIError

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
COUNTRIES_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/servers/countries"
DEFAULT_TIMEOUT = 10  # seconds


# Display deprecation warning when the module is imported
warnings.warn(
    "The v1_countries module is deprecated and will be removed in a future version. "
    "Please use the NordVPNAPI class from nyord_vpn.api.api instead.",
    DeprecationWarning,
    stacklevel=2,
)


class City(BaseModel):
    """City information."""

    id: int
    name: str
    latitude: float
    longitude: float
    dns_name: str
    hub_score: int
    server_count: int


class Country(BaseModel):
    """Country information from the v1 API."""

    id: int
    name: str
    code: str
    server_count: int
    cities: list[City]


class NordVPNCountriesV1:
    """Client for the NordVPN v1 countries API.

    This class provides methods to fetch and work with country and server location
    information from the NordVPN v1 API.

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
            "NordVPNCountriesV1 is deprecated. Use NordVPNAPI instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.timeout = timeout

    def fetch_countries(self) -> list[Country]:
        """Fetch available countries and their server information from the v1 API.

        Returns:
            List of countries with server information.

        Raises:
            VPNAPIError: If the API request fails or returns invalid data.

        """
        try:
            response = requests.get(COUNTRIES_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [Country.model_validate(country) for country in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN countries: {e}")
            raise VPNAPIError(
                "Failed to fetch countries from v1 API",
                details=str(e),
                cause=e,
            )
        except (ValueError, TypeError) as e:
            logger.error(f"Failed to parse NordVPN countries: {e}")
            raise VPNAPIError(
                "Failed to parse countries from v1 API",
                details=str(e),
                cause=e,
            )


def get_country_by_code(countries: list[Country], country_code: str) -> Country:
    """Find a country by its code.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

    Args:
        countries: List of countries to search.
        country_code: Two-letter country code (e.g., 'US', 'DE').

    Returns:
        The matching country.

    Raises:
        ValueError: If no country matches the code.

    """
    warnings.warn(
        "get_country_by_code is deprecated. Use NordVPNAPI methods instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    for country in countries:
        if country.code.upper() == country_code.upper():
            return country
    raise ValueError(f"No country found with code: {country_code}")


def get_countries_by_min_servers(
    countries: list[Country], min_servers: int
) -> list[Country]:
    """Filter countries by minimum number of servers.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

    Args:
        countries: List of countries to filter.
        min_servers: Minimum number of servers required.

    Returns:
        List of countries with at least the specified number of servers.

    """
    warnings.warn(
        "get_countries_by_min_servers is deprecated. Use NordVPNAPI methods instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return [country for country in countries if country.server_count >= min_servers]


def get_city_by_name(country: Country, city_name: str) -> City:
    """Find a city by name within a country.

    Note:
        This function is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

    Args:
        country: Country to search in.
        city_name: Name of the city.

    Returns:
        The matching city.

    Raises:
        ValueError: If no city matches the name.

    """
    warnings.warn(
        "get_city_by_name is deprecated. Use NordVPNAPI methods instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    for city in country.cities:
        if city.name.lower() == city_name.lower():
            return city
    raise ValueError(f"No city found with name '{city_name}' in {country.name}")
