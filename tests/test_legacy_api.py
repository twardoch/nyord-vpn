"""Tests for LegacyAPI implementation."""

import pytest
from pathlib import Path
from aiohttp import ClientError

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.api.legacy import LegacyAPI
from tests.conftest import TEST_PASSWORD, TEST_USERNAME


@pytest.mark.asyncio
async def test_init():
    """Test LegacyAPI initialization."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    assert api.username == TEST_USERNAME
    assert isinstance(api.password, str)
    assert api.password == TEST_PASSWORD.get_secret_value()


@pytest.mark.asyncio
async def test_get_servers(mock_aiohttp_session):
    """Test server list retrieval."""
    api = LegacyAPI(username="test", password="test")

    # Test successful server list
    servers = await api._get_servers("US")
    assert isinstance(servers, list)
    assert len(servers) > 0
    assert all(isinstance(s, dict) for s in servers)
    assert all("name" in s and "id" in s for s in servers)

    # Mock error response
    mock_aiohttp_session.get.side_effect = Exception("Failed to get servers")
    with pytest.raises(VPNError, match="Failed to get server list"):
        await api._get_servers("US")


@pytest.mark.asyncio
async def test_connect_success(mock_session):
    """Test successful connection."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    assert await api.connect() is True


@pytest.mark.asyncio
async def test_connect_failure(mock_session_error):
    """Test connection failure."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    with pytest.raises(ClientError):
        await api.connect()


@pytest.mark.asyncio
async def test_disconnect_success(mock_session):
    """Test successful disconnection."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    assert await api.disconnect() is True


@pytest.mark.asyncio
async def test_status_connected(mock_session):
    """Test status when connected."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    status = await api.status()
    assert status["connected"] is True
    assert status["country"] == "Test Country"
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "test.server.com"


@pytest.mark.asyncio
async def test_list_countries(mock_session):
    """Test listing available countries."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    countries = await api.list_countries()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert all(isinstance(c, str) for c in countries)


@pytest.mark.asyncio
async def test_get_credentials():
    """Test retrieving credentials."""
    api = LegacyAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    username, password = await api.get_credentials()
    assert username == TEST_USERNAME
    assert password == TEST_PASSWORD.get_secret_value()
