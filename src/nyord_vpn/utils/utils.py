"""Utility functions and constants for the NordVPN client.

this_file: src/nyord_vpn/utils/utils.py

This module provides core utilities and configuration management.
It handles file paths, state persistence, and common functionality.

Directory Structure:
1. Cache Directory (~/.cache/nyord-vpn/):
   - Server information cache
   - Connection state
   - OpenVPN configuration
   - Authentication data

2. Config Directory (~/.cache/nyord-vpn/):
   - User configuration
   - Custom settings
   - Persistent data

3. Package Data:
   - Country mappings
   - Default configurations
   - Templates

Integration Points:
- Used throughout codebase for paths
- Used by Client (core/client.py) for state
- Used by VPNConnectionManager for config
- Used by API client for caching

Constants and Settings:
1. File Paths:
   - Cache locations
   - Config locations
   - State management
   - Log files

2. API Configuration:
   - Request headers
   - Cache settings
   - Country mappings

3. OpenVPN Settings:
   - Configuration paths
   - Authentication paths
   - Log paths

State Management:
- Implements atomic file operations
- Handles concurrent access
- Provides fallback data
- Manages cache lifecycle

The module ensures proper directory structure exists
and provides fallback data when needed, serving as
the foundation for the client's file operations and
state management.
"""

import contextlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from loguru import logger
from platformdirs import user_cache_dir, user_config_dir
from rich.console import Console

console = Console()

# Application directories
APP_NAME = "nyord-vpn"
APP_AUTHOR = "twardoch"
CACHE_DIR = Path(user_cache_dir(APP_NAME, APP_AUTHOR))
CONFIG_DIR = Path(user_config_dir(APP_NAME, APP_AUTHOR))

# Ensure directories exist with proper permissions
CACHE_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
CONFIG_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)

# File paths
PACKAGE_DIR = Path(__file__).parent
DATA_DIR = PACKAGE_DIR / "data"
CACHE_FILE = DATA_DIR / "countries.json"
COUNTRIES_CACHE = CACHE_DIR / "countries.json"
COUNTRY_IDS_FILE = DATA_DIR / "country_ids.json"
STATE_FILE = CACHE_DIR / "state.json"
OPENVPN_CONFIG = CACHE_DIR / "openvpn.ovpn"
OPENVPN_AUTH = CACHE_DIR / "openvpn.auth"
OPENVPN_LOG = CACHE_DIR / "openvpn.log"

# Cache expiry in seconds (24 hours)
CACHE_EXPIRY = 24 * 60 * 60  # 24 hours in seconds


def check_root() -> bool:
    """Check if running with root privileges.

    Returns:
        bool: True if already running as root, False if needs elevation

    """
    return os.geteuid() == 0


def ensure_root() -> None:
    """Request root privileges using sudo.

    This function checks if the current process has root privileges.
    If not, it attempts to re-run the script with sudo.

    The function will:
    1. Check current user's effective UID
    2. If not root, re-run with sudo
    3. Display appropriate messages
    4. Exit with status code on failure

    Note:
        This is required for OpenVPN operations which need
        root access to configure network interfaces.

    """
    if not check_root():
        try:
            # Get the original command without sudo
            cmd = sys.argv[:]
            if cmd[0].startswith("sudo"):
                cmd = cmd[1:]

            # Re-run the script with sudo, preserving environment variables
            env = os.environ.copy()

            # If in virtualenv, use nyord-vpn from virtualenv bin
            if os.environ.get("VIRTUAL_ENV"):
                nyord_vpn_path = os.path.join(
                    os.environ["VIRTUAL_ENV"], "bin", "nyord-vpn"
                )
                if os.path.exists(nyord_vpn_path):
                    args = ["sudo", "-E", nyord_vpn_path, *cmd[1:]]
                else:
                    # Fallback to system nyord-vpn
                    args = ["sudo", "-E", "nyord-vpn", *cmd[1:]]
            else:
                # Not in virtualenv, use system nyord-vpn
                args = ["sudo", "-E", "nyord-vpn", *cmd[1:]]

            console.print(
                "[yellow]This command requires admin privileges.[/yellow]",
            )
            console.print(
                "[cyan]Enter your computer admin (sudo) password when asked.[/cyan]"
            )

            if logger.level("DEBUG").no <= logger.level("INFO").no:
                logger.debug(f"Running command: {' '.join(args)}")

            subprocess.run(args, env=env, check=True)
            sys.exit(0)
        except subprocess.CalledProcessError as e:
            console.print("[red]Error: Admin privileges required.[/red]")
            console.print("[yellow]Run the command again with sudo:[/yellow]")
            console.print(f"[blue]sudo -E {' '.join(sys.argv)}[/blue]")
            if logger.level("DEBUG").no <= logger.level("INFO").no:
                logger.debug(f"Command failed with error: {e}")
            sys.exit(1)


