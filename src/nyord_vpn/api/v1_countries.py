#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pydantic", "requests", "loguru"]
# ///
# this_file: src/nyord_vpn/api/v1-countries.py

"""NordVPN API v1 countries client.

This module provides a clean interface to the NordVPN v1 countries API endpoint.
The v1 countries API provides information about server locations and availability by country.
"""

from loguru import logger
import requests
from pydantic import BaseModel

# Constants
NORDVPN_API_BASE = "https://api.nordvpn.com"
COUNTRIES_V1_ENDPOINT = f"{NORDVPN_API_BASE}/v1/servers/countries"
DEFAULT_TIMEOUT = 10  # seconds


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
    """

    def __init__(self, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Initialize the API client.

        Args:
            timeout: Request timeout in seconds.

        """
        self.timeout = timeout

    def fetch_countries(self) -> list[Country]:
        """Fetch available countries and their server information from the v1 API.

        Returns:
            List of countries with server information.

        Raises:
            requests.exceptions.RequestException: If the API request fails.

        """
        try:
            response = requests.get(COUNTRIES_V1_ENDPOINT, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            return [Country.model_validate(country) for country in data]

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NordVPN countries: {e}")
            raise


def get_country_by_code(countries: list[Country], country_code: str) -> Country:
    """Find a country by its code.

    Args:
        countries: List of countries to search.
        country_code: Two-letter country code (e.g., 'US', 'DE').

    Returns:
        The matching country.

    Raises:
        ValueError: If no country matches the code.

    """
    for country in countries:
        if country.code.upper() == country_code.upper():
            return country
    raise ValueError(f"No country found with code: {country_code}")


def get_countries_by_min_servers(
    countries: list[Country], min_servers: int
) -> list[Country]:
    """Filter countries by minimum number of servers.

    Args:
        countries: List of countries to filter.
        min_servers: Minimum number of servers required.

    Returns:
        List of countries with at least the specified number of servers.

    """
    return [country for country in countries if country.server_count >= min_servers]


def get_city_by_name(country: Country, city_name: str) -> City:
    """Find a city by name within a country.

    Args:
        country: Country to search in.
        city_name: Name of the city.

    Returns:
        The matching city.

    Raises:
        ValueError: If no city matches the name.

    """
    for city in country.cities:
        if city.name.lower() == city_name.lower():
            return city
    raise ValueError(f"No city found with name '{city_name}' in {country.name}")


if __name__ == "__main__":
    # Example usage
    client = NordVPNCountriesV1()
    try:
        countries = client.fetch_countries()

        # Print summary of server availability by country
        logger.info("Server availability by country:")
        for country in sorted(countries, key=lambda x: x.server_count, reverse=True)[
            :10
        ]:
            logger.info(
                f"{country.name} ({country.code}): {country.server_count} servers"
            )
            for city in country.cities:
                logger.info(f"  - {city.name}: {city.server_count} servers")

        # Example: Find countries with many servers
        large_countries = get_countries_by_min_servers(countries, 100)
        logger.info(f"\nCountries with 100+ servers: {len(large_countries)}")
        for country in large_countries:
            logger.info(f"- {country.name}: {country.server_count} servers")

        # Example: Get specific country and city details
        try:
            us = get_country_by_code(countries, "US")
            nyc = get_city_by_name(us, "New York")
            logger.info("\nNew York server details:")
            logger.info(f"Total servers: {nyc.server_count}")
            logger.info(f"Location: {nyc.latitude}, {nyc.longitude}")
            logger.info(f"DNS name: {nyc.dns_name}")
        except ValueError as e:
            logger.error(e)

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch countries: {e}")
