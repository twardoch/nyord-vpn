"""Tests for NjordAPI implementation."""

import pytest
from aiohttp import ClientError

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.api.njord import NjordAPI


@pytest.mark.asyncio
async def test_init(test_credentials):
    """Test NjordAPI initialization."""
    username, password = test_credentials
    api = NjordAPI(username=username, password=password.get_secret_value())
    assert isinstance(api, NjordAPI)


@pytest.mark.asyncio
async def test_get_recommended_server(mock_aiohttp_session, mock_pycountry):
    """Test server recommendation."""
    api = NjordAPI()
    server = await api.get_recommended_server("Sweden")
    assert isinstance(server, str)
    assert "test.server.com" in server


@pytest.mark.asyncio
async def test_connect(mock_aiohttp_session, mock_pycountry):
    """Test VPN connection."""
    api = NjordAPI()
    result = await api.connect("Sweden")
    assert result is True


@pytest.mark.asyncio
async def test_disconnect(mock_aiohttp_session):
    """Test VPN disconnection."""
    api = NjordAPI()
    result = await api.disconnect()
    assert result is True


@pytest.mark.asyncio
async def test_status(mock_aiohttp_session):
    """Test VPN status check."""
    api = NjordAPI()
    status = await api.status()
    assert isinstance(status, dict)
    assert status["connected"] is True
    assert status["country"] == "Test Country"
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "test.server.com"


@pytest.mark.asyncio
async def test_list_countries(mock_aiohttp_session, mock_pycountry):
    """Test country listing."""
    api = NjordAPI()
    countries = await api.list_countries()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert all(isinstance(c, str) for c in countries)


@pytest.mark.asyncio
async def test_error_handling(mock_aiohttp_session):
    """Test error handling."""
    api = NjordAPI()

    # Test connection error
    mock_aiohttp_session.get.side_effect = ClientError()
    with pytest.raises(VPNError, match="Failed to get server recommendations"):
        await api.get_recommended_server("Sweden")

    # Test invalid country
    with pytest.raises(VPNError, match="Invalid country"):
        await api.get_recommended_server("Invalid Country")

    # Test no servers found
    mock_aiohttp_session.get.side_effect = None
    mock_aiohttp_session.get.return_value.__aenter__.return_value.json.return_value = []
    with pytest.raises(VPNError, match="No servers found"):
        await api.get_recommended_server("Sweden")
