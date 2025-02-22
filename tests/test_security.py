"""Tests for security utilities."""

import os
import pytest
from pathlib import Path

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.security import (
    create_secure_tempfile,
    validate_file_permissions,
    validate_path,
    generate_secure_token,
)


def test_create_secure_tempfile(temp_dir):
    """Test secure temporary file creation."""
    # Test successful file creation
    temp_file = create_secure_tempfile()
    assert temp_file.exists()
    assert temp_file.is_file()
    assert oct(temp_file.stat().st_mode)[-3:] == "600"

    # Test with custom prefix and suffix
    temp_file = create_secure_tempfile(prefix="test_", suffix=".conf")
    assert temp_file.exists()
    assert temp_file.name.startswith("test_")
    assert temp_file.name.endswith(".conf")
    assert oct(temp_file.stat().st_mode)[-3:] == "600"

    # Test file creation failure
    with pytest.raises(VPNError, match="Failed to create secure temporary file"):
        with pytest.raises(OSError):
            create_secure_tempfile(prefix="/invalid/")


def test_validate_file_permissions(temp_dir):
    """Test file permission validation."""
    # Create test file
    test_file = temp_dir / "test.txt"
    test_file.touch(mode=0o644)

    # Test permission fixing
    validate_file_permissions(test_file)
    assert oct(test_file.stat().st_mode)[-3:] == "600"

    # Test non-existent file
    with pytest.raises(VPNError, match="File not found"):
        validate_file_permissions(temp_dir / "nonexistent.txt")

    # Test permission change failure
    test_file.chmod(0o444)  # Make read-only
    with pytest.raises(VPNError, match="Failed to set file permissions"):
        validate_file_permissions(test_file)


def test_validate_path():
    """Test path validation."""
    # Test absolute path
    path = Path(__file__).resolve()
    validated = validate_path(path)
    assert validated == path
    assert validated.is_absolute()

    # Test string path
    validated = validate_path(str(path))
    assert validated == path
    assert validated.is_absolute()

    # Test relative path
    with pytest.raises(VPNError, match="Path must be absolute"):
        validate_path("relative/path")

    # Test non-existent path
    with pytest.raises(VPNError, match="Path does not exist"):
        validate_path("/nonexistent/path")

    # Test invalid path
    with pytest.raises(VPNError, match="Invalid path"):
        validate_path("\0invalid")


def test_generate_secure_token():
    """Test secure token generation."""
    # Test default length
    token = generate_secure_token()
    assert isinstance(token, str)
    assert len(token) == 64  # 32 bytes = 64 hex chars

    # Test custom length
    token = generate_secure_token(length=16)
    assert len(token) == 32  # 16 bytes = 32 hex chars

    # Test uniqueness
    tokens = {generate_secure_token() for _ in range(100)}
    assert len(tokens) == 100  # All tokens should be unique
