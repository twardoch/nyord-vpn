from typing import Optional, Tuple, List, Dict, Any, TypedDict, cast, Sequence, Union
import random
import subprocess
import time
import json
from pathlib import Path

import requests
from rich.progress import Progress, SpinnerColumn, TextColumn

from .utils import API_HEADERS, CACHE_DIR, CACHE_EXPIRY
from .models import ServerError


class ServerLocation(TypedDict):
    country: Dict[str, str]


class ServerTechnology(TypedDict):
    id: int
    status: str


class ServerData(TypedDict):
    hostname: str
    load: int
    status: str
    location_ids: List[str]
    technologies: List[ServerTechnology]
    station: Optional[str]


class APIResponse(TypedDict):
    servers: List[ServerData]
    locations: Dict[str, ServerLocation]


class ServerManager:
    def __init__(self, client) -> None:
        self.client = client
        self._failed_servers = set()  # Track failed servers in this session

    def fetch_server_info(
        self, country: Optional[str] = None
    ) -> Optional[Tuple[str, str]]:
        """Fetch information about a recommended server that supports OpenVPN."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://nordvpn.com/",
            "Origin": "https://nordvpn.com",
        }
        url = f"{self.client.BASE_API_URL}/servers/recommendations"
        params = {
            "filters[servers_technologies][identifier]": "openvpn_tcp",
            "limit": "5",
        }
        if country:
            from .utils import NORDVPN_COUNTRY_IDS

            country_id = NORDVPN_COUNTRY_IDS.get(country.upper())
            if not country_id:
                raise ServerError(f"Country code '{country}' not found")
            params["filters[country_id]"] = country_id

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, list) or not data:
                params.pop("filters[servers_technologies][identifier]", None)
                response = requests.get(url, params=params, headers=headers, timeout=10)
                response.raise_for_status()
                data = response.json()
            if not isinstance(data, list) or not data:
                raise ServerError(
                    f"No servers available{' in ' + country.upper() if country else ''}"
                )
            if self.client.verbose:
                self.client.logger.debug("Available servers retrieved.")
            server = min(data, key=lambda x: x.get("load", 100))
            hostname = server.get("hostname")
            if not isinstance(hostname, str) or not hostname:
                raise ServerError("Invalid server data received.")
            return hostname, server.get("station", "")
        except requests.RequestException as e:
            raise ServerError(f"Failed to fetch server info: {e}")

    def get_servers_cache(self) -> dict:
        """Get cached server list or fetch from API.

        Returns:
            dict: Server cache containing list of servers and metadata
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
                        if self.client.verbose:
                            self.client.logger.debug(
                                f"Using cached server list with {len(valid_servers)} valid servers"
                            )
                        cache["servers"] = valid_servers
                        return cache
                    else:
                        if self.client.verbose:
                            self.client.logger.warning(
                                "No valid servers in cache, fetching fresh data"
                            )
            except Exception as e:
                if self.client.verbose:
                    self.client.logger.warning(f"Failed to read cache: {e}")

        try:
            if self.client.verbose:
                self.client.logger.debug("Fetching server list from API...")

            # Use v2 API which has more detailed server info
            response = requests.get(
                f"{self.client.BASE_API_V2_URL}/servers",
                headers=API_HEADERS,
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            if self.client.verbose:
                self.client.logger.debug("Successfully fetched server data from API")

            # Extract servers from response
            raw_servers: List[Dict[str, Any]] = []
            locations_list: List[Dict[str, Any]] = []

            if isinstance(data, dict):
                if "servers" in data:
                    raw_servers = [dict(s) for s in data["servers"]]
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Found {len(raw_servers)} servers in API response"
                        )
                if "locations" in data:
                    locations_list = data["locations"]
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Found {len(locations_list)} locations in API response"
                        )
            elif isinstance(data, list):
                raw_servers = [dict(s) for s in data]
                if self.client.verbose:
                    self.client.logger.debug(
                        f"Found {len(raw_servers)} servers in API response (list format)"
                    )
            else:
                raise ValueError(f"Unexpected API response format: {type(data)}")

            # Create locations lookup
            locations: Dict[str, Dict[str, Any]] = {}
            for location in locations_list:
                if not isinstance(location, dict):
                    continue
                location_id = str(location.get("id"))
                if location_id:
                    locations[location_id] = location

            # Filter and validate servers
            valid_servers = []
            invalid_count = 0
            for server in raw_servers:
                if not isinstance(server, dict):
                    invalid_count += 1
                    continue

                # Check if server is online and supports OpenVPN TCP
                if server.get("status") != "online":
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Skipping offline server: {server.get('hostname')}"
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
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Skipping server without OpenVPN TCP: {server.get('hostname')}"
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
                        if not isinstance(location_id, (str, int)):
                            continue
                        location = locations.get(str(location_id))
                        if location and isinstance(location, dict):
                            country = location.get("country", {})
                            if isinstance(country, dict):
                                country_info = {
                                    "code": country.get("code", "").upper(),
                                    "name": country.get("name", "Unknown"),
                                }
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
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Skipping server without country info: {hostname}"
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
                    f"Total servers: {len(raw_servers)}, Invalid: {invalid_count}"
                )

            if self.client.verbose:
                country_counts = {}
                for server in valid_servers:
                    code = server["country"]["code"]
                    country_counts[code] = country_counts.get(code, 0) + 1
                self.client.logger.debug(
                    f"Found {len(valid_servers)} valid servers. "
                    f"Country distribution: "
                    + ", ".join(f"{k}: {v}" for k, v in sorted(country_counts.items()))
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
            self.client.logger.error(f"Failed to fetch servers: {e}")
            if cache_file.exists():
                try:
                    cache = json.loads(cache_file.read_text())
                    if isinstance(cache, dict) and isinstance(
                        cache.get("servers", []), list
                    ):
                        # Validate cached servers even in fallback
                        valid_servers = [
                            s for s in cache["servers"] if self._is_valid_server(s)
                        ]
                        if valid_servers:
                            if self.client.verbose:
                                self.client.logger.info(
                                    f"Using fallback cache with {len(valid_servers)} valid servers"
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

            if self.client.verbose:
                self.client.logger.debug(f"Running ping command: {' '.join(cmd)}")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3,  # Overall timeout
            )

            if result.returncode == 0:
                # Extract time from ping output more robustly
                min_time = float("inf")
                for line in result.stdout.splitlines():
                    if self.client.verbose:
                        self.client.logger.debug(f"Ping output line: {line}")

                    # Look for min/avg/max line
                    if "min/avg/max" in line:
                        try:
                            # Format: round-trip min/avg/max/stddev = 18.894/18.894/18.894/0.000 ms
                            stats = line.split("=")[1].strip().split("/")
                            min_time = float(stats[0])
                            if self.client.verbose:
                                self.client.logger.debug(
                                    f"Parsed min time from stats: {min_time}ms"
                                )
                            return min_time
                        except (IndexError, ValueError) as e:
                            if self.client.verbose:
                                self.client.logger.debug(
                                    f"Failed to parse min/avg/max line '{line}': {e}"
                                )
                            continue
                    # Look for individual ping responses
                    elif "time=" in line:
                        try:
                            time_str = line.split("time=")[1].split()[0].rstrip("ms")
                            ping_time = float(time_str)
                            min_time = min(min_time, ping_time)
                            if self.client.verbose:
                                self.client.logger.debug(
                                    f"Parsed time from response: {ping_time}ms"
                                )
                        except (IndexError, ValueError) as e:
                            if self.client.verbose:
                                self.client.logger.debug(
                                    f"Failed to parse time from line '{line}': {e}"
                                )
                            continue

                if min_time < float("inf"):
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Server {hostname} responded in {min_time}ms"
                        )
                    return min_time

                # If we couldn't parse any times but ping succeeded
                if self.client.verbose:
                    self.client.logger.debug(
                        f"Server {hostname} responded but couldn't parse time from output:\n{result.stdout}"
                    )
                return float("inf")
            else:
                if self.client.verbose:
                    self.client.logger.debug(
                        f"Server {hostname} ping failed with code {result.returncode}:\n"
                        f"stdout: {result.stdout}\n"
                        f"stderr: {result.stderr}"
                    )
                return float("inf")

        except subprocess.TimeoutExpired:
            if self.client.verbose:
                self.client.logger.debug(f"Server {hostname} ping timed out")
            return float("inf")
        except Exception as e:
            if self.client.verbose:
                self.client.logger.debug(f"Server {hostname} ping error: {e}")
                import traceback

                self.client.logger.debug(f"Traceback: {traceback.format_exc()}")
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
        if not isinstance(load, (int, float)) or load < 0 or load > 100:
            return False

        return True

    def select_fastest_server(
        self,
        country_code: Optional[str] = None,
        random_select: bool = False,
        _retry_count: int = 0,
    ) -> Optional[Union[Dict[str, Any], str]]:
        """Select fastest server from list.

        Args:
            country_code: Optional country code to filter by
            random_select: Whether to select a random server instead of fastest
            _retry_count: Internal retry counter to prevent infinite recursion

        Returns:
            Server hostname or dict with server info
        """
        if _retry_count >= 3:
            self.client.logger.error(
                "Maximum retry count reached, clearing failed servers"
            )
            self._failed_servers.clear()
            return None

        try:
            cache = self.get_servers_cache()
            servers = cache.get("servers", [])
            if self.client.verbose:
                self.client.logger.debug(f"Got {len(servers)} servers from cache")
            if not servers:
                return None

            # Filter by country if specified
            if country_code:
                if self.client.verbose:
                    self.client.logger.debug(
                        f"Filtering servers for country: {country_code}"
                    )
                servers = [
                    s
                    for s in servers
                    if s.get("country", {}).get("code", "").upper()
                    == country_code.upper()
                ]
                if self.client.verbose:
                    self.client.logger.debug(
                        f"Found {len(servers)} servers for {country_code}"
                    )
                if not servers:
                    return None

            # Skip servers that have failed
            original_count = len(servers)
            servers = [
                s for s in servers if s.get("hostname") not in self._failed_servers
            ]
            if self.client.verbose:
                skipped = original_count - len(servers)
                if skipped > 0:
                    self.client.logger.debug(
                        f"Skipped {skipped} previously failed servers"
                    )

            if not servers:
                self.client.logger.warning(
                    "All servers have failed, clearing failed servers list"
                )
                self._failed_servers.clear()
                return self.select_fastest_server(
                    country_code, random_select, _retry_count + 1
                )

            # Select random server if requested
            if random_select:
                server = random.choice(servers)
                if self.client.verbose:
                    self.client.logger.debug(
                        f"Randomly selected server: {server.get('hostname')} "
                        f"({server.get('load', '?')}% load)"
                    )
                return server

            # Sort by load and take top servers
            servers.sort(key=lambda x: x.get("load", 100))
            servers = servers[:5]  # Test top 5 servers
            if self.client.verbose:
                self.client.logger.debug(
                    "Top 5 servers by load: "
                    + ", ".join(
                        f"{s.get('hostname')}({s.get('load', '?')}%)" for s in servers
                    )
                )

            # Test response times
            server_times = []
            for server in servers:
                hostname = server.get("hostname")
                if not hostname:
                    if self.client.verbose:
                        self.client.logger.warning(f"Server missing hostname: {server}")
                    continue

                if self.client.verbose:
                    self.client.logger.debug(f"Testing server {hostname}...")

                response_time = self._ping_server(hostname)
                if response_time is not None and response_time < float("inf"):
                    server_times.append((server, response_time))
                    if self.client.verbose:
                        self.client.logger.debug(
                            f"Server {hostname} responded in {response_time}ms"
                        )
                else:
                    if self.client.verbose:
                        self.client.logger.warning(
                            f"Server {hostname} failed ping test"
                        )

            if not server_times:
                if self.client.verbose:
                    self.client.logger.warning(
                        "No servers responded to ping test, falling back to load-based selection"
                    )
                # If no servers respond to ping, just use the one with lowest load
                return servers[0]

            # Select fastest server
            fastest_server = min(server_times, key=lambda x: x[1])[0]
            if self.client.verbose:
                self.client.logger.info(
                    f"Selected fastest server: {fastest_server.get('hostname')} "
                    f"({fastest_server.get('load', '?')}% load, "
                    f"{min(t for _, t in server_times)}ms)"
                )

            return fastest_server

        except Exception as e:
            self.client.logger.error(f"Error selecting fastest server: {e}")
            if self.client.verbose:
                import traceback

                self.client.logger.debug(f"Traceback: {traceback.format_exc()}")
            return None

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
            self.client.logger.error(f"Failed to get random country: {e}")
            return "US"
