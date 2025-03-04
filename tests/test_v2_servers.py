"""Tests for the NordVPN v2 servers API module.

this_file: tests/test_v2_servers.py

This module contains tests for the v2_servers module, which provides
access to server information from the NordVPN v2 API.
"""

from unittest.mock import MagicMock, patch

import pytest

from nyord_vpn.api.v2_servers import (
    NordVPNServersV2,
    get_servers_by_country,
    get_servers_by_group,
)


@pytest.fixture
def sample_technology_metadata() -> dict:
    """Create a sample technology metadata for testing."""
    return {"name": "port", "value": "1194"}


@pytest.fixture
def sample_tech() -> dict:
    """Create a sample technology for testing."""
    return {
        "id": 1,
        "name": "OpenVPN UDP",
        "identifier": "openvpn_udp",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "status": "active",
        "metadata": [{"name": "port", "value": "1194"}],
    }


@pytest.fixture
def sample_ip() -> dict:
    """Create a sample IP for testing."""
    return {"id": 1, "ip": "192.168.1.1", "version": 4}


@pytest.fixture
def sample_server_ip(sample_ip) -> dict:
    """Create a sample server IP for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "server_id": 1,
        "ip_id": 1,
        "type": "primary",
        "ip": sample_ip,
    }


@pytest.fixture
def sample_specification_value() -> dict:
    """Create a sample specification value for testing."""
    return {"id": 1, "value": "1 Gbps"}


@pytest.fixture
def sample_specification(sample_specification_value) -> dict:
    """Create a sample specification for testing."""
    return {
        "id": 1,
        "title": "Bandwidth",
        "identifier": "bandwidth",
        "values": [sample_specification_value],
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
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "title": "P2P",
        "identifier": "legacy_p2p",
        "type": sample_group_type,
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
def sample_city() -> dict:
    """Create a sample city for testing."""
    return {
        "id": 1,
        "name": "New York",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "dns_name": "us-nyc.nordvpn.com",
        "hub_score": 1,
        "server_count": 50,
    }


@pytest.fixture
def sample_country(sample_city) -> dict:
    """Create a sample country for testing."""
    return {
        "id": 1,
        "name": "United States",
        "code": "US",
        "city": sample_city,
        "server_count": 100,
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
def sample_server(
    sample_server_ip,
    sample_specification,
    sample_tech,
    sample_group,
    sample_service,
    sample_location,
) -> dict:
    """Create a sample server for testing."""
    return {
        "id": 1,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
        "name": "us1234.nordvpn.com",
        "station": "us1234",
        "ipv6_station": "",
        "hostname": "us1234.nordvpn.com",
        "status": "online",
        "load": 45,
        "ips": [sample_server_ip],
        "specifications": [sample_specification],
        "technologies": [sample_tech],
        "groups": [
            {
                "id": sample_group["id"],
                "title": sample_group["title"],
                "identifier": sample_group["identifier"],
                "created_at": sample_group["created_at"],
                "updated_at": sample_group["updated_at"],
                "type": sample_group["type"],
                "pivot": {"server_id": 1, "group_id": sample_group["id"]},
            }
        ],
        "services": [sample_service],
        "locations": [
            {
                "id": sample_location["id"],
                "created_at": sample_location["created_at"],
                "updated_at": sample_location["updated_at"],
                "country": sample_location["country"],
                "pivot": {"server_id": 1, "location_id": sample_location["id"]},
            }
        ],
    }


@pytest.fixture
def sample_api_response(
    sample_server,
    sample_group,
    sample_service,
    sample_location,
    sample_tech,
) -> dict:
    """Create a sample API response for testing."""
    return {
        "servers": [sample_server],
        "groups": [sample_group],
        "services": [sample_service],
        "locations": [sample_location],
        "technologies": [sample_tech],
    }


def test_fetch_all(sample_api_response) -> None:
    """Test fetching all server data from the API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNServersV2()
        servers, groups, services, locations, technologies = client.fetch_all()

        # Test server data
        assert len(servers) == 1
        server = servers[0]
        assert server.name == "us1234.nordvpn.com"
        assert server.station == "us1234"
        assert server.load == 45
        assert server.status == "online"

        # Test server relationships
        assert len(server.ips) == 1
        assert server.ips[0].ip.ip == "192.168.1.1"
        assert len(server.specifications) == 1
        assert server.specifications[0].title == "Bandwidth"
        assert len(server.technologies) == 1
        assert server.technologies[0].name == "OpenVPN UDP"
        assert len(server.groups) == 1
        assert server.groups[0].title == "P2P"
        assert len(server.services) == 1
        assert server.services[0].name == "P2P"
        assert len(server.locations) == 1
        assert server.locations[0].country.name == "United States"

        # Test other entities
        assert len(groups) == 1
        assert groups[0].title == "P2P"
        assert len(services) == 1
        assert services[0].name == "P2P"
        assert len(locations) == 1
        assert locations[0].country.name == "United States"
        assert len(technologies) == 1
        assert technologies[0].name == "OpenVPN UDP"


def test_get_servers_by_country(sample_api_response) -> None:
    """Test filtering servers by country code."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNServersV2()
        servers, *_ = client.fetch_all()

        # Test finding US servers
        us_servers = get_servers_by_country(servers, "US")
        assert len(us_servers) == 1
        assert us_servers[0].hostname == "us1234.nordvpn.com"

        # Test case insensitivity
        us_servers_lower = get_servers_by_country(servers, "us")
        assert len(us_servers_lower) == 1

        # Test non-existent country
        de_servers = get_servers_by_country(servers, "DE")
        assert len(de_servers) == 0


def test_get_servers_by_group(sample_api_response) -> None:
    """Test filtering servers by group identifier."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNServersV2()
        servers, *_ = client.fetch_all()

        # Test finding P2P servers
        p2p_servers = get_servers_by_group(servers, "legacy_p2p")
        assert len(p2p_servers) == 1
        assert p2p_servers[0].hostname == "us1234.nordvpn.com"

        # Test non-existent group
        standard_servers = get_servers_by_group(servers, "standard")
        assert len(standard_servers) == 0
