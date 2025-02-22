"""Security utilities."""

import secrets
import tempfile
from pathlib import Path
from typing import NoReturn
from cryptography.fernet import Fernet

from nyord_vpn.core.exceptions import VPNError

MIN_PASSWORD_LENGTH = 8


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
        if not temp_file.exists():
            msg = "Failed to create temporary file"
            raise VPNError(msg)
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


def _raise_path_error(error: str) -> NoReturn:
    msg = f"Invalid path: {error}"
    raise VPNError(msg)


def _raise_absolute_path_error(path: str) -> NoReturn:
    msg = f"Path must be absolute: {path}"
    raise VPNError(msg)


def _raise_nonexistent_path_error(path: str) -> NoReturn:
    msg = f"Path does not exist: {path}"
    raise VPNError(msg)


def validate_path(path: str | Path) -> Path:
    """Validate a path string or Path object."""
    try:
        path_obj = Path(path)
        if not path_obj.is_absolute():
            _raise_absolute_path_error(str(path))
        elif not path_obj.exists():
            _raise_nonexistent_path_error(str(path))
        else:
            return path_obj
    except Exception as e:
        _raise_path_error(str(e))


def generate_secure_token(length: int = 32) -> str:
    """Generate a cryptographically secure random token.

    Args:
        length: Length of the token in bytes

    Returns:
        str: Hex-encoded random token
    """
    return secrets.token_hex(length)


def validate_password(password: str) -> bool:
    """Validate password meets security requirements."""
    try:
        if not password or len(password) < MIN_PASSWORD_LENGTH:
            msg = f"Password must be at least {MIN_PASSWORD_LENGTH} characters"
            raise VPNError(msg)
        return True
    except Exception as e:
        msg = f"Password validation failed: {e}"
        raise VPNError(msg) from e


def encrypt_password(password: str) -> str:
    """Encrypt password using Fernet encryption."""
    try:
        if not password:
            msg = "Password cannot be empty"
            raise VPNError(msg)
        key = Fernet.generate_key()
        f = Fernet(key)
        return f.encrypt(password.encode()).decode()
    except Exception as e:
        msg = f"Password encryption failed: {e}"
        raise VPNError(msg) from e
