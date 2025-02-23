"""Data models and exceptions for the NordVPN client.

this_file: src/nyord_vpn/storage/models.py

This module defines the core data structures and error handling for the client.
It provides type-safe models for API data and a comprehensive exception hierarchy.

Data Models:
1. TypedDict classes for API responses:
   - City: Server location information
   - Country: Country-level server data
   - CountryCache: Cache storage format

Integration Points:
- Used by Client (core/client.py) for data handling
- Used by NordVPNAPIClient (core/api.py) for responses
- Used by ServerManager (network/server.py) for data
- Used throughout codebase for error handling

Exception Hierarchy:
1. VPNError - Base exception for all client errors
2. Specific exceptions for different scenarios:
   - ServerError: Server selection issues
   - ConnectionError: Connection failures
   - AuthenticationError: Credential problems
   - StateError: State management issues
   - CacheError: Cache operation failures

Error Handling Design:
- Each exception provides detailed error messages
- Includes recovery suggestions in messages
- Maintains consistent error handling patterns
- Supports both CLI and library usage

The models ensure type safety and data validation throughout
the codebase, while the exception hierarchy provides clear
error handling patterns and user-friendly error messages.
"""

from typing import List, TypedDict


class City(TypedDict):
    """City information from NordVPN API.

    Represents a city where NordVPN servers are located, including:
    - Geographic information (coordinates)
    - Server infrastructure details
    - Connection quality metrics

    Attributes:
        dns_name: DNS hostname component for server addresses
        hub_score: Infrastructure quality score (0-100)
        id: Unique city identifier
        latitude: Geographic latitude
        longitude: Geographic longitude
        name: Human-readable city name
        serverCount: Number of available servers
    """

    dns_name: str
    hub_score: int
    id: int
    latitude: float
    longitude: float
    name: str
    serverCount: int


class Country(TypedDict):
    """Country information from NordVPN API.

    Represents a country with NordVPN server presence, containing:
    - Basic country information
    - List of cities with servers
    - Server availability metrics

    Attributes:
        cities: List of City objects with server information
        code: Two-letter ISO country code
        id: Unique country identifier
        name: Full country name
        serverCount: Total servers in the country

    Note:
        The serverCount is the sum of all servers across cities,
        providing a quick way to assess server availability.
    """

    cities: List[City]
    code: str
    id: int
    name: str
    serverCount: int


class CountryCache(TypedDict):
    """Cache structure for country and server information.

    Provides a persistent storage format for server data:
    - Complete country and city information
    - Cache metadata for freshness checking

    Attributes:
        countries: List of Country objects with full server info
        last_updated: ISO 8601 timestamp of last update

    Note:
        This structure is used for both file storage and memory
        caching, ensuring consistent data representation.
    """

    countries: List[Country]
    last_updated: str


class VPNError(Exception):
    """Base exception for all VPN-related errors.

    Provides common functionality for VPN error handling:
    1. Default error messages
    2. Optional custom messages
    3. Base for specific error types

    All VPN-related exceptions should inherit from this class
    to ensure consistent error handling throughout the client.
    """

    def __init__(self, message: str | None = None):
        """Initialize base VPN error.

        Args:
            message: Optional custom error message
                    Falls back to generic message if None
        """
        super().__init__(message or "An unknown VPN error occurred")


class ServerError(VPNError):
    """Exception for server selection and availability issues.

    Raised when:
    1. No servers available in selected country
    2. Server selection algorithm fails
    3. Selected server becomes unavailable
    4. Load balancing cannot find suitable server

    The error message includes suggestions for resolution,
    such as trying a different country or server.
    """

    def __init__(self, message: str | None = None):
        """Initialize server error with helpful message.

        Args:
            message: Optional specific error details
                    Falls back to guidance message if None
        """
        super().__init__(
            message
            or "Failed to select a server. Please try again or choose a different country."
        )


class ConnectionError(VPNError):
    """Exception for VPN connection establishment failures.

    Raised when:
    1. OpenVPN process fails to start
    2. Connection times out
    3. Network is unreachable
    4. System configuration prevents connection

    Includes diagnostic information and recovery steps
    in the error message.
    """

    def __init__(self, message: str | None = None):
        """Initialize connection error with diagnostics.

        Args:
            message: Optional connection failure details
                    Falls back to troubleshooting steps if None
        """
        super().__init__(
            message
            or "Failed to establish VPN connection. Please check your internet connection and try again."
        )


class AuthenticationError(VPNError):
    """Exception for NordVPN authentication failures.

    Raised when:
    1. Invalid credentials provided
    2. Account is inactive or expired
    3. API authentication fails
    4. Token refresh fails

    Provides clear guidance on credential verification
    and account status checking.
    """

    def __init__(self, message: str | None = None):
        """Initialize authentication error with guidance.

        Args:
            message: Optional auth failure details
                    Falls back to credential check message if None
        """
        super().__init__(
            message or "Authentication failed. Please check your NordVPN credentials."
        )


class CredentialsError(VPNError):
    """Exception for missing or invalid credentials.

    Raised when:
    1. Required environment variables are missing
    2. Credentials file is not found
    3. Credentials format is invalid
    4. Credentials are not properly set

    Provides detailed instructions for credential setup
    including environment variables and file locations.
    """

    def __init__(self, message: str | None = None):
        """Initialize credentials error with setup instructions.

        Args:
            message: Optional specific error details
                    Falls back to setup instructions if None
        """
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


class StateError(VPNError):
    """Exception for VPN state management failures.

    Raised when:
    1. State file operations fail
    2. State becomes inconsistent
    3. State transition fails
    4. State validation fails

    Includes recovery steps to restore consistent state
    through disconnection and reconnection.
    """

    def __init__(self, message: str | None = None):
        """Initialize state error with recovery steps.

        Args:
            message: Optional state error details
                    Falls back to recovery instructions if None
        """
        super().__init__(
            message
            or "Failed to manage VPN state. Please try disconnecting and reconnecting."
        )


class CacheError(VPNError):
    """Exception for cache operation failures.

    Raised when:
    1. Cache file operations fail
    2. Cache data is corrupted
    3. Cache update fails
    4. Cache validation fails

    Provides instructions for cache refresh and
    manual cache management when needed.
    """

    def __init__(self, message: str | None = None):
        """Initialize cache error with refresh instructions.

        Args:
            message: Optional cache error details
                    Falls back to refresh instructions if None
        """
        super().__init__(
            message
            or "Failed to manage cache. Try running 'nyord-vpn update' to refresh the cache."
        )
