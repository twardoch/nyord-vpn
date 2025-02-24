"""OpenVPN configuration templates and utilities.

this_file: src/nyord_vpn/utils/templates.py

This module handles OpenVPN configuration file management:
1. Config directory setup and maintenance
2. Config file download and extraction
3. Path resolution for config files
4. Secure file handling and permissions
"""

import shutil
import zipfile
import tempfile
from pathlib import Path
import os
import subprocess
from datetime import datetime, timedelta
from typing import Optional
import time
import random
import fcntl
import contextlib

import requests
from loguru import logger

from nyord_vpn.exceptions import VPNConfigError

# Constants
CACHE_DIR = Path.home() / ".cache" / "nyord-vpn"
CONFIG_DIR = CACHE_DIR / "configs"
CONFIG_ZIP = CACHE_DIR / "ovpn.zip"
LOCK_FILE = CACHE_DIR / ".lock"
OVPN_CONFIG_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"
ZIP_MAX_AGE_DAYS = 7  # Maximum age of ZIP file before redownload
MAX_CACHED_CONFIGS = 5  # Maximum number of cached config files
MAX_RETRIES = 3  # Maximum number of download retries
INITIAL_RETRY_DELAY = 1  # Initial retry delay in seconds
MAX_RETRY_DELAY = 30  # Maximum retry delay in seconds
LOCK_TIMEOUT = 60  # Maximum time to wait for lock in seconds

# Browser-like headers to avoid 403
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://nordvpn.com/",
    "Origin": "https://nordvpn.com",
}


@contextlib.contextmanager
def file_lock():
    """Context manager for file-based locking to prevent concurrent access.

    Uses fcntl for atomic file locking. Will wait up to LOCK_TIMEOUT seconds
    to acquire the lock.

    Raises:
        VPNConfigError: If lock cannot be acquired or released
    """
    lock_fd = None
    try:
        # Create lock file if it doesn't exist
        LOCK_FILE.touch(mode=0o600, exist_ok=True)

        # Open the lock file
        lock_fd = os.open(str(LOCK_FILE), os.O_RDWR)

        # Try to acquire lock with timeout
        start_time = time.monotonic()
        while True:
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() - start_time > LOCK_TIMEOUT:
                    raise VPNConfigError(
                        f"Failed to acquire lock after {LOCK_TIMEOUT} seconds"
                    )
                time.sleep(0.1)

        log_debug("Acquired file lock")
        yield

    except Exception as e:
        if not isinstance(e, VPNConfigError):
            raise VPNConfigError(f"Error while holding file lock: {e}") from e
        raise

    finally:
        if lock_fd is not None:
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_UN)
                os.close(lock_fd)
                log_debug("Released file lock")
            except Exception as e:
                logger.error("Failed to release file lock: {}", e)


def log_debug(msg: str, *args: object, **kwargs: object) -> None:
    """Log debug message only if debug logging is enabled.

    Args:
        msg: Message to log
        *args: Additional positional args for format string
        **kwargs: Additional keyword args for format string
    """
    if logger.level("DEBUG").no <= logger.level("INFO").no:
        logger.debug(msg.format(*args, **kwargs))


def get_zip_age() -> Optional[timedelta]:
    """Get the age of the cached ZIP file.

    Returns:
        Age of the ZIP file as timedelta, or None if file doesn't exist or error occurs
    """
    try:
        if not CONFIG_ZIP.exists():
            return None

        mtime = datetime.fromtimestamp(CONFIG_ZIP.stat().st_mtime)
        return datetime.now() - mtime
    except Exception as e:
        log_debug("Failed to get ZIP file age: {}", e)
        return None


def is_zip_expired() -> bool:
    """Check if the cached ZIP file is older than ZIP_MAX_AGE_DAYS.

    Returns:
        True if ZIP file is expired or doesn't exist, False otherwise
    """
    age = get_zip_age()
    if age is None:
        return True
    return age > timedelta(days=ZIP_MAX_AGE_DAYS)


