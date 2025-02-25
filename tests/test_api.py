"""Tests for the NordVPN API client module.

this_file: tests/test_api.py

This module contains tests for the api module, which provides
a unified interface to the NordVPN API endpoints.
"""

import pytest
from unittest.mock import MagicMock, patch

from nyord_vpn.api.api import NordVPNAPI


@pytest.fixture
def sample_country() -> dict:
    """Create a sample country for testing."""
    return {
        "id": 1,
        "name": "United States",
        "code": "US",
        "server_count": 100,
        "cities": [
            {
                "id": 1,
                "name": "New York",
                "latitude": 40.7128,
                "longitude": -74.0060,
                "dns_name": "us-nyc.nordvpn.com",
                "hub_score": 1.0,
                "server_count": 50,
            }
        ],
    }


@pytest.fixture
def sample_group_type() -> dict:
    """Create a sample group type for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "title": "Legacy Groups",
        "identifier": "legacy_group_category",
    }


@pytest.fixture
def sample_group(sample_group_type) -> dict:
    """Create a sample group for testing."""
    return {
        "id": 1,
        "title": "P2P",
        "identifier": "p2p",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "type": sample_group_type,
    }


@pytest.fixture
def sample_technology() -> dict:
    """Create a sample technology for testing."""
    return {
        "id": 1,
        "name": "OpenVPN UDP",
        "identifier": "openvpn_udp",
        "internal_identifier": "openvpn_udp_1194",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def sample_server(sample_group_type) -> dict:
    """Create a sample server for testing."""
    return {
        "id": 1,
        "name": "us1234.nordvpn.com",
        "station": "us1234",
        "hostname": "us1234.nordvpn.com",
        "load": 45,
        "status": "online",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "ipv6_station": "",
        "ips": [],
        "specifications": [],
        "groups": [
            {
                "id": 1,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "title": "P2P",
                "identifier": "legacy_p2p",
                "type": sample_group_type,
                "pivot": {"server_id": 1, "group_id": 1},
            }
        ],
        "locations": [
            {
                "id": 1,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
                "latitude": 40.7128,
                "longitude": -74.0060,
                "country": {
                    "id": 1,
                    "name": "United States",
                    "code": "US",
                    "server_count": 100,
                    "city": {
                        "id": 1,
                        "name": "New York",
                        "latitude": 40.7128,
                        "longitude": -74.0060,
                        "dns_name": "us-nyc.nordvpn.com",
                        "hub_score": 1,
                        "server_count": 50,
                    },
                },
            }
        ],
        "technologies": [
            {
                "id": 1,
                "name": "OpenVPN UDP",
                "identifier": "openvpn_udp",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z",
            }
        ],
    }


def test_get_countries(sample_country) -> None:
    """Test fetching countries from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [sample_country]
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        countries = client.get_countries()

        assert len(countries) == 1
        assert countries[0].name == "United States"
        assert countries[0].code == "US"
        assert len(countries[0].cities) == 1
        assert countries[0].cities[0].name == "New York"
        assert countries[0].cities[0].dns_name == "us-nyc.nordvpn.com"


def test_get_groups(sample_group) -> None:
    """Test fetching groups from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [sample_group]
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        groups = client.get_groups()

        assert len(groups) == 1
        assert groups[0].title == "P2P"
        assert groups[0].identifier == "p2p"


def test_get_technologies(sample_technology) -> None:
    """Test fetching technologies from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [sample_technology]
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        technologies = client.get_technologies()

        assert len(technologies) == 1
        assert technologies[0].name == "OpenVPN UDP"
        assert technologies[0].identifier == "openvpn_udp"
        assert technologies[0].internal_identifier == "openvpn_udp_1194"


def test_get_servers(sample_server) -> None:
    """Test fetching servers from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "servers": [sample_server],
            "groups": [sample_server["groups"][0]],
            "services": [],
            "locations": [sample_server["locations"][0]],
            "technologies": [sample_server["technologies"][0]],
        }
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        servers = client.get_servers()

        assert len(servers[0]) == 1  # First element is list of servers
        server = servers[0][0]
        assert server.name == "us1234.nordvpn.com"
        assert server.station == "us1234"
        assert server.load == 45
        assert server.status == "online"
        assert len(server.locations) == 1
        assert server.locations[0].country.name == "United States"
        assert server.locations[0].country.city.name == "New York"
        assert len(server.technologies) == 1
        assert server.technologies[0].name == "OpenVPN UDP"
        assert len(server.groups) == 1
        assert server.groups[0].title == "P2P"
