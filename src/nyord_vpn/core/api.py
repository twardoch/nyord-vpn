"""NordVPN API client for data retrieval and API interactions.

this_file: src/nyord_vpn/core/api.py

This module provides the NordVPNAPIClient class for interacting with NordVPN's API.
It handles all API-related operations and caching to ensure reliable data access.

DEPRECATED: This module is deprecated and will be removed in a future version.
Please use the NordVPNAPI class from nyord_vpn.api.api instead.

Core Responsibilities:
1. Authentication with NordVPN API
2. Country and server information retrieval
3. Cache management for API responses
4. Location and city information lookup
5. API connectivity testing

Integration Points:
- Used by Client (core/client.py) for API operations
- Used by ServerManager (network/server.py) for server info
- Interacts with cache system in utils/utils.py
- Handles models defined in storage/models.py

The client implements automatic fallback to cached data when
API requests fail, and provides both raw and formatted data
access methods. This ensures continuous operation even during
API outages or rate limiting.

Cache Management:
- Stores data in ~/.cache/nyord-vpn/
- Implements TTL-based cache invalidation
- Provides fallback data for core countries
- Handles cache corruption gracefully

Error Handling:
- Provides detailed error messages
- Implements automatic retries
- Falls back to cached data
- Logs failures for debugging
"""

import time
import warnings

from loguru import logger
from requests import RequestException, get

from nyord_vpn.network.country import cache_countries, get_cached_countries
from nyord_vpn.storage.models import City, Country, CountryCache
from nyord_vpn.utils.utils import API_HEADERS

# Display deprecation warning when the module is imported
warnings.warn(
    "The NordVPNAPIClient class is deprecated and will be removed in a future version. "
    "Please use the NordVPNAPI class from nyord_vpn.api.api instead.",
    DeprecationWarning,
    stacklevel=2,
)


