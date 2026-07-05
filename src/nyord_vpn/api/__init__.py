"""API modules for nyord-vpn.

this_file: src/nyord_vpn/api/__init__.py

This package contains modules for interacting with the NordVPN API,
including both v1 and v2 API endpoints. The API modules handle server
discovery, recommendations, and configuration retrieval.
"""

from .api import NordVPNAPI

__all__ = ["NordVPNAPI"]
