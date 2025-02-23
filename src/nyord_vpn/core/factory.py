"""Factory for creating VPN clients."""

from typing import Literal

from loguru import logger

from nyord_vpn.core.base import BaseVPNClient
from nyord_vpn.core.exceptions import VPNConfigError
from nyord_vpn.api.legacy import LegacyVPNClient

try:
    from nyord_vpn.api.njord import NjordVPNClient

    HAS_NJORD = True
except ImportError:
    HAS_NJORD = False


def create_client(api: Literal["legacy", "njord"] = "legacy") -> BaseVPNClient:
    """Create a VPN client.

    Args:
        api: API implementation to use (legacy or njord)

    Returns:
        BaseVPNClient: VPN client instance

    Raises:
        VPNConfigError: If requested API is not available
    """
    if api == "legacy":
        logger.debug("Using legacy VPN API")
        return LegacyVPNClient()
    elif api == "njord":
        if not HAS_NJORD:
            msg = "Njord API not available. Install njord package first."
            raise VPNConfigError(
                msg
            )
        logger.debug("Using njord VPN API")
        return NjordVPNClient()
    else:
        msg = f"Unknown API: {api}"
        raise VPNConfigError(msg)
