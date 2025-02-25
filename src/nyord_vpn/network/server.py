import json
import platform
import subprocess
import time
import secrets
import re
from typing import Any, TypedDict, NotRequired, cast

from loguru import logger
import requests

from nyord_vpn.api.api import NordVPNAPI
from nyord_vpn.storage.models import ServerError
from nyord_vpn.utils.utils import API_HEADERS, CACHE_DIR


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
- Uses NordVPNAPI (api/api.py) for server data
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


class TechnologyMetadata(TypedDict):
    """Metadata for technology information."""

    name: str
    value: str


class Technology(TypedDict):
    """Server technology information."""

    id: int
    status: str
    metadata: NotRequired[list[TechnologyMetadata]]


class ServerInfo(TypedDict):
    """Server information structure."""

    hostname: str
    location_ids: list[str]
    status: str
    load: int
    technologies: list[Technology]


class ServerCache(TypedDict):
    """Cache structure for server information."""

    servers: list[ServerInfo]
    locations: dict[str, ServerLocation]
    last_updated: float


# Constants
SERVERS_CACHE_FILE = CACHE_DIR / "servers.json"
SERVERS_CACHE_TTL = 3600  # 1 hour in seconds


def _safe_dict_get(d: dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary."""
    return d.get(key, default) if isinstance(d, dict) else default


def _safe_get(d: dict[str, Any] | None, key: str, default: Any = None) -> Any:
    """Safely get a value from a dictionary that might be None."""
    if d is None:
        return default
    return _safe_dict_get(d, key, default)


def _safe_str_get(s: str | None, key: str, default: Any = None) -> Any:
    """Safely get a value from a string that might be None."""
    if s is None:
        return default
    try:
        return s[int(key)] if key.isdigit() else default
    except (ValueError, IndexError):
        return default


def _safe_dict_access(d: dict[str, Any], key: str) -> Any:
    """Safely access a dictionary key that must exist."""
    if not isinstance(d, dict) or key not in d:
        raise KeyError(f"Required key {key} not found in dictionary")
    return d[key]


def _safe_dict_cast(d: Any) -> dict[str, Any]:
    """Cast a value to a dictionary if possible."""
    if not isinstance(d, dict):
        return {}
    return cast(dict[str, Any], d)


def _safe_dict_get_str(d: dict[str, Any], key: str, default: str = "") -> str:
    """Safely get a string value from a dictionary."""
    value = _safe_dict_get(d, key, default)
    return str(value) if value is not None else default


def _safe_dict_get_int(d: dict[str, Any], key: str, default: int = 0) -> int:
    """Safely get an integer value from a dictionary."""
    value = _safe_dict_get(d, key, default)
    try:
        return int(value) if value is not None else default
    except (ValueError, TypeError):
        return default


def _safe_dict_get_list(
    d: dict[str, Any], key: str, default: list[Any] | None = None
) -> list[Any]:
    """Safely get a list value from a dictionary."""
    if default is None:
        default = []
    value = _safe_dict_get(d, key, default)
    return value if isinstance(value, list) else default


def _safe_dict_get_dict(
    d: dict[str, Any], key: str, default: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Safely get a dictionary value from a dictionary."""
    if default is None:
        default = {}
    value = _safe_dict_get(d, key, default)
    return value if isinstance(value, dict) else default


def cache_servers(data: dict[str, Any]) -> None:
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
        temp_file = SERVERS_CACHE_FILE.with_suffix(".tmp")
        temp_file.write_text(json.dumps(data, indent=2))

        # Atomic rename
        temp_file.replace(SERVERS_CACHE_FILE)

    except Exception as e:
        logger.warning(f"Failed to cache server information: {e}")


def _parse_timestamp(timestamp: Any) -> float:
    """Parse a timestamp value into a float.

    Handles both float timestamps and ISO format strings.
    """
    if isinstance(timestamp, int | float):
        return float(timestamp)
    if isinstance(timestamp, str):
        try:
            # Try parsing as float first
            return float(timestamp)
        except ValueError:
            try:
                # Try parsing as ISO format
                from datetime import datetime

                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                return dt.timestamp()
            except ValueError:
                return 0.0
    return 0.0


def get_cached_servers() -> ServerCache | None:
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
            "servers": cast(list[ServerInfo], _safe_dict_get_list(data, "servers", [])),
            "locations": cast(
                dict[str, ServerLocation], _safe_dict_get_dict(data, "locations", {})
            ),
            "last_updated": last_updated,
        }

        return cache_data

    except (OSError, json.JSONDecodeError) as e:
        logger.warning(f"Failed to load cached server information: {e}")
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

    def __init__(self, api_client: NordVPNAPI) -> None:
        """Initialize server manager with API client.

        Sets up the server manager with:
        1. API client for server information retrieval
        2. Logging configuration
        3. Server cache initialization
        4. Failed servers tracking

        Args:
            api_client: NordVPN API client for server information

        """
        self.api_client = api_client
        self.logger = logger
        self._servers_cache: ServerCache | None = None
        self._last_cache_update: float = 0
        self._failed_servers: set[str] = set()  # Track failed servers in this session
        self._verbose: bool = False

    @property
    def verbose(self) -> bool:
        """Get verbose mode setting."""
        return self._verbose

    @verbose.setter
    def verbose(self, value: bool) -> None:
        """Set verbose mode.

        Args:
            value: Whether to enable verbose logging

        """
        self._verbose = value

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

        # Get servers from the new API
        try:
            servers, _, _, locations, _ = self.api_client.get_servers()

            # Verify country exists
            for location in locations:
                if location.country and location.country.code.upper() == normalized:
                    return normalized

            # Get list of available countries for better error message
            available_countries = sorted(
                {
                    loc.country.code.upper()
                    for loc in locations
                    if loc.country and loc.country.code
                }
            )

            raise ServerError(
                f"Country code not found: {normalized}. "
                f"Available countries: {', '.join(available_countries)}"
            )

        except Exception:
            # Fall back to the cache method
            cache = self.get_servers_cache()
            if not cache:
                raise ServerError("No server information available")

            for location in cache["locations"].values():
                if location["country"]["code"].upper() == normalized:
                    return normalized

            # Get list of available countries for better error message
            available_countries = sorted(
                {
                    loc["country"]["code"].upper()
                    for loc in cache["locations"].values()
                    if loc["country"]["code"]
                }
            )

            raise ServerError(
                f"Country code not found: {normalized}. "
                f"Available countries: {', '.join(available_countries)}"
            )

    def fetch_server_info(self, country: str | None = None) -> tuple[str, str] | None:
        """Fetch information about recommended servers supporting OpenVPN.

        Queries the NordVPN API for servers based on:
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
            # Validate country code
            country_code = self._validate_country_code(country)

            # Find best server using the new API
            best_server = self.api_client.find_best_server(
                country_code=country_code,
                technology_identifier="openvpn_tcp",
                use_v2=True,
            )

            # Extract hostname
            hostname = getattr(best_server, "hostname", None)
            if not hostname:
                raise ServerError("Best server has no hostname")

            # Extract station (if available)
            station = getattr(best_server, "station", "")

            return hostname, station

        except Exception as e:
            if isinstance(e, ServerError):
                raise
            raise ServerError(f"Failed to fetch server information: {e}")

    def get_servers_cache(self) -> ServerCache | None:
        """Get server information from cache or API.

        Returns:
            Server information if available, None if both cache and API fail

        """
        try:
            # Try to get from memory cache first
            if (
                self._servers_cache
                and time.time() - self._last_cache_update <= SERVERS_CACHE_TTL
            ):
                return self._servers_cache

            # Try to get from file cache
            file_cache = get_cached_servers()
            if file_cache:
                self._servers_cache = file_cache
                self._last_cache_update = time.time()
                return file_cache

            # Try to get from the new API and convert to cache format
            try:
                servers_data, _, _, locations_data, technologies_data = (
                    self.api_client.get_servers()
                )

                # Convert to ServerCache format
                new_cache: ServerCache = {
                    "servers": [],
                    "locations": {},
                    "last_updated": time.time(),
                }

                # Process locations
                for location in locations_data:
                    if location.id and location.country:
                        location_id = str(location.id)
                        new_cache["locations"][location_id] = {
                            "id": location_id,
                            "country": {
                                "name": location.country.name,
                                "code": location.country.code,
                            },
                        }

                # Process servers
                for server in servers_data:
                    # Skip servers without hostname
                    if not server.hostname:
                        continue

                    # Process technologies
                    server_technologies: list[Technology] = []
                    for tech in server.technologies:
                        technology: Technology = {
                            "id": tech.id,
                            "status": tech.status or "",
                        }
                        if hasattr(tech, "metadata") and tech.metadata:
                            technology["metadata"] = [
                                {"name": meta.name, "value": meta.value}
                                for meta in tech.metadata
                            ]
                        server_technologies.append(technology)

                    # Create server info
                    server_info: ServerInfo = {
                        "hostname": server.hostname,
                        "location_ids": [
                            str(loc.id) for loc in server.locations if loc.id
                        ],
                        "status": server.status,
                        "load": server.load,
                        "technologies": server_technologies,
                    }
                    new_cache["servers"].append(server_info)

                # Cache the results
                self._servers_cache = new_cache
                self._last_cache_update = time.time()
                cache_servers(cast(dict[str, Any], new_cache))

                return new_cache

            except Exception as e:
                logger.warning(f"Failed to get server information from API: {e}")

                # Fetch from legacy API as fallback
                response = requests.get(
                    "https://api.nordvpn.com/v2/servers",
                    headers=API_HEADERS,
                    timeout=10,
                )
                response.raise_for_status()
                api_data = response.json()

                # Process API response
                if not isinstance(api_data, dict):
                    self.logger.warning(
                        "Invalid API response format - expected object with servers and locations"
                    )
                    return None

                # Initialize cache data structure
                new_cache: ServerCache = {
                    "servers": [],
                    "locations": {},
                    "last_updated": time.time(),
                }

                # Extract servers and build locations map
                servers: list[ServerInfo] = []
                locations: dict[str, ServerLocation] = {}

                # First pass: Process locations from the API response
                for location in api_data.get("locations", []):
                    if not isinstance(location, dict):
                        continue

                    location_id = str(location.get("id", ""))
                    if not location_id:
                        continue

                    country_data = location.get("country", {})
                    if isinstance(country_data, dict):
                        country: Country = {
                            "name": str(country_data.get("name", "")),
                            "code": str(country_data.get("code", "")),
                        }
                        locations[location_id] = {"id": location_id, "country": country}

                # Second pass: Process servers
                for item in api_data.get("servers", []):
                    if not isinstance(item, dict):
                        continue

                    # Get technologies
                    technologies: list[Technology] = []
                    for tech in item.get("technologies", []):
                        if not isinstance(tech, dict):
                            continue
                        tech_id = tech.get("id")
                        if tech_id is None:
                            continue
                        technology: Technology = {
                            "id": int(tech_id),
                            "status": str(tech.get("status", "")),
                        }
                        if tech.get("metadata"):
                            technology["metadata"] = [
                                {
                                    "name": str(meta.get("name", "")),
                                    "value": str(meta.get("value", "")),
                                }
                                for meta in tech.get("metadata", [])
                                if isinstance(meta, dict)
                            ]
                        technologies.append(technology)

                    # Create server info
                    server_info: ServerInfo = {
                        "hostname": str(item.get("hostname", "")),
                        "location_ids": [
                            str(lid) for lid in item.get("location_ids", [])
                        ],
                        "status": str(item.get("status", "")),
                        "load": int(item.get("load", 0)),
                        "technologies": technologies,
                    }
                    servers.append(server_info)

                new_cache["servers"] = servers
                new_cache["locations"] = locations

                # Cache the results
                self._servers_cache = new_cache
                self._last_cache_update = time.time()
                cache_servers(cast(dict[str, Any], new_cache))

                return new_cache

        except Exception as e:
            self.logger.warning(f"Failed to get server information: {e}")
            return None

    def _is_valid_hostname(self, hostname: str) -> bool:
        """Validate hostname format to prevent command injection.

        Args:
            hostname: Hostname to validate

        Returns:
            bool: True if hostname is valid, False otherwise

        """
        # Check for valid hostname format (letters, numbers, dots, hyphens)
        # This is a strict check to prevent command injection
        if not hostname or len(hostname) > 253:
            return False

        # Split the hostname into parts and validate each part
        parts = hostname.split(".")

        # Check if we have at least 2 parts (domain.tld)
        if len(parts) < 2:
            return False

        # Validate each part of the hostname
        for part in parts:
            # Each part must:
            # - Not be empty
            # - Start and end with alphanumeric characters
            # - Contain only alphanumeric characters and hyphens
            # - Not exceed 63 characters
            if not part or len(part) > 63:
                return False

            if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$", part):
                return False

        return True

    def _ping_server(self, hostname: str) -> float:
        """Ping a server and return response time in ms.

        Args:
            hostname: Server hostname to ping

        Returns:
            float: Ping time in milliseconds, or float('inf') if ping failed

        """
        try:
            # Platform-specific ping command
            system = platform.system().lower()

            # Validate hostname (strict defense against command injection)
            if not self._is_valid_hostname(hostname):
                self.logger.warning(f"Invalid hostname format: {hostname}")
                return float("inf")

            # Convert hostname to lowercase for consistency
            hostname = hostname.lower()

            # Ensure hostname is not an IP address to prevent IP-based injection
            if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", hostname):
                self.logger.warning(
                    f"IP addresses not allowed for ping safety: {hostname}"
                )
                return float("inf")

            # Construct command based on platform with proper escaping
            if system == "windows":
                cmd = ["ping", "-n", "2", "-w", "1000", hostname]
            elif system == "darwin":  # macOS
                cmd = ["ping", "-c", "2", "-W", "1", "-t", "1", hostname]
            else:  # Linux and others
                cmd = ["ping", "-c", "2", "-W", "1", hostname]

            # Log the command if in verbose mode
            if self.verbose:
                self.logger.debug(f"Running ping command: {' '.join(cmd)}")

            # Execute the command securely with resource limitations
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3,
                check=False,  # Don't raise an exception on non-zero return
                env={},  # Run with empty environment for additional security
            )

            if result.returncode == 0:
                # Extract time from ping output more robustly
                min_time = float("inf")
                for line in result.stdout.splitlines():
                    if self.verbose:
                        self.logger.debug(f"Ping output line: {line}")

                    # Look for min/avg/max line
                    if "min/avg/max" in line:
                        try:
                            # Format: round-trip min/avg/max/stddev = 18.894/18.894/18.894/0.000 ms
                            stats = line.split("=")[1].strip().split("/")
                            min_time = float(stats[0])
                            if self.verbose:
                                self.logger.debug(
                                    f"Parsed min time from stats: {min_time}ms",
                                )
                            return min_time
                        except (IndexError, ValueError) as e:
                            if self.verbose:
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
                            if self.verbose:
                                self.logger.debug(
                                    f"Parsed time from response: {ping_time}ms",
                                )
                        except (IndexError, ValueError) as e:
                            if self.verbose:
                                self.logger.debug(
                                    f"Failed to parse time from line '{line}': {e}",
                                )
                            continue

                if min_time < float("inf"):
                    if self.verbose:
                        self.logger.debug(
                            f"Server {hostname} responded in {min_time}ms",
                        )
                    return min_time

                # If we couldn't parse any times but ping succeeded
                if self.verbose:
                    self.logger.debug(
                        f"Server {hostname} responded but couldn't parse time from output:\n{result.stdout}",
                    )
                return float("inf")
            if self.verbose:
                self.logger.debug(
                    f"Server {hostname} ping failed with code {result.returncode}:\n"
                    f"stdout: {result.stdout}\n"
                    f"stderr: {result.stderr}",
                )
            return float("inf")
        except (subprocess.SubprocessError, subprocess.TimeoutExpired) as e:
            if self.verbose:
                self.logger.debug(f"Error pinging {hostname}: {e}")
            return float("inf")

    def _is_valid_server(self, server: Any) -> bool:
        """Check if a server is valid and usable.

        Args:
            server: Server object to validate

        Returns:
            bool: True if server is valid, False otherwise

        A valid server must:
        1. Be online
        2. Have a valid hostname (not in failed servers list)
        3. Support OpenVPN TCP technology

        """
        # Basic validation for dictionary-like objects
        if not hasattr(server, "get") and not hasattr(server, "__dict__"):
            return False

        # Get hostname - works for both dict and object
        hostname = (
            server.get("hostname", "")
            if hasattr(server, "get")
            else getattr(server, "hostname", "")
        )

        # Check hostname
        if not hostname or hostname in self._failed_servers:
            return False

        # Get status - works for both dict and object
        status = (
            server.get("status", "")
            if hasattr(server, "get")
            else getattr(server, "status", "")
        )

        # Check status
        if status != "online":
            return False

        # Check for OpenVPN TCP support
        technologies = (
            server.get("technologies", [])
            if hasattr(server, "get")
            else getattr(server, "technologies", [])
        )

        # Look for OpenVPN TCP in technologies
        has_openvpn_tcp = False
        for tech in technologies:
            if hasattr(tech, "get"):
                tech_name = tech.get("name", "")
            else:
                tech_name = getattr(tech, "name", "")

            if "OpenVPN TCP" in tech_name:
                if self.verbose:
                    self.logger.debug(f"Found OpenVPN TCP support: {tech_name}")
                has_openvpn_tcp = True
                break

        if not has_openvpn_tcp and self.verbose:
            self.logger.debug(f"Server {hostname} does not support OpenVPN TCP")

        return has_openvpn_tcp

    def _test_server(self, server: Any) -> tuple[Any, float]:
        """Test server response time and load.

        Args:
            server: Server object to test

        Returns:
            Tuple of server object and calculated score (lower is better)

        """
        hostname = server.get("hostname", "")
        if not hostname:
            return server, float("inf")

        # Get server load
        load = server.get("load", 100)

        # Ping the server
        ping_time = self._ping_server(hostname)

        # Calculate score: combination of ping time and load
        # Lower score is better
        score = ping_time * (1 + load / 100)

        # Update server with ping time
        server_copy = server.copy()
        server_copy["ping_time"] = ping_time

        return server_copy, score

    def _select_diverse_servers(
        self, servers: list[ServerInfo], count: int = 4
    ) -> list[ServerInfo]:
        """Select a diverse set of servers for testing.

        This method selects a diverse sample of servers to test,
        ensuring variety in load and geographical distribution.

        Args:
            servers: List of servers to select from
            count: Number of servers to select

        Returns:
            List of selected servers

        """
        if not servers:
            return []

        # If we have few servers, test them all
        if len(servers) <= count:
            return servers

        # Divide servers into load groups (low, medium, high)
        servers_by_load = sorted(servers, key=lambda s: s.get("load", 100))

        # Select servers using cryptographic random for security
        result = []

        # Get low-load servers (first 25%)
        low_load = servers_by_load[: len(servers_by_load) // 4]
        if low_load:
            result.append(low_load[secrets.randbelow(len(low_load))])

        # Get medium-load servers (middle 50%)
        mid_start = len(servers_by_load) // 4
        mid_end = mid_start + len(servers_by_load) // 2
        medium_load = servers_by_load[mid_start:mid_end]
        if medium_load:
            result.append(medium_load[secrets.randbelow(len(medium_load))])

        # Get remaining servers randomly to fill the count
        remaining = count - len(result)
        if remaining > 0 and servers:
            # Convert to set to avoid duplicates
            selected_hostnames = {s.get("hostname", "") for s in result}
            remaining_servers = [
                s for s in servers if s.get("hostname", "") not in selected_hostnames
            ]

            for _ in range(min(remaining, len(remaining_servers))):
                if not remaining_servers:
                    break
                idx = secrets.randbelow(len(remaining_servers))
                result.append(remaining_servers[idx])
                remaining_servers.pop(idx)

        return result

    def select_fastest_server(
        self, country_code: str | None = None
    ) -> list[dict[str, Any]]:
        """Select fastest servers in a country based on ping times.

        Args:
            country_code: Two-letter country code

        Returns:
            List of server dicts sorted by speed (fastest first)

        """
        try:
            # Try to use the new API first
            try:
                # Validate country code
                if country_code:
                    country_code = self._validate_country_code(country_code)

                # Find best server using the API
                best_server = self.api_client.find_best_server(
                    country_code=country_code,
                    technology_identifier="openvpn_tcp",
                    use_v2=True,
                )

                # Convert API server to dict format for consistency
                server_dict = {
                    "hostname": best_server.hostname,
                    "load": best_server.load,
                    "status": best_server.status,
                    "ping_time": 0,  # We don't have this yet
                }

                # Test the ping time
                hostname = server_dict["hostname"]
                if hostname:
                    ping_time = self._ping_server(hostname)
                    server_dict["ping_time"] = ping_time

                return [server_dict]

            except Exception as e:
                logger.warning(
                    f"Failed to get fastest server from API, falling back to cache: {e}"
                )
                # Fall back to cache method

            # Get all servers from cache
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
                        if (
                            location
                            and location["country"]["code"].upper() == country_code
                        ):
                            filtered_servers.append(server)
                            break

                servers = filtered_servers

                if not servers:
                    # Get list of available countries
                    available_countries = sorted(
                        {
                            loc["country"]["code"].upper()
                            for loc in locations.values()
                            if loc["country"]["code"]
                        }
                    )
                    raise ServerError(
                        f"No servers available in {country_code}. "
                        f"Available countries: {', '.join(available_countries)}"
                    )

            # Remove failed servers
            servers = [s for s in servers if s["hostname"] not in self._failed_servers]
            if not servers:
                self._failed_servers.clear()  # Reset failed servers if none left
                return self.select_fastest_server(country_code)  # Try again

            # Select a diverse set of servers to test
            test_servers = self._select_diverse_servers(servers)

            # Test response times
            results = []
            for server in test_servers:
                hostname = server["hostname"]
                if not hostname:
                    continue

                # Test server response time
                server_result, score = self._test_server(server)
                if score < float("inf"):
                    results.append((server_result, score))

            # Sort by response time
            results.sort(key=lambda x: x[1])
            return [r[0] for r in results]  # Return servers only, sorted by speed

        except Exception as e:
            if isinstance(e, ServerError):
                raise
            raise ServerError(f"Failed to select server: {e}")

    def get_country_info(self, country_code: str) -> dict[str, Any]:
        """Get information about a country by its code.

        Args:
            country_code: Two-letter country code

        Returns:
            Dict with country information

        Raises:
            ServerError: If country not found or invalid code

        """
        # Validate country code
        normalized_code = self._validate_country_code(country_code)
        if not normalized_code:
            raise ServerError(f"Invalid country code: {country_code}")

        # Try to use the new API first
        try:
            # Get country info from API
            _, _, _, locations, _ = self.api_client.get_servers()

            # Find the country
            for location in locations:
                if (
                    location.country
                    and location.country.code.upper() == normalized_code
                ):
                    return {
                        "name": location.country.name,
                        "code": location.country.code,
                        "id": getattr(location.country, "id", None),
                    }

            raise ServerError(f"Country not found: {normalized_code}")

        except Exception as e:
            if isinstance(e, ServerError):
                raise

            logger.warning(
                f"Failed to get country info from API, falling back to cache: {e}"
            )

            # Fall back to cache method
            cache = self.get_servers_cache()
            if not cache:
                raise ServerError("No server information available")

            # Find the country in locations
            for loc in cache["locations"].values():
                country_dict: dict[str, Any] = {}
                country_dict.update(loc["country"])
                return country_dict

            raise ServerError(f"Country not found: {normalized_code}")

    def get_random_country(self) -> str:
        """Get a random country code.

        Returns:
            Two-letter country code

        Raises:
            ServerError: If no countries available

        """
        # Try to use the new API first
        try:
            # Get countries from API
            _, _, _, locations, _ = self.api_client.get_servers()

            # Extract country codes
            country_codes = [
                loc.country.code.upper()
                for loc in locations
                if loc.country and loc.country.code
            ]

            if not country_codes:
                raise ServerError("No countries available")

            # Select a random country using cryptographically secure random
            return country_codes[secrets.randbelow(len(country_codes))]

        except Exception as e:
            logger.warning(
                f"Failed to get random country from API, falling back to cache: {e}"
            )

            # Fall back to cache method
            cache = self.get_servers_cache()
            if not cache:
                raise ServerError("No server information available")

            # Extract country codes
            country_codes = sorted(
                {
                    loc["country"]["code"].upper()
                    for loc in cache["locations"].values()
                    if loc["country"]["code"]
                }
            )

            if not country_codes:
                raise ServerError("No countries available")

            # Select a random country using cryptographically secure random
            return country_codes[secrets.randbelow(len(country_codes))]
