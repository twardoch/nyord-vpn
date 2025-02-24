"""OpenVPN configuration management utilities.

this_file: src/nyord_vpn/utils/templates.py

This module provides OpenVPN configuration management for NordVPN.
It handles downloading, caching, and managing OpenVPN configurations
directly from NordVPN's servers.
"""

import os
import shutil
import tempfile
from pathlib import Path
import requests
import zipfile
import logging
from typing import Optional

# Constants
OVPN_CONFIG_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"
CONFIG_CACHE_DIR = Path.home() / ".config" / "nyord-vpn" / "configs"

# Browser-like headers to avoid 403
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://nordvpn.com/",
    "Origin": "https://nordvpn.com",
}


def setup_config_directory() -> None:
    """Setup and populate the OpenVPN configuration directory.

    Downloads and extracts the latest OpenVPN configurations from NordVPN
    if they don't exist or are outdated.
    """
    CONFIG_CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Download configurations
        response = requests.get(OVPN_CONFIG_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Create a temporary directory for extraction
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_path = Path(temp_dir) / "ovpn.zip"
            zip_path.write_bytes(response.content)

            # Extract only TCP configs
            with zipfile.ZipFile(zip_path) as zf:
                for info in zf.infolist():
                    if "ovpn_tcp" in info.filename:
                        zf.extract(info, CONFIG_CACHE_DIR)

            # Move TCP configs to the root of CONFIG_CACHE_DIR
            tcp_dir = CONFIG_CACHE_DIR / "ovpn_tcp"
            if tcp_dir.exists():
                for config in tcp_dir.glob("*.ovpn"):
                    config.rename(CONFIG_CACHE_DIR / config.name)
                shutil.rmtree(tcp_dir)

    except (requests.RequestException, zipfile.BadZipFile, OSError) as e:
        logging.error(f"Failed to download/extract OpenVPN configurations: {e}")
        raise


def get_config_path(server: str) -> Optional[Path]:
    """Get the path to the OpenVPN configuration file for a server.

    Args:
        server: Server hostname (e.g., 'de1076.nordvpn.com')

    Returns:
        Path to the configuration file or None if not found
    """
    # Ensure configs are downloaded
    if not CONFIG_CACHE_DIR.exists() or not any(CONFIG_CACHE_DIR.glob("*.ovpn")):
        setup_config_directory()

    # Look for exact match
    config_path = CONFIG_CACHE_DIR / f"{server}.tcp.ovpn"
    if config_path.exists():
        return config_path

    # Try without .tcp suffix
    config_path = CONFIG_CACHE_DIR / f"{server}.ovpn"
    if config_path.exists():
        return config_path

    return None


def refresh_configs() -> None:
    """Force refresh of OpenVPN configurations."""
    if CONFIG_CACHE_DIR.exists():
        shutil.rmtree(CONFIG_CACHE_DIR)
    setup_config_directory()


def get_openvpn_command(
    config_path: Path, auth_path: Path, log_path: Optional[Path] = None
) -> list[str]:
    """Get the OpenVPN command with optimal parameters.

    Args:
        config_path: Path to the OpenVPN configuration file
        auth_path: Path to the authentication file
        log_path: Optional path to log file

    Returns:
        List of command arguments for OpenVPN
    """
    cmd = [
        "sudo",
        "openvpn",
        "--config",
        str(config_path),
        "--auth-user-pass",
        str(auth_path),
        "--daemon",
        "--verb",
        "5",  # Increased verbosity for better debugging
        "--connect-retry",
        "2",  # Retry connection twice
        "--connect-timeout",
        "10",  # 10 seconds connection timeout
        "--resolv-retry",
        "infinite",  # Keep trying to resolve DNS
        "--ping",
        "10",  # Send ping every 10 seconds
        "--ping-restart",
        "60",  # Restart if no ping response for 60 seconds
    ]

    if log_path:
        cmd.extend(["--log", str(log_path)])

    return cmd
