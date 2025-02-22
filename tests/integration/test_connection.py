"""Integration tests for VPN connection handling."""

import asyncio
import pytest
from unittest.mock import AsyncMock

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.exceptions import VPNError, VPNConnectionError
from tests.conftest import TEST_PASSWORD, TEST_USERNAME


@pytest.mark.asyncio
async def test_connect_disconnect():
    """Test basic connection and disconnection."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Test connection
    assert await client.connect() is True
    status = await client.status()
    assert status["connected"] is True
    assert status["country"] == "Test Country"
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "test.server.com"

    # Test disconnection
    assert await client.disconnect() is True
    status = await client.status()
    assert status["connected"] is False


@pytest.mark.asyncio
async def test_connect_with_country():
    """Test connection to specific country."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Test connection to specific country
    assert await client.connect("Norway") is True
    status = await client.status()
    assert status["connected"] is True
    assert status["country"] == "Norway"

    # Cleanup
    await client.disconnect()


@pytest.mark.asyncio
async def test_connection_failure():
    """Test handling of connection failures."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Test invalid country
    with pytest.raises(VPNConnectionError):
        await client.connect("Invalid Country")

    # Test connection timeout
    with pytest.raises(VPNConnectionError):
        await client.connect("Timeout Country")


@pytest.mark.asyncio
async def test_disconnect_failure():
    """Test handling of disconnection failures."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Connect first
    await client.connect()

    # Test disconnection failure
    with pytest.raises(VPNConnectionError):
        await client.disconnect()


@pytest.mark.asyncio
async def test_status_check():
    """Test VPN status checking."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Test initial status
    status = await client.status()
    assert status["connected"] is False

    # Test status after connection
    await client.connect()
    status = await client.status()
    assert status["connected"] is True
    assert "country" in status
    assert "ip" in status
    assert "server" in status

    # Cleanup
    await client.disconnect()


@pytest.mark.asyncio
async def test_country_listing():
    """Test listing available countries."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Test country listing
    countries = await client.list_countries()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert all(isinstance(c, str) for c in countries)


@pytest.mark.asyncio
async def test_context_manager():
    """Test VPN client as context manager."""
    async with VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    ) as client:
        # Test connection inside context
        assert await client.connect() is True
        status = await client.status()
        assert status["connected"] is True

    # Test automatic disconnection after context
    status = await client.status()
    assert status["connected"] is False


@pytest.mark.integration
@pytest.mark.asyncio
async def test_successful_connection(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test successful VPN connection flow."""
    # Test connection with default country
    async with mock_client as client:
        result = await client.connect()
        assert result is True

        # Verify status
        status = await client.status()
        assert status["connected"] is True
        assert status["country"] == "Test Country"
        assert status["ip"] == "1.2.3.4"
        assert status["server"] == "test.server.com"

        # Test disconnection
        result = await client.disconnect()
        assert result is True

        # Verify disconnected status
        status = await client.status()
        assert status["connected"] is False

    # Test connection with specific country
    async with mock_client as client:
        result = await client.connect("Norway")
        assert result is True

        # Verify status
        status = await client.status()
        assert status["connected"] is True
        assert status["country"] == "Test Country"
        assert status["ip"] == "1.2.3.4"
        assert status["server"] == "test.server.com"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_connection_failure(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test VPN connection failure handling."""
    # Test primary API failure
    mock_client.primary_api.connect.side_effect = VPNError("Primary API failed")
    mock_client.fallback_api.connect.side_effect = VPNError("Fallback API failed")

    with pytest.raises(VPNConnectionError, match="Both primary and fallback failed"):
        async with mock_client as client:
            await client.connect()

    # Test network error
    mock_aiohttp_session.get.side_effect = asyncio.TimeoutError()
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test subprocess error
    mock_subprocess.side_effect = Exception("Subprocess error")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_fallback_behavior(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test API fallback behavior."""
    # Make primary API fail
    mock_client.primary_api.connect.side_effect = VPNError("Primary API failed")
    mock_client.primary_api.status.side_effect = VPNError("Primary API failed")

    # Test successful fallback
    async with mock_client as client:
        result = await client.connect()
        assert result is True

        # Verify status using fallback
        status = await client.status()
        assert status["connected"] is True
        assert status["country"] == "Test Country"
        assert status["ip"] == "1.2.3.4"
        assert status["server"] == "test.server.com"

    # Test fallback with specific country
    async with mock_client as client:
        result = await client.connect("Sweden")
        assert result is True

        # Verify status using fallback
        status = await client.status()
        assert status["connected"] is True
        assert status["country"] == "Test Country"
        assert status["ip"] == "1.2.3.4"
        assert status["server"] == "test.server.com"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_connection_retry(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test connection retry behavior."""
    # Make first attempt fail, second succeed
    attempts = 0

    async def mock_connect(*args, **kwargs):
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            msg = "First attempt failed"
            raise VPNError(msg)
        return True

    mock_client.primary_api.connect = AsyncMock(side_effect=mock_connect)

    # Test successful retry
    async with mock_client as client:
        result = await client.connect()
        assert result is True
        assert attempts == 2  # Should have retried once

    # Test max retries exceeded
    attempts = 0
    mock_client.primary_api.connect = AsyncMock(
        side_effect=VPNError("All attempts failed")
    )
    mock_client.fallback_api.connect = AsyncMock(
        side_effect=VPNError("All attempts failed")
    )

    with pytest.raises(VPNConnectionError, match="Both primary and fallback failed"):
        async with mock_client as client:
            await client.connect()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_connection_cleanup(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
    temp_dir,
):
    """Test connection resource cleanup."""
    # Create test files
    config_file = temp_dir / "config.toml"
    config_file.write_text(
        """
        username = "test_user"
        password = "test_pass"
        default_country = "Test Country"
        """
    )

    # Test cleanup after successful connection
    async with VPNClient(config_file=config_file) as client:
        await client.connect()
        status = await client.status()
        assert status["connected"] is True

    # Verify cleanup
    status = await client.status()
    assert status["connected"] is False
    assert status["server"] == ""

    # Test cleanup after error
    mock_client.primary_api.connect.side_effect = VPNError("Connection failed")
    mock_client.fallback_api.connect.side_effect = VPNError("Connection failed")

    try:
        async with VPNClient(config_file=config_file) as client:
            await client.connect()
    except VPNConnectionError:
        pass

    # Verify cleanup
    status = await client.status()
    assert status["connected"] is False
    assert status["server"] == ""
