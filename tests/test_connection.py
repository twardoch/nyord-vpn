"""Tests for nyord_vpn.utils.connection (pure logic + mocked psutil).

this_file: tests/test_connection.py
"""

from unittest.mock import MagicMock, patch

from nyord_vpn.utils.connection import compute_connection_status, is_openvpn_running


def _proc(name: str) -> MagicMock:
    proc = MagicMock()
    proc.info = {"name": name}
    return proc


def test_is_openvpn_running_true() -> None:
    """An openvpn process among running processes is detected."""
    with patch(
        "nyord_vpn.utils.connection.psutil.process_iter",
        return_value=[_proc("bash"), _proc("openvpn")],
    ):
        assert is_openvpn_running() is True


def test_is_openvpn_running_false() -> None:
    """No openvpn process present -> False."""
    with patch(
        "nyord_vpn.utils.connection.psutil.process_iter",
        return_value=[_proc("bash"), _proc("zsh")],
    ):
        assert is_openvpn_running() is False


def test_compute_connection_status_with_nord_status_true() -> None:
    """A truthy nord_status can substitute for an exact IP match."""
    assert (
        compute_connection_status(
            current_ip="1.2.3.4",
            initial_ip="9.9.9.9",
            connected_ip="5.6.7.8",  # deliberately mismatched
            openvpn_running=True,
            nord_status=True,
        )
        is True
    )


def test_compute_connection_status_ip_mismatch_and_no_nord_status() -> None:
    """Without nord_status, a mismatched connected_ip means not connected."""
    assert (
        compute_connection_status(
            current_ip="1.2.3.4",
            initial_ip="9.9.9.9",
            connected_ip="5.6.7.8",
            openvpn_running=True,
            nord_status=None,
        )
        is False
    )


def test_compute_connection_status_matching_ip() -> None:
    """Matching connected_ip with process running -> connected."""
    assert (
        compute_connection_status(
            current_ip="5.6.7.8",
            initial_ip="9.9.9.9",
            connected_ip="5.6.7.8",
            openvpn_running=True,
            nord_status=None,
        )
        is True
    )


def test_compute_connection_status_process_not_running() -> None:
    """No OpenVPN process means never connected regardless of IPs."""
    assert (
        compute_connection_status(
            current_ip="5.6.7.8",
            initial_ip=None,
            connected_ip="5.6.7.8",
            openvpn_running=False,
            nord_status=True,
        )
        is False
    )


def test_compute_connection_status_same_as_initial_ip() -> None:
    """Current IP equal to the pre-VPN IP means the tunnel isn't active."""
    assert (
        compute_connection_status(
            current_ip="9.9.9.9",
            initial_ip="9.9.9.9",
            connected_ip="9.9.9.9",
            openvpn_running=True,
            nord_status=None,
        )
        is True
    )
