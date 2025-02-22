"""Integration tests for VPN connection flow."""

import asyncio
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.exceptions import VPNError, VPNConnectionError


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
            raise VPNError("First attempt failed")
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
