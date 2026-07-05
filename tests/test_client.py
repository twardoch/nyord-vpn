"""Tests for the high-level VPN Client.

this_file: tests/test_client.py

These tests exercise the current (v2-only) Client surface with every network,
subprocess, and VPN interaction mocked via the ``mock_client`` fixture.
"""

import pytest

from nyord_vpn.core.client import Client
from nyord_vpn.exceptions import VPNError


def test_status(mock_client: Client) -> None:
    """status() proxies the VPN manager and reports connection details."""
    status = mock_client.status()
    assert status["connected"] is True
    assert status["ip"] == "1.2.3.4"
    assert status["server"] == "us1234.nordvpn.com"


def test_go_connects(mock_client: Client) -> None:
    """go() selects a server and drives setup + connect."""
    mock_client.vpn_manager.reset_mock()
    mock_client.go("US")

    mock_client.server_manager.select_fastest_server.assert_called_once_with("US")
    mock_client.vpn_manager.setup_connection.assert_called_once()
    mock_client.vpn_manager.connect.assert_called_once()


def test_go_dry_run(mock_client: Client) -> None:
    """A dry run reports the selection without connecting."""
    mock_client.vpn_manager.reset_mock()
    mock_client.go("US", dry_run=True)

    mock_client.server_manager.select_fastest_server.assert_called_once_with("US")
    mock_client.vpn_manager.setup_connection.assert_not_called()
    mock_client.vpn_manager.connect.assert_not_called()


def test_go_no_servers_raises(mock_client: Client) -> None:
    """go() raises VPNError when no servers are available."""
    mock_client.server_manager.select_fastest_server.return_value = []
    with pytest.raises(VPNError):
        mock_client.go("US")


def test_list_countries(mock_client: Client, capsys: pytest.CaptureFixture[str]) -> None:
    """list_countries() fetches from the v2 API and prints the results."""
    mock_client.list_countries()
    mock_client.api_client.get_all_countries_from_v2.assert_called_once()
    out = capsys.readouterr().out
    assert "United States" in out
    assert "US" in out


def test_missing_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    """Client construction fails cleanly without credentials."""
    for var in ("NORD_USER", "NORDVPN_LOGIN", "NORD_PASSWORD", "NORDVPN_PASSWORD"):
        monkeypatch.delenv(var, raising=False)
    with pytest.raises(VPNError):
        Client(None, None)


def test_format_minimal_output_connected(mock_client: Client) -> None:
    """Connected status renders as 'IP: server'."""
    out = mock_client._format_minimal_output(
        {"connected": True, "ip": "1.2.3.4", "server": "us1.nordvpn.com"}
    )
    assert out == "1.2.3.4: us1.nordvpn.com"


def test_format_minimal_output_disconnected(mock_client: Client) -> None:
    """Disconnected status renders as 'IP: -'."""
    out = mock_client._format_minimal_output({"connected": False, "ip": "1.2.3.4"})
    assert out == "1.2.3.4: -"


def test_info_connected(
    mock_client: Client, capsys: pytest.CaptureFixture[str]
) -> None:
    """info() in non-verbose mode prints the minimal 'IP: server' summary."""
    mock_client.info()
    out = capsys.readouterr().out
    assert "1.2.3.4: us1234.nordvpn.com" in out


def test_info_disconnected(
    mock_client: Client, capsys: pytest.CaptureFixture[str]
) -> None:
    """info() reports disconnected status without a server name."""
    mock_client.vpn_manager.status.return_value = {
        "connected": False,
        "ip": "9.9.9.9",
        "server": None,
        "country": None,
    }
    mock_client.info()
    out = capsys.readouterr().out
    assert "9.9.9.9: -" in out


def test_bye_disconnects_when_connected(
    mock_client: Client, monkeypatch: pytest.MonkeyPatch
) -> None:
    """bye() disconnects an active VPN session and persists the new state."""
    saved_states = []
    monkeypatch.setattr(
        "nyord_vpn.core.client.save_vpn_state", saved_states.append
    )
    mock_client.vpn_manager.status.return_value = {"connected": True}
    mock_client.vpn_manager.is_connected.return_value = True
    mock_client.vpn_manager.get_current_ip.return_value = "7.7.7.7"

    mock_client.bye()

    mock_client.vpn_manager.disconnect.assert_called()
    assert saved_states
    assert saved_states[-1]["connected"] is False
    assert saved_states[-1]["current_ip"] == "7.7.7.7"


def test_bye_noop_when_not_connected(
    mock_client: Client, monkeypatch: pytest.MonkeyPatch
) -> None:
    """bye() is a safe no-op (beyond state save) when already disconnected."""
    saved_states = []
    monkeypatch.setattr(
        "nyord_vpn.core.client.save_vpn_state", saved_states.append
    )
    mock_client.vpn_manager.status.return_value = {"connected": False}
    mock_client.vpn_manager.is_connected.return_value = False

    mock_client.bye()

    mock_client.vpn_manager.disconnect.assert_not_called()
    assert saved_states


def test_constructor_swallows_hostname_setup_error(
    mock_env_credentials: None, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A hostname-related VPNError from initial setup_connection() is swallowed.

    The Client constructor calls vpn_manager.setup_connection("", user, pass)
    to prime credentials before a real hostname is known; a "hostname" error
    at that point is expected and must not prevent construction.
    """
    from unittest.mock import patch

    with (
        patch("nyord_vpn.core.client.NordVPNAPI"),
        patch("nyord_vpn.core.client.ServerManager"),
        patch("nyord_vpn.core.client.VPNConnectionManager") as mock_vpn_manager,
    ):
        mock_vpn_manager.return_value.setup_connection.side_effect = VPNError(
            "missing hostname"
        )
        client = Client("test_user", "test_pass")
        assert client.username == "test_user"


def test_constructor_reraises_non_hostname_setup_error(
    mock_env_credentials: None,
) -> None:
    """A non-hostname VPNError from initial setup is not swallowed."""
    from unittest.mock import patch

    with (
        patch("nyord_vpn.core.client.NordVPNAPI"),
        patch("nyord_vpn.core.client.ServerManager"),
        patch("nyord_vpn.core.client.VPNConnectionManager") as mock_vpn_manager,
    ):
        mock_vpn_manager.return_value.setup_connection.side_effect = VPNError(
            "auth file missing"
        )
        with pytest.raises(VPNError, match="auth file missing"):
            Client("test_user", "test_pass")


def test_init_success(mock_client: Client) -> None:
    """init() creates cache/config dirs and verifies API + IP connectivity."""
    mock_client.api_client.get_servers.return_value = ([], [], [], [], [])
    mock_client.vpn_manager.get_current_ip.return_value = "1.2.3.4"

    mock_client.init()

    mock_client.api_client.get_servers.assert_called_once_with(refresh=True)


def test_init_raises_connection_error_on_api_failure(mock_client: Client) -> None:
    """init() reports API failures as VPNConnectionError."""
    from nyord_vpn.exceptions import VPNConnectionError

    mock_client.api_client.get_servers.side_effect = RuntimeError("api down")

    with pytest.raises(VPNConnectionError):
        mock_client.init()
