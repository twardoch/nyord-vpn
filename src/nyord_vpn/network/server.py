import json
import random
import subprocess
import time
import socket
import ssl
from pathlib import Path
from typing import Any, TypedDict, NotRequired, Dict, List, Optional, cast, Sequence
from loguru import logger
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


class Country(TypedDict):
    """Country information."""
    name: str
    code: str


class ServerLocation(TypedDict):
    """Server location information."""
    id: str
    country: Country


class Technology(TypedDict):
    """Server technology information."""
    id: int
    status: str
    metadata: NotRequired[List[Dict[str, str]]]


class ServerInfo(TypedDict):
    """Server information structure."""
    hostname: str
    location_ids: List[str]
    status: str
    load: int
    technologies: List[Technology]


class ServerCache(TypedDict):
    """Cache structure for server information."""
    servers: List[ServerInfo]
    locations: Dict[str, ServerLocation]
    last_updated: float


# Constants
SERVERS_CACHE_FILE = CACHE_DIR / "servers.json"
SERVERS_CACHE_TTL = 3600  # 1 hour in seconds


def _safe_dict_get(d: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary."""
    return d.get(key, default) if isinstance(d, dict) else default


def _safe_get(d: Optional[Dict[str, Any]], key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary that might be None."""
    if d is None:
        return default
    return _safe_dict_get(d, key, default)


def _safe_str_get(s: Optional[str], key: str, default: Any = None) -> Any:
    """Safely get a value from a string that might be None."""
    if s is None:
        return default
    try:
        return s[int(key)] if key.isdigit() else default
    except (ValueError, IndexError):
        return default


def _safe_dict_access(d: Dict[str, Any], key: str) -> Any:
    """Safely access a dictionary key that must exist."""
    if not isinstance(d, dict) or key not in d:
        raise KeyError(f"Required key {key} not found in dictionary")
    return d[key]


def _safe_dict_cast(d: Any) -> Dict[str, Any]:
    """Cast a value to a dictionary if possible."""
    if not isinstance(d, dict):
        return {}
    return cast(Dict[str, Any], d)


def _safe_dict_get_str(d: Dict[str, Any], key: str, default: str = "") -> str:
    """Safely get a string value from a dictionary."""
    value = _safe_dict_get(d, key, default)
    return str(value) if value is not None else default


def _safe_dict_get_int(d: Dict[str, Any], key: str, default: int = 0) -> int:
    """Safely get an integer value from a dictionary."""
    value = _safe_dict_get(d, key, default)
    try:
        return int(value) if value is not None else default
    except (ValueError, TypeError):
        return default


def _safe_dict_get_list(d: Dict[str, Any], key: str, default: Optional[List[Any]] = None) -> List[Any]:
    """Safely get a list value from a dictionary."""
    if default is None:
        default = []
    value = _safe_dict_get(d, key, default)
    return value if isinstance(value, list) else default


def _safe_dict_get_dict(d: Dict[str, Any], key: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Safely get a dictionary value from a dictionary."""
    if default is None:
        default = {}
    value = _safe_dict_get(d, key, default)
    return value if isinstance(value, dict) else default


def cache_servers(data: Dict[str, Any]) -> None:
    """Cache server information from the API.

    Args:
        data: Server data from the API to cache in the ServerCache format
    """
    try:
        if not isinstance(data, dict):
            logger.warning("Invalid server data format")
            return

        # Ensure cache directory exists
        SERVERS_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # Write to temporary file first
        temp_file = SERVERS_CACHE_FILE.with_suffix('.tmp')
        temp_file.write_text(json.dumps(data, indent=2))
        
        # Atomic rename
        temp_file.replace(SERVERS_CACHE_FILE)
        
    except Exception as e:
        logger.warning(f"Failed to cache server information: {e}")


def _parse_timestamp(timestamp: Any) -> float:
    """Parse a timestamp value into a float.
    
    Handles both float timestamps and ISO format strings.
    """
    if isinstance(timestamp, (int, float)):
        return float(timestamp)
    if isinstance(timestamp, str):
        try:
            # Try parsing as float first
            return float(timestamp)
        except ValueError:
            try:
                # Try parsing as ISO format
                from datetime import datetime
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                return dt.timestamp()
            except ValueError:
                return 0.0
    return 0.0


def get_cached_servers() -> Optional[ServerCache]:
    """Get cached server information if available and not expired.

    Returns:
        Cached server data if available and fresh, None otherwise
    """
    try:
        if not SERVERS_CACHE_FILE.exists():
            return None
            
        data = json.loads(SERVERS_CACHE_FILE.read_text())
        if not isinstance(data, dict):
            return None

        last_updated = _parse_timestamp(_safe_dict_get(data, "last_updated", 0))
        
        # Check if cache is expired
        if time.time() - last_updated > SERVERS_CACHE_TTL:
            return None
            
        # Validate and convert data
        cache_data: ServerCache = {
            "servers": cast(List[ServerInfo], _safe_dict_get_list(data, "servers", [])),
            "locations": cast(Dict[str, ServerLocation], _safe_dict_get_dict(data, "locations", {})),
            "last_updated": last_updated
        }
        
        return cache_data
        
    except Exception as e:
        logger.warning(f"Failed to read server cache: {e}")
        return None


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
        self._servers_cache: Optional[ServerCache] = None
        self._last_cache_update: float = 0
        self._failed_servers = set()  # Track failed servers in this session

    def _validate_country_code(self, country_code: str | None) -> str | None:
        """Validate and normalize country code.

        Args:
            country_code: Two-letter country code or None

        Returns:
            Normalized uppercase country code or None if no code provided

        Raises:
            ServerError: If country code is invalid

        """
        if not country_code:
            return None

        normalized = country_code.upper()
        if not isinstance(normalized, str) or len(normalized) != 2:
            raise ServerError(f"Invalid country code format: {country_code}")

        # Verify country exists in cache
        cache = self.get_servers_cache()
        if not cache:
            raise ServerError("No server information available")

        for location in cache["locations"].values():
            if location["country"]["code"].upper() == normalized:
                return normalized

        # Get list of available countries for better error message
        available_countries = sorted(list({
            loc["country"]["code"].upper()
            for loc in cache["locations"].values()
            if loc["country"]["code"]
        }))

        raise ServerError(
            f"Country code not found: {normalized}. "
            f"Available countries: {', '.join(available_countries)}"
        )

    def fetch_server_info(self, country: str | None = None) -> tuple[str, str] | None:
        """Fetch information about recommended servers supporting OpenVPN.

        Queries the NordVPN v2 API for servers based on:
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
        try:
            # Get all servers from cache or API
            cache = self.get_servers_cache()
            if not cache:
                raise ServerError("Failed to get server list")

            servers = cache["servers"]
            locations = cache["locations"]

            # Create location lookup by ID
            location_lookup = {}
            for loc_id, location in locations.items():
                if isinstance(location, dict):
                    location_lookup[str(loc_id)] = location

            # Filter for online servers with OpenVPN TCP support
            filtered_servers = []
            for server in servers:
                # Check if server is online
                if server["status"] != "online":
                    continue

                # Check if server has OpenVPN TCP (id: 5)
                has_tcp = False
                for tech in server["technologies"]:
                    if tech["id"] == 5 and tech["status"] == "online":
                        has_tcp = True
                        break
                if not has_tcp:
                    continue

                # Filter by country if specified
                if country:
                    normalized_country = self._validate_country_code(country)
                    server_country = None
                    for loc_id in server["location_ids"]:
                        location = location_lookup.get(str(loc_id))
                        if location and location["country"]["code"].upper() == normalized_country:
                            server_country = normalized_country
                            break
                    if not server_country:
                        continue

                filtered_servers.append(server)

            if not filtered_servers:
                # Get list of available countries
                available_countries = sorted(list({
                    loc["country"]["code"].upper()
                    for loc in locations.values()
                    if loc["country"]["code"]
                }))
                error_msg = f"No servers available{' in ' + country.upper() if country else ''}"
                if country:
                    error_msg += f"\nAvailable countries: {', '.join(available_countries)}"
                raise ServerError(error_msg)

            # Sort by load and select the least loaded server
            server = min(filtered_servers, key=lambda x: x["load"])
            hostname = server["hostname"]
            if not hostname:
                raise ServerError("Invalid server data received")

            if self.api_client.verbose:
                self.logger.debug(f"Selected server {hostname} with load {server['load']}%")

            return hostname, server.get("station", "")

        except Exception as e:
            raise ServerError(f"Failed to fetch server info: {e}")

    def get_servers_cache(self) -> Optional[ServerCache]:
        """Get server information from cache or API.

        Returns:
            Server information if available, None if both cache and API fail
        """
        try:
            # Try to get from memory cache first
            if self._servers_cache and time.time() - self._last_cache_update <= SERVERS_CACHE_TTL:
                return self._servers_cache

            # Try to get from file cache
            file_cache = get_cached_servers()
            if file_cache:
                self._servers_cache = file_cache
                self._last_cache_update = time.time()
                return file_cache

            # Fetch from API
            response = requests.get(
                "https://api.nordvpn.com/v1/servers",  # Use v1 API for more reliable response format
                headers=API_HEADERS,
                timeout=10
            )
            response.raise_for_status()
            api_data = response.json()

            # Initialize cache data structure
            new_cache: ServerCache = {
                "servers": [],
                "locations": {},
                "last_updated": time.time()
            }

            # Process API response (v1 API returns a list of servers)
            if not isinstance(api_data, list):
                self.logger.warning("Invalid API response format")
                return None

            # Extract servers and locations
            servers: List[ServerInfo] = []
            locations: Dict[str, ServerLocation] = {}
            location_ids = set()

            for item in api_data:
                if not isinstance(item, dict):
                    continue

                # Extract server data
                if "hostname" in item:
                    # Get technologies
                    technologies: List[Technology] = []
                    for tech in item.get("technologies", []):
                        if not isinstance(tech, dict):
                            continue
                        tech_id = tech.get("id")
                        if tech_id is None:
                            continue
                        technology: Technology = {
                            "id": int(tech_id),
                            "status": str(tech.get("status", ""))
                        }
                        if tech.get("metadata"):
                            technology["metadata"] = cast(List[Dict[str, str]], tech["metadata"])
                        technologies.append(technology)

                    server_info: ServerInfo = {
                        "hostname": str(item.get("hostname", "")),
                        "location_ids": [str(item.get("location", {}).get("id", ""))],
                        "status": str(item.get("status", "")),
                        "load": int(item.get("load", 0)),
                        "technologies": technologies
                    }
                    servers.append(server_info)

                # Extract location data
                location_data = item.get("location", {})
                if isinstance(location_data, dict):
                    loc_id = str(location_data.get("id", ""))
                    if loc_id and loc_id not in location_ids:
                        country_data = location_data.get("country", {})
                        if isinstance(country_data, dict):
                            country: Country = {
                                "name": str(country_data.get("name", "")),
                                "code": str(country_data.get("code", ""))
                            }
                            location: ServerLocation = {
                                "id": loc_id,
                                "country": country
                            }
                            locations[loc_id] = location
                            location_ids.add(loc_id)

            new_cache["servers"] = servers
            new_cache["locations"] = locations

            # Cache the data
            cache_servers(cast(Dict[str, Any], new_cache))
            
            self._servers_cache = new_cache
            self._last_cache_update = time.time()
            return new_cache

        except Exception as e:
            self.logger.warning(f"Failed to get server information: {e}")
            return None

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
        """Basic server validation.

        Only checks:
        1. Has valid hostname
        2. Has OpenVPN TCP support

        Args:
            server: Server data to validate

        Returns:
            bool: True if server data is valid
        """
        if not isinstance(server, dict):
            return False

        # Check hostname
        hostname = server.get("hostname")
        if not isinstance(hostname, str) or not hostname:
            return False

        # Check OpenVPN TCP support
        has_openvpn_tcp = False
        for tech in server.get("technologies", []):
            tech_name = tech.get("name", "")
            if (
                isinstance(tech, dict)
                and isinstance(tech_name, str)
                and "OpenVPN TCP" in tech_name
            ):
                has_openvpn_tcp = True
                break

        return has_openvpn_tcp

    def _test_server(self, server: Dict[str, Any]) -> tuple[Dict[str, Any], float]:
        """Test a server's response time using both ping and TCP connection.

        Args:
            server: Server information dictionary

        Returns:
            Tuple of (server, score) where score is combined ping/TCP time
            Lower score is better, float('inf') means failed
        """
        hostname = _safe_dict_get(server, "hostname")
        if not hostname:
            return server, float("inf")

        try:
            # Quick TCP connection test first (more important for VPN)
            tcp_time = float("inf")
            try:
                # Create a less strict SSL context for testing
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                start = time.time()
                with socket.create_connection((hostname, 443), timeout=1) as sock:
                    # Just test basic TCP connection first
                    tcp_time = (time.time() - start) * 1000  # Convert to ms
                    
                    try:
                        # Try SSL handshake but don't fail if it doesn't work
                        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                            ssock.do_handshake()
                    except ssl.SSLError:
                        # SSL failed but TCP worked, add penalty to score
                        tcp_time *= 1.5

            except (socket.timeout, socket.error) as e:
                if self.api_client.verbose:
                    self.logger.debug(f"TCP test failed for {hostname}: {e}")
                return server, float("inf")

            # Quick single ping test
            ping_time = float("inf")
            try:
                import platform
                system = platform.system().lower()

                if system == "darwin":  # macOS
                    cmd = ["ping", "-c", "1", "-W", "1", "-t", "1", hostname]
                elif system == "windows":
                    cmd = ["ping", "-n", "1", "-w", "1000", hostname]
                else:  # Linux and others
                    cmd = ["ping", "-c", "1", "-W", "1", hostname]

                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=2,
                    check=False
                )

                if result.returncode == 0:
                    # Parse time from output
                    if system == "darwin":
                        # macOS: round-trip min/avg/max/stddev = 20.237/20.237/20.237/0.000 ms
                        for line in result.stdout.splitlines():
                            if "round-trip" in line:
                                try:
                                    ping_time = float(line.split("=")[1].strip().split("/")[0])
                                    break
                                except (IndexError, ValueError):
                                    continue
                    else:
                        # Linux/Windows: time=20.2 ms
                        try:
                            ping_time = float(result.stdout.split("time=")[1].split()[0].rstrip("ms"))
                        except (IndexError, ValueError):
                            pass

            except (subprocess.TimeoutExpired, subprocess.SubprocessError) as e:
                if self.api_client.verbose:
                    self.logger.debug(f"Ping failed for {hostname}: {e}")
                # Don't fail completely if ping fails but TCP worked
                ping_time = tcp_time * 1.5  # Estimate ping as 1.5x TCP time

            # Combined score (70% TCP, 30% ping)
            # TCP matters more for VPN performance
            score = (tcp_time * 0.7) + (ping_time * 0.3)

            if self.api_client.verbose:
                self.logger.debug(
                    f"Server {hostname} test results: "
                    f"tcp={tcp_time:.1f}ms, ping={ping_time:.1f}ms, score={score:.1f}ms"
                )

            return server, score

        except Exception as e:
            if self.api_client.verbose:
                self.logger.debug(f"Failed to test server {hostname}: {e}")
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
            List of selected servers, may be fewer than requested count if not enough servers available

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

        # If we still need more servers and have unselected ones available
        remaining_servers = [s for s in servers if s not in selected]
        if remaining_servers and len(selected) < count:
            # Only try to sample what's available
            sample_size = min(count - len(selected), len(remaining_servers))
            if sample_size > 0:
                remaining = random.sample(remaining_servers, sample_size)
                selected.extend(remaining)

        if not selected:
            # Ensure we return at least one server if available
            if servers:
                selected.append(random.choice(servers))

        return selected

    def select_fastest_server(self, country_code: str | None = None) -> list[Dict[str, Any]]:
        """Select fastest servers in a country based on ping times.

        Args:
            country_code: Two-letter country code

        Returns:
            List of server dicts sorted by speed (fastest first)
        """
        try:
            # Get all servers
            cache = self.get_servers_cache()
            if not cache:
                raise ServerError("No servers available")

            servers = cache["servers"]
            locations = cache["locations"]

            if not servers:
                raise ServerError("No servers available")

            # Create location lookup by ID
            location_lookup = {str(loc["id"]): loc for loc in locations.values()}

            # Filter by country if specified
            if country_code:
                country_code = country_code.upper()
                filtered_servers = []
                
                for server in servers:
                    # Check each location ID
                    for loc_id in server["location_ids"]:
                        location = location_lookup.get(str(loc_id))
                        if location and location["country"]["code"].upper() == country_code:
                            filtered_servers.append(server)
                            break
                
                servers = filtered_servers

                if not servers:
                    # Get list of available countries
                    available_countries = sorted(list({
                        loc["country"]["code"].upper()
                        for loc in locations.values()
                        if loc["country"]["code"]
                    }))
                    raise ServerError(
                        f"No servers available in {country_code}. "
                        f"Available countries: {', '.join(available_countries)}"
                    )

            # Remove failed servers
            servers = [s for s in servers if s["hostname"] not in self._failed_servers]
            if not servers:
                self._failed_servers.clear()  # Reset failed servers if none left
                return self.select_fastest_server(country_code)  # Try again

            # Take 20 servers with highest load
            servers.sort(key=lambda x: x["load"])
            logger.debug(servers)

            # Test response times
            results = []
            for server in servers:
                hostname = server["hostname"]
                if not hostname:
                    continue

                # Test server response time
                server_result, score = self._test_server(cast(Dict[str, Any], server))
                if score < float("inf"):
                    results.append((server_result, score))

            # Sort by response time
            results.sort(key=lambda x: x[1])
            return [r[0] for r in results]  # Return servers only, sorted by speed

        except Exception as e:
            if isinstance(e, ServerError):
                raise
            raise ServerError(f"Failed to select server: {e}")

    def _get_country_id(self, country_code: str) -> str:
        """Get NordVPN country ID from country code.

        Args:
            country_code: Two-letter country code

        Returns:
            Country ID or empty string if not found
        """
        try:
            # Check our cache
            cache = self.get_servers_cache()
            if not cache:
                return ""

            # Look through locations for matching country
            for location in cache["locations"].values():
                if isinstance(location, dict) and isinstance(location.get("country"), dict):
                    country = location["country"]
                    if country.get("code", "").upper() == country_code.upper():
                        return str(country.get("id", ""))

        except Exception as e:
            if self.api_client.verbose:
                self.logger.warning(f"Failed to get country ID: {e}")

        return ""

    def get_random_country(self) -> str:
        """Get a random country code from available servers.

        Returns:
            Two-letter country code, defaults to "US" on error

        Note:
            Uses cache to avoid unnecessary API calls.

        """
        try:
            cache = self.get_servers_cache()
            if not cache:
                raise ServerError("No servers available")

            countries = {
                loc["country"]["code"].upper()
                for loc in cache["locations"].values()
                if loc["country"]["code"]
            }
            if not countries:
                raise ServerError("No countries found in server list")

            selected = random.choice(list(countries))
            if self.api_client.verbose:
                self.logger.debug(f"Selected random country: {selected}")
            return selected

        except Exception as e:
            self.logger.warning(f"Failed to get random country: {e}")
            return "US"

    def get_country_info(self, country_code: str) -> dict[str, Any] | None:
        """Get country information from NordVPN API.

        Args:
            country_code: Two-letter country code

        Returns:
            Dictionary with country information or None if not found

        Note:
            Uses cache first, falls back to API if needed.
            Cache format matches API response for consistency.

        """
        if not country_code:
            return None

        normalized = country_code.upper()

        try:
            # First check cache
            cache = self.get_servers_cache()
            if not cache:
                return None

            for location in cache["locations"].values():
                if location["country"]["code"].upper() == normalized:
                    return {
                        "code": location["country"]["code"],
                        "name": location["country"]["name"],
                        "id": location["id"],
                    }

            return None

        except Exception as e:
            if self.api_client.verbose:
                self.logger.warning(f"Failed to get country info for {normalized}: {e}")
            return None
