"""Tests for VPNConnectionManager's mockable, non-subprocess logic.

this_file: tests/test_vpn_manager.py

OpenVPN process spawning (setup_connection/connect) and platform-specific
interface checks (verify_connection) need a real OpenVPN binary and a live
network interface, so they are intentionally left to integration testing.
This module covers everything that can be exercised through mocking:
construction, status/is_connected, IP lookup, the IP cache, process
liveness checks, connection-state inspection from the log file, and a
clean disconnect with no real OpenVPN processes present.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from nyord_vpn.network.vpn import VPNConnectionManager


@pytest.fixture
def vpn_manager(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> VPNConnectionManager:
    """A VPNConnectionManager built without touching real state/OpenVPN/network."""
    monkeypatch.setattr(
        "nyord_vpn.network.vpn.load_vpn_state",
        lambda: {
            "normal_ip": None,
            "connected_ip": None,
            "server": None,
            "country": None,
        },
    )
    monkeypatch.setattr("nyord_vpn.network.vpn.OPENVPN_AUTH", tmp_path / "openvpn.auth")
    monkeypatch.setattr("nyord_vpn.network.vpn.OPENVPN_LOG", tmp_path / "openvpn.log")

    api_client = MagicMock()
    server_manager = MagicMock()

    # Force check_openvpn_installation() to fail deterministically so
    # construction never depends on whether the host actually has OpenVPN.
    with (
        patch("nyord_vpn.network.vpn.subprocess.run", side_effect=FileNotFoundError()),
        patch("pathlib.Path.exists", return_value=False),
    ):
        return VPNConnectionManager(
            api_client=api_client, server_manager=server_manager, verbose=False
        )


def test_construction_without_openvpn_leaves_path_none(
    vpn_manager: VPNConnectionManager,
) -> None:
    """When OpenVPN can't be located, openvpn_path stays None (no crash)."""
    assert vpn_manager.openvpn_path is None
    assert vpn_manager._normal_ip is None
    assert vpn_manager.process is None


def test_is_connected_false_when_no_process(
    vpn_manager: VPNConnectionManager,
) -> None:
    """No tracked process -> not connected."""
    assert vpn_manager.is_connected() is False


def test_is_connected_true_when_process_alive(
    vpn_manager: VPNConnectionManager,
) -> None:
    """poll() returning None means the OpenVPN process is still running."""
    vpn_manager.process = MagicMock(poll=MagicMock(return_value=None))
    assert vpn_manager.is_connected() is True


def test_is_connected_false_when_process_exited(
    vpn_manager: VPNConnectionManager,
) -> None:
    """A non-None poll() return code means the process has exited."""
    vpn_manager.process = MagicMock(poll=MagicMock(return_value=0))
    assert vpn_manager.is_connected() is False


def test_invalidate_ip_cache_resets_fields(
    vpn_manager: VPNConnectionManager,
) -> None:
    """_invalidate_ip_cache clears both the cached value and its timestamp."""
    vpn_manager._cached_ip = "1.2.3.4"
    vpn_manager._cached_ip_time = 12345.0

    vpn_manager._invalidate_ip_cache()

    assert vpn_manager._cached_ip is None
    assert vpn_manager._cached_ip_time == 0


def test_get_current_ip_primary_service_success(
    vpn_manager: VPNConnectionManager,
) -> None:
    """A valid IP from the primary service (ipify) is returned immediately."""
    response = MagicMock()
    response.json.return_value = {"ip": "203.0.113.5"}
    with patch("nyord_vpn.network.vpn.requests.get", return_value=response):
        assert vpn_manager.get_current_ip() == "203.0.113.5"


def test_get_current_ip_falls_back_to_backup_service(
    vpn_manager: VPNConnectionManager,
) -> None:
    """If the primary service fails, the ip-api.com backup is used."""

    def _get(url: str, timeout: int = 3) -> MagicMock:
        response = MagicMock()
        if "ipify" in url:
            raise ConnectionError("primary down")
        response.json.return_value = {"query": "198.51.100.9"}
        return response

    with (
        patch("nyord_vpn.network.vpn.requests.get", side_effect=_get),
        patch("nyord_vpn.network.vpn.time.sleep"),
    ):
        assert vpn_manager.get_current_ip() == "198.51.100.9"


def test_get_current_ip_all_services_fail_returns_none(
    vpn_manager: VPNConnectionManager,
) -> None:
    """When every IP service fails, get_current_ip returns None (not raise)."""
    with (
        patch(
            "nyord_vpn.network.vpn.requests.get", side_effect=ConnectionError("down")
        ),
        patch("nyord_vpn.network.vpn.time.sleep"),
    ):
        assert vpn_manager.get_current_ip() is None


