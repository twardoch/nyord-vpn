"""OpenVPN configuration templates and utilities.

this_file: src/nyord_vpn/utils/templates.py

This module handles OpenVPN configuration file management:
1. Config directory setup and maintenance
2. Config file download and extraction
3. Path resolution for config files
4. Secure file handling and permissions
"""

import contextlib
import hashlib
import os
import random
import shutil
import subprocess
import time
import zipfile
from datetime import datetime, timedelta
from pathlib import Path

import requests
from loguru import logger

from nyord_vpn.exceptions import VPNConfigError
from nyord_vpn.utils.utils import CONFIG_DIR # Import the standard CONFIG_DIR

# Constants
# CACHE_DIR definition removed as it's not used in this file.
# If general caching utilities were needed here, CACHE_DIR could be imported from utils.utils too.
CONFIG_ZIP = CONFIG_DIR / "ovpn.zip" # Store the downloaded zip in the user's config directory
OVPN_CONFIG_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"
ZIP_MAX_AGE_DAYS = 7  # Maximum age of ZIP file before redownload
MAX_CACHED_CONFIGS = 5  # Maximum number of cached config files for .ovpn files within CONFIG_DIR
MAX_RETRIES = 3  # Maximum number of download retries
INITIAL_RETRY_DELAY = 1  # Initial retry delay in seconds
MAX_RETRY_DELAY = 30  # Maximum retry delay in seconds

# Browser-like headers to avoid 403
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://nordvpn.com/",
    "Origin": "https://nordvpn.com",
}


def log_debug(msg: str, *args: object, **kwargs: object) -> None:
    """Log debug message only if debug logging is enabled."""
    if logger.level("DEBUG").no <= logger.level("INFO").no:
        logger.debug(msg.format(*args, **kwargs))


def calculate_sha256(data: bytes) -> str:
    """Calculate SHA256 hash of data."""
    return hashlib.sha256(data).hexdigest()


def verify_file_integrity(path: Path, expected_hash: str) -> bool:
    """Verify file integrity using SHA256 hash."""
    try:
        actual_hash = calculate_sha256(path.read_bytes())
        return actual_hash == expected_hash
    except Exception as e:
        log_debug("Failed to verify file integrity: {}", e)
        return False


def get_zip_age() -> timedelta | None:
    """Get the age of the cached ZIP file."""
    try:
        if not CONFIG_ZIP.exists():
            return None
        mtime = datetime.fromtimestamp(CONFIG_ZIP.stat().st_mtime)
        return datetime.now() - mtime
    except Exception as e:
        log_debug("Failed to get ZIP file age: {}", e)
        return None


def is_zip_expired() -> bool:
    """Check if the cached ZIP file is older than ZIP_MAX_AGE_DAYS."""
    age = get_zip_age()
    if age is None:
        return True
    return age > timedelta(days=ZIP_MAX_AGE_DAYS)


def secure_directory(path: Path, mode: int = 0o700) -> None:
    """Create directory with secure permissions."""
    try:
        path.mkdir(mode=mode, parents=True, exist_ok=True)
        stat_info = path.stat()
        if stat_info.st_mode & 0o777 != mode:
            path.chmod(mode)
            log_debug("Fixed directory permissions for {}", path)
        user_id = os.getuid()
        group_id = os.getgid()
        try:
            os.chown(path, user_id, group_id)
        except PermissionError:
            try:
                subprocess.run(
                    ["sudo", "chown", f"{user_id}:{group_id}", str(path)],
                    check=True,
                    capture_output=True,
                )
            except subprocess.CalledProcessError as e:
                raise VPNConfigError(
                    f"Failed to set ownership with sudo: {e.stderr.decode()}"
                ) from e
        log_debug("Set ownership of {} to {}:{}", path, user_id, group_id)
    except Exception as e:
        raise VPNConfigError(f"Failed to secure directory {path}: {e}")


def cleanup_old_configs() -> None:
    """Clean up old config files if more than MAX_CACHED_CONFIGS exist."""
    try:
        existing_configs = list(CONFIG_DIR.glob("*.tcp.ovpn"))
        if len(existing_configs) > MAX_CACHED_CONFIGS:
            log_debug("Cleaning up old config files...")
            existing_configs.sort(key=lambda p: p.stat().st_mtime)
            for config in existing_configs[:-MAX_CACHED_CONFIGS]:
                try:
                    config.unlink()
                    log_debug("Removed old config: {}", config)
                except Exception as e:
                    log_debug("Failed to remove old config {}: {}", config, e)
    except Exception as e:
        log_debug("Failed to cleanup old configs: {}", e)


