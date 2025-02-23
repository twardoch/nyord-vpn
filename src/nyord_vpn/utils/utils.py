"""Utility functions and constants for the NordVPN client.

This module provides core utilities and configuration:

Directory Structure:
1. Cache Directory (~/.cache/nyord-vpn/)
   - Server information cache
   - Connection state
   - OpenVPN configuration
   - Authentication data

2. Config Directory (~/.config/nyord-vpn/)
   - User configuration
   - Custom settings
   - Persistent data

3. Package Data
   - Country mappings
   - Default configurations
   - Templates

Constants and Settings:
1. File Paths
   - Cache locations
   - Config locations
   - State management
   - Log files

2. API Configuration
   - Request headers
   - Cache settings
   - Country mappings

3. OpenVPN Settings
   - Configuration paths
   - Authentication paths
   - Log paths

The module ensures proper directory structure exists
and provides fallback data when needed.
"""

import json
import os
import time
from pathlib import Path

from loguru import logger
from platformdirs import user_cache_dir, user_config_dir

# Application directories with platform-specific paths
APP_NAME = "nyord-vpn"
APP_AUTHOR = "twardoch"
CACHE_DIR = Path(user_cache_dir(APP_NAME, APP_AUTHOR))
CONFIG_DIR = Path(user_config_dir(APP_NAME, APP_AUTHOR))

# Ensure core directories exist
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

# File paths for various components
PACKAGE_DIR = Path(__file__).parent
DATA_DIR = PACKAGE_DIR / "data"
CACHE_FILE = DATA_DIR / "countries.json"
COUNTRIES_CACHE = CACHE_DIR / "countries.json"
COUNTRY_IDS_FILE = DATA_DIR / "country_ids.json"
STATE_FILE = CACHE_DIR / "vpn_state.json"
OPENVPN_CONFIG = CACHE_DIR / "openvpn.ovpn"
OPENVPN_AUTH = CACHE_DIR / "openvpn.auth"
OPENVPN_LOG = CACHE_DIR / "openvpn.log"

# Cache settings
CACHE_EXPIRY = 24 * 60 * 60  # 24 hours in seconds


def is_process_running(process_id):
    """Check if a process is running using its PID.

    Uses sudo to check process existence since OpenVPN
    processes run with elevated privileges. This is more
    reliable than direct process checking for root processes.

    Args:
        process_id: Process ID to check

    Returns:
        bool: True if process exists, False otherwise

    Note:
        This function requires sudo access and is specifically
        designed for checking OpenVPN processes.
    """
    try:
        os.system("sudo kill -0 " + str(process_id))
        return True
    except Exception:
        return False


def ensure_data_dir() -> None:
    """Create data directory if it doesn't exist.

    This function ensures the package data directory exists:
    1. Creates directory with parents if needed
    2. Sets appropriate permissions
    3. Handles concurrent creation safely

    The data directory stores:
    - Country information
    - Default configurations
    - Static resources
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)


# Initialize data directory
ensure_data_dir()


# Load country ID mappings with fallback data
try:
    with open(COUNTRY_IDS_FILE) as f:
        NORDVPN_COUNTRY_IDS: dict[str, str] = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # Fallback to core countries if file is missing/invalid
    NORDVPN_COUNTRY_IDS = {
        "US": "228",  # United States
        "GB": "227",  # United Kingdom
        "DE": "81",  # Germany
    }

# API request headers to mimic browser behavior
API_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://nordvpn.com/",
    "Origin": "https://nordvpn.com",
}


def save_vpn_state(state: dict) -> None:
    """Save VPN connection state to persistent storage.

    Maintains a record of the VPN connection state including:
    1. Connection status and timing
    2. IP address information (original and VPN)
    3. Server details and location
    4. State metadata

    Args:
        state: Dictionary containing state information:
            - connected (bool): Current connection status
            - initial_ip (str): Original IP before VPN
            - connected_ip (str): VPN-assigned IP
            - server (str): Connected server hostname
            - country (str): Server country
            - timestamp (float): State update time

    Note:
        The state file is used for connection recovery
        and status monitoring. Failed saves are logged
        but don't raise exceptions to prevent disrupting
        VPN operations.
    """
    try:
        STATE_FILE.write_text(json.dumps(state, indent=2))
    except Exception as e:
        logger.warning(f"Failed to save VPN state: {e}")


def load_vpn_state() -> dict:
    """Load VPN connection state from storage.

    Retrieves and validates the stored VPN state:
    1. Checks state file existence
    2. Validates state freshness (5 minute TTL)
    3. Provides default state if needed

    Returns:
        dict: State information containing:
            - connected (bool): Connection status
            - initial_ip (str|None): Original IP
            - connected_ip (str|None): VPN IP
            - server (str|None): Server hostname
            - country (str|None): Server country
            - timestamp (float): Update time

    Note:
        The state is considered stale after 5 minutes
        to prevent using outdated connection information.
        Failed loads return a safe default state.
    """
    try:
        if STATE_FILE.exists():
            state = json.loads(STATE_FILE.read_text())
            # State is valid for 5 minutes
            if time.time() - state.get("timestamp", 0) < 300:
                return state
    except Exception as e:
        logger.warning(f"Failed to load VPN state: {e}")

    return {
        "connected": False,
        "initial_ip": None,  # Original IP before VPN connection
        "connected_ip": None,  # IP address when connected to VPN
        "server": None,
        "country": None,
        "timestamp": time.time(),
    }
