"""Integration tests for error handling."""

import asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock
import json
from pathlib import Path

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.exceptions import VPNError, VPNConnectionError, VPNConfigError
from tests.conftest import TEST_PASSWORD, TEST_USERNAME


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


@pytest.mark.asyncio
async def test_invalid_credentials():
    """Test handling of invalid credentials."""
    client = VPNClient(username="invalid", password=TEST_PASSWORD.get_secret_value())
    with pytest.raises(VPNConnectionError):
        await client.connect()


@pytest.mark.asyncio
async def test_network_errors():
    """Test handling of network errors."""
    client = VPNClient(username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value())

    # Test connection with network error
    with pytest.raises(VPNConnectionError):
        await client.connect()

    # Test status check with network error
    with pytest.raises(VPNError):
        await client.status()

    # Test country listing with network error
    with pytest.raises(VPNError):
        await client.list_countries()


@pytest.mark.asyncio
async def test_timeout_handling(tmp_path: Path):
    """Test handling of timeouts."""
    # Create config with short timeout
    config_path = tmp_path / "timeout_config.json"
    config_data = {
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD.get_secret_value(),
        "api_timeout": 1,
    }
    config_path.write_text(json.dumps(config_data))

    client = VPNClient(config_file=config_path)

    # Test connection timeout
    with pytest.raises(VPNConnectionError):
        await client.connect()

    # Test status check timeout
    with pytest.raises(VPNError):
        await client.status()


@pytest.mark.asyncio
async def test_retry_behavior(tmp_path: Path):
    """Test retry behavior on failures."""
    # Create config with retry settings
    config_path = tmp_path / "retry_config.json"
    config_data = {
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD.get_secret_value(),
        "retry_attempts": 2,
    }
    config_path.write_text(json.dumps(config_data))

    client = VPNClient(config_file=config_path)

    # Test connection retries
    with pytest.raises(VPNConnectionError):
        await client.connect()

    # Test status check retries
    with pytest.raises(VPNError):
        await client.status()


@pytest.mark.asyncio
async def test_fallback_behavior():
    """Test fallback to legacy API."""
    client = VPNClient(
        username=TEST_USERNAME,
        password=TEST_PASSWORD.get_secret_value(),
        use_legacy_fallback=True,
    )

    # Test connection with fallback
    assert await client.connect() is True
    status = await client.status()
    assert status["connected"] is True

    # Cleanup
    await client.disconnect()


@pytest.mark.asyncio
async def test_invalid_country():
    """Test handling of invalid country names."""
    client = VPNClient(
        username=TEST_USERNAME, password=TEST_PASSWORD.get_secret_value()
    )

    # Test connection with invalid country
    with pytest.raises(VPNConnectionError):
        await client.connect("Invalid Country")

    # Test connection with empty country
    with pytest.raises(VPNConnectionError):
        await client.connect("")