def download_with_retry(
    url: str, headers: dict, timeout: int = 30
) -> tuple[bytes, str]:
    """Download a file with exponential backoff retry."""
    last_error = None
    delay = INITIAL_RETRY_DELAY

    for attempt in range(MAX_RETRIES):
        try:
            if attempt > 0:
                jitter = random.uniform(0, 0.1) * delay
                sleep_time = delay + jitter
                log_debug(
                    "Retry attempt {} after {:.1f}s delay...", attempt + 1, sleep_time
                )
                time.sleep(sleep_time)

            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            content = response.content
            content_hash = calculate_sha256(content)
            return content, content_hash

        except requests.RequestException as e:
            last_error = e
            if isinstance(e, requests.HTTPError) and (
                400 <= e.response.status_code < 500 and e.response.status_code != 429
            ):
                raise VPNConfigError(
                    f"Failed to download (HTTP {e.response.status_code}): {e}"
                ) from e
            delay = min(delay * 2, MAX_RETRY_DELAY)
            log_debug(
                "Download failed (attempt {}/{}): {}", attempt + 1, MAX_RETRIES, str(e)
            )

    if isinstance(last_error, requests.HTTPError):
        raise VPNConfigError(
            f"Failed to download after {MAX_RETRIES} retries "
            f"(HTTP {last_error.response.status_code}): {last_error}"
        ) from last_error
    raise VPNConfigError(
        f"Failed to download after {MAX_RETRIES} retries: {last_error}"
    ) from last_error


def extract_config_from_zip(server: str) -> Path:
    """Extract a single OpenVPN config file from ZIP.

    Args:
        server: Server hostname (should be a full server name like 'de123.nordvpn.com')

    Returns:
        Path to the extracted config file

    Raises:
        VPNConfigError: If extraction fails or the file is not found in the ZIP

    """
    server_file = f"{server}.tcp.ovpn"
    # The path inside the ZIP file where configs are stored
    zip_config_path = f"ovpn_tcp/{server_file}"
    log_debug("Extracting config file {} from {}", zip_config_path, CONFIG_ZIP)

    try:
        os.makedirs(CONFIG_DIR, exist_ok=True)

        # Make sure the directory has the right permissions
        try:
            CONFIG_DIR.chmod(0o700)
        except Exception as e:
            log_debug("Failed to set directory permissions: {}", e)

        # Try to extract the file
        try:
            with zipfile.ZipFile(CONFIG_ZIP) as zip_ref:
                # Check if the file exists in the ZIP
                try:
                    file_info = zip_ref.getinfo(zip_config_path)
                except KeyError:
                    # Log some debug info about the ZIP contents
                    tcp_configs = [
                        f
                        for f in zip_ref.namelist()
                        if f.startswith("ovpn_tcp/") and f.endswith(".tcp.ovpn")
                    ]
                    log_debug("Available TCP configs in ZIP: {}", len(tcp_configs))
                    if tcp_configs:
                        log_debug("Sample configs: {}", tcp_configs[:5])
                    raise VPNConfigError(
                        f"Config file {zip_config_path} not found in ZIP. ZIP contains {len(tcp_configs)} TCP configs."
                    )

                # Extract the file
                zip_ref.extract(file_info, CONFIG_DIR.parent)

                # The extracted file will be in a subdirectory structure
                # Move it to the expected location
                extracted_path = CONFIG_DIR.parent / zip_config_path
                target_path = CONFIG_DIR / server_file

                # Rename if needed
                if extracted_path != target_path:
                    # Make sure parent directories exist
                    target_path.parent.mkdir(parents=True, exist_ok=True)

                    # Move the file
                    if target_path.exists():
                        target_path.unlink()
                    shutil.move(str(extracted_path), str(target_path))

                    # Clean up empty directories
                    try:
                        extracted_dir = extracted_path.parent
                        if extracted_dir.exists() and not any(extracted_dir.iterdir()):
                            shutil.rmtree(str(extracted_dir))
                    except Exception as e:
                        log_debug("Failed to clean up empty directory: {}", e)

                # Set permissions
                try:
                    target_path.chmod(0o600)
                except Exception as e:
                    log_debug("Failed to set file permissions: {}", e)

                # Return the path to the extracted file
                return target_path

        except zipfile.BadZipFile as e:
            # If the ZIP is corrupted, delete it
            with contextlib.suppress(Exception):
                CONFIG_ZIP.unlink()
            raise VPNConfigError(f"Corrupted ZIP file: {e}") from e

    except Exception as e:
        # Catch-all for any other errors
        raise VPNConfigError(f"Failed to extract config file: {e}") from e