def test_status_reports_disconnected(vpn_manager: VPNConnectionManager) -> None:
    """status() reflects is_connected()/get_current_ip() when nothing is set up."""
    with patch("nyord_vpn.network.vpn.requests.get", side_effect=ConnectionError()):
        status = vpn_manager.status()
    assert status["connected"] is False
    assert status["server"] is None
    assert status["country"] is None


def test_status_resolves_country_from_server_cache(
    vpn_manager: VPNConnectionManager,
) -> None:
    """status() looks up the connected server's country via the server cache."""
    vpn_manager._server = "us1234.nordvpn.com"
    vpn_manager.server_manager.get_servers_cache.return_value = {
        "servers": [{"hostname": "us1234.nordvpn.com", "location_ids": ["1"]}],
        "locations": {"1": {"country": {"name": "United States", "code": "US"}}},
    }
    with patch("nyord_vpn.network.vpn.requests.get", side_effect=ConnectionError()):
        status = vpn_manager.status()
    assert status["country"] == "United States"


def test_status_falls_back_to_hostname_country_lookup(
    vpn_manager: VPNConnectionManager,
) -> None:
    """When the server isn't in the cache, the hostname prefix resolves the country."""
    vpn_manager._server = "us1234.nordvpn.com"
    vpn_manager.server_manager.get_servers_cache.return_value = None
    vpn_manager.api_client.get_all_countries_from_v2.return_value = [
        {"name": "United States", "code": "US"},
    ]
    with patch("nyord_vpn.network.vpn.requests.get", side_effect=ConnectionError()):
        status = vpn_manager.status()
    assert status["country"] == "United States"


def test_is_process_running_true(vpn_manager: VPNConnectionManager) -> None:
    """os.kill succeeding means the process is alive."""
    with patch("nyord_vpn.network.vpn.os.kill", return_value=None):
        assert vpn_manager._is_process_running(1234) is True


def test_is_process_running_false_on_oserror(
    vpn_manager: VPNConnectionManager,
) -> None:
    """OSError means the process is not running."""
    with patch("nyord_vpn.network.vpn.os.kill", side_effect=OSError("no such process")):
        assert vpn_manager._is_process_running(1234) is False


def test_check_connection_state_false_without_process_id(
    vpn_manager: VPNConnectionManager,
) -> None:
    """No tracked process_id in state -> not connected."""
    with patch(
        "nyord_vpn.network.vpn.load_vpn_state",
        return_value={"process_id": None, "connected": False},
    ):
        assert vpn_manager.check_connection_state() is False


def test_check_connection_state_true_when_log_shows_completion(
    vpn_manager: VPNConnectionManager, tmp_path: Path
) -> None:
    """A running process plus a completed-init log line means connected."""
    log_path = tmp_path / "openvpn.log"
    log_path.write_text("some preamble\nInitialization Sequence Completed\n")

    with (
        patch(
            "nyord_vpn.network.vpn.load_vpn_state",
            return_value={"process_id": 999, "connected": True},
        ),
        patch("nyord_vpn.network.vpn.OPENVPN_LOG", log_path),
        patch.object(vpn_manager, "_is_process_running", return_value=True),
    ):
        assert vpn_manager.check_connection_state() is True


def test_check_connection_state_false_when_process_dead_triggers_disconnect(
    vpn_manager: VPNConnectionManager,
) -> None:
    """A dead but 'connected' process triggers a disconnect() call."""
    with (
        patch(
            "nyord_vpn.network.vpn.load_vpn_state",
            return_value={"process_id": 999, "connected": True},
        ),
        patch.object(vpn_manager, "_is_process_running", return_value=False),
        patch.object(vpn_manager, "disconnect") as mock_disconnect,
    ):
        assert vpn_manager.check_connection_state() is False
        mock_disconnect.assert_called_once()


def test_disconnect_clean_when_no_openvpn_processes(
    vpn_manager: VPNConnectionManager,
) -> None:
    """disconnect() completes cleanly when no OpenVPN processes are found."""
    vpn_manager.process = None
    vpn_manager._server = "us1234.nordvpn.com"

    with (
        patch("nyord_vpn.network.vpn.psutil.process_iter", return_value=[]),
        patch("nyord_vpn.network.vpn.save_vpn_state") as mock_save,
    ):
        vpn_manager.disconnect()

    assert vpn_manager._server is None
    assert vpn_manager._connected_ip is None
    mock_save.assert_called_once()
    saved_state = mock_save.call_args[0][0]
    assert saved_state["connected"] is False
