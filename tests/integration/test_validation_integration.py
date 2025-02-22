"""Integration tests for validation utilities."""

import pytest
from pathlib import Path

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.api.legacy import LegacyAPI
from nyord_vpn.api.njord import NjordAPI
from nyord_vpn.utils.validation import (
    validate_command,
    validate_env_var,
)


@pytest.mark.integration
async def test_legacy_api_validation(test_username, test_password):
    """Test validation in LegacyAPI."""
    # Test valid credentials
    api = LegacyAPI(test_username, test_password)
    assert api.username == test_username
    assert api.password == test_password

    # Test invalid credentials
    with pytest.raises(VPNError, match="Username must be a non-empty string"):
        LegacyAPI("", test_password)
    with pytest.raises(VPNError, match="Password must be a non-empty string"):
        LegacyAPI(test_username, "")

    # Test country validation in connect
    with pytest.raises(VPNError, match="Country must be a non-empty string"):
        await api.connect("")
    with pytest.raises(VPNError, match="Invalid country name format"):
        await api.connect("!@#$%^")

    # Test hostname validation in _get_servers
    with pytest.raises(VPNError, match="Invalid country name format"):
        await api._get_servers("!@#$%^")


@pytest.mark.integration
async def test_njord_api_validation(test_username, test_password):
    """Test validation in NjordAPI."""
    # Test valid credentials
    api = NjordAPI(test_username, test_password)
    username, password = await api.get_credentials()
    assert username == test_username
    assert password == test_password

    # Test invalid credentials
    with pytest.raises(VPNError, match="Username must be a non-empty string"):
        NjordAPI("", test_password)
    with pytest.raises(VPNError, match="Password must be a non-empty string"):
        NjordAPI(test_username, "")

    # Test country validation in connect
    with pytest.raises(VPNError, match="Country must be a non-empty string"):
        await api.connect("")
    with pytest.raises(VPNError, match="Invalid country name format"):
        await api.connect("!@#$%^")

    # Test hostname validation in get_recommended_server
    with pytest.raises(VPNError, match="Invalid country name format"):
        await api.get_recommended_server("!@#$%^")


@pytest.mark.integration
def test_command_validation_integration(tmp_path):
    """Test command validation with real files."""
    # Create test executable
    test_cmd = tmp_path / "test_cmd"
    test_cmd.write_text("#!/bin/bash\necho test")
    test_cmd.chmod(0o755)  # rwxr-xr-x

    # Test with LegacyAPI
    api = LegacyAPI("test_user", "test_pass")
    assert isinstance(api.nordvpn_path, Path)
    assert api.nordvpn_path.is_file()
    assert api.nordvpn_path.stat().st_mode & 0o111  # Check executable

    # Test with unsafe file
    unsafe_cmd = tmp_path / "unsafe_cmd"
    unsafe_cmd.write_text("#!/bin/bash\necho test")
    unsafe_cmd.chmod(0o777)  # rwxrwxrwx

    with pytest.raises(VPNError, match="Unsafe permissions"):
        validate_command(unsafe_cmd)


@pytest.mark.integration
def test_env_var_validation_integration():
    """Test environment variable validation with real env vars."""
    # Test with real environment variables
    path = validate_env_var("PATH", "/usr/local/bin:/usr/bin")
    assert path == "/usr/local/bin:/usr/bin"

    lang = validate_env_var("LANG", "en_US.UTF-8")
    assert lang == "en_US.UTF-8"

    # Test with potentially dangerous values
    with pytest.raises(VPNError, match="Invalid characters in environment variable"):
        validate_env_var("TEST_VAR", "$(id)")  # Command substitution

    with pytest.raises(VPNError, match="Invalid characters in environment variable"):
        validate_env_var("TEST_VAR", "`whoami`")  # Backtick substitution

    with pytest.raises(VPNError, match="Invalid characters in environment variable"):
        validate_env_var("TEST_VAR", "value; cat /etc/passwd")  # Command chaining
