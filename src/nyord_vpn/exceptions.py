"""Custom exceptions for the NordVPN client.

this_file: src/nyord_vpn/exceptions.py

This module defines custom exceptions used throughout the NordVPN client.
Each exception type corresponds to a specific category of errors that may
occur during VPN operations.

The exception hierarchy is:
- NyordVPNError (base)
  - VPNError (VPN-specific base)
    - VPNConfigError
    - VPNAuthenticationError
    - VPNProcessError
    - VPNConnectionError
    - VPNDisconnectionError
  - CredentialsError
  - ConnectionError
  - DisconnectionError
  - ServerNotFoundError
  - VPNServerError
  - VPNTimeoutError
"""


class NyordVPNError(Exception):
    """Base exception for all NordVPN client errors.

    This is the root exception class for all errors that may occur in the NordVPN client.
    It provides a consistent interface for error handling and logging.

    Args:
        message: A descriptive error message
        details: Additional error details or context
        cause: The underlying exception that caused this error

    """

    def __init__(
        self,
        message: str = "An error occurred in the NordVPN client",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        self.message = message
        self.details = details
        self.cause = cause
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        """Format the complete error message including details and cause."""
        msg = self.message
        if self.details:
            msg += f"\nDetails: {self.details}"
        if self.cause:
            msg += f"\nCause: {self.cause!s}"
        return msg


class VPNError(NyordVPNError):
    """Base exception for VPN-related errors.

    This exception serves as a base for all VPN-specific errors that may occur
    during VPN operations like configuration, authentication, and process management.
    """

    def __init__(
        self,
        message: str = "A VPN-related error occurred",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class CredentialsError(NyordVPNError):
    """Raised when there are issues with VPN credentials.

    This exception is raised when there are problems with user credentials,
    such as missing, invalid, or expired credentials.
    """

    def __init__(
        self,
        message: str = "Invalid or missing VPN credentials",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class ConnectionError(NyordVPNError):
    """Raised when connection to VPN server fails.

    This exception indicates a failure to establish a connection to the VPN server,
    which could be due to network issues, server problems, or client configuration.
    """

    def __init__(
        self,
        message: str = "Failed to connect to VPN server",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class DisconnectionError(NyordVPNError):
    """Raised when disconnection from VPN fails.

    This exception is raised when there are problems disconnecting from the VPN,
    such as stuck processes or network issues.
    """

    def __init__(
        self,
        message: str = "Failed to disconnect from VPN",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class ServerNotFoundError(NyordVPNError):
    """Raised when a VPN server cannot be found.

    This exception indicates that the requested VPN server is not available
    or cannot be found in the server list.
    """

    def __init__(
        self,
        message: str = "VPN server not found",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNConfigError(VPNError):
    """Raised when there are issues with OpenVPN configuration.

    This exception is raised when there are problems with the OpenVPN configuration,
    such as invalid settings, missing files, or permission issues.
    """

    def __init__(
        self,
        message: str = "Invalid or missing OpenVPN configuration",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNServerError(NyordVPNError):
    """Raised when there are issues with VPN server selection or availability.

    This exception indicates problems with VPN server selection or availability,
    such as server overload, maintenance, or network issues.
    """

    def __init__(
        self,
        message: str = "VPN server error or unavailable",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNAuthenticationError(VPNError):
    """Raised when authentication fails.

    This exception is raised when authentication with the VPN server fails,
    which could be due to invalid credentials or server-side issues.
    """

    def __init__(
        self,
        message: str = "VPN authentication failed",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNTimeoutError(NyordVPNError):
    """Raised when VPN operations timeout.

    This exception indicates that a VPN operation took too long to complete,
    such as connection establishment or server response.
    """

    def __init__(
        self,
        message: str = "VPN operation timed out",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNProcessError(VPNError):
    """Raised when there are issues with the OpenVPN process.

    This exception is raised when there are problems managing the OpenVPN process,
    such as startup failures, crashes, or unexpected termination.
    """

    def __init__(
        self,
        message: str = "OpenVPN process error",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNConnectionError(VPNError):
    """Raised when connection establishment fails.

    This exception indicates a failure in establishing the VPN connection,
    which could be due to network issues, configuration problems, or server errors.
    """

    def __init__(
        self,
        message: str = "Failed to establish VPN connection",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)


class VPNDisconnectionError(VPNError):
    """Raised when disconnection fails.

    This exception is raised when there are problems disconnecting from the VPN,
    such as process cleanup issues or network problems.
    """

    def __init__(
        self,
        message: str = "Failed to disconnect from VPN",
        details: str | None = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message, details, cause)
