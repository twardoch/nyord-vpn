"""OpenVPN configuration templates and utilities.

this_file: src/nyord_vpn/utils/templates.py

This module handles OpenVPN configuration file management:
1. Config directory setup and maintenance
2. Config file download and extraction
3. Path resolution for config files
"""

import io
import shutil
import zipfile
from pathlib import Path

import requests
from loguru import logger

from nyord_vpn.exceptions import VPNConfigError

# Constants
CACHE_DIR = Path.home() / ".cache" / "nyord-vpn"
CONFIG_DIR = CACHE_DIR / "configs"
CONFIG_ZIP = CACHE_DIR / "ovpn.zip"
OVPN_CONFIG_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"

# Browser-like headers to avoid 403
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://nordvpn.com/",
    "Origin": "https://nordvpn.com",
}


def extract_config_zip() -> None:
    """Extract OpenVPN configuration ZIP file.

    Extracts the downloaded ZIP file containing OpenVPN configurations.
    Removes UDP configurations as they are not used.

    Raises:
        VPNConfigError: If extraction fails
    """
    try:
        # Create config directory if needed
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensuring config directory exists: {CONFIG_DIR}")

        # Extract configurations
        logger.debug(f"Extracting configurations from {CONFIG_ZIP}")
        with zipfile.ZipFile(CONFIG_ZIP) as zip_ref:
            # Log zip contents
            logger.debug("ZIP contents:")
            for name in zip_ref.namelist()[:5]:  # Show first 5 files
                logger.debug(f"  {name}")
            zip_ref.extractall(CONFIG_DIR)

        # Remove UDP configs as they're not used
        udp_dir = CONFIG_DIR / "ovpn_udp"
        if udp_dir.exists():
            logger.debug(f"Removing UDP configs directory: {udp_dir}")
            shutil.rmtree(udp_dir)

        # Fix ownership of extracted files
        import os
        import subprocess

        user_id = os.getuid()
        group_id = os.getgid()
        logger.debug(f"Fixing ownership to {user_id}:{group_id}")
        subprocess.run(
            ["sudo", "chown", "-R", f"{user_id}:{group_id}", str(CONFIG_DIR)],
            check=True,
        )

        # Log final state
        logger.debug(f"Extraction complete. Contents of {CONFIG_DIR}:")
        for item in CONFIG_DIR.iterdir():
            logger.debug(f"  {item}")

        logger.debug(f"OpenVPN configurations extracted to {CONFIG_DIR}")
    except Exception as e:
        raise VPNConfigError(f"Failed to extract configurations: {e}")


def download_config_zip() -> None:
    """Download and cache the OpenVPN configuration ZIP file.

    Downloads the ZIP file containing all OpenVPN configurations from NordVPN
    and caches it locally. The ZIP contains two folders:
    - ovpn_tcp/: TCP configurations
    - ovpn_udp/: UDP configurations (not used)

    Raises:
        VPNConfigError: If download or caching fails
    """
    try:
        # Create cache directory if needed
        CACHE_DIR.mkdir(parents=True, exist_ok=True)

        # Download configurations
        logger.debug("Downloading OpenVPN configurations...")
        response = requests.get(OVPN_CONFIG_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Cache the ZIP file
        CONFIG_ZIP.write_bytes(response.content)
        logger.debug(f"OpenVPN configurations cached at {CONFIG_ZIP}")

        # Extract the configurations
        extract_config_zip()

        # Clean up the ZIP file
        CONFIG_ZIP.unlink()
    except Exception as e:
        raise VPNConfigError(f"Failed to download/cache configurations: {e}")


def get_config_path(server: str) -> Path:
    """Get path to OpenVPN config file for server.

    Args:
        server: Server hostname (e.g. us123.nordvpn.com)

    Returns:
        Path to config file

    Raises:
        VPNConfigError: If config file cannot be found or downloaded
    """
    # Remove .tcp suffix if present as configs are already in tcp directory
    server = server.replace(".tcp", "")

    # The config files in the ZIP have .tcp.ovpn extension
    config_path = CONFIG_DIR / "ovpn_tcp" / f"{server}.tcp.ovpn"
    logger.debug(f"Looking for config file at: {config_path}")

    # Log the directory contents if it exists
    if CONFIG_DIR.exists():
        logger.debug(f"Contents of {CONFIG_DIR}:")
        try:
            for item in CONFIG_DIR.iterdir():
                logger.debug(f"  {item}")

            tcp_dir = CONFIG_DIR / "ovpn_tcp"
            if tcp_dir.exists():
                logger.debug(f"Contents of {tcp_dir} (sample):")
                for item in list(tcp_dir.iterdir())[:5]:  # Show first 5 files
                    logger.debug(f"  {item}")
            else:
                logger.warning(f"TCP config directory not found at: {tcp_dir}")
        except Exception as e:
            logger.error(f"Error listing directory contents: {e}")

    # If config doesn't exist, try downloading
    if not config_path.exists():
        logger.debug(f"Config file not found at: {config_path}")
        logger.debug("Attempting to download configurations...")
        download_config_zip()

        # Verify config exists after download
        if not config_path.exists():
            logger.error(
                f"Config file still not found at: {config_path} after download"
            )
            logger.debug("Directory structure after download:")
            try:
                for item in CONFIG_DIR.iterdir():
                    logger.debug(f"  {item}")
                tcp_dir = CONFIG_DIR / "ovpn_tcp"
                if tcp_dir.exists():
                    logger.debug(f"Sample contents of {tcp_dir}:")
                    for item in list(tcp_dir.iterdir())[:5]:
                        logger.debug(f"  {item}")
            except Exception as e:
                logger.error(f"Error listing directory contents: {e}")
            raise VPNConfigError(f"Config file not found for server: {server}")
        else:
            logger.debug(f"Successfully found config at: {config_path} after download")

    return config_path
