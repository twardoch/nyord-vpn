"""Tests for OpenVPN command construction (pure logic, no subprocess execution).

this_file: tests/test_vpn_commands.py

`OpenVPNConfig` validation and `get_openvpn_command` only build argument
lists -- they never invoke a real OpenVPN process. `shutil.which("openvpn")`
is mocked so these tests don't depend on OpenVPN actually being installed.
"""

from pathlib import Path
from unittest.mock import patch

import pytest

from nyord_vpn.exceptions import VPNConfigError
from nyord_vpn.network.vpn_commands import (
    OpenVPNConfig,
    OpenVPNVerbosity,
    create_default_config,
    get_openvpn_command,
)


@pytest.fixture
def config_files(tmp_path: Path) -> tuple[Path, Path]:
    """A real (empty) config + auth file pair, as OpenVPNConfig requires."""
    config_path = tmp_path / "server.ovpn"
    auth_path = tmp_path / "auth.txt"
    config_path.write_text("client\n")
    auth_path.write_text("user\npass\n")
    return config_path, auth_path


def test_config_requires_existing_config_file(tmp_path: Path) -> None:
    """A missing config file is rejected at construction time."""
    auth_path = tmp_path / "auth.txt"
    auth_path.write_text("user\npass\n")

    with pytest.raises(VPNConfigError, match="config file not found"):
        OpenVPNConfig(config_path=tmp_path / "missing.ovpn", auth_path=auth_path)


def test_config_requires_existing_auth_file(tmp_path: Path) -> None:
    """A missing auth file is rejected at construction time."""
    config_path = tmp_path / "server.ovpn"
    config_path.write_text("client\n")

    with pytest.raises(VPNConfigError, match="auth file not found"):
        OpenVPNConfig(config_path=config_path, auth_path=tmp_path / "missing.auth")


def test_config_accepts_string_paths(config_files: tuple[Path, Path]) -> None:
    """String paths are coerced to Path objects."""
    config_path, auth_path = config_files
    config = OpenVPNConfig(config_path=str(config_path), auth_path=str(auth_path))
    assert isinstance(config.config_path, Path)
    assert isinstance(config.auth_path, Path)


def test_config_creates_log_directory(
    config_files: tuple[Path, Path], tmp_path: Path
) -> None:
    """A log_path in a not-yet-created directory has that directory made."""
    config_path, auth_path = config_files
    log_path = tmp_path / "nested" / "openvpn.log"

    OpenVPNConfig(config_path=config_path, auth_path=auth_path, log_path=log_path)

    assert log_path.parent.is_dir()


@pytest.mark.parametrize("verbosity", [0, 7, -1])
def test_config_rejects_invalid_verbosity(
    config_files: tuple[Path, Path], verbosity: int
) -> None:
    """Verbosity outside 1-6 is rejected."""
    config_path, auth_path = config_files
    with pytest.raises(VPNConfigError, match="verbosity"):
        OpenVPNConfig(config_path=config_path, auth_path=auth_path, verbosity=verbosity)


def test_config_converts_int_verbosity_to_enum(
    config_files: tuple[Path, Path],
) -> None:
    """A valid integer verbosity is normalized to the OpenVPNVerbosity enum."""
    config_path, auth_path = config_files
    config = OpenVPNConfig(config_path=config_path, auth_path=auth_path, verbosity=3)
    assert config.verbosity == OpenVPNVerbosity.WARNING


@pytest.mark.parametrize(
    ("field", "value", "match"),
    [
        ("connect_retry", 0, "connect_retry"),
        ("connect_timeout", 0, "connect_timeout"),
        ("ping_interval", 0, "ping_interval"),
        ("ping_restart", 5, "ping_restart"),  # <= default ping_interval (10)
    ],
)
def test_config_rejects_invalid_numeric_params(
    config_files: tuple[Path, Path], field: str, value: int, match: str
) -> None:
    """Each numeric parameter has its constraint enforced."""
    config_path, auth_path = config_files
    with pytest.raises(VPNConfigError, match=match):
        OpenVPNConfig(config_path=config_path, auth_path=auth_path, **{field: value})


