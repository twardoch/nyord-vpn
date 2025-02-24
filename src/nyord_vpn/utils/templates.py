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
CONFIG_DIR = Path.home() / ".config" / "nyord-vpn" / "configs"
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
        CACHE_DIR.chmod(0o700)  # Secure permissions

        # Download configurations
        logger.debug("Downloading OpenVPN configurations...")
        response = requests.get(OVPN_CONFIG_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Cache the ZIP file
        CONFIG_ZIP.write_bytes(response.content)
        CONFIG_ZIP.chmod(0o600)  # Secure permissions

        logger.debug(f"OpenVPN configurations cached at {CONFIG_ZIP}")
    except Exception as e:
        raise VPNConfigError(f"Failed to download/cache configurations: {e}")


def get_config_path(hostname: str) -> Path | None:
    """Get path to OpenVPN config file for a server.

    Extracts the specific config file for the requested server from the cached
    ZIP file. Only TCP configurations are supported.

    Args:
        hostname: Server hostname (e.g. 'us123.nordvpn.com')

    Returns:
        Path to config file or None if not found

    Raises:
        VPNConfigError: If config extraction fails
    """
    try:
        # Download ZIP if not cached
        if not CONFIG_ZIP.exists():
            download_config_zip()

        # Create config directory if needed
        tcp_dir = CONFIG_DIR / "ovpn_tcp"
        tcp_dir.mkdir(parents=True, exist_ok=True)
        tcp_dir.chmod(0o700)

        # Construct config file path
        base_name = hostname.replace(".tcp", "")
        config_path = tcp_dir / f"{base_name}.tcp.ovpn"

        # Extract if not already present
        if not config_path.exists():
            zip_path = f"ovpn_tcp/{base_name}.tcp.ovpn"
            with zipfile.ZipFile(CONFIG_ZIP) as zf:
                try:
                    config_bytes = zf.read(zip_path)
                except KeyError:
                    return None

                # Write config file
                config_path.write_bytes(config_bytes)
                config_path.chmod(0o600)

        return config_path

    except Exception as e:
        raise VPNConfigError(f"Failed to extract config for {hostname}: {e}")


def get_openvpn_command(
    config_path: Path, auth_path: Path, log_path: Path
) -> list[str]:
    """Get OpenVPN command with all necessary arguments.

    Args:
        config_path: Path to OpenVPN config file
        auth_path: Path to authentication file
        log_path: Path to log file

    Returns:
        List of command arguments
    """
    return [
        "sudo",
        "openvpn",
        "--config",
        str(config_path),
        "--auth-user-pass",
        str(auth_path),
        "--daemon",
        "--verb",
        "5",  # Increased verbosity
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
        "--log",
        str(log_path),  # Log to file for debugging
    ]
