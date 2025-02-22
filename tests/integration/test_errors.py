"""Integration tests for error handling."""

import asyncio
import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.exceptions import VPNError, VPNConnectionError, VPNConfigError


@pytest.mark.integration
@pytest.mark.asyncio
async def test_network_errors(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test handling of network-related errors."""
    # Test connection timeout
    mock_aiohttp_session.get.side_effect = asyncio.TimeoutError()
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test connection refused
    mock_aiohttp_session.get.side_effect = ConnectionRefusedError()
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test DNS resolution error
    mock_aiohttp_session.get.side_effect = Exception("DNS resolution failed")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test SSL error
    mock_aiohttp_session.get.side_effect = Exception("SSL verification failed")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_subprocess_errors(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test handling of subprocess-related errors."""
    # Test command not found
    mock_subprocess.side_effect = FileNotFoundError("Command not found")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test permission denied
    mock_subprocess.side_effect = PermissionError("Permission denied")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test command timeout
    mock_subprocess.side_effect = TimeoutError("Command timed out")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()

    # Test command failure
    mock_subprocess.return_value.returncode = 1
    mock_subprocess.return_value.communicate.return_value = (b"", b"Command failed")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        async with mock_client as client:
            await client.connect()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_configuration_errors(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
    temp_dir,
):
    """Test handling of configuration-related errors."""
    # Test missing credentials
    with pytest.raises(VPNConfigError, match="Field required"):
        VPNClient()

    # Test invalid config file
    config_file = temp_dir / "invalid.toml"
    config_file.write_text("invalid = toml [ content")
    with pytest.raises(VPNConfigError, match="Failed to load configuration"):
        VPNClient(config_file=config_file)

    # Test non-existent config file
    with pytest.raises(VPNConfigError, match="Failed to load configuration"):
        VPNClient(config_file=temp_dir / "nonexistent.toml")

    # Test invalid config directory
    config_file = temp_dir / "config.toml"
    config_file.write_text(
        """
        username = "test_user"
        password = "test_pass"
        config_dir = "/nonexistent/dir"
        """
    )
    with pytest.raises(VPNConfigError, match="Failed to setup config directory"):
        VPNClient(config_file=config_file)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_api_errors(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test handling of API-related errors."""
    # Test invalid country
    mock_pycountry.countries.get.return_value = None
    mock_pycountry.countries.search_fuzzy.return_value = []
    with pytest.raises(VPNError, match="Country not found"):
        async with mock_client as client:
            await client.connect("Invalid Country")

    # Test API authentication error
    mock_client.primary_api.connect.side_effect = VPNError("Authentication failed")
    mock_client.fallback_api.connect.side_effect = VPNError("Authentication failed")
    with pytest.raises(VPNConnectionError, match="Both primary and fallback failed"):
        async with mock_client as client:
            await client.connect()

    # Test API rate limit
    mock_client.primary_api.connect.side_effect = VPNError("Rate limit exceeded")
    mock_client.fallback_api.connect.side_effect = VPNError("Rate limit exceeded")
    with pytest.raises(VPNConnectionError, match="Both primary and fallback failed"):
        async with mock_client as client:
            await client.connect()

    # Test API server error
    mock_client.primary_api.connect.side_effect = VPNError("Server error")
    mock_client.fallback_api.connect.side_effect = VPNError("Server error")
    with pytest.raises(VPNConnectionError, match="Both primary and fallback failed"):
        async with mock_client as client:
            await client.connect()


@pytest.mark.integration
@pytest.mark.asyncio
async def test_error_recovery(
    mock_client,
    mock_aiohttp_session,
    mock_subprocess,
    mock_pycountry,
):
    """Test error recovery behavior."""
    # Test recovery after network error
    mock_aiohttp_session.get.side_effect = [
        asyncio.TimeoutError(),  # First attempt fails
        MagicMock(  # Second attempt succeeds
            status=200,
            json=AsyncMock(
                return_value={
                    "ip": "1.2.3.4",
                    "country": "Test Country",
                    "hostname": "test.server.com",
                }
            ),
        ),
    ]

    async with mock_client as client:
        result = await client.connect()
        assert result is True

        # Verify status
        status = await client.status()
        assert status["connected"] is True

    # Test recovery after subprocess error
    mock_subprocess.side_effect = [
        Exception("First attempt failed"),  # First attempt fails
        MagicMock(  # Second attempt succeeds
            returncode=0,
            communicate=AsyncMock(return_value=(b"Success", b"")),
        ),
    ]

    async with mock_client as client:
        result = await client.connect()
        assert result is True

        # Verify status
        status = await client.status()
        assert status["connected"] is True