def secure_directory(path: Path, mode: int = 0o700) -> None:
    """Create directory with secure permissions.

    Args:
        path: Directory path to create
        mode: Directory permissions (default: 0o700)

    Raises:
        VPNConfigError: If directory creation or permission setting fails
    """
    try:
        # Create directory with secure permissions
        path.mkdir(mode=mode, parents=True, exist_ok=True)

        # Verify permissions
        stat_info = path.stat()
        if stat_info.st_mode & 0o777 != mode:
            path.chmod(mode)
            log_debug("Fixed directory permissions for {}", path)

        # Set ownership to current user
        user_id = os.getuid()
        group_id = os.getgid()
        try:
            os.chown(path, user_id, group_id)
        except PermissionError:
            # Fall back to sudo if needed
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
    """Clean up old config files if more than MAX_CACHED_CONFIGS exist.

    Removes oldest config files based on modification time.
    """
    try:
        existing_configs = list(CONFIG_DIR.glob("*.tcp.ovpn"))
        if len(existing_configs) > MAX_CACHED_CONFIGS:
            log_debug("Cleaning up old config files...")
            # Sort by modification time, oldest first
            existing_configs.sort(key=lambda p: p.stat().st_mtime)
            # Remove oldest files, keeping MAX_CACHED_CONFIGS most recent
            for config in existing_configs[:-MAX_CACHED_CONFIGS]:
                try:
                    config.unlink()
                    log_debug("Removed old config: {}", config)
                except Exception as e:
                    log_debug("Failed to remove old config {}: {}", config, e)
    except Exception as e:
        log_debug("Failed to cleanup old configs: {}", e)


def download_with_retry(url: str, headers: dict, timeout: int = 30) -> bytes:
    """Download a file with exponential backoff retry.

    Args:
        url: URL to download from
        headers: Request headers
        timeout: Request timeout in seconds

    Returns:
        Downloaded file content

    Raises:
        VPNConfigError: If download fails after all retries
    """
    last_error = None
    delay = INITIAL_RETRY_DELAY

    for attempt in range(MAX_RETRIES):
        try:
            if attempt > 0:
                # Add jitter to avoid thundering herd
                jitter = random.uniform(0, 0.1) * delay
                sleep_time = delay + jitter
                log_debug(
                    "Retry attempt {} after {:.1f}s delay...", attempt + 1, sleep_time
                )
                time.sleep(sleep_time)

            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response.content

        except requests.RequestException as e:
            last_error = e
            if isinstance(e, requests.HTTPError):
                # Don't retry on 4xx errors except 429 (Too Many Requests)
                if (
                    400 <= e.response.status_code < 500
                    and e.response.status_code != 429
                ):
                    raise VPNConfigError(
                        f"Failed to download (HTTP {e.response.status_code}): {e}"
                    ) from e

            # Exponential backoff with max delay
            delay = min(delay * 2, MAX_RETRY_DELAY)
            log_debug(
                "Download failed (attempt {}/{}): {}", attempt + 1, MAX_RETRIES, str(e)
            )

    # If we get here, all retries failed
    if isinstance(last_error, requests.HTTPError):
        raise VPNConfigError(
            f"Failed to download after {MAX_RETRIES} retries "
            f"(HTTP {last_error.response.status_code}): {last_error}"
        ) from last_error
    raise VPNConfigError(
        f"Failed to download after {MAX_RETRIES} retries: {last_error}"
    ) from last_error


def extract_config_from_zip(server: str) -> Path:
    """Extract a single OpenVPN configuration file from the ZIP.

    Args:
        server: Server hostname (e.g. us123.nordvpn.com)

    Returns:
        Path to the extracted config file

    Raises:
        VPNConfigError: If extraction fails
    """
    try:
        # Create config directory with secure permissions
        secure_directory(CONFIG_DIR)

        # Clean up old config files
        cleanup_old_configs()

        # The config files in the ZIP have .tcp.ovpn extension and are in ovpn_tcp directory
        zip_path = f"ovpn_tcp/{server}.tcp.ovpn"
        config_path = CONFIG_DIR / f"{server}.tcp.ovpn"

        # Extract single config file
        log_debug("Extracting config file {} from {}", zip_path, CONFIG_ZIP)
        try:
            with zipfile.ZipFile(CONFIG_ZIP) as zip_ref:
                try:
                    zip_ref.extract(zip_path, CONFIG_DIR)
                except KeyError:
                    # List available configs for debugging
                    tcp_configs = [
                        name
                        for name in zip_ref.namelist()
                        if name.startswith("ovpn_tcp/") and name.endswith(".tcp.ovpn")
                    ]
                    log_debug("Available TCP configs in ZIP: {}", len(tcp_configs))
                    if tcp_configs:
                        log_debug("Sample configs: {}", tcp_configs[:5])
                    raise VPNConfigError(
                        f"Config file {zip_path} not found in ZIP. "
                        f"ZIP contains {len(tcp_configs)} TCP configs."
                    )
        except zipfile.BadZipFile as e:
            # ZIP file is corrupted, delete it
            try:
                CONFIG_ZIP.unlink()
            except Exception:
                pass
            raise VPNConfigError(f"Corrupted ZIP file: {e}") from e

        # Move file from nested directory to config dir
        extracted_path = CONFIG_DIR / zip_path
        try:
            extracted_path.rename(config_path)
        except Exception as e:
            raise VPNConfigError(f"Failed to move config file: {e}") from e

        # Remove the now-empty ovpn_tcp directory
        try:
            (CONFIG_DIR / "ovpn_tcp").rmdir()
        except (FileNotFoundError, OSError):
            pass  # Directory might not exist or might not be empty

        # Set secure permissions
        try:
            config_path.chmod(0o600)
            log_debug("Set permissions on {}", config_path)
        except Exception as e:
            raise VPNConfigError(f"Failed to set config file permissions: {e}") from e

        return config_path

    except VPNConfigError:
        raise
    except Exception as e:
        raise VPNConfigError(f"Failed to extract configuration: {e}")


