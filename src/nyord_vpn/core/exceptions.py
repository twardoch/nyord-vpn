"""Exceptions for VPN operations."""

from typing import Any


class VPNError(Exception):
    """Base exception for VPN operations."""

    def __init__(self, message: str, details: Any = None) -> None:
        super().__init__(message)
        self.details = details


class VPNConnectionError(VPNError):
    """Error during VPN connection."""


class VPNCredentialsError(VPNError):
    """Invalid or missing VPN credentials."""


class VPNConfigError(VPNError):
    """Error with VPN configuration."""


class VPNServerError(VPNError):
    """Error getting VPN server information."""
