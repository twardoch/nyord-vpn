"""Tests for the NordVPN v1 recommendations API module.

this_file: tests/test_v1_recommendations.py

This module contains tests for the v1_recommendations module, which provides
access to server recommendations from the NordVPN v1 API.
"""

from unittest.mock import MagicMock, patch

import pytest

from nyord_vpn.api.v1_recommendations import (
    NordVPNRecommendationsV1,
    get_recommendations_by_country,
    get_recommendations_by_group,
)


@pytest.fixture
def sample_city() -> dict:
    """Create a sample city for testing."""
    return {
        "id": 1,
        "name": "New York",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "dns_name": "new-york",
        "hub_score": 100,
    }


@pytest.fixture
def sample_country(sample_city) -> dict:
    """Create a sample country for testing."""
    return {
        "id": 1,
        "name": "United States",
        "code": "US",
        "city": sample_city,
    }


@pytest.fixture
def sample_location(sample_country) -> dict:
    """Create a sample location for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "country": sample_country,
    }


@pytest.fixture
def sample_group() -> dict:
    """Create a sample group for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "title": "P2P",
        "identifier": "legacy_p2p",
        "type": {
            "id": 1,
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z",
            "title": "Legacy Groups",
            "identifier": "legacy_group_category",
        },
    }


@pytest.fixture
def sample_service() -> dict:
    """Create a sample service for testing."""
    return {
        "id": 1,
        "name": "P2P",
        "identifier": "p2p",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def sample_technology() -> dict:
    """Create a sample technology for testing."""
    return {
        "id": 1,
        "name": "OpenVPN TCP",
        "identifier": "openvpn_tcp",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "status": "online",
        "metadata": [{"name": "port", "value": "443"}],
        "pivot": {
            "technology_id": 1,
            "server_id": 1,
            "status": "online",
        },
    }


@pytest.fixture
def sample_server(
    sample_location, sample_group, sample_service, sample_technology
) -> dict:
    """Create a sample server for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "name": "United States #1",
        "station": "us1.nordvpn.com",
        "ipv6_station": "",
        "hostname": "us1.nordvpn.com",
        "status": "online",
        "load": 50,
        "locations": [sample_location],
        "services": [sample_service],
        "technologies": [sample_technology],
        "groups": [sample_group],
        "specifications": [],
        "ips": [],
    }


def test_fetch_recommendations(sample_server) -> None:
    """Test fetching server recommendations from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [sample_server]
        mock_get.return_value = mock_response

        client = NordVPNRecommendationsV1()
        servers = client.fetch_recommendations()

        assert len(servers) == 1
        server = servers[0]
        assert server.name == "United States #1"
        assert server.hostname == "us1.nordvpn.com"
        assert server.load == 50
        assert len(server.locations) == 1
        assert server.locations[0].country.code == "US"
        assert len(server.groups) == 1
        assert server.groups[0].identifier == "legacy_p2p"
        assert len(server.services) == 1
        assert server.services[0].identifier == "p2p"


def test_get_recommendations_by_country(sample_server) -> None:
    """Test filtering recommendations by country code."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [sample_server]
        mock_get.return_value = mock_response

        client = NordVPNRecommendationsV1()
        servers = client.fetch_recommendations()

        # Test finding US servers
        us_servers = get_recommendations_by_country(servers, "US")
        assert len(us_servers) == 1
        assert us_servers[0].hostname == "us1.nordvpn.com"

        # Test case insensitivity
        us_servers_lower = get_recommendations_by_country(servers, "us")
        assert len(us_servers_lower) == 1

        # Test non-existent country
        de_servers = get_recommendations_by_country(servers, "DE")
        assert len(de_servers) == 0


def test_get_recommendations_by_group(sample_server) -> None:
    """Test filtering recommendations by group identifier."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = [sample_server]
        mock_get.return_value = mock_response

        client = NordVPNRecommendationsV1()
        servers = client.fetch_recommendations()

        # Test finding P2P servers
        p2p_servers = get_recommendations_by_group(servers, "legacy_p2p")
        assert len(p2p_servers) == 1
        assert p2p_servers[0].hostname == "us1.nordvpn.com"

        # Test non-existent group
        standard_servers = get_recommendations_by_group(servers, "standard")
        assert len(standard_servers) == 0
