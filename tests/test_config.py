"""Tests for VPN configuration handling."""

import json
from pathlib import Path

import pytest
from pydantic import SecretStr, ValidationError

from nyord_vpn.core.config import VPNConfig
from nyord_vpn.core.exceptions import VPNConfigError
from tests.conftest import TEST_PASSWORD, TEST_USERNAME


def test_basic_config():
    """Test basic configuration initialization."""
    config = VPNConfig(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )
    assert config.username == TEST_USERNAME
    assert isinstance(config.password, SecretStr)
    assert config.password.get_secret_value() == TEST_PASSWORD.get_secret_value()


def test_custom_config():
    """Test configuration with custom values."""
    config = VPNConfig(
        username=TEST_USERNAME,
        password=TEST_PASSWORD.get_secret_value(),
        api_timeout=30,
        retry_attempts=5,
        default_country="Norway",
    )
    assert config.username == TEST_USERNAME
    assert config.password.get_secret_value() == TEST_PASSWORD.get_secret_value()
    assert config.api_timeout == 30
    assert config.retry_attempts == 5
    assert config.default_country == "Norway"


def test_invalid_config():
    """Test configuration validation."""
    with pytest.raises(ValidationError, match="ensure this value is greater than 0"):
        VPNConfig(
            username=TEST_USERNAME,
            password=TEST_PASSWORD.get_secret_value(),
            retry_attempts=0,
        )

    with pytest.raises(ValidationError, match="ensure this value is greater than 0"):
        VPNConfig(
            username=TEST_USERNAME,
            password=TEST_PASSWORD.get_secret_value(),
            api_timeout=0,
        )


def test_from_file(tmp_path: Path):
    """Test loading configuration from file."""
    config_path = tmp_path / "config.json"
    config_data = {
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD.get_secret_value(),
        "api_timeout": 30,
        "retry_attempts": 5,
    }
    config_path.write_text(json.dumps(config_data))

    config = VPNConfig.from_file(config_path)
    assert config.username == TEST_USERNAME
    assert config.password.get_secret_value() == TEST_PASSWORD.get_secret_value()
    assert config.api_timeout == 30
    assert config.retry_attempts == 5


def test_from_env():
    """Test loading configuration from environment variables."""
    config = VPNConfig.from_env()
    assert config.username == TEST_USERNAME
    assert config.password.get_secret_value() == TEST_PASSWORD.get_secret_value()


def test_config_precedence(tmp_path: Path):
    """Test configuration precedence (file > env)."""
    # Create config file
    config_path = tmp_path / "config.json"
    config_data = {
        "username": "file_user",
        "password": "file_pass",
        "api_timeout": 30,
    }
    config_path.write_text(json.dumps(config_data))

    # Test loading from file (should override env)
    config = VPNConfig.from_file(config_path)
    assert config.username == "file_user"
    assert config.password.get_secret_value() == "file_pass"
    assert config.api_timeout == 30


def test_invalid_config_file(tmp_path: Path):
    """Test handling of invalid configuration files."""
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        VPNConfig.from_file(tmp_path / "nonexistent.json")

    # Test invalid JSON
    invalid_path = tmp_path / "invalid.json"
    invalid_path.write_text("invalid json content")
    with pytest.raises(json.JSONDecodeError):
        VPNConfig.from_file(invalid_path)

    # Test missing required fields
    empty_path = tmp_path / "empty.json"
    empty_path.write_text("{}")
    with pytest.raises(ValidationError):
        VPNConfig.from_file(empty_path)
