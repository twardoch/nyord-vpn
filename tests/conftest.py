"""Test fixtures for nyord-vpn."""

import os
from pathlib import Path
from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest
from pydantic import SecretStr

from nyord_vpn.api.njord import NjordVPNClient
from nyord_vpn.api.legacy import LegacyVPNClient
from nyord_vpn.core.client import VPNClient

# Test credentials - load from environment variables
TEST_USERNAME = os.getenv("NORD_USER", "test_user")
TEST_PASSWORD = SecretStr(os.getenv("NORD_PASSWORD", "test_password"))


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for tests."""
    return tmp_path


@pytest.fixture
def mock_client() -> Generator[VPNClient, None, None]:
    """Create a mock VPN client."""
    with (
        patch("nyord_vpn.api.njord.NjordVPNClient") as mock_njord,
        patch("nyord_vpn.api.legacy.LegacyVPNClient") as mock_legacy,
    ):
        # Setup mock APIs
        mock_njord.return_value.connect.return_value = True
        mock_njord.return_value.disconnect.return_value = True
        mock_njord.return_value.status.return_value = {
            "connected": True,
            "country": "Test Country",
            "ip": "1.2.3.4",
            "server": "test.server.com",
        }
        mock_njord.return_value.list_countries.return_value = [
            {"name": "Country 1", "code": "1"},
            {"name": "Country 2", "code": "2"},
        ]

        mock_legacy.return_value.connect.return_value = True
        mock_legacy.return_value.disconnect.return_value = True
        mock_legacy.return_value.status.return_value = {
            "connected": True,
            "country": "Test Country",
            "ip": "1.2.3.4",
            "server": "test.server.com",
        }
        mock_legacy.return_value.list_countries.return_value = [
            {"name": "Country 1", "code": "1"},
            {"name": "Country 2", "code": "2"},
        ]

        # Create client with test credentials
        client = VPNClient()
        yield client


@pytest.fixture
def mock_subprocess() -> Generator[MagicMock, None, None]:
    """Mock subprocess calls."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = b"Connected to test.server.com"
        yield mock_run


@pytest.fixture(autouse=True)
def mock_nordvpn_command(monkeypatch, tmp_path: Path) -> Generator[Path, None, None]:
    """Mock nordvpn command."""
    nordvpn_path = tmp_path / "nordvpn"
    nordvpn_path.write_text("#!/bin/sh\nexit 0\n")
    nordvpn_path.chmod(0o755)
    monkeypatch.setenv("PATH", str(tmp_path))
    yield nordvpn_path


@pytest.fixture(autouse=True)
def mock_env_credentials(monkeypatch):
    """Mock environment credentials for tests."""
    monkeypatch.setenv("NORD_USER", TEST_USERNAME)
    monkeypatch.setenv("NORD_PASSWORD", TEST_PASSWORD.get_secret_value())
