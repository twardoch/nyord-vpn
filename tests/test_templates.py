"""Tests for the pure, file-based helpers in nyord_vpn.utils.templates.

this_file: tests/test_templates.py

Only hashing / file-age helpers are exercised here -- the network download and
zip-extraction paths need a real NordVPN config archive and are out of scope
for unit tests (see the ``fail_under`` note in pyproject.toml).
"""

import time
from datetime import timedelta
from pathlib import Path

import pytest

from nyord_vpn.utils import templates


def test_calculate_sha256_is_deterministic() -> None:
    """Same bytes always hash to the same digest."""
    digest = templates.calculate_sha256(b"hello world")
    assert digest == templates.calculate_sha256(b"hello world")
    assert len(digest) == 64  # sha256 hex digest length


def test_verify_file_integrity_matching_hash(tmp_path: Path) -> None:
    """A file's contents match their own freshly computed hash."""
    file_path = tmp_path / "data.bin"
    file_path.write_bytes(b"some config bytes")
    expected = templates.calculate_sha256(b"some config bytes")

    assert templates.verify_file_integrity(file_path, expected) is True


def test_verify_file_integrity_mismatched_hash(tmp_path: Path) -> None:
    """A wrong expected hash fails verification."""
    file_path = tmp_path / "data.bin"
    file_path.write_bytes(b"some config bytes")

    assert templates.verify_file_integrity(file_path, "0" * 64) is False


def test_verify_file_integrity_missing_file_returns_false(tmp_path: Path) -> None:
    """A missing file is treated as a verification failure, not an error."""
    missing = tmp_path / "does-not-exist.bin"
    assert templates.verify_file_integrity(missing, "0" * 64) is False


def test_get_zip_age_missing_file_returns_none(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """No cached ZIP -> age is None."""
    monkeypatch.setattr(templates, "CONFIG_ZIP", tmp_path / "ovpn.zip")
    assert templates.get_zip_age() is None


def test_get_zip_age_returns_positive_timedelta(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An existing ZIP reports a non-negative age."""
    zip_path = tmp_path / "ovpn.zip"
    zip_path.write_bytes(b"fake zip contents")
    monkeypatch.setattr(templates, "CONFIG_ZIP", zip_path)

    age = templates.get_zip_age()
    assert age is not None
    assert age >= timedelta(0)


def test_is_zip_expired_true_when_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A missing ZIP is always considered expired."""
    monkeypatch.setattr(templates, "CONFIG_ZIP", tmp_path / "missing.zip")
    assert templates.is_zip_expired() is True


def test_is_zip_expired_false_when_fresh(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A freshly written ZIP is not expired."""
    zip_path = tmp_path / "ovpn.zip"
    zip_path.write_bytes(b"fresh")
    monkeypatch.setattr(templates, "CONFIG_ZIP", zip_path)

    assert templates.is_zip_expired() is False


def test_is_zip_expired_true_when_old(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A ZIP older than ZIP_MAX_AGE_DAYS is expired."""
    zip_path = tmp_path / "ovpn.zip"
    zip_path.write_bytes(b"old")
    old_time = time.time() - (templates.ZIP_MAX_AGE_DAYS + 1) * 86400
    import os

    os.utime(zip_path, (old_time, old_time))
    monkeypatch.setattr(templates, "CONFIG_ZIP", zip_path)

    assert templates.is_zip_expired() is True
