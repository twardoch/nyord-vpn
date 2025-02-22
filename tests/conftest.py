"""Test fixtures for nyord-vpn."""

import asyncio
from pathlib import Path
from typing import Any, AsyncGenerator, Generator
from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest
import pytest_asyncio

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.config import VPNConfig
from nyord_vpn.core.exceptions import VPNError


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    """Create a temporary directory for tests."""
    return tmp_path


@pytest.fixture
def config_file(temp_dir: Path) -> Path:
    """Create a temporary config file."""
    config = temp_dir / "config.toml"
    config.write_text(
        """
        username = "test_user"
        password = "test_pass"
        default_country = "Test Country"
        """
    )
    return config


@pytest.fixture
def mock_config() -> VPNConfig:
    """Create a mock VPN configuration."""
    return VPNConfig(
        username="test_user",
        password="test_pass",
        default_country="Test Country",
    )


@pytest_asyncio.fixture
async def mock_client(mock_config: VPNConfig) -> AsyncGenerator[VPNClient, None]:
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

        client = VPNClient(
            username=mock_config.username,
            password=mock_config.password.get_secret_value(),
        )
        yield client


@pytest_asyncio.fixture
async def mock_aiohttp_session() -> AsyncGenerator[aiohttp.ClientSession, None]:
    """Create a mock aiohttp session."""
    async with aiohttp.ClientSession() as session:
        with patch.object(session, "get") as mock_get:
            mock_response = MagicMock()
            mock_response.status = 200
            mock_response.json = AsyncMock(
                return_value={
                    "ip": "1.2.3.4",
                    "country": "Test Country",
                    "hostname": "test.server.com",
                }
            )
            mock_get.return_value.__aenter__.return_value = mock_response
            yield session


@pytest.fixture
def mock_subprocess() -> Generator[MagicMock, None, None]:
    """Create a mock subprocess."""
    with patch("asyncio.create_subprocess_exec") as mock_exec:
        process = AsyncMock()
        process.returncode = 0
        process.communicate = AsyncMock(
            return_value=(b"Success output", b"Error output")
        )
        mock_exec.return_value = process
        yield mock_exec


@pytest.fixture
def mock_shutil() -> Generator[MagicMock, None, None]:
    """Create a mock shutil."""
    with patch("shutil.which") as mock_which:
        mock_which.return_value = "/usr/local/bin/nordvpn"
        yield mock_which


@pytest.fixture
def mock_secrets() -> Generator[MagicMock, None, None]:
    """Create a mock secrets module."""
    with patch("secrets.randbelow") as mock_randbelow:
        mock_randbelow.return_value = 0
        yield mock_randbelow


@pytest.fixture
def mock_pycountry() -> Generator[MagicMock, None, None]:
    """Create a mock pycountry module."""
    with patch("pycountry.countries") as mock_countries:
        mock_country = MagicMock()
        mock_country.alpha_2 = "US"
        mock_country.name = "United States"
        mock_countries.get.return_value = mock_country
        mock_countries.search_fuzzy.return_value = [mock_country]
        yield mock_countries
