"""Base API interface for VPN operations."""

from abc import ABC, abstractmethod
from typing import Any


class BaseAPI(ABC):
    """Abstract base class defining the VPN API interface."""

    @abstractmethod
    async def connect(self, country: str) -> bool:
        """Connect to VPN in specified country.

        Args:
            country: Country name or code to connect to

        Returns:
            bool: True if connection successful

        Raises:
            VPNConnectionError: If connection fails
        """

    @abstractmethod
    async def disconnect(self) -> bool:
        """Disconnect from VPN.

        Returns:
            bool: True if disconnection successful

        Raises:
            VPNConnectionError: If disconnection fails
        """

    @abstractmethod
    async def status(self) -> dict[str, Any]:
        """Get current VPN connection status.

        Returns:
            dict: Status information including:
                - connected (bool): Whether connected
                - country (str): Connected country if any
                - ip (str): Current IP address
                - server (str): Connected server if any
        """

    @abstractmethod
    async def list_countries(self) -> list[str]:
        """Get list of available countries.

        Returns:
            list[str]: List of country names
        """

    @abstractmethod
    async def get_credentials(self) -> tuple[str, str]:
        """Get VPN credentials.

        Returns:
            tuple[str, str]: Username and password
        """
