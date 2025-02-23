"""NordVPN API client for basic data retrieval and API interactions."""

import json
import time
from typing import List, Optional
import requests
from loguru import logger

from .models import City, Country, CountryCache
from .utils import API_HEADERS, CACHE_FILE
from .country_cache import get_cached_countries, cache_countries


class NordVPNAPIClient:
    """Base client for NordVPN API interactions."""

    BASE_API_URL: str = "https://api.nordvpn.com"
    BASE_API_V1_URL: str = f"{BASE_API_URL}/v1"
    BASE_API_V2_URL: str = f"{BASE_API_URL}/v2"

    def __init__(self, username: str, password: str, verbose: bool = False):
        """Initialize API client.

        Args:
            username: NordVPN username
            password: NordVPN password
            verbose: Enable verbose logging
        """
        self.username = username
        self.password = password
        self.verbose = verbose
        self.logger = logger
        self.cache_file = CACHE_FILE

    def list_countries(self, use_cache: bool = True) -> List[Country]:
        """Fetch list of available server countries."""
        try:
            url = f"{self.BASE_API_URL}/servers/countries"
            response = requests.get(url, headers=API_HEADERS, timeout=10)
            response.raise_for_status()
            countries: List[Country] = response.json()

            cache_data: CountryCache = {
                "countries": countries,
                "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            cache_countries(cache_data)
            return countries

        except requests.RequestException as e:
            self.logger.warning(f"Failed to fetch countries: {e}")
            cached = get_cached_countries()
            if cached:
                return cached["countries"]
            return []

    def get_country_by_code(self, code: str) -> Optional[Country]:
        """Get country info by code."""
        code = code.upper()
        for country in self.list_countries():
            if country["code"] == code:
                return country
        return None

    def get_country_by_name(self, name: str) -> Optional[Country]:
        """Get country info by name."""
        name = name.lower()
        for country in self.list_countries():
            if country["name"].lower() == name:
                return country
        return None

    def get_available_locations(self) -> List[str]:
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

    def get_best_city(self, country_code: str) -> Optional[City]:
        """Get best city in country based on hub score."""
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
        """Test connection to NordVPN API."""
        try:
            response = requests.get(
                f"{self.BASE_API_V2_URL}/servers", headers=API_HEADERS, timeout=5
            )
            response.raise_for_status()
            return True
        except Exception as e:
            if self.verbose:
                self.logger.error(f"API connectivity test failed: {e}")
            return False
