"""Input validation utilities."""

import re
import stat
from pathlib import Path
from typing import Any

from nyord_vpn.core.exceptions import VPNError


def validate_country(country: str) -> str:
    """Validate and normalize country name/code.

    Args:
        country: Country name or code

    Returns:
        Normalized country name

    Raises:
        VPNError: If country is invalid
    """
    if not country or not isinstance(country, str):
        msg = "Country must be a non-empty string"
        raise VPNError(msg)

    # Remove special characters and extra whitespace
    country = re.sub(r"[^\w\s-]", "", country).strip()
    if not country:
        msg = "Invalid country name format"
        raise VPNError(msg)

    return country


def validate_credentials(username: str, password: str) -> tuple[str, str]:
    """Validate VPN credentials.

    Args:
        username: VPN username
        password: VPN password

    Returns:
        Tuple of (username, password)

    Raises:
        VPNError: If credentials are invalid
    """
    if not username or not isinstance(username, str):
        msg = "Username must be a non-empty string"
        raise VPNError(msg)

    if not password or not isinstance(password, str):
        msg = "Password must be a non-empty string"
        raise VPNError(msg)

    # Remove special characters and whitespace
    username = username.strip()
    password = password.strip()

    if not username or not password:
        msg = "Invalid credentials format"
        raise VPNError(msg)

    return username, password


def validate_hostname(hostname: str) -> str:
    """Validate server hostname.

    Args:
        hostname: Server hostname

    Returns:
        Validated hostname

    Raises:
        VPNError: If hostname is invalid
    """
    if not hostname or not isinstance(hostname, str):
        msg = "Hostname must be a non-empty string"
        raise VPNError(msg)

    # Basic hostname validation
    hostname = hostname.strip().lower()
    if not re.match(
        r"^[a-z0-9]([a-z0-9\-]{0,61}[a-z0-9])?(\.[a-z0-9]([a-z0-9\-]{0,61}[a-z0-9])?)*$",
        hostname,
    ):
        msg = "Invalid hostname format"
        raise VPNError(msg)

    return hostname


def validate_command(cmd: str | Path) -> Path:
    """Validate command path.

    Args:
        cmd: Command path

    Returns:
        Resolved Path object

    Raises:
        VPNError: If command is invalid
    """
    if not cmd:
        msg = "Command path cannot be empty"
        raise VPNError(msg)

    try:
        cmd_path = Path(cmd).resolve()
    except Exception as e:
        msg = f"Invalid command path: {e}"
        raise VPNError(msg) from e

    if not cmd_path.exists():
        msg = f"Command not found: {cmd_path}"
        raise VPNError(msg)

    if not cmd_path.is_file():
        msg = f"Not a file: {cmd_path}"
        raise VPNError(msg)

    # Check permissions
    mode = cmd_path.stat().st_mode
    if not mode & stat.S_IXUSR:
        msg = f"Command not executable: {cmd_path}"
        raise VPNError(msg)

    if mode & (stat.S_IWGRP | stat.S_IWOTH):
        msg = f"Unsafe permissions on command: {cmd_path}"
        raise VPNError(msg)

    return cmd_path


def validate_env_var(name: str, value: Any) -> str:
    """Validate environment variable.

    Args:
        name: Variable name
        value: Variable value

    Returns:
        Validated value

    Raises:
        VPNError: If variable is invalid
    """
    if not name or not isinstance(name, str):
        msg = "Environment variable name must be a non-empty string"
        raise VPNError(msg)

    if not value or not isinstance(value, str | int | float | bool):
        msg = f"Invalid environment variable value for {name}"
        raise VPNError(msg)

    # Convert to string and validate
    value = str(value).strip()
    if not value:
        msg = f"Empty environment variable value for {name}"
        raise VPNError(msg)

    # Check for injection patterns
    if re.search(r"[;&|`$]", value):
        msg = f"Invalid characters in environment variable {name}"
        raise VPNError(msg)

    return value
