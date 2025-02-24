import json
import random
import subprocess
import time
import socket
from typing import Any, TypedDict
from concurrent.futures import ThreadPoolExecutor

import requests

from nyord_vpn.core.api import NordVPNAPIClient
from nyord_vpn.storage.models import ServerError
from nyord_vpn.utils.utils import API_HEADERS, CACHE_DIR, CACHE_EXPIRY


"""Server management and selection for NordVPN.

this_file: src/nyord_vpn/network/server.py

This module provides server selection and management functionality for NordVPN.
It implements intelligent server selection based on multiple metrics and maintains
server state information.

Core Responsibilities:
1. Server discovery and filtering
2. Load balancing and server selection
3. Server performance measurement
4. Country-based server filtering
5. Cache management for server information

Integration Points:
- Used by Client (core/client.py) for server selection
- Uses NordVPNAPIClient (core/api.py) for server data
- Uses models from storage/models.py
- Uses cache system from utils/utils.py

Selection Algorithm:
The server selection process considers multiple factors:
1. Server load (from API)
2. Geographic proximity (ping times)
3. Connection stability (failure tracking)
4. Feature support (OpenVPN TCP)

Cache Management:
- Implements TTL-based caching
- Handles API failures gracefully
- Provides fallback data
- Validates cached entries

Error Handling:
- Tracks failed servers
- Implements automatic retries
- Provides fallback options
- Detailed error reporting

The module uses TypedDict classes to ensure type safety when
handling server information from the NordVPN API.
"""


class ServerLocation(TypedDict):
    """Server location information from NordVPN API.

    Attributes:
        country: Dictionary containing country information
                with keys for code and name

    """

    country: dict[str, str]


class ServerTechnology(TypedDict):
    """Server technology support information.

    Attributes:
        id: Technology identifier (e.g. 5 for OpenVPN TCP)
        status: Technology status ('online' or 'offline')

    """

    id: int
    status: str


class ServerData(TypedDict):
    """Complete server information from NordVPN API.

    Attributes:
        hostname: Server's hostname for connection
        load: Current server load percentage (0-100)
        status: Server status ('online' or 'offline')
        location_ids: List of location identifiers
        technologies: List of supported technologies
        station: Optional station identifier

    """

    hostname: str
    load: int
    status: str
    location_ids: list[str]
    technologies: list[ServerTechnology]
    station: str | None


class APIResponse(TypedDict):
    """NordVPN API response structure.

    Attributes:
        servers: List of available servers
        locations: Mapping of location IDs to location info

    """

    servers: list[ServerData]
    locations: dict[str, ServerLocation]


