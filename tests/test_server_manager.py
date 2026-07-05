"""Tests for the ServerManager class.

this_file: tests/test_server_manager.py

This module contains unit tests for the ServerManager class,
which is responsible for server selection and optimization.
"""

from unittest.mock import MagicMock

import pytest

from nyord_vpn.api.api import NordVPNAPI
from nyord_vpn.network.server import ServerManager


@pytest.fixture
def mock_api_client():
    """Create a mock API client."""
    client = MagicMock(spec=NordVPNAPI)
    client.verbose = True
    client.logger = MagicMock()
    return client


@pytest.fixture
def server_manager(mock_api_client):
    """Create a server manager instance."""
    return ServerManager(mock_api_client)


def test_openvpn_tcp_validation(server_manager) -> None:
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


def test_is_valid_server_filters_by_technology_and_status(server_manager) -> None:
    """Only online NordVPN hosts advertising OpenVPN TCP are considered valid."""
    candidates = [
        {
            "hostname": "tcp1.nordvpn.com",
            "status": "online",
            "load": 50,
            "technologies": [{"id": 5, "name": "OpenVPN TCP", "status": "online"}],
        },
        {
            "hostname": "tcp2.nordvpn.com",
            "status": "online",
            "load": 60,
            "technologies": [
                {"id": 45, "name": "OpenVPN TCP Dedicated", "status": "online"},
            ],
        },
        {
            "hostname": "udp1.nordvpn.com",  # no TCP -> invalid
            "status": "online",
            "load": 40,
            "technologies": [{"id": 3, "name": "OpenVPN UDP", "status": "online"}],
        },
        {
            "hostname": "offline1.nordvpn.com",  # offline -> invalid
            "status": "offline",
            "load": 30,
            "technologies": [{"id": 5, "name": "OpenVPN TCP", "status": "online"}],
        },
    ]

    valid = [c for c in candidates if server_manager._is_valid_server(c)]

    assert len(valid) == 2
    hostnames = {s["hostname"] for s in valid}
    assert hostnames == {"tcp1.nordvpn.com", "tcp2.nordvpn.com"}


def test_is_valid_server_accepts_alternate_tech_statuses(server_manager) -> None:
    """Technology status is treated leniently (enabled/active/online)."""
    for status in ("enabled", "active", "online"):
        server = {
            "hostname": "test.nordvpn.com",
            "status": "online",
            "load": 10,
            "technologies": [{"id": 5, "name": "OpenVPN TCP", "status": status}],
        }
        assert server_manager._is_valid_server(server) is True


def test_is_valid_server_rejects_non_dict(server_manager) -> None:
    """Non-dict inputs are rejected without raising."""
    assert server_manager._is_valid_server(None) is False
    assert server_manager._is_valid_server("not-a-server") is False
