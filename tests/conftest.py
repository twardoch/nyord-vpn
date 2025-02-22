"""Test fixtures for nyord-vpn."""

import os
from pathlib import Path
from collections.abc import AsyncGenerator, Generator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import pytest_asyncio
from pydantic import SecretStr

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.config import VPNConfig

# Test credentials - load from environment variables
TEST_USERNAME = os.getenv("TEST_NORDVPN_USERNAME", "test_user")
TEST_PASSWORD = SecretStr(os.getenv("TEST_NORDVPN_PASSWORD", "test_password"))


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for tests."""
    return tmp_path


@pytest.fixture
def test_credentials() -> tuple[str, SecretStr]:
    """Get test credentials from environment."""
    return TEST_USERNAME, TEST_PASSWORD


@pytest.fixture
def test_config(test_credentials: tuple[str, SecretStr]) -> VPNConfig:
    """Create a test configuration."""
    username, password = test_credentials
    return VPNConfig(
        username=username,
        password=password.get_secret_value(),
        default_country="Test Country",
        retry_attempts=3,
        use_legacy_fallback=True,
        api_timeout=10,
    )


@pytest_asyncio.fixture
async def mock_client(test_config: VPNConfig) -> AsyncGenerator[VPNClient, None]:
    """Create a mock VPN client."""
    with (
        patch("nyord_vpn.api.njord.NjordAPI") as mock_njord,
        patch("nyord_vpn.api.legacy.LegacyAPI") as mock_legacy,
    ):
        # Setup mock APIs
        mock_njord.return_value.connect = AsyncMock(return_value=True)
        mock_njord.return_value.disconnect = AsyncMock(return_value=True)
        mock_njord.return_value.status = AsyncMock(
            return_value={
                "connected": True,
                "country": "Test Country",
                "ip": "1.2.3.4",
                "server": "test.server.com",
            }
        )
        mock_njord.return_value.list_countries = AsyncMock(
            return_value=["Country 1", "Country 2"]
        )

        # Setup legacy API similarly
        mock_legacy.return_value.connect = AsyncMock(return_value=True)
        mock_legacy.return_value.disconnect = AsyncMock(return_value=True)
        mock_legacy.return_value.status = AsyncMock(
            return_value={
                "connected": True,
                "country": "Test Country",
                "ip": "1.2.3.4",
                "server": "test.server.com",
            }
        )
        mock_legacy.return_value.list_countries = AsyncMock(
            return_value=["Country 1", "Country 2"]
        )

        # Create client with test config
        client = VPNClient(
            username=test_config.username,
            password=test_config.password.get_secret_value(),
        )
        yield client


@pytest.fixture
def mock_aiohttp_session() -> Generator[MagicMock, None, None]:
    """Mock aiohttp ClientSession."""
    with patch("aiohttp.ClientSession") as mock_session:
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(
            return_value={
                "ip": "1.2.3.4",
                "country": "Test Country",
                "hostname": "test.server.com",
            }
        )
        mock_session.return_value.__aenter__.return_value.get.return_value.__aenter__.return_value = mock_response
        yield mock_session.return_value


@pytest.fixture
def mock_subprocess() -> Generator[MagicMock, None, None]:
    """Mock subprocess.run."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="Success output",
            stderr="Error output",
        )
        yield mock_run


@pytest.fixture
def mock_pycountry() -> Generator[MagicMock, None, None]:
    """Mock pycountry module."""
    with patch("pycountry.countries") as mock_countries:
        mock_country = MagicMock()
        mock_country.alpha_2 = "SE"
        mock_country.name = "Sweden"
        mock_countries.get.return_value = mock_country
        mock_countries.search_fuzzy.return_value = [mock_country]
        yield mock_countries


@pytest.fixture(autouse=True)
def mock_nordvpn_command(monkeypatch, tmp_path: Path) -> Generator[Path, None, None]:
    """Mock the nordvpn command for tests."""
    # Create a mock nordvpn command
    mock_cmd = tmp_path / "nordvpn"
    mock_cmd.write_text("#!/bin/bash\nexit 0")
    mock_cmd.chmod(0o755)

    # Add the mock command to PATH
    new_path = f"{tmp_path}:{os.environ.get('PATH', '')}"
    monkeypatch.setenv("PATH", new_path)

    yield mock_cmd


@pytest.fixture(autouse=True)
def mock_env_credentials(monkeypatch):
    """Mock environment credentials for tests."""
    monkeypatch.setenv("NORDVPN_USERNAME", TEST_USERNAME)
    monkeypatch.setenv("NORDVPN_PASSWORD", TEST_PASSWORD.get_secret_value())
