"""Integration tests for configuration loading."""

import os
import pytest
from pathlib import Path

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.config import VPNConfig, load_config
from nyord_vpn.core.exceptions import VPNConfigError


@pytest.mark.integration
async def test_file_loading(temp_dir):
    """Test configuration loading from file."""
    # Create config file with all options
    config_file = temp_dir / "config.toml"
    config_file.write_text(
        """
        username = "file_user"
        password = "file_pass"
        default_country = "Sweden"
        retry_attempts = 5
        use_legacy_fallback = false
        config_dir = "custom/config/dir"
        api_timeout = 60
        """
    )

    # Test loading with VPNClient
    client = VPNClient(config_file=config_file)
    assert client.config.username == "file_user"
    assert client.config.password.get_secret_value() == "file_pass"
    assert client.config.default_country == "Sweden"
    assert client.config.retry_attempts == 5
    assert client.config.use_legacy_fallback is False
    assert client.config.config_dir == Path("custom/config/dir").resolve()
    assert client.config.api_timeout == 60

    # Test loading with load_config
    config = load_config(config_file)
    assert config.username == "file_user"
    assert config.password.get_secret_value() == "file_pass"
    assert config.default_country == "Sweden"
    assert config.retry_attempts == 5
    assert config.use_legacy_fallback is False
    assert config.config_dir == Path("custom/config/dir").resolve()
    assert config.api_timeout == 60


@pytest.mark.integration
async def test_environment_loading(monkeypatch):
    """Test configuration loading from environment variables."""
    # Set environment variables
    monkeypatch.setenv("NORDVPN_USERNAME", "env_user")
    monkeypatch.setenv("NORDVPN_PASSWORD", "env_pass")
    monkeypatch.setenv("NORDVPN_DEFAULT_COUNTRY", "Norway")
    monkeypatch.setenv("NORDVPN_RETRY_ATTEMPTS", "4")
    monkeypatch.setenv("NORDVPN_USE_LEGACY_FALLBACK", "false")
    monkeypatch.setenv("NORDVPN_API_TIMEOUT", "45")

    # Test loading with VPNClient
    client = VPNClient()
    assert client.config.username == "env_user"
    assert client.config.password.get_secret_value() == "env_pass"
    assert client.config.default_country == "Norway"
    assert client.config.retry_attempts == 4
    assert client.config.use_legacy_fallback is False
    assert client.config.api_timeout == 45

    # Test loading with load_config
    config = load_config()
    assert config.username == "env_user"
    assert config.password.get_secret_value() == "env_pass"
    assert config.default_country == "Norway"
    assert config.retry_attempts == 4
    assert config.use_legacy_fallback is False
    assert config.api_timeout == 45


@pytest.mark.integration
async def test_default_values():
    """Test configuration default values."""
    # Test with minimal configuration
    config = VPNConfig(username="test", password="test")
    assert config.username == "test"
    assert config.password.get_secret_value() == "test"
    assert config.default_country == "United States"
    assert config.retry_attempts == 3
    assert config.use_legacy_fallback is True
    assert config.config_dir == Path.home() / ".config" / "nyord-vpn"
    assert config.api_timeout == 30

    # Test with VPNClient
    client = VPNClient(username="test", password="test")
    assert client.config.username == "test"
    assert client.config.password.get_secret_value() == "test"
    assert client.config.default_country == "United States"
    assert client.config.retry_attempts == 3
    assert client.config.use_legacy_fallback is True
    assert client.config.config_dir == Path.home() / ".config" / "nyord-vpn"
    assert client.config.api_timeout == 30


@pytest.mark.integration
async def test_config_precedence(temp_dir, monkeypatch):
    """Test configuration loading precedence."""
    # Create config file
    config_file = temp_dir / "config.toml"
    config_file.write_text(
        """
        username = "file_user"
        password = "file_pass"
        default_country = "Sweden"
        retry_attempts = 5
        """
    )

    # Set environment variables
    monkeypatch.setenv("NORDVPN_USERNAME", "env_user")
    monkeypatch.setenv("NORDVPN_DEFAULT_COUNTRY", "Norway")
    monkeypatch.setenv("NORDVPN_API_TIMEOUT", "45")

    # Test with VPNClient - explicit args > file > env > defaults
    client = VPNClient(
        config_file=config_file,
        username="arg_user",
        password="arg_pass",
    )
    assert client.config.username == "arg_user"  # From arg
    assert client.config.password.get_secret_value() == "arg_pass"  # From arg
    assert client.config.default_country == "Sweden"  # From file
    assert client.config.retry_attempts == 5  # From file
    assert client.config.api_timeout == 45  # From env
    assert client.config.use_legacy_fallback is True  # Default

    # Test with load_config - file > env > defaults
    config = load_config(config_file)
    assert config.username == "file_user"  # From file
    assert config.password.get_secret_value() == "file_pass"  # From file
    assert config.default_country == "Sweden"  # From file
    assert config.retry_attempts == 5  # From file
    assert config.api_timeout == 45  # From env
    assert config.use_legacy_fallback is True  # Default


@pytest.mark.integration
async def test_config_validation(temp_dir):
    """Test configuration validation."""
    # Test invalid retry attempts
    config_file = temp_dir / "invalid_retry.toml"
    config_file.write_text(
        """
        username = "test"
        password = "test"
        retry_attempts = 0
        """
    )
    with pytest.raises(VPNConfigError, match="ensure this value is greater than 0"):
        load_config(config_file)

    # Test invalid timeout
    config_file = temp_dir / "invalid_timeout.toml"
    config_file.write_text(
        """
        username = "test"
        password = "test"
        api_timeout = -1
        """
    )
    with pytest.raises(VPNConfigError, match="ensure this value is greater than 0"):
        load_config(config_file)

    # Test invalid config directory
    config_file = temp_dir / "invalid_dir.toml"
    config_file.write_text(
        """
        username = "test"
        password = "test"
        config_dir = "/nonexistent/dir"
        """
    )
    with pytest.raises(VPNConfigError, match="Failed to setup config directory"):
        load_config(config_file)

    # Test missing required fields
    config_file = temp_dir / "missing_fields.toml"
    config_file.write_text(
        """
        default_country = "Sweden"
        retry_attempts = 5
        """
    )
    with pytest.raises(VPNConfigError, match="Field required"):
        load_config(config_file)
