"""Test fixtures and configuration.

this_file: tests/conftest.py

All fixtures here keep tests fully offline: no real network, subprocess, or
VPN operations are ever performed. The high-level :class:`Client` is built
with its API, server-manager, and VPN-manager collaborators replaced by mocks.
"""

from collections.abc import Iterator
from unittest.mock import patch

import pytest

from nyord_vpn.core.client import Client

# Shared dummy credentials used across the test-suite.
TEST_USERNAME = "test_user"
TEST_PASSWORD = "test_pass"


@pytest.fixture
def mock_env_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    """Mock environment variables for testing."""
    monkeypatch.setenv("NORD_USER", TEST_USERNAME)
    monkeypatch.setenv("NORD_PASSWORD", TEST_PASSWORD)


@pytest.fixture
def mock_client(mock_env_credentials: None) -> Iterator[Client]:
    """Create a Client with every network-facing collaborator mocked."""
    with (
        patch("nyord_vpn.core.client.NordVPNAPI") as mock_api,
        patch("nyord_vpn.core.client.ServerManager") as mock_server_manager,
        patch("nyord_vpn.core.client.VPNConnectionManager") as mock_vpn_manager,
    ):
        vpn = mock_vpn_manager.return_value
        vpn.status.return_value = {
            "connected": True,
            "ip": "1.2.3.4",
            "country": "US",
            "server": "us1234.nordvpn.com",
        }
        vpn.get_current_ip.return_value = "1.2.3.4"
        vpn.is_connected.return_value = True

        server_manager = mock_server_manager.return_value
        server_manager.select_fastest_server.return_value = [
            {"hostname": "us1234.nordvpn.com", "load": 10, "status": "online"},
        ]

        api = mock_api.return_value
        api.get_all_countries_from_v2.return_value = [
            {"name": "United States", "code": "US"},
            {"name": "Germany", "code": "DE"},
        ]

        client = Client(TEST_USERNAME, TEST_PASSWORD)
        # Expose the mocks for assertions in tests.
        client.api_client = api
        client.server_manager = server_manager
        client.vpn_manager = vpn
        yield client
