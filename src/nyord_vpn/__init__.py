"""NordVPN client with API fallback support."""

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.config import VPNConfig, load_config
from nyord_vpn.core.exceptions import (
    VPNError,
    VPNConnectionError,
    VPNConfigError,
    VPNCredentialsError,
)

__version__ = "0.1.0"
__all__ = [
    "VPNClient",
    "VPNConfig",
    "VPNConfigError",
    "VPNConnectionError",
    "VPNCredentialsError",
    "VPNError",
    "load_config",
]
