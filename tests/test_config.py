"""Tests for VPN configuration handling."""

import json
from pathlib import Path

import pytest
from pydantic import SecretStr

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
    with pytest.raises(VPNConfigError):
        VPNConfig(
            username=TEST_USERNAME,
            password=TEST_PASSWORD.get_secret_value(),
            retry_attempts=0,
        )

    with pytest.raises(VPNConfigError):
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


def test_from_env(monkeypatch):
    """Test loading configuration from environment variables."""
    monkeypatch.setenv("NORDVPN_USERNAME", TEST_USERNAME)
    monkeypatch.setenv("NORDVPN_PASSWORD", TEST_PASSWORD.get_secret_value())
    monkeypatch.setenv("NORDVPN_API_TIMEOUT", "30")
    monkeypatch.setenv("NORDVPN_RETRY_ATTEMPTS", "5")

    config = VPNConfig.from_env()
    assert config.username == TEST_USERNAME
    assert config.password.get_secret_value() == TEST_PASSWORD.get_secret_value()
    assert config.api_timeout == 30
    assert config.retry_attempts == 5


def test_config_precedence(tmp_path: Path, monkeypatch):
    """Test configuration precedence (file > env > defaults)."""
    # Setup file config
    config_path = tmp_path / "config.json"
    config_data = {
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD.get_secret_value(),
        "api_timeout": 30,
    }
    config_path.write_text(json.dumps(config_data))

    # Setup env config (should be overridden by file)
    monkeypatch.setenv("NORDVPN_USERNAME", "env_user")
    monkeypatch.setenv("NORDVPN_PASSWORD", "env_pass")
    monkeypatch.setenv("NORDVPN_API_TIMEOUT", "20")

    # Load config from file
    config = VPNConfig.from_file(config_path)
    assert config.username == TEST_USERNAME  # From file
    assert (
        config.password.get_secret_value() == TEST_PASSWORD.get_secret_value()
    )  # From file
    assert config.api_timeout == 30  # From file