def is_process_running(process_id: int) -> bool | None:
    """Check if a process is running by its PID.

    Args:
        process_id: Process ID to check

    Returns:
        bool: True if running, False if not, None if check fails

    """
    try:
        os.kill(process_id, 0)
        return True
    except OSError:
        return False
    except Exception:
        return None


def ensure_data_dir() -> None:
    """Ensure data directory exists and is writable."""
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

    Args:
        state: Dictionary containing state information:
            - connected (bool): Current connection status
            - normal_ip (str): IP address when not connected to VPN
            - connected_ip (str): VPN-assigned IP
            - server (str): Connected server hostname
            - country (str): Server country
            - timestamp (float): State update time
            - current_ip (str, optional): Current IP after disconnection

    """
    try:
        # Load existing state to preserve important info
        existing = {}
        if STATE_FILE.exists():
            with contextlib.suppress(json.JSONDecodeError):
                existing = json.loads(STATE_FILE.read_text())

        # If we're disconnected and have a current_ip, that's our normal_ip
        if not state.get("connected") and state.get("current_ip"):
            state["normal_ip"] = state["current_ip"]
            state["connected_ip"] = None
        # If we're connected and have a current_ip, that's our VPN IP
        elif state.get("connected") and state.get("current_ip"):
            state["connected_ip"] = state["current_ip"]
            # Keep existing normal_ip
            if not state.get("normal_ip") and existing.get("normal_ip"):
                state["normal_ip"] = existing.get("normal_ip")

        # Ensure timestamp is updated
        state["timestamp"] = time.time()

        # Write state atomically using temp file
        temp_state = STATE_FILE.with_suffix(".tmp")
        temp_state.write_text(json.dumps(state, indent=2))
        temp_state.chmod(0o600)
        temp_state.replace(STATE_FILE)

        if logger.level("DEBUG").no <= logger.level("INFO").no:
            logger.debug(f"Saved state to {STATE_FILE}: {json.dumps(state, indent=2)}")

    except Exception as e:
        logger.warning(f"Failed to save VPN state: {e}")


def load_vpn_state() -> dict:
    """Load VPN connection state from storage."""
    try:
        if STATE_FILE.exists():
            try:
                state = json.loads(STATE_FILE.read_text())
                if logger.level("DEBUG").no <= logger.level("INFO").no:
                    logger.debug(
                        f"Loaded state from {STATE_FILE}: {json.dumps(state, indent=2)}"
                    )
                # State is valid for 5 minutes
                if time.time() - state.get("timestamp", 0) < 300:
                    return state
                # Even if state is stale, preserve IPs
                return {
                    "connected": False,
                    "normal_ip": state.get("normal_ip"),
                    "connected_ip": None,
                    "server": None,
                    "country": None,
                    "timestamp": time.time(),
                }
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse state file: {e}")
    except Exception as e:
        logger.warning(f"Failed to load VPN state: {e}")

    return {
        "connected": False,
        "normal_ip": None,
        "connected_ip": None,
        "server": None,
        "country": None,
        "timestamp": time.time(),
    }
