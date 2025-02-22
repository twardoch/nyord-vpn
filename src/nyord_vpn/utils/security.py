"""Security utilities for VPN operations."""

import os
import secrets
import tempfile
from pathlib import Path

from nyord_vpn.core.exceptions import VPNError


def create_secure_tempfile(prefix: str = "nyord_vpn_", suffix: str = "") -> Path:
    """Create a secure temporary file with proper permissions.

    Args:
        prefix: Prefix for the temporary file name
        suffix: Suffix for the temporary file name

    Returns:
        Path: Path to the created temporary file

    Raises:
        VPNError: If file creation fails
    """
    try:
        # Create a unique temporary file
        temp_file = Path(tempfile.mkstemp(prefix=prefix, suffix=suffix)[1])
        # Set secure permissions (600)
        temp_file.chmod(0o600)
        return temp_file
    except OSError as e:
        msg = f"Failed to create secure temporary file: {e}"
        raise VPNError(msg) from e


def validate_file_permissions(path: Path, mode: int = 0o600) -> None:
    """Validate and fix file permissions.

    Args:
        path: Path to the file
        mode: Required file mode (default: 600)

    Raises:
        VPNError: If file doesn't exist or permissions can't be set
    """
    if not path.exists():
        msg = f"File not found: {path}"
        raise VPNError(msg)

    try:
        current_mode = path.stat().st_mode & 0o777
        if current_mode != mode:
            path.chmod(mode)
    except OSError as e:
        msg = f"Failed to set file permissions: {e}"
        raise VPNError(msg) from e


def validate_path(path: str | Path) -> Path:
    """Validate that a path is absolute and exists.

    Args:
        path: Path to validate

    Returns:
        Path: Validated Path object

    Raises:
        VPNError: If path is invalid
    """
    try:
        path_obj = Path(path)
        if not path_obj.is_absolute():
            msg = f"Path must be absolute: {path}"
            raise VPNError(msg)
        if not path_obj.exists():
            msg = f"Path does not exist: {path}"
            raise VPNError(msg)
        return path_obj
    except Exception as e:
        msg = f"Invalid path: {e}"
        raise VPNError(msg) from e


def generate_secure_token(length: int = 32) -> str:
    """Generate a cryptographically secure random token.

    Args:
        length: Length of the token in bytes

    Returns:
        str: Hex-encoded random token
    """
    return secrets.token_hex(length)
