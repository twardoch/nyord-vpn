"""Tests for ServerManager transform/selection logic against real v2 models.

this_file: tests/test_server_transform.py

Unlike tests/test_server_manager.py (which exercises `_is_valid_server` against
plain dicts), this module feeds `ServerManager` real `nyord_vpn.api.v2_servers`
pydantic model instances -- as `NordVPNAPI.get_servers()`/`find_best_server()`
actually return -- via a MagicMock API client. No network I/O occurs.
"""

from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest

from nyord_vpn.api import v2_servers as v2
from nyord_vpn.api.api import NordVPNAPI
from nyord_vpn.network.server import ServerManager

_TS = datetime(2024, 1, 1, tzinfo=timezone.utc)


def _make_city(city_id: int = 1, name: str = "New York") -> v2.City:
    return v2.City(
        id=city_id,
        name=name,
        latitude=40.7128,
        longitude=-74.0060,
        dns_name="us-nyc.nordvpn.com",
        hub_score=1,
    )


def _make_country(code: str = "US", name: str = "United States") -> v2.Country:
    return v2.Country(id=1, name=name, code=code, city=_make_city())


def _make_location(location_id: int = 1, country_code: str = "US") -> v2.Location:
    return v2.Location(
        id=location_id,
        created_at=_TS,
        updated_at=_TS,
        latitude=40.7128,
        longitude=-74.0060,
        country=_make_country(country_code),
    )


def _make_technology(
    name: str = "OpenVPN TCP", status: str = "online", tech_id: int = 3
) -> v2.Technology:
    return v2.Technology(
        id=tech_id,
        name=name,
        identifier="openvpn_tcp",
        created_at=_TS,
        updated_at=_TS,
        status=status,
    )


def _make_server(
    hostname: str = "us1234.nordvpn.com",
    load: int = 45,
    status: str = "online",
    server_id: int = 1,
    locations: list[v2.Location] | None = None,
    technologies: list[v2.Technology] | None = None,
) -> v2.Server:
    return v2.Server(
        id=server_id,
        created_at=_TS,
        updated_at=_TS,
        name=hostname,
        station=hostname.split(".", maxsplit=1)[0],
        ipv6_station="",
        hostname=hostname,
        status=status,
        load=load,
        ips=[],
        specifications=[],
        technologies=technologies if technologies is not None else [_make_technology()],
        groups=[],
        services=[],
        locations=locations if locations is not None else [_make_location()],
    )


@pytest.fixture
def mock_api_client() -> MagicMock:
    """A MagicMock API client returning real v2 model instances."""
    return MagicMock(spec=NordVPNAPI)


@pytest.fixture
def server_manager(mock_api_client: MagicMock) -> ServerManager:
    """A ServerManager wired to the mocked API client."""
    return ServerManager(mock_api_client)


