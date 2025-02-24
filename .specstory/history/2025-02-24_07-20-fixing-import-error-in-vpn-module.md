## SpecStory

## Fixing Import Error in VPN Module (24/02/2025, 07:20:31)

_**User**_

Password:
Traceback (most recent call last):
  File "/usr/local/bin/nyord-vpn", line 5, in <module>
    from nyord_vpn.__main__ import main
  File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/__init__.py", line 78, in <module>
    from nyord_vpn.core.client import Client
  File "/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/core/client.py", line 58, in <module>
    from nyord_vpn.network.server import ServerManager, get_servers, select_server
ImportError: cannot import name 'get_servers' from 'nyord_vpn.network.server' (/Users/adam/Developer/vcs/github.twardoch/pub/nyord_vpn/src/nyord_vpn/network/server.py)

---

_**Assistant**_

Based on the error message and linter errors, there seems to be an issue with importing functions from the server module. Let's fix the imports and create the missing functions.

First, let's create/update the server module:

```python:src/nyord_vpn/network/server.py
"""Server management module for NordVPN connections.

this_file: src/nyord_vpn/network/server.py

This module handles server selection and management for NordVPN connections.
It provides functionality to:
1. Get available servers from NordVPN API
2. Filter and select optimal servers
3. Cache server information
"""

import json
import time
from pathlib import Path
from typing import Any, List, Dict, Optional
import requests
from loguru import logger

from nyord_vpn.exceptions import VPNError
from nyord_vpn.utils.utils import API_HEADERS

# Constants
CACHE_TTL = 3600  # 1 hour cache TTL
CACHE_FILE = Path.home() / ".cache" / "nyord-vpn" / "servers.json"

class ServerManager:
    """Manages NordVPN server information and selection."""
    
    def __init__(self, verbose: bool = False):
        """Initialize server manager.
        
        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose
        self.logger = logger
        
        # Ensure cache directory exists
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

    def get_servers(self, country: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get list of available NordVPN servers.
        
        Args:
            country: Optional country code to filter servers
            
        Returns:
            List of server dictionaries with hostname, load, features etc.
            
        Raises:
            VPNError: If unable to get server list
        """
        try:
            servers = self._get_cached_servers()
            if not servers:
                servers = self._fetch_servers()
                self._cache_servers(servers)
                
            if country:
                servers = [s for s in servers if s.get("country_code", "").lower() == country.lower()]
                
            return servers
            
        except Exception as e:
            raise VPNError(f"Failed to get server list: {e}")

    def select_server(self, servers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Select optimal server from list based on load and features.
        
        Args:
            servers: List of server dictionaries to select from
            
        Returns:
            Selected server dictionary
            
        Raises:
            VPNError: If no suitable server found
        """
        if not servers:
            raise VPNError("No servers available to select from")
            
        # Sort by load ascending
        servers = sorted(servers, key=lambda s: s.get("load", 100))
        
        # Take first server with acceptable load
        for server in servers:
            if server.get("load", 100) < 70:  # Load under 70%
                return server
                
        # If no server with good load, take first available
        return servers[0]

    def _get_cached_servers(self) -> List[Dict[str, Any]]:
        """Get servers from cache if valid."""
        try:
            if not CACHE_FILE.exists():
                return []
                
            data = json.loads(CACHE_FILE.read_text())
            cache_time = data.get("timestamp", 0)
            
            if time.time() - cache_time > CACHE_TTL:
                return []  # Cache expired
                
            return data.get("servers", [])
            
        except Exception as e:
            if self.verbose:
                self.logger.warning(f"Failed to read server cache: {e}")
            return []

    def _cache_servers(self, servers: List[Dict[str, Any]]) -> None:
        """Cache server list to file."""
        try:
            cache_data = {
                "timestamp": time.time(),
                "servers": servers
            }
            CACHE_FILE.write_text(json.dumps(cache_data))
            
            if self.verbose:
                self.logger.debug(f"Cached {len(servers)} servers")
                
        except Exception as e:
            if self.verbose:
                self.logger.warning(f"Failed to cache servers: {e}")

    def _fetch_servers(self) -> List[Dict[str, Any]]:
        """Fetch server list from NordVPN API."""
        try:
            response = requests.get(
                "https://api.nordvpn.com/v1/servers",
                headers=API_HEADERS,
                timeout=10
            )
            response.raise_for_status()
            
            servers = response.json()
            if self.verbose:
                self.logger.debug(f"Fetched {len(servers)} servers from API")
                
            return servers
            
        except Exception as e:
            raise VPNError(f"Failed to fetch servers from API: {e}")

# Module level functions that use ServerManager internally
_manager = ServerManager()

def get_servers(country: Optional[str] = None) -> List[Dict[str, Any]]:
    """Get list of available NordVPN servers.
    
    Args:
        country: Optional country code to filter servers
        
    Returns:
        List of server dictionaries
    """
    return _manager.get_servers(country)

def select_server(servers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Select optimal server from list.
    
    Args:
        servers: List of server dictionaries
        
    Returns:
        Selected server dictionary

---



---

