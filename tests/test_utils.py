"""Tests for nyord_vpn.utils.utils (pure logic, no network/subprocess).

this_file: tests/test_utils.py
"""

import json
from pathlib import Path

import pytest

from nyord_vpn.utils import utils


@pytest.fixture(autouse=True)
def isolated_state_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Redirect STATE_FILE to a throwaway path so tests never touch real state."""
    state_file = tmp_path / "state.json"
    monkeypatch.setattr(utils, "STATE_FILE", state_file)
    return state_file


def test_check_root_true_when_euid_zero(monkeypatch: pytest.MonkeyPatch) -> None:
    """check_root() reports True when the effective UID is 0 (root)."""
    monkeypatch.setattr(utils.os, "geteuid", lambda: 0)
    assert utils.check_root() is True


def test_check_root_false_when_euid_nonzero(monkeypatch: pytest.MonkeyPatch) -> None:
    """check_root() reports False for a non-root effective UID."""
    monkeypatch.setattr(utils.os, "geteuid", lambda: 501)
    assert utils.check_root() is False


def test_is_process_running_true(monkeypatch: pytest.MonkeyPatch) -> None:
    """os.kill(pid, 0) succeeding means the process is alive."""
    monkeypatch.setattr(utils.os, "kill", lambda *_a: None)
    assert utils.is_process_running(12345) is True


def test_is_process_running_false_on_oserror(monkeypatch: pytest.MonkeyPatch) -> None:
    """OSError (e.g. ESRCH) means the process is not running."""

    def _raise_oserror(*_a: object) -> None:
        raise OSError("No such process")

    monkeypatch.setattr(utils.os, "kill", _raise_oserror)
    assert utils.is_process_running(12345) is False


def test_is_process_running_none_on_unexpected_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Any other exception is treated as an inconclusive check."""

    def _raise_other(*_a: object) -> None:
        raise ValueError("unexpected")

    monkeypatch.setattr(utils.os, "kill", _raise_other)
    assert utils.is_process_running(12345) is None


def test_save_and_load_vpn_state_roundtrip(isolated_state_file: Path) -> None:
    """save_vpn_state writes atomically and load_vpn_state reads it back."""
    utils.save_vpn_state(
        {"connected": True, "current_ip": "10.0.0.1", "server": "us1.nordvpn.com"}
    )

    saved = json.loads(isolated_state_file.read_text())
    assert saved["connected_ip"] == "10.0.0.1"

    loaded = utils.load_vpn_state()
    assert loaded["connected"] is True
    assert loaded["connected_ip"] == "10.0.0.1"


def test_load_vpn_state_missing_file_returns_default() -> None:
    """No state file yet -> a safe disconnected default is returned."""
    result = utils.load_vpn_state()
    assert result == {
        "connected": False,
        "normal_ip": None,
        "connected_ip": None,
        "server": None,
        "country": None,
        "timestamp": result["timestamp"],
    }


def test_load_vpn_state_bad_json_returns_default(isolated_state_file: Path) -> None:
    """Corrupted state file -> falls back to the default state."""
    isolated_state_file.write_text("{not json")
    result = utils.load_vpn_state()
    assert result["connected"] is False
    assert result["normal_ip"] is None


def test_ensure_root_noop_when_already_root(monkeypatch: pytest.MonkeyPatch) -> None:
    """ensure_root() does nothing (no subprocess/exit) when already root."""
    monkeypatch.setattr(utils.os, "geteuid", lambda: 0)
    called = []
    monkeypatch.setattr(
        utils.subprocess, "run", lambda *a, **kw: called.append((a, kw))
    )
    utils.ensure_root()
    assert called == []


def test_ensure_root_reexecs_with_sudo_on_success(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Non-root re-execs the command with sudo and exits 0 on success."""
    monkeypatch.setattr(utils.os, "geteuid", lambda: 501)
    monkeypatch.setattr(utils.sys, "argv", ["nyord-vpn", "go", "us"])
    monkeypatch.delenv("VIRTUAL_ENV", raising=False)
    monkeypatch.setattr(utils.subprocess, "run", lambda *_a, **_kw: None)

    with pytest.raises(SystemExit) as exc_info:
        utils.ensure_root()
    assert exc_info.value.code == 0


def test_ensure_root_exits_1_when_sudo_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A failed sudo re-exec exits with status 1, not an uncaught traceback."""
    import subprocess as subprocess_mod

    monkeypatch.setattr(utils.os, "geteuid", lambda: 501)
    monkeypatch.setattr(utils.sys, "argv", ["nyord-vpn", "go", "us"])
    monkeypatch.delenv("VIRTUAL_ENV", raising=False)

    def _raise(*_a: object, **_kw: object) -> None:
        raise subprocess_mod.CalledProcessError(1, "sudo")

    monkeypatch.setattr(utils.subprocess, "run", _raise)

    with pytest.raises(SystemExit) as exc_info:
        utils.ensure_root()
    assert exc_info.value.code == 1