def test_get_openvpn_command_raises_when_openvpn_missing(
    config_files: tuple[Path, Path],
) -> None:
    """No openvpn binary on PATH -> VPNConfigError, not a confusing crash later."""
    config_path, auth_path = config_files
    config = OpenVPNConfig(config_path=config_path, auth_path=auth_path)

    with (
        patch("nyord_vpn.network.vpn_commands.shutil.which", return_value=None),
        pytest.raises(VPNConfigError, match="not found in PATH"),
    ):
        get_openvpn_command(config)


def test_get_openvpn_command_includes_core_options(
    config_files: tuple[Path, Path],
) -> None:
    """The base command always references config/auth files and key options."""
    config_path, auth_path = config_files
    config = OpenVPNConfig(config_path=config_path, auth_path=auth_path)

    with patch(
        "nyord_vpn.network.vpn_commands.shutil.which", return_value="/usr/sbin/openvpn"
    ):
        cmd = get_openvpn_command(config)

    assert cmd[0] == "openvpn"
    assert "--config" in cmd
    assert str(config_path) in cmd
    assert "--auth-user-pass" in cmd
    assert str(auth_path) in cmd
    assert "--data-ciphers" in cmd
    assert "--persist-tun" in cmd


def test_get_openvpn_command_adds_log_path_when_set(
    config_files: tuple[Path, Path], tmp_path: Path
) -> None:
    """A configured log_path is passed through as --log."""
    config_path, auth_path = config_files
    log_path = tmp_path / "openvpn.log"
    config = OpenVPNConfig(
        config_path=config_path, auth_path=auth_path, log_path=log_path
    )

    with patch(
        "nyord_vpn.network.vpn_commands.shutil.which", return_value="/usr/sbin/openvpn"
    ):
        cmd = get_openvpn_command(config)

    assert "--log" in cmd
    assert str(log_path) in cmd


def test_get_openvpn_command_adds_extra_options(
    config_files: tuple[Path, Path],
) -> None:
    """extra_options renders boolean flags and value options correctly."""
    config_path, auth_path = config_files
    config = OpenVPNConfig(
        config_path=config_path,
        auth_path=auth_path,
        extra_options={"mute-replay-warnings": True, "route-metric": 512, "skip": None},
    )

    with patch(
        "nyord_vpn.network.vpn_commands.shutil.which", return_value="/usr/sbin/openvpn"
    ):
        cmd = get_openvpn_command(config)

    assert "--mute-replay-warnings" in cmd
    assert "--route-metric" in cmd
    assert "512" in cmd
    assert "--skip" not in cmd


@pytest.mark.parametrize("system_name", ["Darwin", "Linux", "Windows", "FreeBSD"])
def test_get_openvpn_command_across_platforms(
    config_files: tuple[Path, Path], system_name: str
) -> None:
    """Every platform branch (macOS/Linux/Windows/generic) produces --redirect-gateway."""
    config_path, auth_path = config_files
    config = OpenVPNConfig(config_path=config_path, auth_path=auth_path)

    with (
        patch(
            "nyord_vpn.network.vpn_commands.shutil.which",
            return_value="/usr/sbin/openvpn",
        ),
        patch(
            "nyord_vpn.network.vpn_commands.platform.system", return_value=system_name
        ),
    ):
        cmd = get_openvpn_command(config)

    assert "--redirect-gateway" in cmd
    assert "def1" in cmd
    # DNS options are added on every platform in this codebase.
    assert cmd.count("--dhcp-option") == len(config.dns_servers)


def test_create_default_config(config_files: tuple[Path, Path]) -> None:
    """create_default_config produces a valid, ready-to-use configuration."""
    config_path, auth_path = config_files
    config = create_default_config(config_path, auth_path)

    assert config.verbosity == OpenVPNVerbosity.DETAIL
    assert config.connect_retry == 2
    assert config.ping_restart == 60
