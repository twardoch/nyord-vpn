"""Tests for validation utilities."""

import pytest

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.validation import (
    validate_country,
    validate_credentials,
    validate_hostname,
    validate_command,
    validate_env_var,
)


def test_validate_country():
    """Test country validation."""
    # Valid cases
    assert validate_country("United States") == "United States"
    assert validate_country("US") == "US"
    assert validate_country("united-states") == "united-states"

    # Invalid cases
    with pytest.raises(VPNError, match="Country must be a non-empty string"):
        validate_country("")
    with pytest.raises(VPNError, match="Country must be a non-empty string"):
        validate_country(None)  # type: ignore
    with pytest.raises(VPNError, match="Invalid country name format"):
        validate_country("!@#$%^")


def test_validate_credentials():
    """Test credentials validation."""
    # Valid cases
    username, password = validate_credentials("user123", "pass456")
    assert username == "user123"
    assert password == "pass456"

    # Invalid cases
    with pytest.raises(VPNError, match="Username must be a non-empty string"):
        validate_credentials("", "pass123")
    with pytest.raises(VPNError, match="Password must be a non-empty string"):
        validate_credentials("user123", "")
    with pytest.raises(VPNError, match="Username must be a non-empty string"):
        validate_credentials(None, "pass123")  # type: ignore
    with pytest.raises(VPNError, match="Password must be a non-empty string"):
        validate_credentials("user123", None)  # type: ignore


def test_validate_hostname():
    """Test hostname validation."""
    # Valid cases
    assert validate_hostname("server1.nordvpn.com") == "server1.nordvpn.com"
    assert validate_hostname("test-server.com") == "test-server.com"
    assert validate_hostname("a" * 63 + ".com") == "a" * 63 + ".com"

    # Invalid cases
    with pytest.raises(VPNError, match="Hostname must be a non-empty string"):
        validate_hostname("")
    with pytest.raises(VPNError, match="Hostname must be a non-empty string"):
        validate_hostname(None)  # type: ignore
    with pytest.raises(VPNError, match="Invalid hostname format"):
        validate_hostname("server!@#.com")
    with pytest.raises(VPNError, match="Invalid hostname format"):
        validate_hostname("a" * 64 + ".com")  # Too long label
    with pytest.raises(VPNError, match="Invalid hostname format"):
        validate_hostname("-server.com")  # Starts with hyphen
    with pytest.raises(VPNError, match="Invalid hostname format"):
        validate_hostname("server-.com")  # Ends with hyphen


def test_validate_command(tmp_path):
    """Test command validation."""
    # Create test executable
    test_cmd = tmp_path / "test_cmd"
    test_cmd.write_text("#!/bin/bash\necho test")
    test_cmd.chmod(0o755)  # rwxr-xr-x

    # Valid case
    assert validate_command(test_cmd) == test_cmd.resolve()

    # Invalid cases
    with pytest.raises(VPNError, match="Command path cannot be empty"):
        validate_command("")
    with pytest.raises(VPNError, match="Command not found"):
        validate_command("/nonexistent/cmd")

    # Non-executable file
    non_exec = tmp_path / "non_exec"
    non_exec.write_text("test")
    non_exec.chmod(0o644)  # rw-r--r--
    with pytest.raises(VPNError, match="Command not executable"):
        validate_command(non_exec)

    # World-writable file
    world_writable = tmp_path / "world_writable"
    world_writable.write_text("#!/bin/bash\necho test")
    world_writable.chmod(0o757)  # rwxr-xrwx
    with pytest.raises(VPNError, match="Unsafe permissions"):
        validate_command(world_writable)


def test_validate_env_var():
    """Test environment variable validation."""
    # Valid cases
    assert validate_env_var("TEST_VAR", "value123") == "value123"
    assert validate_env_var("DEBUG", True) == "True"
    assert validate_env_var("PORT", 8080) == "8080"
    assert validate_env_var("RATIO", 3.14) == "3.14"

    # Invalid cases
    with pytest.raises(
        VPNError, match="Environment variable name must be a non-empty string"
    ):
        validate_env_var("", "value")
    with pytest.raises(
        VPNError, match="Environment variable name must be a non-empty string"
    ):
        validate_env_var(None, "value")  # type: ignore
    with pytest.raises(VPNError, match="Invalid environment variable value"):
        validate_env_var("TEST_VAR", None)  # type: ignore
    with pytest.raises(VPNError, match="Invalid environment variable value"):
        validate_env_var("TEST_VAR", [])  # type: ignore
    with pytest.raises(VPNError, match="Empty environment variable value"):
        validate_env_var("TEST_VAR", "   ")
    with pytest.raises(VPNError, match="Invalid characters in environment variable"):
        validate_env_var("TEST_VAR", "value; rm -rf /")  # Command injection
    with pytest.raises(VPNError, match="Invalid characters in environment variable"):
        validate_env_var("TEST_VAR", "value | grep secret")  # Pipe injection