def download_config_zip() -> None:
    """Download and cache the OpenVPN configuration ZIP file.

    Downloads the ZIP file containing all OpenVPN configurations from NordVPN
    and caches it locally. The ZIP contains two folders:
    - ovpn_tcp/: TCP configurations (used)
    - ovpn_udp/: UDP configurations (not used)

    Raises:
        VPNConfigError: If download or caching fails
    """
    try:
        # Create cache directory with secure permissions
        secure_directory(CACHE_DIR)

        # Download to temp file first
        temp_zip = CACHE_DIR / f".ovpn.{os.getpid()}.zip.tmp"
        try:
            log_debug("Downloading OpenVPN configurations...")

            # Download with retry
            content = download_with_retry(OVPN_CONFIG_URL, HEADERS)

            # Write to temp file
            try:
                temp_zip.write_bytes(content)
                temp_zip.chmod(0o600)
            except Exception as e:
                raise VPNConfigError(f"Failed to write temporary ZIP file: {e}") from e

            # Verify ZIP file is valid
            try:
                with zipfile.ZipFile(temp_zip) as zip_ref:
                    # Check if ZIP contains TCP configs
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

            # Move to final location (atomic)
            try:
                temp_zip.replace(CONFIG_ZIP)
                log_debug("OpenVPN configurations cached at {}", CONFIG_ZIP)
            except Exception as e:
                raise VPNConfigError(f"Failed to save ZIP file: {e}") from e

        except Exception:
            # Clean up temp file if it exists
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
        server: Server hostname (e.g. us123.nordvpn.com)

    Returns:
        Path to config file

    Raises:
        VPNConfigError: If config file cannot be found or downloaded
    """
    # Use file locking to prevent concurrent access
    with file_lock():
        # Remove .tcp suffix if present as configs are already in tcp directory
        server = server.replace(".tcp", "")

        # The config files in the ZIP have .tcp.ovpn extension
        config_path = CONFIG_DIR / f"{server}.tcp.ovpn"
        log_debug("Looking for config file at: {}", config_path)

        # Check if we need to download a fresh ZIP
        if is_zip_expired():
            age = get_zip_age()
            if age:
                log_debug(
                    "ZIP file is {} days old, downloading fresh copy...", age.days
                )
            else:
                log_debug("ZIP file is missing, downloading...")
            if CONFIG_ZIP.exists():
                try:
                    CONFIG_ZIP.unlink()
                except Exception as e:
                    log_debug("Failed to remove old ZIP file: {}", e)
            download_config_zip()

        # If config doesn't exist, try downloading and extracting
        if not config_path.exists():
            log_debug("Config file not found at: {}", config_path)

            # Download ZIP if needed
            if not CONFIG_ZIP.exists():
                download_config_zip()

            # Extract just the needed config
            config_path = extract_config_from_zip(server)
            log_debug("Successfully extracted config to: {}", config_path)

        # Verify config file permissions
        try:
            stat_info = config_path.stat()
            if stat_info.st_mode & 0o777 != 0o600:
                config_path.chmod(0o600)
                log_debug("Fixed config file permissions for {}", config_path)
        except Exception as e:
            raise VPNConfigError(f"Failed to verify config file permissions: {e}")

        return config_path
