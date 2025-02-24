"""Custom exceptions for the NordVPN client.

this_file: src/nyord_vpn/exceptions.py

This module defines custom exceptions used throughout the NordVPN client.
Each exception type corresponds to a specific category of errors that may
occur during VPN operations.
"""


class NyordVPNError(Exception):
    """Base exception for all NordVPN client errors."""


class VPNError(NyordVPNError):
    """Raised when VPN connection operations fail."""


class CredentialsError(NyordVPNError):
    """Raised when there are issues with VPN credentials."""


class ConnectionError(NyordVPNError):
    """Raised when connection to VPN server fails."""


class DisconnectionError(NyordVPNError):
    """Raised when disconnection from VPN fails."""


class ServerNotFoundError(NyordVPNError):
    """Raised when a VPN server cannot be found."""


class VPNConfigError(NyordVPNError):
    """Raised when there are issues with VPN configuration."""


class VPNServerError(NyordVPNError):
    """Raised when there are issues with VPN server selection or availability."""


class VPNAuthenticationError(NyordVPNError):
    """Raised when authentication with VPN server fails."""


class VPNTimeoutError(NyordVPNError):
    """Raised when VPN operations timeout."""


class VPNProcessError(NyordVPNError):
    """Raised when there are issues with the OpenVPN process."""
