import json # Keep for TypedDict and any potential direct use
# import os # Removed
# import platform # Removed
# import random # Removed
import re # Still used by _is_valid_hostname
# import secrets # Removed
# import socket # Removed
# import subprocess # Removed
import time # Still used by get_servers_cache
from typing import Any, NotRequired, TypedDict # cast removed

# import requests # Removed as it's no longer used after removing API fallbacks and pinging.
from loguru import logger

from nyord_vpn.api.api import NordVPNAPI
from nyord_vpn.storage.models import ServerError
# API_HEADERS and CACHE_DIR are no longer used in this file.
# from nyord_vpn.utils.utils import API_HEADERS, CACHE_DIR

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
    name: NotRequired[str]
    identifier: NotRequired[str]
    metadata: NotRequired[list[TechnologyMetadata]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]


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
# SERVERS_CACHE_FILE = CACHE_DIR / "servers.json" # Removed
# SERVERS_CACHE_TTL = 3600  # 1 hour in seconds # Removed


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
    return cast("dict[str, Any]", d)


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


class ServerManager:
    """Manages NordVPN server selection and optimization.

    This class handles all server-related operations including:
    1. Server discovery and filtering
    2. Performance measurement and ranking (Simplified for MVP)
    3. Load balancing across available servers (Simplified for MVP)
    4. Relies on NordVPNAPI for server information and its caching.
    5. Country-based server selection

    Tracks failed servers within a session to avoid repeated connection
    attempts to problematic servers.
    """

    def __init__(self, api_client: NordVPNAPI) -> None:
        """Initialize server manager with API client.

        Args:
            api_client: NordVPN API client for server information
        """
        self.api_client = api_client
        self.logger = logger
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
            # No direct cache fallback here for validation, rely on API client's cache for get_servers()
            servers_data, _, _, locations_data, _ = self.api_client.get_servers(refresh_cache=False)

            # Verify country exists
            for loc_obj in locations_data:
                if loc_obj.country and loc_obj.country.code.upper() == normalized:
                    return normalized

            # Get list of available countries for better error message
            available_countries = sorted(
                list(set( # Use set to ensure uniqueness
                    loc_obj.country.code.upper()
                    for loc_obj in locations_data
                    if loc_obj.country and loc_obj.country.code
                ))
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
                technology_identifier="openvpn_tcp" # use_v2 parameter removed from find_best_server
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

    def get_servers_cache(self, refresh: bool = False) -> ServerCache | None:
        """Get server information from the API and transform it to ServerCache format.

        This method now directly fetches from NordVPNAPI.get_servers() and
        transforms the v2 output to the legacy ServerCache format.
        The NordVPNAPI client handles its own instance-level caching.

        Args:
            refresh: Whether to force a refresh of the API client's cache.

        Returns:
            Server information in ServerCache format if available, None otherwise.
        """
        try:
            # Get data from NordVPNAPI (v2 focused)
            # The NordVPNAPI's get_servers method handles its own caching.
            servers_data, _, _, locations_data, _ = (
                self.api_client.get_servers(refresh=refresh) # Pass refresh to API client
            )

            # Transform to ServerCache format
            # This transformation is to maintain compatibility with downstream methods
            # that expect the old ServerCache structure.
            # Ideally, those methods would be refactored to use v2_servers models directly.
            transformed_cache: ServerCache = {
                "servers": [],
                "locations": {},
                "last_updated": time.time(), # Current time, as this is freshly transformed
            }

            # Process locations from v2_servers.Location into ServerLocation format
            for loc_v2 in locations_data:
                if loc_v2.id and loc_v2.country:
                    location_id_str = str(loc_v2.id)
                    transformed_cache["locations"][location_id_str] = {
                        "id": location_id_str,
                        "country": {
                            "name": loc_v2.country.name,
                            "code": loc_v2.country.code,
                        },
                    }

            # Process servers from v2_servers.Server into ServerInfo format
            for server_v2 in servers_data:
                if not server_v2.hostname: # Skip servers without a hostname
                    continue

                # Transform technologies
                server_technologies_transformed: list[Technology] = []
                for tech_v2 in server_v2.technologies:
                    tech_transformed: Technology = {
                        "id": tech_v2.id,
                        "status": tech_v2.status or "", # Ensure status is a string
                    }
                    if tech_v2.metadata:
                        tech_transformed["metadata"] = [
                            {"name": meta.name, "value": meta.value}
                            for meta in tech_v2.metadata
                        ]
                    server_technologies_transformed.append(tech_transformed)

                # Create ServerInfo object
                server_info_transformed: ServerInfo = {
                    "hostname": server_v2.hostname,
                    "location_ids": [
                        str(loc.id) for loc in server_v2.locations if loc.id
                    ],
                    "status": server_v2.status,
                    "load": server_v2.load,
                    "technologies": server_technologies_transformed,
                }
                transformed_cache["servers"].append(server_info_transformed)

            return transformed_cache

        except Exception as e:
            self.logger.warning(f"Failed to get and transform server information: {e}")
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

    # _ping_server, _check_for_ping_command, _fallback_ping, _measure_socket_connection removed for MVP.
    # _test_server removed for MVP.

    def _is_valid_server(self, server: Any) -> bool:
        """Check if a server is valid and usable.

        Args:
            server: Server object (expected to be a dict from ServerInfo or similar) to validate

        Returns:
            bool: True if server is valid, False otherwise

        A valid server must:
        1. Be online
        2. Have a valid hostname (not in failed servers list)
        3. Support OpenVPN TCP technology (as per transformed ServerInfo structure)
        """
        # Basic validation for dictionary-like objects
        if not isinstance(server, dict): # server is now expected to be a dict (ServerInfo)
            return False

        hostname = server.get("hostname", "")

        # Check hostname
        if not hostname or hostname in self._failed_servers:
            if self.verbose and hostname in self._failed_servers:
                self.logger.debug(f"Server {hostname} is in failed servers list.")
            return False

        # Check status
        if server.get("status") != "online":
            if self.verbose:
                self.logger.debug(f"Server {hostname} is not online (status: {server.get('status')}).")
            return False

        # Check for OpenVPN TCP support from the 'technologies' field in ServerInfo
        technologies = server.get("technologies", []) # Expected to be list[Technology] (TypedDict)

        has_openvpn_tcp = False
        for tech_info in technologies:
            # tech_info is expected to be a Technology TypedDict
            # Example: {'id': 3, 'name': 'OpenVPN TCP', 'status': 'enabled', ...}
            # We need to check the 'name' or 'identifier' if available and status.
            # For simplicity, assuming 'OpenVPN TCP' will be in the name if it's the TCP variant.
            # The original check was `if "OpenVPN TCP" in tech_name:`.
            # The v2_servers.Technology model has 'name' and 'identifier'.
            # The transformed ServerInfo has 'technologies' as list[Technology] (TypedDict)
            # where Technology is {'id': int, 'status': str, 'name': NotRequired[str], ...}

            tech_name = tech_info.get("name", "") # Get name from Technology TypedDict
            tech_status = tech_info.get("status", "")

            # A more robust check might involve looking at identifiers if they are consistent
            # For now, matching by name and ensuring status is 'enabled' or similar
            if "OpenVPN TCP" in tech_name and tech_status.lower() == "enabled": # Or check for specific identifier
                if self.verbose:
                    self.logger.debug(f"Server {hostname} supports OpenVPN TCP (Name: {tech_name}, Status: {tech_status}).")
                has_openvpn_tcp = True
                break
            # Fallback or alternative check if 'name' is not always 'OpenVPN TCP'
            # This depends on how 'identifier' is structured in v2_servers.Technology
            # For example, if identifier is 'openvpn_tcp':
            # tech_identifier = tech_info.get("identifier", "")
            # if tech_identifier == "openvpn_tcp" and tech_status.lower() == "enabled":
            #     has_openvpn_tcp = True
            #     break

        if not has_openvpn_tcp and self.verbose:
            self.logger.debug(f"Server {hostname} does not support OpenVPN TCP or it's not enabled.")

        return has_openvpn_tcp

    # _select_diverse_servers is removed as active server testing is removed.

    def select_fastest_server(
        self, country_code: str | None = None, num_servers: int = 3
    ) -> list[dict[str, Any]]:
        """Select suitable servers, prioritizing low load.

        For MVP, this method fetches servers, filters them, and returns a list
        sorted by load. Active pinging is removed.

        Args:
            country_code: Two-letter country code.
            num_servers: The number of servers to return.

        Returns:
            List of server dicts (ServerInfo format) sorted by load (lowest first).
            Returns an empty list if no suitable servers are found.
        """
        try:
            if country_code:
                country_code = self._validate_country_code(country_code) # Validates and normalizes

            # Attempt to get a single best server directly from API client first
            # This uses the v2_servers.Server model.
            try:
                if self.verbose:
                    self.logger.debug(f"Attempting to find best server directly for country: {country_code}")

                # We need to specify the technology we are interested in, e.g., OpenVPN TCP
                # The technology_identifier should match what's used in v2_servers.Technology
                # Assuming 'openvpn_tcp' is a valid identifier.
                # This was previously "openvpn_tcp" in fetch_server_info
                # and self.api_client.find_best_server in the old select_fastest_server
                best_server_v2_model = self.api_client.find_best_server(
                    country_code=country_code,
                    technology_identifier="openvpn_tcp" # Ensure this matches a valid v2 tech identifier
                )

                if best_server_v2_model and best_server_v2_model.hostname:
                    # Transform this v2_servers.Server object to the ServerInfo dict format
                    # This part is a bit manual as there's no direct utility for single server transformation
                    # It mirrors the transformation logic in get_servers_cache
                    transformed_techs = []
                    for tech_v2 in best_server_v2_model.technologies:
                        tech_transformed: Technology = {"id": tech_v2.id, "status": tech_v2.status or ""}
                        if tech_v2.name: tech_transformed["name"] = tech_v2.name
                        if tech_v2.identifier: tech_transformed["identifier"] = tech_v2.identifier
                        if tech_v2.metadata:
                            tech_transformed["metadata"] = [{"name": m.name, "value": m.value} for m in tech_v2.metadata]
                        transformed_techs.append(tech_transformed)

                    server_info_dict: ServerInfo = {
                        "hostname": best_server_v2_model.hostname,
                        "load": best_server_v2_model.load,
                        "status": best_server_v2_model.status,
                        "location_ids": [str(loc.id) for loc in best_server_v2_model.locations if loc.id],
                        "technologies": transformed_techs
                        # 'ping_time' is no longer added as pinging is removed
                    }
                    if self.verbose:
                        self.logger.debug(f"Found best server via API: {server_info_dict['hostname']} (Load: {server_info_dict['load']})")
                    return [server_info_dict] # Return as a list with one server

            except VPNAPIError as e:
                if self.verbose:
                    self.logger.warning(f"Could not find single best server via API client directly: {e}. Falling back to list filtering.")
            # Fallback to fetching all, filtering, and sorting if direct find_best_server fails or for more options

            server_data_cache = self.get_servers_cache(refresh=False)
            if not server_data_cache or not server_data_cache["servers"]:
                if self.verbose:
                    self.logger.info("No servers in initial cache, attempting refresh from API for select_fastest_server.")
                server_data_cache = self.get_servers_cache(refresh=True)
                if not server_data_cache or not server_data_cache["servers"]:
                    raise ServerError("No servers available even after refresh for select_fastest_server.")

            all_servers_info = server_data_cache["servers"]
            locations_info = server_data_cache["locations"] # Needed for country filtering

            candidate_servers: list[ServerInfo] = []

            if country_code:
                for server_info_item in all_servers_info:
                    is_in_country = False
                    for loc_id_str in server_info_item.get("location_ids", []):
                        location = locations_info.get(loc_id_str)
                        if location and location["country"]["code"].upper() == country_code:
                            is_in_country = True
                            break
                    if is_in_country:
                        candidate_servers.append(server_info_item)
                if not candidate_servers and self.verbose:
                     self.logger.warning(f"No servers found for country: {country_code} after filtering transformed cache.")
            else:
                candidate_servers = all_servers_info

            valid_servers = [
                s_info for s_info in candidate_servers if self._is_valid_server(s_info)
            ]

            if not valid_servers:
                err_msg = "No valid OpenVPN TCP servers available"
                if country_code:
                    err_msg += f" in {country_code}"
                self._failed_servers.clear() # Clear failed servers if we are desperate
                raise ServerError(err_msg + ".")

            # Sort valid servers by load (ascending)
            sorted_servers = sorted(valid_servers, key=lambda s: s.get("load", 100))

            if self.verbose:
                self.logger.debug(f"Returning up to {num_servers} servers sorted by load. Found {len(sorted_servers)} total valid servers.")
                for i, s in enumerate(sorted_servers[:num_servers]):
                    self.logger.debug(f"  {i+1}. {s['hostname']} (Load: {s['load']})")

            return sorted_servers[:num_servers]

        except ServerError:
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error in select_fastest_server: {e}", exc_info=True)
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
