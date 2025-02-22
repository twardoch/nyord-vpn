"""Tests for configuration handling."""

import os
import pytest
from pathlib import Path
from pydantic import SecretStr

from nyord_vpn.core.exceptions import VPNConfigError
from nyord_vpn.core.config import VPNConfig, load_config


def test_config_defaults():
    """Test default configuration values."""
    config = VPNConfig(username="test", password="test")
    assert config.username == "test"
    assert isinstance(config.password, SecretStr)
    assert config.password.get_secret_value() == "test"
    assert config.default_country == "United States"
    assert config.retry_attempts == 3
    assert config.use_legacy_fallback is True
    assert config.config_dir == Path.home() / ".config" / "nyord-vpn"
    assert config.api_timeout == 30


def test_config_custom_values():
    """Test custom configuration values."""
    config = VPNConfig(
        username="custom_user",
        password="custom_pass",
        default_country="Norway",
        retry_attempts=5,
        use_legacy_fallback=False,
        config_dir="/custom/config/dir",
        api_timeout=60,
    )
    assert config.username == "custom_user"
    assert config.password.get_secret_value() == "custom_pass"
    assert config.default_country == "Norway"
    assert config.retry_attempts == 5
    assert config.use_legacy_fallback is False
    assert config.config_dir == Path("/custom/config/dir")
    assert config.api_timeout == 60


def test_config_validation():
    """Test configuration validation."""
    # Test missing required fields
    with pytest.raises(VPNConfigError, match="Field required"):
        VPNConfig()

    # Test invalid retry attempts
    with pytest.raises(VPNConfigError, match="ensure this value is greater than 0"):
        VPNConfig(username="test", password="test", retry_attempts=0)

    # Test invalid timeout
    with pytest.raises(VPNConfigError, match="ensure this value is greater than 0"):
        VPNConfig(username="test", password="test", api_timeout=0)


def test_config_directory_creation(temp_dir):
    """Test configuration directory creation."""
    config = VPNConfig(
        username="test",
        password="test",
        config_dir=temp_dir / "config",
    )
    assert config.config_dir.exists()
    assert config.config_dir.is_dir()
    assert oct(config.config_dir.stat().st_mode)[-3:] == "700"


def test_config_from_file(temp_dir):
    """Test loading configuration from file."""
    # Create config file
    config_file = temp_dir / "config.toml"
    config_file.write_text(
        """
        username = "file_user"
        password = "file_pass"
        default_country = "Sweden"
        retry_attempts = 4
        """
    )

    # Test loading from file
    config = load_config(config_file)
    assert config.username == "file_user"
    assert config.password.get_secret_value() == "file_pass"
    assert config.default_country == "Sweden"
    assert config.retry_attempts == 4

    # Test invalid file
    invalid_file = temp_dir / "invalid.toml"
    invalid_file.write_text("invalid = toml [ content")
    with pytest.raises(VPNConfigError, match="Failed to load configuration"):
        load_config(invalid_file)

    # Test non-existent file
    with pytest.raises(VPNConfigError, match="Failed to load configuration"):
        load_config(temp_dir / "nonexistent.toml")


def test_config_from_env(monkeypatch):
    """Test loading configuration from environment variables."""
    # Set environment variables
    monkeypatch.setenv("NORDVPN_USERNAME", "env_user")
    monkeypatch.setenv("NORDVPN_PASSWORD", "env_pass")
    monkeypatch.setenv("NORDVPN_DEFAULT_COUNTRY", "Denmark")
    monkeypatch.setenv("NORDVPN_RETRY_ATTEMPTS", "6")
    monkeypatch.setenv("NORDVPN_USE_LEGACY_FALLBACK", "false")

    # Test loading from environment
    config = load_config()
    assert config.username == "env_user"
    assert config.password.get_secret_value() == "env_pass"
    assert config.default_country == "Denmark"
    assert config.retry_attempts == 6
    assert config.use_legacy_fallback is False

    # Test invalid environment values
    monkeypatch.setenv("NORDVPN_RETRY_ATTEMPTS", "invalid")
    with pytest.raises(VPNConfigError, match="Failed to load configuration"):
        load_config()


def test_config_precedence(temp_dir, monkeypatch):
    """Test configuration precedence (file > env > defaults)."""
    # Create config file
    config_file = temp_dir / "config.toml"
    config_file.write_text(
        """
        username = "file_user"
        password = "file_pass"
        default_country = "Sweden"
        """
    )

    # Set environment variables
    monkeypatch.setenv("NORDVPN_USERNAME", "env_user")
    monkeypatch.setenv("NORDVPN_DEFAULT_COUNTRY", "Denmark")
    monkeypatch.setenv("NORDVPN_RETRY_ATTEMPTS", "6")

    # Test precedence
    config = load_config(config_file)
    assert config.username == "file_user"  # From file
    assert config.password.get_secret_value() == "file_pass"  # From file
    assert config.default_country == "Sweden"  # From file
    assert config.retry_attempts == 6  # From env
    assert config.use_legacy_fallback is True  # Default value
