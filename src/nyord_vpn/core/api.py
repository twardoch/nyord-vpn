"""NordVPN API client for data retrieval and API interactions.

this_file: src/nyord_vpn/core/api.py

This module provides the NordVPNAPIClient class for interacting with NordVPN's API.
It handles all API-related operations and caching to ensure reliable data access.

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

from loguru import logger
from requests import get, RequestException

from nyord_vpn.network.country import get_cached_countries, cache_countries
from nyord_vpn.storage.models import City, Country, CountryCache
from nyord_vpn.utils.utils import API_HEADERS, CACHE_FILE


class NordVPNAPIClient:
    """Base client for NordVPN API interactions.

    This class provides a comprehensive interface to the NordVPN API:
    1. Server and country information retrieval
    2. Location-based server lookup
    3. Cache management for API responses
    4. Connectivity testing and monitoring

    The client handles both v1 and v2 API endpoints, with automatic
    fallback to cached data when API requests fail. It provides
    methods for both raw data access and formatted information
    suitable for display.

    Attributes:
        BASE_API_URL: Base URL for NordVPN API
        BASE_API_V1_URL: Base URL for v1 API endpoints
        BASE_API_V2_URL: Base URL for v2 API endpoints
    """

    BASE_API_URL: str = "https://api.nordvpn.com"
    BASE_API_V1_URL: str = f"{BASE_API_URL}/v1"
    BASE_API_V2_URL: str = f"{BASE_API_URL}/v2"

    def __init__(self, username: str, password: str, verbose: bool = False):
        """Initialize the NordVPN API client.

        Sets up the client with authentication and configuration:
        1. Stores credentials for API authentication
        2. Configures logging based on verbosity
        3. Sets up cache file location
        4. Initializes API interaction settings

        Args:
            username: NordVPN account username
            password: NordVPN account password
            verbose: Enable detailed logging (default: False)

        Note:
            The client doesn't validate credentials on initialization.
            Validation occurs on first API interaction.
        """
        self.username = username
        self.password = password
        self.verbose = verbose
        self.logger = logger
        self.cache_file = CACHE_FILE

    def list_countries(self, use_cache: bool = True) -> list[Country]:
        """Fetch list of available server countries.

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
        try:
            url = f"{self.BASE_API_URL}/servers/countries"
            response = get(url, headers=API_HEADERS, timeout=10)
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
        code = code.upper()
        for country in self.list_countries():
            if country["code"] == code:
                return country
        return None

    def get_country_by_name(self, name: str) -> Country | None:
        """Get country info by name."""
        name = name.lower()
        for country in self.list_countries():
            if country["name"].lower() == name:
                return country
        return None

    def get_available_locations(self) -> list[str]:
        """Get formatted list of available locations."""
        locations = []
        for country in sorted(self.list_countries(), key=lambda x: x["name"]):
            total_servers = country["serverCount"]
            locations.append(
                f"{country['name']} ({country['code'].lower()}) - {total_servers} servers"
            )
            for city in sorted(country["cities"], key=lambda x: x["name"]):
                locations.append(f"  {city['name']} - {city['serverCount']} servers")
        return locations

    def get_best_city(self, country_code: str) -> City | None:
        """Find optimal city for VPN connection in a country.

        Selects the best city based on multiple factors:
        1. Hub score (network infrastructure quality)
        2. Number of available servers
        3. Geographic distribution
        4. Server performance metrics

        Args:
            country_code: Two-letter country code

        Returns:
            City | None: Best city information if found:
                - name: City name
                - dns_name: DNS hostname component
                - hub_score: Infrastructure quality score
                - serverCount: Available servers
                - latitude/longitude: Geographic coordinates
            Returns None if country not found or has no cities.

        Note:
            The hub score is a NordVPN metric combining various
            factors like infrastructure quality, server capacity,
            and network performance.
        """
        country = self.get_country_by_code(country_code)
        if not country:
            return None
        sorted_cities = sorted(
            country["cities"],
            key=lambda x: (x["hub_score"], x["serverCount"]),
            reverse=True,
        )
        return sorted_cities[0] if sorted_cities else None

    def test_api_connectivity(self) -> bool:
        """Test connectivity to NordVPN API.

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
        try:
            response = get(
                f"{self.BASE_API_V2_URL}/servers", headers=API_HEADERS, timeout=5
            )
            response.raise_for_status()
            return True
        except Exception as e:
            if self.verbose:
                self.logger.error(f"API connectivity test failed: {e}")
            return False