def download_config_zip() -> None:
    """Download and cache the OpenVPN configuration ZIP file."""
    try:
        secure_directory(CACHE_DIR)
        temp_zip = CACHE_DIR / f".ovpn.{os.getpid()}.zip.tmp"
        try:
            log_debug("Downloading OpenVPN configurations...")
            content, content_hash = download_with_retry(OVPN_CONFIG_URL, HEADERS)

            try:
                temp_zip.write_bytes(content)
                temp_zip.chmod(0o600)
                if not verify_file_integrity(temp_zip, content_hash):
                    raise VPNConfigError("Downloaded file corrupted during write")
            except Exception as e:
                raise VPNConfigError(f"Failed to write temporary ZIP file: {e}") from e

            try:
                with zipfile.ZipFile(temp_zip) as zip_ref:
                    tcp_configs = [
                        name
                        for name in zip_ref.namelist()
                        if name.startswith("ovpn_tcp/") and name.endswith(".tcp.ovpn")
                    ]
                    if not tcp_configs:
                        raise VPNConfigError(
                            "Downloaded ZIP contains no TCP configurations"
                        )
                    log_debug("ZIP contains {} TCP configs", len(tcp_configs))
            except zipfile.BadZipFile as e:
                raise VPNConfigError("Downloaded file is not a valid ZIP") from e

            try:
                temp_zip.replace(CONFIG_ZIP)
                if not verify_file_integrity(CONFIG_ZIP, content_hash):
                    raise VPNConfigError("ZIP file corrupted during move")
                log_debug("OpenVPN configurations cached at {}", CONFIG_ZIP)
            except Exception as e:
                raise VPNConfigError(f"Failed to save ZIP file: {e}") from e

        except Exception:
            try:
                if temp_zip.exists():
                    temp_zip.unlink()
            except Exception:
                pass
            raise

    except VPNConfigError:
        raise
    except Exception as e:
        raise VPNConfigError(f"Failed to download/cache configurations: {e}")


def get_config_path(server: str) -> Path:
    """Get path to OpenVPN config file for server.

    Args:
        server: Server hostname (e.g., 'de123.nordvpn.com') or country code (e.g., 'de')

    Returns:
        Path: Path to the config file

    Raises:
        VPNConfigError: If the config file cannot be found or extracted

    """
    # Ensure the config directory exists and has proper permissions
    secure_directory(CONFIG_DIR)

    # Clean up old configs to prevent accumulation
    cleanup_old_configs()

    # Handle the case where server is just a country code (e.g., 'de')
    if len(server) <= 3 and "." not in server:
        log_debug("Received country code '{}' instead of full hostname", server)
        # We'll need to find a server for this country from the ZIP
        is_country_code = True
    else:
        is_country_code = False

    # Normalize server name by removing .tcp suffix if present
    server = server.replace(".tcp", "")

    # If server is a country code, we won't have a specific config path yet
    if is_country_code:
        # We'll handle this after downloading the ZIP
        config_path = None
    else:
        config_path = CONFIG_DIR / f"{server}.tcp.ovpn"
        log_debug("Looking for config file at: {}", config_path)

        # Check if the specified config exists
        if config_path and config_path.exists():
            try:
                stat_info = config_path.stat()
                if stat_info.st_mode & 0o777 != 0o600:
                    config_path.chmod(0o600)
                    log_debug("Fixed config file permissions for {}", config_path)
                return config_path
            except Exception as e:
                raise VPNConfigError(f"Failed to verify config file permissions: {e}")

    # If we're here, we need to download or extract from the ZIP
    if is_zip_expired():
        age = get_zip_age()
        if age:
            log_debug("ZIP file is {} days old, downloading fresh copy...", age.days)
        else:
            log_debug("ZIP file is missing, downloading...")
        if CONFIG_ZIP.exists():
            try:
                CONFIG_ZIP.unlink()
            except Exception as e:
                log_debug("Failed to remove old ZIP file: {}", e)
        download_config_zip()

    if not CONFIG_ZIP.exists():
        download_config_zip()

    # For country codes, find a suitable server
    if is_country_code:
        log_debug("Finding server for country code: {}", server)
        try:
            with zipfile.ZipFile(CONFIG_ZIP) as zip_ref:
                # Find servers for this country
                country_servers = [
                    name
                    for name in zip_ref.namelist()
                    if name.startswith(f"ovpn_tcp/{server}")
                    and name.endswith(".tcp.ovpn")
                ]

                if not country_servers:
                    raise VPNConfigError(
                        f"No servers found for country code '{server}' in the ZIP file"
                    )

                # Sort by server number and pick the first one (usually lower load)
                country_servers.sort()
                selected_server = (
                    country_servers[0].split("/")[-1].replace(".tcp.ovpn", "")
                )
                log_debug(
                    "Selected server {} from {} available servers",
                    selected_server,
                    len(country_servers),
                )

                # Now extract this server's config
                server = selected_server
                config_path = CONFIG_DIR / f"{server}.tcp.ovpn"
        except zipfile.BadZipFile as e:
            with contextlib.suppress(Exception):
                CONFIG_ZIP.unlink()
            raise VPNConfigError(f"Corrupted ZIP file: {e}") from e

    # Now extract the config (either the original server or one we found for the country code)
    if not config_path or not config_path.exists():
        log_debug(
            "Config file not found at: {}", config_path if config_path else "None"
        )
        config_path = extract_config_from_zip(server)
        log_debug("Successfully extracted config to: {}", config_path)

    try:
        stat_info = config_path.stat()
        if stat_info.st_mode & 0o777 != 0o600:
            config_path.chmod(0o600)
            log_debug("Fixed config file permissions for {}", config_path)
    except Exception as e:
        raise VPNConfigError(f"Failed to verify config file permissions: {e}")

    return config_path
