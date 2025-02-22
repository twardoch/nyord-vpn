"""Tests for LegacyAPI implementation."""

import pytest
from pathlib import Path

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.api.legacy import LegacyAPI


@pytest.mark.asyncio
async def test_init(mock_shutil):
    """Test API initialization."""
    # Test successful initialization
    api = LegacyAPI(username="test", password="test")
    assert api.username == "test"
    assert api.password == "test"
    assert api.nordvpn_path == Path("/usr/local/bin/nordvpn").resolve()

    # Test nordvpn not found
    mock_shutil.return_value = None
    with pytest.raises(VPNError, match="nordvpn command not found"):
        LegacyAPI(username="test", password="test")


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
async def test_connect(mock_subprocess):
    """Test VPN connection."""
    api = LegacyAPI(username="test", password="test")

    # Test successful connection without country
    result = await api.connect()
    assert result is True
    mock_subprocess.assert_called_once_with(
        str(api.nordvpn_path),
        "connect",
        stdout=mock_subprocess.return_value.stdout,
        stderr=mock_subprocess.return_value.stderr,
    )

    # Test successful connection with country
    mock_subprocess.reset_mock()
    result = await api.connect("United States")
    assert result is True
    mock_subprocess.assert_called_once()
    assert "United States" in mock_subprocess.call_args[0]

    # Test invalid country name
    with pytest.raises(VPNError, match="Invalid country name"):
        await api.connect("")

    # Test connection failure
    mock_subprocess.return_value.returncode = 1
    mock_subprocess.return_value.communicate.return_value = (b"", b"Connection failed")
    with pytest.raises(VPNError, match="Failed to connect"):
        await api.connect()

    # Test connection timeout
    mock_subprocess.return_value.communicate.side_effect = TimeoutError()
    with pytest.raises(VPNError, match="Connection timed out"):
        await api.connect()


@pytest.mark.asyncio
async def test_disconnect(mock_subprocess):
    """Test VPN disconnection."""
    api = LegacyAPI(username="test", password="test")

    # Test successful disconnection
    result = await api.disconnect()
    assert result is True
    mock_subprocess.assert_called_once_with(
        str(api.nordvpn_path),
        "disconnect",
        stdout=mock_subprocess.return_value.stdout,
        stderr=mock_subprocess.return_value.stderr,
    )

    # Test disconnection failure
    mock_subprocess.return_value.returncode = 1
    mock_subprocess.return_value.communicate.return_value = (b"", b"Disconnect failed")
    with pytest.raises(VPNError, match="Failed to disconnect"):
        await api.disconnect()

    # Test disconnection timeout
    mock_subprocess.return_value.communicate.side_effect = TimeoutError()
    with pytest.raises(VPNError, match="Disconnect timed out"):
        await api.disconnect()


@pytest.mark.asyncio
async def test_status(mock_subprocess, mock_aiohttp_session):
    """Test VPN status check."""
    api = LegacyAPI(username="test", password="test")

    # Test successful status check
    status = await api.status()
    assert isinstance(status, dict)
    assert "ip" in status
    assert "country" in status
    assert "status" in status
    mock_subprocess.assert_called_once_with(
        str(api.nordvpn_path),
        "status",
        stdout=mock_subprocess.return_value.stdout,
        stderr=mock_subprocess.return_value.stderr,
    )

    # Test status command failure
    mock_subprocess.return_value.returncode = 1
    mock_subprocess.return_value.communicate.return_value = (
        b"",
        b"Status check failed",
    )
    with pytest.raises(VPNError, match="Failed to get status"):
        await api.status()

    # Test IP info failure
    mock_aiohttp_session.get.side_effect = Exception("Failed to get IP info")
    with pytest.raises(VPNError, match="Failed to get status"):
        await api.status()


@pytest.mark.asyncio
async def test_list_countries(mock_aiohttp_session):
    """Test country listing."""
    api = LegacyAPI(username="test", password="test")

    # Test successful country listing
    countries = await api.list_countries()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert all(isinstance(c, str) for c in countries)

    # Test listing failure
    mock_aiohttp_session.get.side_effect = Exception("Failed to get countries")
    with pytest.raises(VPNError, match="Failed to get country list"):
        await api.list_countries()


@pytest.mark.asyncio
async def test_get_credentials():
    """Test credential retrieval."""
    api = LegacyAPI(username="test_user", password="test_pass")
    username, password = await api.get_credentials()
    assert username == "test_user"
    assert password == "test_pass"
