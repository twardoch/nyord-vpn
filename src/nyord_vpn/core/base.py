"""Base NordVPN client implementation.

this_file: src/nyord_vpn/core/base.py

This module contains the base NordVPN client class that handles:
- Country list management
- Cache handling
- Location lookup
- API interaction

DEPRECATED: This module is deprecated and will be removed in a future version.
Please use the NordVPNAPI class from nyord_vpn.api.api instead.

This class is extended by the main Client class to add connection functionality.
"""

import sys
import warnings

from loguru import logger

from nyord_vpn.network.country import get_cached_countries
from nyord_vpn.storage.models import City, Country, CountryCache
from nyord_vpn.utils.utils import CACHE_FILE

# Display deprecation warning when the module is imported
warnings.warn(
    "The NordVPNClient class is deprecated and will be removed in a future version. "
    "Please use the NordVPNAPI class from nyord_vpn.api.api instead.",
    DeprecationWarning,
    stacklevel=2,
)

# Fallback data in case API is unreachable
FALLBACK_DATA: CountryCache = {
    "countries": [
        {
            "cities": [
                {
                    "dns_name": "new-york",
                    "hub_score": 0,
                    "id": 8971718,
                    "latitude": 40.7141667,
                    "longitude": -74.0063889,
                    "name": "New York",
                    "serverCount": 529,
                },
            ],
            "code": "US",
            "id": 228,
            "name": "United States",
            "serverCount": 529,
        },
        {
            "cities": [
                {
                    "dns_name": "london",
                    "hub_score": 0,
                    "id": 2989907,
                    "latitude": 51.514125,
                    "longitude": -0.093689,
                    "name": "London",
                    "serverCount": 360,
                },
            ],
            "code": "GB",
            "id": 78,
            "name": "United Kingdom",
            "serverCount": 360,
        },
        {
            "cities": [
                {
                    "dns_name": "berlin",
                    "hub_score": 0,
                    "id": 2811287,
                    "latitude": 52.5186,
                    "longitude": 13.4083,
                    "name": "Berlin",
                    "serverCount": 225,
                },
            ],
            "code": "DE",
            "id": 65,
            "name": "Germany",
            "serverCount": 225,
        },
    ],
    "last_updated": "1970-01-01T00:00:00Z",
}


class NordVPNClient:
    """Base NordVPN client for managing country data and API interactions.

    DEPRECATED: This class is deprecated and will be removed in a future version.
    Please use the NordVPNAPI class from nyord_vpn.api.api instead.
    """

    BASE_API_URL: str = "https://api.nordvpn.com/v1"

    def __init__(self, username: str, password: str, *, verbose: bool = False) -> None:
        """Initialize the NordVPN client.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class from nyord_vpn.api.api instead.

        Args:
            username: NordVPN account username.
            password: NordVPN account password.
            verbose: Whether to enable verbose logging.

        """
        warnings.warn(
            "NordVPNClient is deprecated. Use NordVPNAPI from nyord_vpn.api.api instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        self.username = username
        self.password = password
        self.verbose = verbose
        self.logger = logger
        self.cache_file = CACHE_FILE
        self.countries = self._load_countries()
        self.logger.add(sys.stdout, level="DEBUG" if self.verbose else "INFO")

    def _load_countries(self) -> list[Country]:
        """Load country data from cache or fallback data.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class from nyord_vpn.api.api instead.

        Returns:
            List of countries with their information.

        """
        cached = get_cached_countries()
        if cached:
            return cached["countries"]
        return FALLBACK_DATA["countries"]

    def get_country_by_code(self, code: str) -> Country | None:
        """Find a country by its code.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class from nyord_vpn.api.api instead.

        Args:
            code: Two-letter country code (e.g., 'US', 'DE').

        Returns:
            The country information if found, None otherwise.

        """
        warnings.warn(
            "get_country_by_code is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        code = code.upper()
        for country in self.countries:
            if country["code"] == code:
                return country
        return None

    def get_country_by_name(self, name: str) -> Country | None:
        """Find a country by its name.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class from nyord_vpn.api.api instead.

        Args:
            name: Country name (case insensitive).

        Returns:
            The country information if found, None otherwise.

        """
        warnings.warn(
            "get_country_by_name is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        name = name.lower()
        for country in self.countries:
            if country["name"].lower() == name:
                return country
        return None

    def get_available_locations(self) -> list[str]:
        """Get a formatted list of available locations.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class from nyord_vpn.api.api instead.

        Returns:
            Formatted list of available locations.

        """
        warnings.warn(
            "get_available_locations is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        locations = []
        for country in sorted(self.countries, key=lambda x: x["name"]):
            total_servers = country["serverCount"]
            locations.append(
                f"{country['name']} ({country['code'].lower()}) - {total_servers} servers"
            )
            locations.extend(
                f"  {city['name']} - {city['serverCount']} servers"
                for city in sorted(country["cities"], key=lambda x: x["name"])
            )
        return locations

    def get_best_city(self, country_code: str) -> City | None:
        """Get the best city in a country for VPN connection.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the find_best_server method from NordVPNAPI class instead.

        Args:
            country_code: Two-letter country code (e.g., 'US').

        Returns:
            The best city for connection, or None if no suitable city is found.

        """
        warnings.warn(
            "get_best_city is deprecated. Use NordVPNAPI.find_best_server instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        country = self.get_country_by_code(country_code)
        if not country:
            return None
        sorted_cities = sorted(
            country["cities"],
            key=lambda x: (x["hub_score"], x["serverCount"]),
            reverse=True,
        )
        return sorted_cities[0] if sorted_cities else None

    def list_countries(self, **kwargs) -> list[Country]:
        """List all countries with server information.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the get_countries method from NordVPNAPI class instead.

        Returns:
            List of countries with server information.

        """
        warnings.warn(
            "list_countries is deprecated. Use NordVPNAPI.get_countries instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        return self.countries
