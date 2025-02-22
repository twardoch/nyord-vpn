"""Tests for NjordAPI implementation."""

import pytest
from unittest.mock import MagicMock
from aiohttp import ClientError
from njord import Client

from nyord_vpn.core.exceptions import VPNError, VPNConnectionError, VPNStatusError
from nyord_vpn.api.njord import NjordAPI
from tests.conftest import TEST_PASSWORD, TEST_USERNAME


@pytest.mark.asyncio
async def test_get_recommended_server(mock_pycountry, mock_aiohttp_session):
    """Test server recommendation functionality."""
    api = NjordAPI(username="test", password="test")

    # Test successful server recommendation
    server = await api.get_recommended_server("United States")
    assert isinstance(server, str)
    assert server == "test.server.com"

    # Test country not found
    mock_pycountry.countries.get.return_value = None
    mock_pycountry.countries.search_fuzzy.return_value = []
    with pytest.raises(VPNError, match="Country not found"):
        await api.get_recommended_server("Invalid Country")

    # Test country not supported
    mock_country = MagicMock()
    mock_country.alpha_2 = "XX"
    mock_pycountry.countries.get.return_value = mock_country
    with pytest.raises(VPNError, match="Country not supported"):
        await api.get_recommended_server("Unsupported Country")


@pytest.mark.asyncio
async def test_connect(mocker, mock_pycountry, mock_aiohttp_session):
    """Test VPN connection."""
    api = NjordAPI(username="test", password="test")

    # Mock njord client methods
    mock_connect = mocker.patch.object(api._client, "connect", return_value=True)
    mock_status = mocker.patch.object(
        api._client,
        "status",
        return_value={"server": "test.server.com"},
    )

    # Test successful connection
    result = await api.connect("United States")
    assert result is True
    assert api._connected is True
    assert api._current_server == "test.server.com"
    mock_connect.assert_called_once()
    mock_status.assert_called_once()

    # Test connection failure
    mock_connect.return_value = False
    result = await api.connect("United States")
    assert result is False
    assert api._connected is False

    # Test connection error
    mock_connect.side_effect = Exception("Connection failed")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        await api.connect("United States")


@pytest.mark.asyncio
async def test_disconnect(mocker):
    """Test VPN disconnection."""
    api = NjordAPI(username="test", password="test")
    api._connected = True
    api._current_server = "test.server.com"

    # Mock njord client disconnect
    mock_disconnect = mocker.patch.object(api._client, "disconnect")

    # Test successful disconnection
    result = await api.disconnect()
    assert result is True
    assert api._connected is False
    assert api._current_server is None
    mock_disconnect.assert_called_once()

    # Test disconnection error
    mock_disconnect.side_effect = Exception("Disconnect failed")
    with pytest.raises(VPNConnectionError, match="Failed to disconnect"):
        await api.disconnect()


@pytest.mark.asyncio
async def test_status(mocker):
    """Test VPN status check."""
    api = NjordAPI(username="test", password="test")
    api._connected = True
    api._current_server = "test.server.com"

    # Mock njord client status
    mock_status = mocker.patch.object(
        api._client,
        "status",
        return_value={
            "country": "Test Country",
            "ip": "1.2.3.4",
            "server": "test.server.com",
        },
    )

    # Test successful status check
    status = await api.status()
    assert status["connected"] is True
    assert status["country"] == "Test Country"
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "test.server.com"
    mock_status.assert_called_once()

    # Test status error
    mock_status.side_effect = Exception("Status check failed")
    with pytest.raises(VPNStatusError, match="Failed to get status"):
        await api.status()


@pytest.mark.asyncio
async def test_list_countries(mocker):
    """Test country listing."""
    api = NjordAPI(username="test", password="test")

    # Mock njord client list_countries
    mock_list = mocker.patch.object(
        api._client,
        "list_countries",
        return_value=[{"name": "Country 1"}, {"name": "Country 2"}],
    )

    # Test successful country listing
    countries = await api.list_countries()
    assert isinstance(countries, list)
    assert len(countries) == 2
    assert all(isinstance(c, str) for c in countries)
    assert "Country 1" in countries
    assert "Country 2" in countries
    mock_list.assert_called_once()

    # Test listing error
    mock_list.side_effect = Exception("Failed to get countries")
    with pytest.raises(VPNError, match="Failed to get countries"):
        await api.list_countries()


@pytest.mark.asyncio
async def test_init():
    """Test NjordAPI initialization."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    assert (
        api._client.auth_user == TEST_USERNAME
    )  # Private member access is ok in tests
    assert isinstance(api._client, Client)  # Private member access is ok in tests


@pytest.mark.asyncio
async def test_connect_success(mock_session):
    """Test successful connection."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    assert await api.connect(country="Test Country") is True


@pytest.mark.asyncio
async def test_connect_failure(mock_session_error):
    """Test connection failure."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    with pytest.raises(ClientError):
        await api.connect(country="Test Country")


@pytest.mark.asyncio
async def test_disconnect_success(mock_session):
    """Test successful disconnection."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    assert await api.disconnect() is True


@pytest.mark.asyncio
async def test_status_connected(mock_session):
    """Test status when connected."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    status = await api.status()
    assert status["connected"] is True
    assert status["country"] == "Test Country"
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "test.server.com"


@pytest.mark.asyncio
async def test_list_available_countries(mock_session):
    """Test listing available countries."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    countries = await api.list_countries()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert all(isinstance(c, str) for c in countries)


@pytest.mark.asyncio
async def test_get_credentials():
    """Test retrieving credentials."""
    api = NjordAPI(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())
    username, password = await api.get_credentials()
    assert username == TEST_USERNAME
    assert password == TEST_PASSWORD.get_secret_value()
