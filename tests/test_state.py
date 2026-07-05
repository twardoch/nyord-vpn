"""Tests for nyord_vpn.storage.state (pure file I/O, no network).

this_file: tests/test_state.py
"""

import json
from pathlib import Path

import pytest

from nyord_vpn.storage import state as state_mod


@pytest.fixture(autouse=True)
def isolated_state_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Redirect STATE_FILE to a throwaway path so tests never touch real state."""
    state_file = tmp_path / "state.json"
    monkeypatch.setattr(state_mod, "STATE_FILE", state_file)
    return state_file


def test_load_vpn_state_missing_file_returns_default() -> None:
    """No state file yet -> a safe disconnected default is returned."""
    result = state_mod.load_vpn_state()
    assert result["connected"] is False
    assert result["normal_ip"] is None
    assert result["connected_ip"] is None
    assert result["server"] is None
    assert result["country"] is None
    assert "timestamp" in result


def test_load_vpn_state_bad_json_returns_default(isolated_state_file: Path) -> None:
    """Corrupted state file -> falls back to the default state."""
    isolated_state_file.write_text("not valid json{{{")
    result = state_mod.load_vpn_state()
    assert result["connected"] is False
    assert result["normal_ip"] is None


def test_load_vpn_state_fresh_returns_stored_state(isolated_state_file: Path) -> None:
    """A recently written state is returned as-is."""
    stored = {
        "connected": True,
        "normal_ip": "1.1.1.1",
        "connected_ip": "2.2.2.2",
        "server": "us1.nordvpn.com",
        "country": "US",
        "timestamp": state_mod.time.time(),
    }
    isolated_state_file.write_text(json.dumps(stored))

    result = state_mod.load_vpn_state()
    assert result["connected"] is True
    assert result["connected_ip"] == "2.2.2.2"
    assert result["server"] == "us1.nordvpn.com"


def test_load_vpn_state_stale_clears_connection(isolated_state_file: Path) -> None:
    """State older than the 5-minute TTL reports disconnected but keeps normal_ip."""
    stale = {
        "connected": True,
        "normal_ip": "9.9.9.9",
        "connected_ip": "8.8.8.8",
        "server": "us1.nordvpn.com",
        "country": "US",
        "timestamp": state_mod.time.time() - 301,
    }
    isolated_state_file.write_text(json.dumps(stale))

    result = state_mod.load_vpn_state()
    assert result["connected"] is False
    assert result["normal_ip"] == "9.9.9.9"
    assert result["connected_ip"] is None
    assert result["server"] is None


def test_save_vpn_state_disconnected_sets_normal_ip(isolated_state_file: Path) -> None:
    """Saving a disconnected state with current_ip promotes it to normal_ip."""
    state_mod.save_vpn_state({"connected": False, "current_ip": "3.3.3.3"})

    saved = json.loads(isolated_state_file.read_text())
    assert saved["normal_ip"] == "3.3.3.3"
    assert saved["connected_ip"] is None


def test_save_vpn_state_connected_sets_connected_ip_and_keeps_normal(
    isolated_state_file: Path,
) -> None:
    """Saving a connected state preserves normal_ip from the existing file."""
    isolated_state_file.write_text(
        json.dumps({"normal_ip": "5.5.5.5", "timestamp": state_mod.time.time()})
    )

    state_mod.save_vpn_state({"connected": True, "current_ip": "6.6.6.6"})

    saved = json.loads(isolated_state_file.read_text())
    assert saved["connected_ip"] == "6.6.6.6"
    assert saved["normal_ip"] == "5.5.5.5"


def test_save_vpn_state_failure_is_swallowed(
    isolated_state_file: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A write failure is logged, not raised, so it never disrupts VPN operations."""

    def _boom(*_args: object, **_kwargs: object) -> None:
        raise OSError("disk full")

    monkeypatch.setattr(Path, "write_text", _boom)
    # Should not raise despite the simulated disk failure.
    state_mod.save_vpn_state({"connected": False, "current_ip": "1.2.3.4"})
