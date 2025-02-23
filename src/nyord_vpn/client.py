import os
import random
import subprocess
import tempfile
import time
import json
from typing import Dict, List, Optional, Tuple, Union, TypedDict
from pathlib import Path

import psutil
import requests
from dotenv import load_dotenv
import logging

load_dotenv()

from ._templates import OPENVPN_TEMPLATE

# Constants
PACKAGE_DIR = Path(__file__).parent
DATA_DIR = PACKAGE_DIR / "data"
CACHE_FILE = DATA_DIR / "countries.json"


def get_logger(verbose: bool = False) -> logging.Logger:
    """Get logger instance."""
    logger = logging.getLogger("nyord_vpn")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)
    return logger


# Store cache in the package directory
COUNTRIES_CACHE = PACKAGE_DIR / "data" / "countries.json"


# Type definitions for country data
class City(TypedDict):
    """City information from NordVPN API."""

    dns_name: str
    hub_score: int
    id: int
    latitude: float
    longitude: float
    name: str
    serverCount: int


class Country(TypedDict):
    """Country information from NordVPN API."""

    cities: List[City]
    code: str
    id: int
    name: str
    serverCount: int


class CountryCache(TypedDict):
    """Cache file structure."""

    countries: List[Country]
    last_updated: str


# Fallback country list in case API is unreachable
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
                }
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
                    "serverCount": 785,
                }
            ],
            "code": "GB",
            "id": 227,
            "name": "United Kingdom",
            "serverCount": 785,
        },
        {
            "cities": [
                {
                    "dns_name": "frankfurt",
                    "hub_score": 0,
                    "id": 2215709,
                    "latitude": 50.116667,
                    "longitude": 8.683333,
                    "name": "Frankfurt",
                    "serverCount": 301,
                }
            ],
            "code": "DE",
            "id": 81,
            "name": "Germany",
            "serverCount": 301,
        },
    ],
    "last_updated": "2024-02-23T00:00:00Z",
}

# Cache expiry in seconds (24 hours)
CACHE_EXPIRY = 24 * 60 * 60


class VPNError(Exception):
    """Base exception for VPN-related errors."""


class ServerError(VPNError):
    """Raised when server selection fails."""


class ConnectionError(VPNError):
    """Raised when connection fails."""


class DisconnectionError(VPNError):
    """Raised when disconnection fails."""


class AuthenticationError(VPNError):
    """Raised when credentials are missing or invalid."""


class CredentialsError(VPNError):
    """Raised when credentials are missing or invalid."""

    def __init__(self, message: Optional[str] = None):
        super().__init__(
            message
            or (
                "NordVPN credentials not found. Please set environment variables:\n"
                "  export NORD_USER='your-username'\n"
                "  export NORD_PASSWORD='your-password'\n"
                "\nOr provide them directly when running the command:\n"
                "  NORD_USER='your-username' NORD_PASSWORD='your-password' nyord-vpn <command>"
            )
        )


class NordVPNClient:
    """NordVPN client for managing VPN connections."""

    def __init__(self, username: str, password: str, verbose: bool = False):
        """Initialize NordVPN client."""
        self.username = username
        self.password = password
        self.verbose = verbose
        self.logger = get_logger(verbose)
        self.cache_file = CACHE_FILE
        self.countries = self._load_countries()

    def _load_countries(self) -> List[Country]:
        """Load countries from cache or fallback data."""
        try:
            with open(self.cache_file, "r") as f:
                cache_data: CountryCache = json.load(f)
                return cache_data["countries"]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.logger.warning(f"Failed to load cache: {e}. Using fallback data.")
            return FALLBACK_DATA["countries"]

    def get_country_by_code(self, code: str) -> Optional[Country]:
        """Get country by its code."""
        code = code.upper()
        for country in self.countries:
            if country["code"] == code:
                return country
        return None

    def get_country_by_name(self, name: str) -> Optional[Country]:
        """Get country by its name."""
        name = name.lower()
        for country in self.countries:
            if country["name"].lower() == name:
                return country
        return None

    def get_available_locations(self) -> List[str]:
        """Get list of available locations."""
        locations = []
        for country in sorted(self.countries, key=lambda x: x["name"]):
            total_servers = country["serverCount"]
            locations.append(
                f"{country['name']} ({country['code'].lower()}) - {total_servers} servers"
            )
            for city in sorted(country["cities"], key=lambda x: x["name"]):
                locations.append(f"  {city['name']} - {city['serverCount']} servers")
        return locations

    def get_best_city(self, country_code: str) -> Optional[City]:
        """Get the best city in a country based on hub score and server count."""
        country = self.get_country_by_code(country_code)
        if not country:
            return None

        # Sort cities by hub score (higher is better) and server count
        sorted_cities = sorted(
            country["cities"],
            key=lambda x: (x["hub_score"], x["serverCount"]),
            reverse=True,
        )
        return sorted_cities[0] if sorted_cities else None


