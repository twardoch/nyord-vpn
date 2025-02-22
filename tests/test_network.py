"""Tests for network utilities."""

import asyncio
import pytest
import aiohttp
from unittest.mock import AsyncMock, MagicMock

from nyord_vpn.core.exceptions import VPNError, VPNConnectionError
from nyord_vpn.utils.network import get_public_ip, wait_for_connection


@pytest.mark.asyncio
async def test_get_public_ip(mock_aiohttp_session):
    """Test public IP retrieval."""
    # Test successful IP info retrieval
    ip_info = await get_public_ip()
    assert isinstance(ip_info, dict)
    assert "ip" in ip_info
    assert "country" in ip_info
    assert "hostname" in ip_info

    # Test all services failing
    mock_aiohttp_session.get.side_effect = aiohttp.ClientError()
    with pytest.raises(VPNError, match="All IP info services failed"):
        await get_public_ip()

    # Test timeout
    mock_aiohttp_session.get.side_effect = asyncio.TimeoutError()
    with pytest.raises(VPNError, match="All IP info services failed"):
        await get_public_ip()

    # Test HTTP error
    mock_response = AsyncMock()
    mock_response.raise_for_status.side_effect = aiohttp.ClientResponseError(
        request_info=MagicMock(),
        history=(),
        status=500,
    )
    mock_aiohttp_session.get.return_value.__aenter__.return_value = mock_response
    with pytest.raises(VPNError, match="All IP info services failed"):
        await get_public_ip()


@pytest.mark.asyncio
async def test_wait_for_connection(mocker):
    """Test connection waiting."""
    # Mock get_public_ip
    mock_get_ip = mocker.patch(
        "nyord_vpn.utils.network.get_public_ip",
        new_callable=AsyncMock,
    )

    # Test successful connection
    mock_get_ip.return_value = {
        "hostname": "test.nordvpn.com",
        "ip": "1.2.3.4",
    }
    ip_info = await wait_for_connection("test.server.com", timeout=5)
    assert ip_info["hostname"] == "test.nordvpn.com"
    assert ip_info["ip"] == "1.2.3.4"

    # Test connection timeout
    mock_get_ip.return_value = {"hostname": "not.nordvpn.com"}
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        await wait_for_connection("test.server.com", timeout=1)

    # Test IP check error
    mock_get_ip.side_effect = VPNError("Failed to get IP")
    with pytest.raises(VPNConnectionError, match="Failed to connect"):
        await wait_for_connection("test.server.com", timeout=1)