def test_get_servers_cache_transforms_v2_models(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """get_servers_cache converts real v2 Server/Location objects to ServerInfo."""
    server = _make_server()
    location = server.locations[0]
    mock_api_client.get_servers.return_value = ([server], [], [], [location], [])

    cache = server_manager.get_servers_cache()

    assert cache is not None
    assert cache["last_updated"] > 0
    assert str(location.id) in cache["locations"]
    assert cache["locations"][str(location.id)]["country"]["code"] == "US"

    assert len(cache["servers"]) == 1
    info = cache["servers"][0]
    assert info["hostname"] == "us1234.nordvpn.com"
    assert info["status"] == "online"
    assert info["load"] == 45
    assert info["location_ids"] == [str(location.id)]
    assert info["technologies"][0]["status"] == "online"


def test_get_servers_cache_skips_hostless_servers(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """Servers without a hostname are dropped from the transformed cache."""
    server = _make_server(hostname="")
    mock_api_client.get_servers.return_value = ([server], [], [], [], [])

    cache = server_manager.get_servers_cache()

    assert cache is not None
    assert cache["servers"] == []


def test_get_servers_cache_returns_none_on_api_failure(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """API errors are swallowed and reported as a cache miss, not raised."""
    mock_api_client.get_servers.side_effect = RuntimeError("boom")

    assert server_manager.get_servers_cache() is None


def test_select_fastest_server_uses_direct_best_server(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """When find_best_server succeeds, its result is used directly (no cache fallback)."""
    location = _make_location()
    # _validate_country_code needs get_servers() to include a matching location.
    mock_api_client.get_servers.return_value = ([], [], [], [location], [])
    mock_api_client.find_best_server.return_value = _make_server(
        hostname="best.nordvpn.com", load=5
    )

    result = server_manager.select_fastest_server("US")

    assert len(result) == 1
    assert result[0]["hostname"] == "best.nordvpn.com"
    assert result[0]["load"] == 5
    mock_api_client.find_best_server.assert_called_once_with(
        country_code="US", technology_identifier="openvpn_tcp"
    )


@pytest.mark.parametrize(
    ("hostname", "expected"),
    [
        ("us1234.nordvpn.com", True),
        ("a.b", True),
        ("", False),
        ("no-dot", False),
        ("bad_host!.com", False),
        ("x" * 254 + ".com", False),
        ("-leading.com", False),
    ],
)
def test_is_valid_hostname(
    server_manager: ServerManager, hostname: str, expected: bool
) -> None:
    """_is_valid_hostname enforces a strict DNS-label format."""
    assert server_manager._is_valid_hostname(hostname) is expected


def test_fetch_server_info_returns_hostname_and_station(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """fetch_server_info resolves the best server's hostname/station via the API."""
    location = _make_location()
    mock_api_client.get_servers.return_value = ([], [], [], [location], [])
    mock_api_client.find_best_server.return_value = _make_server(
        hostname="best.nordvpn.com"
    )

    result = server_manager.fetch_server_info("US")

    assert result == ("best.nordvpn.com", "best")


def test_fetch_server_info_raises_server_error_without_hostname(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """A best-server result without a hostname is reported as a ServerError."""
    from nyord_vpn.storage.models import ServerError

    mock_api_client.get_servers.return_value = ([], [], [], [], [])
    mock_api_client.find_best_server.return_value = _make_server(hostname="x.y")
    mock_api_client.find_best_server.return_value.hostname = ""

    with pytest.raises(ServerError):
        server_manager.fetch_server_info(None)


def test_select_fastest_server_falls_back_to_cache_filtering(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """When find_best_server raises, selection falls back to cache filtering.

    Note: get_servers_cache's technology transform does not carry over the
    technology ``name``/``identifier`` fields (only id/status/metadata), so
    ``_is_valid_server``'s "OpenVPN TCP" name check can never match a
    cache-derived server. The fallback path therefore always ends up with an
    empty valid-server list and raises ServerError -- this test documents
    that real, current behavior rather than an idealized one.
    """
    from nyord_vpn.exceptions import VPNAPIError
    from nyord_vpn.storage.models import ServerError

    location = _make_location()
    mock_api_client.get_servers.return_value = (
        [
            _make_server(hostname="busy.nordvpn.com", load=80, locations=[location]),
            _make_server(hostname="quiet.nordvpn.com", load=10, locations=[location]),
        ],
        [],
        [],
        [location],
        [],
    )
    mock_api_client.find_best_server.side_effect = VPNAPIError("no direct match")

    with pytest.raises(ServerError):
        server_manager.select_fastest_server("US", num_servers=2)


def test_select_fastest_server_raises_when_nothing_valid(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """No OpenVPN TCP servers anywhere -> ServerError, not a silent empty list."""
    from nyord_vpn.exceptions import VPNAPIError
    from nyord_vpn.storage.models import ServerError

    mock_api_client.get_servers.return_value = ([], [], [], [], [])
    mock_api_client.find_best_server.side_effect = VPNAPIError("no direct match")

    with pytest.raises(ServerError):
        server_manager.select_fastest_server(None)


def test_get_country_info_from_api(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """get_country_info resolves country details directly from the v2 API."""
    location = _make_location()
    mock_api_client.get_servers.return_value = ([], [], [], [location], [])

    info = server_manager.get_country_info("US")

    assert info["code"] == "US"
    assert info["name"] == "United States"


def test_get_country_info_raises_for_unknown_code(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """An unrecognized country code raises ServerError via _validate_country_code."""
    from nyord_vpn.storage.models import ServerError

    mock_api_client.get_servers.return_value = ([], [], [], [_make_location()], [])

    with pytest.raises(ServerError):
        server_manager.get_country_info("ZZ")


def test_get_random_country_from_api(
    server_manager: ServerManager, mock_api_client: MagicMock
) -> None:
    """get_random_country picks one of the codes returned by the v2 API."""
    locations = [_make_location(1, "US"), _make_location(2, "DE")]
    mock_api_client.get_servers.return_value = ([], [], [], locations, [])

    code = server_manager.get_random_country()

    assert code in {"US", "DE"}