class ServerManager:
    """Manages NordVPN server selection and optimization.

    This class handles all server-related operations including:
    1. Server discovery and filtering
    2. Performance measurement and ranking
    3. Load balancing across available servers
    4. Cache management for server information
    5. Country-based server selection

    The manager maintains a cache of server information and tracks
    failed servers within a session to avoid repeated connection
    attempts to problematic servers.
    """

    def __init__(self, api_client: NordVPNAPIClient) -> None:
        """Initialize server manager with API client.

        Sets up the server manager with:
        1. API client for server information retrieval
        2. Logging configuration from API client
        3. Server cache initialization
        4. Failed servers tracking

        Args:
            api_client: NordVPN API client for server information

        """
        self.api_client = api_client
        self.logger = api_client.logger
        self._servers_cache: list[dict[str, Any]] | None = None
        self._last_cache_update: float = 0
        self._failed_servers = set()  # Track failed servers in this session

    def fetch_server_info(self, country: str | None = None) -> tuple[str, str] | None:
        """Fetch information about recommended servers supporting OpenVPN.

        Queries the NordVPN API for server recommendations based on:
        1. OpenVPN TCP support
        2. Server load
        3. Country preference (if specified)
        4. Server status and availability

        Args:
            country: Optional two-letter country code for filtering

        Returns:
            tuple: (hostname, station) if successful, None if no servers available
                  hostname: Server hostname for connection
                  station: Station identifier (if available)

        Raises:
            ServerError: If server fetch fails or no suitable servers found
                        Includes specific error for invalid country codes

        """
        url = "https://api.nordvpn.com/v1/servers/recommendations"
        params = {
            "filters[servers_technologies][identifier]": "openvpn_tcp",
            "limit": "5",
        }
        if country:
            from nyord_vpn.utils.utils import NORDVPN_COUNTRY_IDS

            country_id = NORDVPN_COUNTRY_IDS.get(country.upper())
            if not country_id:
                # Try to get country ID from API
                country_info = self.get_country_info(country)
                if country_info:
                    country_id = str(country_info["id"])
                else:
                    raise ServerError(f"Country code '{country}' not found")
            params["filters[country_id]"] = country_id

        try:
            response = requests.get(url, params=params, headers=API_HEADERS, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, list) or not data:
                params.pop("filters[servers_technologies][identifier]", None)
                response = requests.get(
                    url,
                    params=params,
                    headers=API_HEADERS,
                    timeout=10,
                )
                response.raise_for_status()
                data = response.json()
            if not isinstance(data, list) or not data:
                raise ServerError(
                    f"No servers available{' in ' + country.upper() if country else ''}",
                )
            if self.api_client.verbose:
                self.logger.debug("Available servers retrieved.")
            server = min(data, key=lambda x: x.get("load", 100))
            hostname = server.get("hostname")
            if not isinstance(hostname, str) or not hostname:
                raise ServerError("Invalid server data received.")
            return hostname, server.get("station", "")
        except requests.RequestException as e:
            raise ServerError(f"Failed to fetch server info: {e}")

    def get_servers_cache(self) -> dict:
        """Manage and retrieve server information cache.

        This method handles the complete server cache lifecycle:
        1. Checks for existing cache file
        2. Validates cache freshness and content
        3. Fetches fresh data from API if needed
        4. Filters and validates server information
        5. Updates cache with fresh data

        The cache includes:
        - Server information (hostname, load, status)
        - Country information
        - Cache metadata (last update, expiry)

        Returns:
            dict: Cache containing:
                - servers: List of valid server information
                - expires_at: Cache expiry timestamp
                - last_updated: Last update timestamp

        Note:
            The cache is considered valid if:
            1. The cache file exists
            2. The cache hasn't expired
            3. The cached servers are valid
            4. The cache format is correct

        """
        cache_file = CACHE_DIR / "servers.json"
        if cache_file.exists():
            try:
                cache = json.loads(cache_file.read_text())
                if (
                    isinstance(cache, dict)
                    and isinstance(cache.get("servers", []), list)
                    and time.time() < cache.get("expires_at", 0)
                ):
                    # Validate cached servers
                    valid_servers = [
                        s for s in cache["servers"] if self._is_valid_server(s)
                    ]
                    if valid_servers:
                        if self.api_client.verbose:
                            self.logger.debug(
                                f"Using cached server list with {len(valid_servers)} valid servers",
                            )
                        cache["servers"] = valid_servers
                        return cache
                    if self.api_client.verbose:
                        self.logger.warning(
                            "No valid servers in cache, fetching fresh data",
                        )
            except Exception as e:
                if self.api_client.verbose:
                    self.logger.warning(f"Failed to read cache: {e}")

        try:
            if self.api_client.verbose:
                self.logger.debug("Fetching server list from API...")

            # Use v2 API which has more detailed server info
            response = requests.get(
                "https://api.nordvpn.com/v1/servers",
                headers=API_HEADERS,
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            if self.api_client.verbose:
                self.logger.debug("Successfully fetched server data from API")

            # Extract servers from response
            raw_servers: list[dict[str, Any]] = []

            if isinstance(data, list):
                raw_servers = [dict(s) for s in data]
                if self.api_client.verbose:
                    self.logger.debug(
                        f"Found {len(raw_servers)} servers in API response",
                    )
            else:
                raise ValueError(f"Unexpected API response format: {type(data)}")

            # Get countries info
            try:
                countries_response = requests.get(
                    "https://api.nordvpn.com/v1/servers/countries",
                    headers=API_HEADERS,
                    timeout=10,
                )
                countries_response.raise_for_status()
                countries_data = countries_response.json()

                # Create countries lookup
                countries = {}
                for country in countries_data:
                    if isinstance(country, dict):
                        country_id = str(country.get("id"))
                        if country_id:
                            countries[country_id] = {
                                "code": country.get("code", "").upper(),
                                "name": country.get("name", "Unknown"),
                            }
            except Exception as e:
                if self.api_client.verbose:
                    self.logger.warning(f"Failed to fetch countries: {e}")
                countries = {}

            # Filter and validate servers
            valid_servers = []
            invalid_count = 0
            for server in raw_servers:
                if not isinstance(server, dict):
                    invalid_count += 1
                    continue

                # Check if server is online and supports OpenVPN TCP
                if server.get("status") != "online":
                    if self.api_client.verbose:
                        self.logger.debug(
                            f"Skipping offline server: {server.get('hostname')}",
                        )
                    continue

                has_openvpn_tcp = False
                for tech in server.get("technologies", []):
                    if (
                        isinstance(tech, dict)
                        and tech.get("id") == 5
                        and tech.get("status") == "online"
                    ):
                        has_openvpn_tcp = True
                        break
                if not has_openvpn_tcp:
                    if self.api_client.verbose:
                        self.logger.debug(
                            f"Skipping server without OpenVPN TCP: {server.get('hostname')}",
                        )
                    continue

                # Get hostname and validate
                hostname = server.get("hostname")
                if not isinstance(hostname, str) or not hostname:
                    invalid_count += 1
                    continue

                # Get country info from location_ids
                country_info = None
                location_ids = server.get("location_ids", [])
                if isinstance(location_ids, list):
                    for location_id in location_ids:
                        if not isinstance(location_id, str | int):
                            continue
                        country_id = str(location_id)
                        country = countries.get(country_id)
                        if country and isinstance(country, dict):
                            country_info = country
                            break

                # If no country info from locations, try direct country field
                if not country_info:
                    country = server.get("country", {})
                    if isinstance(country, dict):
                        country_info = {
                            "code": country.get("code", "").upper(),
                            "name": country.get("name", "Unknown"),
                        }

                if not country_info:
                    if self.api_client.verbose:
                        self.logger.debug(
                            f"Skipping server without country info: {hostname}",
                        )
                    continue

                # Create normalized server entry
                valid_server = {
                    "hostname": hostname,
                    "load": int(server.get("load", 100)),
                    "country": country_info,
                    "status": server.get("status"),
                    "technologies": server.get("technologies", []),
                    "station": server.get("station"),
                }

                # Final validation
                if self._is_valid_server(valid_server):
                    valid_servers.append(valid_server)
                else:
                    invalid_count += 1

            if not valid_servers:
                raise ValueError(
                    f"No valid servers found in API response. "
                    f"Total servers: {len(raw_servers)}, Invalid: {invalid_count}",
                )

            if self.api_client.verbose:
                country_counts = {}
                for server in valid_servers:
                    code = server["country"]["code"]
                    country_counts[code] = country_counts.get(code, 0) + 1
                self.logger.debug(
                    f"Found {len(valid_servers)} valid servers. "
                    f"Country distribution: "
                    + ", ".join(f"{k}: {v}" for k, v in sorted(country_counts.items())),
                )

            cache = {
                "servers": valid_servers,
                "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "expires_at": time.time() + CACHE_EXPIRY,
            }

            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            cache_file.write_text(json.dumps(cache, indent=2))
            return cache

        except Exception as e:
            self.logger.exception(f"Failed to fetch servers: {e}")
            if cache_file.exists():
                try:
                    cache = json.loads(cache_file.read_text())
                    if isinstance(cache, dict) and isinstance(
                        cache.get("servers", []),
                        list,
                    ):
                        # Validate cached servers even in fallback
                        valid_servers = [
                            s for s in cache["servers"] if self._is_valid_server(s)
                        ]
                        if valid_servers:
                            if self.api_client.verbose:
                                self.logger.info(
                                    f"Using fallback cache with {len(valid_servers)} valid servers",
                                )
                            cache["servers"] = valid_servers
                            return cache
                except Exception:
                    pass
            return {"servers": [], "last_updated": "", "expires_at": 0}

    def _ping_server(self, hostname: str) -> float:
        """Ping a server and return response time in ms.

        Args:
            hostname: Server hostname to ping

        Returns:
            float: Ping time in milliseconds, or float('inf') if ping failed

        """
        try:
            # Platform-specific ping command
            import platform

            system = platform.system().lower()

            if system == "windows":
                cmd = ["ping", "-n", "2", "-w", "1000", hostname]
            elif system == "darwin":  # macOS
                cmd = ["ping", "-c", "2", "-W", "1", "-t", "1", hostname]
            else:  # Linux and others
                cmd = ["ping", "-c", "2", "-W", "1", hostname]

            if self.api_client.verbose:
                self.logger.debug(f"Running ping command: {' '.join(cmd)}")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3,
                check=False,  # Overall timeout
            )

            if result.returncode == 0:
                # Extract time from ping output more robustly
                min_time = float("inf")
                for line in result.stdout.splitlines():
                    if self.api_client.verbose:
                        self.logger.debug(f"Ping output line: {line}")

                    # Look for min/avg/max line
                    if "min/avg/max" in line:
                        try:
                            # Format: round-trip min/avg/max/stddev = 18.894/18.894/18.894/0.000 ms
                            stats = line.split("=")[1].strip().split("/")
                            min_time = float(stats[0])
                            if self.api_client.verbose:
                                self.logger.debug(
                                    f"Parsed min time from stats: {min_time}ms",
                                )
                            return min_time
                        except (IndexError, ValueError) as e:
                            if self.api_client.verbose:
                                self.logger.debug(
                                    f"Failed to parse min/avg/max line '{line}': {e}",
                                )
                            continue
                    # Look for individual ping responses
                    elif "time=" in line:
                        try:
                            time_str = line.split("time=")[1].split()[0].rstrip("ms")
                            ping_time = float(time_str)
                            min_time = min(min_time, ping_time)
                            if self.api_client.verbose:
                                self.logger.debug(
                                    f"Parsed time from response: {ping_time}ms",
                                )
                        except (IndexError, ValueError) as e:
                            if self.api_client.verbose:
                                self.logger.debug(
                                    f"Failed to parse time from line '{line}': {e}",
                                )
                            continue

                if min_time < float("inf"):
                    if self.api_client.verbose:
                        self.logger.debug(
                            f"Server {hostname} responded in {min_time}ms",
                        )
                    return min_time

                # If we couldn't parse any times but ping succeeded
                if self.api_client.verbose:
                    self.logger.debug(
                        f"Server {hostname} responded but couldn't parse time from output:\n{result.stdout}",
                    )
                return float("inf")
            if self.api_client.verbose:
                self.logger.debug(
                    f"Server {hostname} ping failed with code {result.returncode}:\n"
                    f"stdout: {result.stdout}\n"
                    f"stderr: {result.stderr}",
                )
            return float("inf")

        except subprocess.TimeoutExpired:
            if self.api_client.verbose:
                self.logger.debug(f"Server {hostname} ping timed out")
            return float("inf")
        except Exception as e:
            if self.api_client.verbose:
                self.logger.debug(f"Server {hostname} ping error: {e}")
                import traceback

                self.logger.debug(f"Traceback: {traceback.format_exc()}")
            return float("inf")

    def _is_valid_server(self, server: Any) -> bool:
        """Validate server data structure.

        Args:
            server: Server data to validate

        Returns:
            bool: True if server data is valid

        """
        if not isinstance(server, dict):
            return False

        # Check required fields
        hostname = server.get("hostname")
        if not isinstance(hostname, str) or not hostname:
            return False

        # Basic hostname validation
        if not hostname.endswith(".nordvpn.com"):
            return False

        # Check country info
        country = server.get("country")
        if not isinstance(country, dict):
            return False

        country_code = country.get("code")
        if not isinstance(country_code, str) or len(country_code) != 2:
            return False

        # Check server status
        status = server.get("status")
        if status != "online":
            return False

        # Check load value
        load = server.get("load")
        return not (not isinstance(load, int | float) or load < 0 or load > 100)

    def _test_server(self, server: dict[str, Any]) -> tuple[dict[str, Any], float]:
        """Test a server's response time using both ping and TCP connection.

        Args:
            server: Server information dictionary

        Returns:
            Tuple of (server, score) where score is combined ping/TCP time
            Lower score is better, float('inf') means failed

        """
        hostname = server.get("hostname")
        if not hostname:
            return server, float("inf")

        try:
            # Platform-specific ping command
            import platform

            system = platform.system().lower()

            if system == "darwin":  # macOS
                cmd = ["ping", "-c", "1", "-W", "1000", "-t", "1", hostname]
            elif system == "windows":
                cmd = ["ping", "-n", "1", "-w", "1000", hostname]
            else:  # Linux and others
                cmd = ["ping", "-c", "1", "-W", "1", hostname]

            if self.api_client.verbose:
                self.logger.debug(f"Running ping command: {' '.join(cmd)}")

            # Run ping
            ping_result = subprocess.run(cmd, capture_output=True, text=True, timeout=2, check=False)

            if ping_result.returncode != 0:
                if self.api_client.verbose:
                    self.logger.debug(
                        f"Ping failed for {hostname}: {ping_result.stderr}"
                    )
                return server, float("inf")

            # Parse ping time based on platform
            ping_time = float("inf")
            output = ping_result.stdout

            if system == "darwin":
                # macOS format: round-trip min/avg/max/stddev = 20.237/20.237/20.237/0.000 ms
                for line in output.splitlines():
                    if "round-trip" in line:
                        try:
                            stats = line.split("=")[1].strip().split("/")
                            ping_time = float(stats[0])  # Use min time
                            break
                        except (IndexError, ValueError) as e:
                            if self.api_client.verbose:
                                self.logger.debug(
                                    f"Failed to parse macOS ping stats: {e}"
                                )
                            continue
            else:
                # Linux/Windows format: time=20.2 ms
                try:
                    ping_time = float(output.split("time=")[1].split()[0].rstrip("ms"))
                except (IndexError, ValueError) as e:
                    if self.api_client.verbose:
                        self.logger.debug(f"Failed to parse ping time: {e}")
                    return server, float("inf")

            if ping_time == float("inf"):
                if self.api_client.verbose:
                    self.logger.debug(
                        f"Could not parse ping time from output: {output}"
                    )
                return server, float("inf")

            # Quick TCP connection test to OpenVPN port
            start = time.time()
            try:
                with socket.create_connection((hostname, 443), timeout=2):
                    tcp_time = (time.time() - start) * 1000  # Convert to ms
            except (TimeoutError, OSError) as e:
                if self.api_client.verbose:
                    self.logger.debug(f"TCP connection failed for {hostname}: {e}")
                return server, float("inf")

            # Combined score (70% ping, 30% TCP)
            score = (ping_time * 0.7) + (tcp_time * 0.3)

            if self.api_client.verbose:
                self.logger.debug(
                    f"Server {hostname} test results: "
                    f"ping={ping_time:.1f}ms, tcp={tcp_time:.1f}ms, score={score:.1f}ms"
                )

            return server, score

        except Exception as e:
            if self.api_client.verbose:
                self.logger.debug(f"Failed to test server {hostname}: {e}")
                import traceback

                self.logger.debug(f"Traceback: {traceback.format_exc()}")
            return server, float("inf")

    def _select_diverse_servers(
        self, servers: list[dict[str, Any]], count: int = 4
    ) -> list[dict[str, Any]]:
        """Select geographically diverse servers.

        When no country is specified, this ensures we test servers from different regions
        to find the best performing one regardless of location.

        Args:
            servers: List of server dictionaries
            count: Number of servers to select

        Returns:
            List of selected servers

        """
        # Group servers by region/continent
        regions = {}
        for server in servers:
            region = server.get("country", {}).get("region", {}).get("name", "Unknown")
            if region not in regions:
                regions[region] = []
            regions[region].append(server)

        # Select servers from different regions if possible
        selected = []
        region_names = list(regions.keys())

        while len(selected) < count and region_names:
            # Cycle through regions
            region = region_names.pop(random.randrange(len(region_names)))
            if region_servers := regions.get(region, []):
                # Select random server from region
                server = random.choice(region_servers)
                selected.append(server)

        # If we still need more servers, take random ones
        if len(selected) < count:
            remaining = random.sample(
                [s for s in servers if s not in selected],
                min(count - len(selected), len(servers)),
            )
            selected.extend(remaining)

        return selected

    def select_fastest_server(
        self,
        country_code: str | None = None,
        random_select: bool = False,
        _retry_count: int = 0,
    ) -> dict[str, Any] | None:
        """Select the optimal server based on parallel performance testing.

        Args:
            country_code: Optional two-letter country code
            random_select: Whether to randomize selection
            _retry_count: Internal retry counter

        Returns:
            Selected server info or None if no suitable server found

        Raises:
            ServerError: If country code is invalid or no servers are available

        """
        try:
            # Validate country code if provided
            if country_code:
                country_code = country_code.upper()
                if not isinstance(country_code, str) or len(country_code) != 2:
                    raise ServerError(
                        f"Invalid country code '{country_code}'. "
                        "Please use a two-letter country code (e.g. 'US', 'GB', 'DE')"
                    )

                # Check if country exists in our cache
                cache = self.get_servers_cache()
                valid_countries = {
                    s.get("country", {}).get("code", "").upper()
                    for s in cache.get("servers", [])
                    if s.get("country", {}).get("code")
                }

                if country_code not in valid_countries:
                    available = ", ".join(sorted(valid_countries))
                    raise ServerError(
                        f"Country code '{country_code}' not found. "
                        f"Available countries: {available}"
                    )

            if _retry_count >= 3:
                # After 3 retries with our testing method, try the NordVPN recommendations API
                try:
                    if self.api_client.verbose:
                        self.logger.info("Falling back to NordVPN recommendations API")

                    # Get recommended server
                    url = "https://api.nordvpn.com/v1/servers/recommendations"
                    params = {
                        "filters[servers_technologies][identifier]": "openvpn_tcp",
                        "limit": "5",
                    }

                    if country_code:
                        params["filters[country_id]"] = self._get_country_id(
                            country_code
                        )

                    response = requests.get(
                        url, params=params, headers=API_HEADERS, timeout=10
                    )
                    response.raise_for_status()
                    servers = response.json()

                    if not servers:
                        if self.api_client.verbose:
                            self.logger.error(
                                "No servers returned by recommendations API"
                            )
                        return None

                    # Get server with lowest load
                    server = min(servers, key=lambda x: x.get("load", 100))

                    # Convert to our format
                    return {
                        "hostname": server["hostname"],
                        "load": server.get("load", 0),
                        "country": {
                            "code": server.get("country", {}).get("code", ""),
                            "name": server.get("country", {}).get("name", "Unknown"),
                        },
                    }

                except Exception as e:
                    if self.api_client.verbose:
                        self.logger.exception(f"Recommendations API fallback failed: {e}")
                    return None

            try:
                # Get cached servers
                cache = self.get_servers_cache()
                servers = cache.get("servers", [])

                if not servers:
                    return None

                # Filter by country if specified
                if country_code:
                    servers = [
                        s
                        for s in servers
                        if s.get("country", {}).get("code", "").upper()
                        == country_code.upper()
                    ]

                # Remove failed servers
                servers = [
                    s for s in servers if s.get("hostname") not in self._failed_servers
                ]

                if not servers:
                    if self._failed_servers:
                        self._failed_servers.clear()
                        return self.select_fastest_server(
                            country_code, random_select, _retry_count + 1
                        )
                    return None

                # Basic filtering
                servers = [
                    s for s in servers if s.get("load", 100) < 90
                ]  # Skip heavily loaded servers

                if random_select:
                    return random.choice(servers)

                # Select 4 servers - use geographic distribution if no country specified
                test_servers = (
                    self._select_diverse_servers(servers, 4)
                    if not country_code
                    else random.sample(servers, min(4, len(servers)))
                )

                # Test servers in parallel using ThreadPoolExecutor
                with ThreadPoolExecutor(max_workers=4) as executor:
                    # Map _test_server over servers in parallel
                    results = list(
                        executor.map(lambda s: self._test_server(s), test_servers)
                    )

                # Filter out failed servers and sort by score
                valid_results = [
                    (s, score) for s, score in results if score < float("inf")
                ]

                if not valid_results:
                    # If all servers failed, mark them as failed and retry
                    for server in test_servers:
                        if hostname := server.get("hostname"):
                            self._failed_servers.add(hostname)
                    return self.select_fastest_server(
                        country_code, random_select, _retry_count + 1
                    )

                # Return server with best score
                best_server = min(valid_results, key=lambda x: x[1])[0]

                if self.api_client.verbose:
                    self.logger.info(
                        f"Selected server: {best_server.get('hostname')} "
                        f"(load: {best_server.get('load')}%, "
                        f"score: {min(s for _, s in valid_results):.1f}ms)"
                    )

                return best_server

            except Exception as e:
                self.logger.exception(f"Error selecting server: {e}")
                return None

        except Exception as e:
            self.logger.exception(f"Error selecting server: {e}")
            return None

    def _get_country_id(self, country_code: str) -> str:
        """Get NordVPN country ID from country code.

        Args:
            country_code: Two-letter country code

        Returns:
            Country ID or empty string if not found

        """
        try:
            # First check our cache
            cache = self.get_servers_cache()
            for server in cache.get("servers", []):
                if (
                    server.get("country", {}).get("code", "").upper()
                    == country_code.upper()
                ) and (country_id := server.get("country", {}).get("id")):
                    return str(country_id)

            # If not in cache, try API
            response = requests.get(
                "https://api.nordvpn.com/v1/servers/countries",
                headers=API_HEADERS,
                timeout=10,
            )
            response.raise_for_status()

            for country in response.json():
                if country.get("code", "").upper() == country_code.upper():
                    return str(country["id"])

        except Exception as e:
            if self.api_client.verbose:
                self.logger.warning(f"Failed to get country ID: {e}")

        return ""

    def get_random_country(self) -> str:
        try:
            cache = self.get_servers_cache()
            countries = {
                s.get("country", {}).get("code")
                for s in cache.get("servers", [])
                if s.get("country", {}).get("code")
            }
            if not countries:
                raise ServerError("No countries found in server list")
            return random.choice(list(countries))
        except Exception as e:
            self.logger.exception(f"Failed to get random country: {e}")
            return "US"

    def get_country_info(self, country_code: str) -> dict[str, Any] | None:
        """Get country information from NordVPN API.

        Args:
            country_code: Two-letter country code

        Returns:
            Dictionary with country information or None if not found

        """
        try:
            # Use v1 API endpoint
            response = requests.get(
                "https://api.nordvpn.com/v1/servers/countries",
                headers=API_HEADERS,
                timeout=10,
            )
            response.raise_for_status()
            countries = response.json()

            # Find country by code
            for country in countries:
                if (
                    isinstance(country, dict)
                    and country.get("code", "").upper() == country_code.upper()
                ):
                    return {
                        "code": country["code"],
                        "name": country["name"],
                        "id": country["id"],
                    }

            return None

        except Exception as e:
            self.logger.exception(f"Failed to get country info: {e}")
            return None