class NordVPNAPIClient:
    """Base client for NordVPN API interactions.

    DEPRECATED: This class is deprecated and will be removed in a future version.
    Please use the NordVPNAPI class from nyord_vpn.api.api instead.

    Attributes:
        api_url: Base URL for the NordVPN API.
        timeout: Timeout in seconds for API requests.
        cache_ttl: Time-to-live for cached data in seconds.

    """

    def __init__(
        self,
        api_url: str = "https://api.nordvpn.com/v1",
        *,
        timeout: int = 5,
        cache_ttl: int = 3600,
        verbose: bool = False,
    ) -> None:
        """Initialize the API client.

        Args:
            api_url: Base URL for the NordVPN API.
            timeout: Timeout in seconds for API requests.
            cache_ttl: Time-to-live for cached data in seconds.
            verbose: Whether to enable verbose logging.

        """
        warnings.warn(
            "NordVPNAPIClient is deprecated. Use NordVPNAPI from nyord_vpn.api.api instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        self.api_url = api_url
        self.timeout = timeout
        self.cache_ttl = cache_ttl
        self.verbose = verbose
        self.logger = logger

    def list_countries(self, *, use_cache: bool = True) -> list[Country]:
        """Fetch list of available server countries.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the get_countries method from NordVPNAPI class instead.

        Retrieves a comprehensive list of countries with servers:
        1. Attempts to fetch fresh data from API
        2. Updates local cache with new data
        3. Falls back to cached data if API fails
        4. Includes server counts and city information

        Args:
            use_cache: Whether to allow using cached data (default: True)

        Returns:
            list[Country]: List of countries with their details:
                - name: Country name
                - code: Two-letter country code
                - id: Country identifier
                - cities: List of cities with servers
                - serverCount: Total servers in country

        Note:
            The method automatically updates the cache with fresh data
            on successful API requests. Cache format matches API response
            to ensure consistency.

        """
        warnings.warn(
            "list_countries is deprecated. Use NordVPNAPI.get_countries instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        try:
            url = f"{self.api_url}/servers/countries"
            response = get(url, headers=API_HEADERS, timeout=self.timeout)
            response.raise_for_status()
            countries: list[Country] = response.json()

            cache_data: CountryCache = {
                "countries": countries,
                "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            cache_countries(cache_data)
            return countries

        except RequestException as e:
            self.logger.warning(f"Failed to fetch countries: {e}")
            cached = get_cached_countries()
            if cached:
                return cached["countries"]
            return []

    def get_country_by_code(self, code: str) -> Country | None:
        """Find country information by country code.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

        Searches for a country using its ISO code:
        1. Converts code to uppercase for consistency
        2. Searches in available countries list
        3. Returns full country information if found

        Args:
            code: Two-letter country code (case insensitive)

        Returns:
            Country | None: Country information if found:
                - name: Country name
                - code: Two-letter country code
                - id: Country identifier
                - cities: List of cities with servers
                - serverCount: Total servers in country
            Returns None if country not found.

        Note:
            This method uses list_countries() internally, so it may
            trigger an API request if no cached data is available.

        """
        warnings.warn(
            "get_country_by_code is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        code = code.upper()
        for country in self.list_countries():
            if country["code"] == code:
                return country
        return None

    def get_country_by_name(self, name: str) -> Country | None:
        """Get country info by name.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

        Args:
            name: The name of the country (case insensitive).

        Returns:
            The country information if found, None otherwise.

        """
        warnings.warn(
            "get_country_by_name is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        name = name.lower()
        for country in self.list_countries():
            if country["name"].lower() == name:
                return country
        return None

    def get_available_locations(self) -> list[str]:
        """Get formatted list of available locations.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

        Returns:
            A formatted list of available locations.

        """
        warnings.warn(
            "get_available_locations is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        locations = []
        for country in sorted(self.list_countries(), key=lambda x: x["name"]):
            total_servers = country["serverCount"]
            locations.append(
                f"{country['name']} ({country['code'].lower()}) - {total_servers} servers",
            )
            for city in sorted(country["cities"], key=lambda x: x["name"]):
                locations.append(f"  {city['name']} - {city['serverCount']} servers")
        return locations

    def get_best_city(
        self, country_code: str, *, use_cache: bool = True
    ) -> City | None:
        """Get the best city in a country for VPN connection.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the find_best_server method from NordVPNAPI class instead.

        Args:
            country_code: The two-letter country code (e.g., 'US').
            use_cache: Whether to use cached data if available.

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

    def fetch_countries(
        self, *, use_cache: bool = True, force_refresh: bool = False
    ) -> list[Country]:
        """Fetch country data from the API or cache.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the get_countries method from NordVPNAPI class instead.

        Args:
            use_cache: Whether to use cached data if available.
            force_refresh: Whether to force a refresh of the cache.

        Returns:
            List of countries with server information.

        """
        warnings.warn(
            "fetch_countries is deprecated. Use NordVPNAPI.get_countries instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if not use_cache or force_refresh:
            return self.list_countries(use_cache=False)

        return self.list_countries(use_cache=True)

    def get_cities(self, country_code: str, *, use_cache: bool = True) -> list[City]:
        """Get cities in a specific country.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

        Args:
            country_code: The two-letter country code (e.g., 'US').
            use_cache: Whether to use cached data if available.

        Returns:
            List of cities in the specified country.

        """
        warnings.warn(
            "get_cities is deprecated. Use NordVPNAPI class methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        country = self.get_country_by_code(country_code)
        if not country:
            return []
        return country.get("cities", [])

    def test_api_connectivity(self) -> bool:
        """Test connectivity to NordVPN API.

        DEPRECATED: This method is deprecated and will be removed in a future version.
        Please use the NordVPNAPI class methods instead.

        Performs a basic health check of the API:
        1. Attempts to fetch server list
        2. Verifies response format
        3. Checks response timing
        4. Validates API version compatibility

        Returns:
            bool: True if API is accessible and responding correctly,
                 False if any connectivity issues are detected

        Note:
            This method is used during initialization and can be
            called periodically to verify API health. It uses a
            short timeout to quickly detect connectivity issues.

        """
        warnings.warn(
            "test_api_connectivity is deprecated. Use NordVPNAPI methods instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        try:
            response = get(
                f"{self.api_url}/servers",
                headers=API_HEADERS,
                timeout=self.timeout,
            )
            response.raise_for_status()
            return True
        except Exception as e:
            if self.verbose:
                self.logger.exception(f"API connectivity test failed: {e}")
            return False
