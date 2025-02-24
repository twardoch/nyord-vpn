#!/usr/bin/env -S uv run -s
# /// script
# dependencies = ["pytest"]
# ///
# this_file: tests/test_server_manager.py

"""Tests for server manager functionality."""

import pytest
from unittest.mock import MagicMock

from nyord_vpn.network.server import ServerManager
from nyord_vpn.core.api import NordVPNAPIClient


@pytest.fixture
def mock_api_client():
    """Create a mock API client."""
    client = MagicMock(spec=NordVPNAPIClient)
    client.verbose = True
    client.logger = MagicMock()
    return client


@pytest.fixture
def server_manager(mock_api_client):
    """Create a server manager instance."""
    return ServerManager(mock_api_client)


def test_openvpn_tcp_validation(server_manager):
    """Test OpenVPN TCP technology validation."""
    # Test regular OpenVPN TCP
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 5, "name": "OpenVPN TCP", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is True

    # Test OpenVPN TCP Dedicated
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is True

    # Test server without OpenVPN TCP
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 3, "name": "OpenVPN UDP", "status": "online"},
            {"id": 35, "name": "Wireguard", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is False

    # Test server with invalid technology format
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 5},  # Missing name
            {"name": "OpenVPN TCP"},  # Missing id
            None,  # Invalid technology
        ],
    }
    assert server_manager._is_valid_server(server) is False

    # Test server with empty technologies
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [],
    }
    assert server_manager._is_valid_server(server) is False

    # Test server with invalid hostname
    server = {
        "hostname": "test.example.com",  # Not a nordvpn.com domain
        "status": "online",
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 5, "name": "OpenVPN TCP", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is False

    # Test server with invalid status
    server = {
        "hostname": "test.nordvpn.com",
        "status": "offline",  # Should be online
        "load": 50,
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 5, "name": "OpenVPN TCP", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is False

    # Test server with invalid load
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 150,  # Should be 0-100
        "country": {"code": "US", "name": "United States"},
        "technologies": [
            {"id": 5, "name": "OpenVPN TCP", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is False

    # Test server with invalid country code
    server = {
        "hostname": "test.nordvpn.com",
        "status": "online",
        "load": 50,
        "country": {"code": "USA", "name": "United States"},  # Should be 2 letters
        "technologies": [
            {"id": 5, "name": "OpenVPN TCP", "status": "online"},
        ],
    }
    assert server_manager._is_valid_server(server) is False


def test_server_filtering(server_manager, mock_api_client):
    """Test server filtering in get_servers_cache."""
    # Mock API response with various server types
    mock_api_client.get.return_value.json.return_value = [
        {
            "hostname": "tcp1.nordvpn.com",
            "status": "online",
            "load": 50,
            "country": {"code": "US", "name": "United States"},
            "technologies": [
                {"id": 5, "name": "OpenVPN TCP", "status": "online"},
            ],
        },
        {
            "hostname": "tcp2.nordvpn.com",
            "status": "online",
            "load": 60,
            "country": {"code": "US", "name": "United States"},
            "technologies": [
                {"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},
            ],
        },
        {
            "hostname": "udp1.nordvpn.com",
            "status": "online",
            "load": 40,
            "country": {"code": "US", "name": "United States"},
            "technologies": [
                {"id": 3, "name": "OpenVPN UDP", "status": "online"},
            ],
        },
        {
            "hostname": "offline1.nordvpn.com",
            "status": "offline",
            "load": 30,
            "country": {"code": "US", "name": "United States"},
            "technologies": [
                {"id": 5, "name": "OpenVPN TCP", "status": "online"},
            ],
        },
    ]

    # Get filtered servers
    cache = server_manager.get_servers_cache()
    servers = cache.get("servers", [])

    # Should only include online servers with OpenVPN TCP
    assert len(servers) == 2
    assert any(s["hostname"] == "tcp1.nordvpn.com" for s in servers)
    assert any(s["hostname"] == "tcp2.nordvpn.com" for s in servers)

    # Verify logging
    mock_api_client.logger.debug.assert_any_call("Found OpenVPN TCP support: OpenVPN TCP")
    mock_api_client.logger.debug.assert_any_call("Found OpenVPN TCP support: OpenVPN TCP Dedicated")
    mock_api_client.logger.debug.assert_any_call(
        "Skipping server without OpenVPN TCP: udp1.nordvpn.com. "
        "Available technologies: ['OpenVPN UDP']"
    ) 