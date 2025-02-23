"""Data models and exceptions for the NordVPN client.

This module contains:
- Type definitions for API responses (City, Country)
- Cache data structures
- Custom exceptions for error handling
"""

from typing import List, TypedDict


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


# Base exceptions
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

    def __init__(self, message: str | None = None):
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
