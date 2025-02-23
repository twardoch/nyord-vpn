"""Base VPN client interface."""

import os
from abc import ABC, abstractmethod
from typing import Any, TypedDict

from loguru import logger

from nyord_vpn.core.exceptions import VPNCredentialsError


class VPNStatus(TypedDict):
    """VPN connection status."""

    connected: bool
    ip: str
    country: str
    server: str


class BaseVPNClient(ABC):
    """Base class for VPN clients."""

    def __init__(self) -> None:
        """Initialize VPN client."""
        self.username = os.getenv("NORD_USER", "")
        self.password = os.getenv("NORD_PASSWORD", "")
        if not self.username or not self.password:
            msg = "Missing credentials. Set NORD_USER and NORD_PASSWORD environment variables."
            raise VPNCredentialsError(
                msg
            )
        logger.debug("Initialized VPN client")

    @abstractmethod
    def connect(self, country: str | None = None) -> bool:
        """Connect to VPN.

        Args:
            country: Optional country to connect to (name or code)

        Returns:
            bool: True if connection successful

        Raises:
            VPNError: If connection fails
        """

    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from VPN.

        Returns:
            bool: True if disconnection successful

        Raises:
            VPNError: If disconnection fails
        """

    @abstractmethod
    def protected(self) -> bool:
        """Check if VPN is active.

        Returns:
            bool: True if VPN is active
        """

    @abstractmethod
    def status(self) -> VPNStatus:
        """Get VPN status.

        Returns:
            VPNStatus: Current VPN status

        Raises:
            VPNError: If status check fails
        """

    @abstractmethod
    def list_countries(self) -> list[dict[str, Any]]:
        """Get list of available countries.

        Returns:
            list: List of countries with name and code

        Raises:
            VPNError: If country list cannot be retrieved
        """
