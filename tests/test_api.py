"""Tests for the NordVPN API client module.

this_file: tests/test_api.py

This module contains tests for the api module, which provides a unified
interface to the NordVPN v2 API endpoints. All HTTP traffic is mocked.
"""

from unittest.mock import MagicMock, patch

import pytest

from nyord_vpn.api.api import NordVPNAPI

_TS = "2024-01-01T00:00:00Z"


@pytest.fixture
def sample_api_response() -> dict:
    """A minimal but valid v2 ``/v2/servers`` payload.

    The server references its relations via ``*_ids`` so that
    ``_link_server_relations`` resolves them from the top-level lists.
    """
    location = {
        "id": 1,
        "created_at": _TS,
        "updated_at": _TS,
        "latitude": 40.7128,
        "longitude": -74.0060,
        "country": {
            "id": 1,
            "name": "United States",
            "code": "US",
            "city": {
                "id": 1,
                "name": "New York",
                "latitude": 40.7128,
                "longitude": -74.0060,
                "dns_name": "us-nyc.nordvpn.com",
                "hub_score": 1,
            },
        },
    }
    group = {
        "id": 1,
        "created_at": _TS,
        "updated_at": _TS,
        "title": "P2P",
        "identifier": "legacy_p2p",
        "type": {
            "id": 1,
            "created_at": _TS,
            "updated_at": _TS,
            "title": "Legacy Groups",
            "identifier": "legacy_group_category",
        },
    }
    technology = {
        "id": 3,
        "name": "OpenVPN TCP",
        "identifier": "openvpn_tcp",
        "created_at": _TS,
        "updated_at": _TS,
        "status": "online",
    }
    server = {
        "id": 1,
        "created_at": _TS,
        "updated_at": _TS,
        "name": "us1234.nordvpn.com",
        "station": "us1234",
        "ipv6_station": "",
        "hostname": "us1234.nordvpn.com",
        "status": "online",
        "load": 45,
        "ips": [],
        "specifications": [],
        "technologies": [technology],
        "group_ids": [1],
        "service_ids": [],
        "location_ids": [1],
    }
    return {
        "servers": [server],
        "groups": [group],
        "services": [],
        "locations": [location],
        "technologies": [technology],
    }


def test_get_servers(sample_api_response: dict) -> None:
    """Test fetching and parsing servers from the v2 API."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        servers, groups, _services, locations, technologies = client.get_servers()

        assert len(servers) == 1
        server = servers[0]
        assert server.name == "us1234.nordvpn.com"
        assert server.station == "us1234"
        assert server.load == 45
        assert server.status == "online"

        assert len(server.locations) == 1
        assert server.locations[0].country.name == "United States"
        assert server.locations[0].country.city.name == "New York"

        assert len(server.technologies) == 1
        assert server.technologies[0].name == "OpenVPN TCP"

        assert len(server.groups) == 1
        assert server.groups[0].title == "P2P"

        assert len(groups) == 1
        assert len(locations) == 1
        assert len(technologies) == 1


def test_find_best_server_picks_lowest_load(sample_api_response: dict) -> None:
    """find_best_server returns the minimum-load matching server."""
    # Add a second, busier US server so min-load selection is observable.
    busy = dict(sample_api_response["servers"][0])
    busy["id"] = 2
    busy["hostname"] = "us5678.nordvpn.com"
    busy["load"] = 90
    sample_api_response["servers"].append(busy)

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        best = client.find_best_server(
            country_code="US", technology_identifier="openvpn_tcp"
        )
        assert best.hostname == "us1234.nordvpn.com"
        assert best.load == 45


def test_get_all_countries_from_v2(sample_api_response: dict) -> None:
    """get_all_countries_from_v2 returns unique name/code dicts."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        countries = client.get_all_countries_from_v2()
        assert {"name": "United States", "code": "US"} in countries


def test_get_server_stats(sample_api_response: dict) -> None:
    """get_server_stats summarizes countries/servers/groups from v2 data."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        stats = client.get_server_stats()

        assert stats["total_countries"] == 1
        assert stats["total_servers"] == 1
        assert stats["total_groups"] == 1
        assert stats["servers_by_country"] == {"US": 1}
        assert stats["servers_by_group"] == {"legacy_p2p": 1}


def test_get_servers_reuses_instance_cache(sample_api_response: dict) -> None:
    """A second get_servers() call without refresh reuses the cached tuple."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        client.get_servers()
        client.get_servers()

        assert mock_get.call_count == 1


def test_get_servers_refresh_forces_new_fetch(sample_api_response: dict) -> None:
    """Passing refresh=True bypasses the instance cache and re-fetches."""
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        client.get_servers()
        client.get_servers(refresh=True)

        assert mock_get.call_count == 2


def test_get_servers_raises_when_request_fails_without_cache() -> None:
    """A RequestException with no prior cache -> VPNAPIError, not a crash."""
    import requests

    from nyord_vpn.exceptions import VPNAPIError

    with patch("requests.get", side_effect=requests.exceptions.ConnectionError("down")):
        client = NordVPNAPI()
        with pytest.raises(VPNAPIError):
            client.get_servers()


def test_get_servers_uses_cache_when_refresh_fails(sample_api_response: dict) -> None:
    """A refresh failure after a successful fetch falls back to the cached data."""
    import requests

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        first = client.get_servers()

        mock_get.side_effect = requests.exceptions.ConnectionError("down")
        second = client.get_servers(refresh=True)

        assert second == first


def test_find_best_server_raises_when_no_match(sample_api_response: dict) -> None:
    """find_best_server raises VPNAPIError when no server matches the filters."""
    from nyord_vpn.exceptions import VPNAPIError

    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = sample_api_response
        mock_get.return_value = mock_response

        client = NordVPNAPI()
        with pytest.raises(VPNAPIError):
            client.find_best_server(country_code="ZZ")