class Client(NordVPNClient):
    """NordVPN client for managing VPN connections."""

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verbose: bool = False,
    ):
        """Initialize NordVPN client."""
        username_str = username or os.getenv("NORD_USER")
        password_str = password or os.getenv("NORD_PASSWORD")
        if not username_str or not password_str:
            raise CredentialsError(
                "NORD_USER and NORD_PASSWORD environment variables must be set"
            )
        super().__init__(username_str, password_str, verbose)
        self.country: Optional[str] = None
        self.config_file: Optional[str] = None
        self.auth_file: Optional[str] = None
        self.connection_retries: int = 0
        self._initial_ip: Optional[str] = None
        self.openvpn: Optional[subprocess.Popen] = None

    BASE_API_URL: str = "https://api.nordvpn.com/v1"
    STATUS_API_URL: str = "https://api.ipify.org?format=json"

    def _create_auth_file(self) -> str:
        """Create a temporary auth file with credentials from environment.

        Returns:
            Path to the temporary auth file
        """
        auth_file = os.path.join(tempfile.gettempdir(), os.urandom(16).hex())
        with open(auth_file, "w") as f:
            f.write(f"{self.username}\n{self.password}")
        os.chmod(auth_file, 0o600)
        return auth_file

    def fetch_server_info(
        self, country: str | None = None
    ) -> Optional[Tuple[str, str]]:
        """Fetch information about a recommended server that supports OpenVPN.

        Args:
            country: Optional 2-letter country code (e.g. 'us', 'uk')
        """
        url = f"{self.BASE_API_URL}/servers/recommendations"
        params = {
            "filters[servers_technologies][identifier]": "openvpn_tcp",
            "limit": "30",
        }

        if country:
            # Get country ID from code
            countries = self.list_countries()
            country_id = None
            for c in countries:
                code = str(c.get("code", ""))
                if code.lower() == country.lower():
                    country_id = str(c.get("id", ""))
                    break
            if not country_id:
                raise ServerError(f"Country code '{country}' not found")
            params["filters[country_id]"] = country_id

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            servers = response.json()

            if not servers:
                raise ServerError("No servers available")

            # Get server with lowest load
            server = min(servers, key=lambda s: s.get("load", 100))
            return server["hostname"], server["station"]

        except requests.RequestException as e:
            raise ServerError(f"Failed to fetch server info: {e}")

    def list_countries(self, use_cache: bool = True) -> List[Country]:
        """Fetch a list of all available server countries from the NordVPN API.

        Args:
            use_cache: Whether to use cached country list (default: True)
                     If False, forces a fresh fetch from the API

        Returns:
            List of dictionaries containing country information
        """
        if use_cache:
            cached = self._get_cached_countries()
            if cached:
                return cached["countries"]

        try:
            url = f"{self.BASE_API_URL}/servers/countries"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            countries: List[Country] = response.json()

            # Cache the fresh data
            cache_data: CountryCache = {
                "countries": countries,
                "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            self._cache_countries(cache_data)
            return countries

        except requests.RequestException as e:
            # If API call fails, try to use cache regardless of use_cache setting
            cached = self._get_cached_countries()
            if cached:
                return cached["countries"]

            # If no cache available, use fallback list
            return FALLBACK_DATA["countries"]

    def _get_cached_countries(self) -> Optional[CountryCache]:
        """Get cached country list if available and not expired."""
        try:
            if not COUNTRIES_CACHE.exists():
                return None

            # Check if cache is expired
            if time.time() - COUNTRIES_CACHE.stat().st_mtime > CACHE_EXPIRY:
                return None

            with COUNTRIES_CACHE.open("r") as f:
                return json.load(f)

        except (json.JSONDecodeError, OSError):
            return None

    def _cache_countries(self, data: CountryCache) -> None:
        """Cache the country list to disk.

        Args:
            data: Dictionary containing countries list and last_updated timestamp
        """
        try:
            COUNTRIES_CACHE.parent.mkdir(parents=True, exist_ok=True)
            with COUNTRIES_CACHE.open("w") as f:
                json.dump(data, f, indent=2, sort_keys=True)
            COUNTRIES_CACHE.chmod(0o644)  # Make readable for all users
        except OSError:
            pass  # Silently fail if caching isn't possible

    def status(self) -> dict:
        """Get current IP info."""
        try:
            response = requests.get(self.STATUS_API_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to get status: {e}")

    def is_protected(self) -> bool:
        """Check if VPN is active by comparing current IP with initial IP."""
        try:
            if self._initial_ip is None:
                self._initial_ip = self.status().get("ip")
                return False

            current_ip = self.status().get("ip")
            return current_ip != self._initial_ip
        except (requests.RequestException, ConnectionError):
            return False

    def connect(self, country: str | None = None, max_retries: int = 5) -> bool:
        """Connect to a NordVPN server.

        Args:
            country: Optional 2-letter country code (e.g. 'us', 'uk')
            max_retries: Number of connection retry attempts
        """
        try:
            # Validate country code if provided
            if country and not isinstance(country, str):
                raise ValueError("Country code must be a string")
            if country:
                country = country.lower()

            subprocess.run(["sudo", "-v"], check=True)
            self.disconnect()

            server_info = self.fetch_server_info(country or self.country)
            if server_info is None:
                raise ServerError("Failed to fetch server info")

            hostname, ip = server_info
            print(f"Selected server: {hostname}")

            file_content = OPENVPN_TEMPLATE.format(ip, hostname)
            self.config_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
            self.auth_file = self._create_auth_file()

            with open(self.config_file, "w") as file:
                file.write(file_content)
            os.chmod(self.config_file, 0o600)

            self.openvpn = subprocess.Popen(
                [
                    "sudo",
                    "openvpn",
                    "--config",
                    self.config_file,
                    "--auth-user-pass",
                    self.auth_file,
                    "--daemon",
                    "--verb",
                    "3",
                    "--connect-retry",
                    "2",
                    "--connect-timeout",
                    "10",
                    "--resolv-retry",
                    "infinite",
                    "--ping",
                    "10",
                    "--ping-restart",
                    "60",
                ],
                shell=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
            )

            # Wait for connection
            for _ in range(30):  # 30 seconds timeout
                time.sleep(1)
                if self.is_protected():
                    print(f"Connected to {hostname}")
                    self.connection_retries = 0
                    return True

            if self.connection_retries < max_retries:
                print("Connection failed - retrying")
                self.connection_retries += 1
                return self.connect(country, max_retries)

            raise ConnectionError("Failed to connect after retries")

        except Exception as e:
            if isinstance(e, (ServerError, ConnectionError)):
                raise
            raise ConnectionError(f"Connection error: {e}")
        finally:
            if not self.is_protected():
                self.disconnect()

    def flush(self) -> None:
        """Terminate all running OpenVPN processes."""
        try:
            for proc in psutil.process_iter(attrs=["name", "pid"]):
                if proc.info["name"] == "openvpn":
                    subprocess.run(
                        ["sudo", "kill", "-9", str(proc.info["pid"])], check=True
                    )
        except Exception as e:
            raise DisconnectionError(f"Failed to flush OpenVPN processes: {e}")

    def disconnect(self) -> None:
        """Disconnect from the current server and clean up."""
        try:
            self.flush()
            if self.config_file and os.path.exists(self.config_file):
                os.unlink(self.config_file)
            if self.auth_file and os.path.exists(self.auth_file):
                os.unlink(self.auth_file)
            self.openvpn = None
            print("Disconnected from VPN")
        except Exception as e:
            raise DisconnectionError(f"Error during disconnect: {e}")

    def go(self, country_code: str) -> None:
        """Connect to VPN in specified country."""
        country = self.get_country_by_code(country_code)
        if not country:
            raise ValueError(f"Country code '{country_code}' not found")

        # Get the best city based on hub score and server count
        best_city = self.get_best_city(country_code)
        if not best_city:
            raise ValueError(f"No available cities in {country['name']}")

        self.logger.info(
            f"Connecting to {country['name']} via {best_city['name']} ({best_city['serverCount']} servers)"
        )

        # Generate OpenVPN config with the correct template formatting
        config = OPENVPN_TEMPLATE.format(
            best_city["dns_name"] + ".nordvpn.com",  # hostname
            best_city["dns_name"] + ".nordvpn.com",  # CN name
        )

        # Save config and connect
        config_path = Path("/tmp/nordvpn.ovpn")
        config_path.write_text(config)
        self.logger.debug(f"Saved OpenVPN config to {config_path}")

        # Run OpenVPN
        cmd = ["sudo", "openvpn", "--config", str(config_path)]
        self.logger.debug(f"Running command: {' '.join(cmd)}")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to connect to VPN: {e}")
        finally:
            config_path.unlink()
