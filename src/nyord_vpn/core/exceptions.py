"""Custom exceptions for VPN operations."""


class VPNError(Exception):
    """Base exception for VPN-related errors."""


class VPNConnectionError(VPNError):
    """Raised when VPN connection fails."""


class VPNStatusError(VPNError):
    """Raised when getting VPN status fails."""


class VPNConfigError(VPNError):
    """Raised when configuration is invalid."""


class VPNCredentialsError(VPNError):
    """Raised when credentials are invalid or missing."""
