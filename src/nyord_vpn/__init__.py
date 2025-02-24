"""Modern Python client for NordVPN with automatic API fallback.

this_file: src/nyord_vpn/__init__.py

This package provides a comprehensive VPN client for NordVPN,
offering both a command-line interface and a Python library.

Package Structure:
1. Core Components (core/):
   - client.py: Main client implementation
   - api.py: NordVPN API client
   - base.py: Base classes and interfaces

2. Network Components (network/):
   - vpn.py: OpenVPN connection management
   - server.py: Server selection and management
   - country.py: Country information handling

3. Storage Components (storage/):
   - models.py: Data models and exceptions
   - state.py: State management

4. Utilities (utils/):
   - connection.py: Connection verification
   - templates.py: OpenVPN templates
   - utils.py: Common utilities

Command-Line Interface:
    nyord-vpn go <country>     Connect to VPN in specified country
    nyord-vpn bye             Disconnect from VPN
    nyord-vpn info            Show connection status
    nyord-vpn where           List available countries
    nyord-vpn update          Update country/server cache

Python Library Usage:
    from nyord_vpn import Client

    client = Client(username="user", password="pass")
    client.go("us")  # Connect to US server
    client.status()  # Check connection
    client.disconnect()  # Disconnect

Features:
1. Modern Security
   - AES-256-GCM encryption
   - ChaCha20-Poly1305 support
   - Strong certificate validation
   - DNS leak prevention

2. Smart Server Selection
   - Load-based balancing
   - Geographic optimization
   - Connection quality metrics
   - Automatic failover

3. Robust Error Handling
   - Comprehensive exception hierarchy
   - Detailed error messages
   - Recovery suggestions
   - Automatic retries

4. Performance Optimization
   - Connection caching
   - State persistence
   - Smart reconnection
   - API result caching

Requirements:
- OpenVPN (install via package manager)
- Python 3.9+
- Root/sudo access for VPN connections

Environment Variables:
    NORD_USER: NordVPN username
    NORD_PASSWORD: NordVPN password
"""

from nyord_vpn.core.client import Client
from nyord_vpn.storage.models import (
    ConnectionError,
    CredentialsError,
    ServerError,
    VPNError,
)

__version__ = "0.1.0"
__all__ = [
    "Client",
    "ConnectionError",
    "CredentialsError",
    "ServerError",
    "VPNError",
]
