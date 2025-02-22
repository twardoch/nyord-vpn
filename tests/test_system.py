"""Tests for system utilities."""

import pytest
from pathlib import Path
from typing import Any, cast

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.system import check_command, run_subprocess_safely


def test_check_command(mock_shutil):
    """Test command existence checking."""
    # Test command exists
    exists, path = check_command("nordvpn")
    assert exists is True
    assert path == "/usr/local/bin/nordvpn"

    # Test command doesn't exist
    mock_shutil.return_value = None
    exists, path = check_command("nonexistent")
    assert exists is False
    assert path == ""


@pytest.mark.asyncio
async def test_run_subprocess_safely(mock_subprocess):
    """Test safe subprocess execution."""
    # Test successful command
    result = run_subprocess_safely(
        ["/usr/local/bin/nordvpn", "status"],
        timeout=10,
    )
    assert result.returncode == 0
    assert result.stdout == "Success output"
    assert result.stderr == "Error output"
    mock_subprocess.assert_called_once()

    # Test non-absolute path
    with pytest.raises(VPNError, match="Executable path must be absolute"):
        run_subprocess_safely(["nordvpn", "status"])

    # Test invalid argument type
    with pytest.raises(VPNError, match="All command arguments must be strings"):
        run_subprocess_safely(
            ["/usr/local/bin/nordvpn", cast(Any, 123)],  # type: ignore
        )

    # Test command failure
    mock_subprocess.return_value.returncode = 1
    with pytest.raises(VPNError, match="Command failed"):
        run_subprocess_safely(["/usr/local/bin/nordvpn", "status"])

    # Test command timeout
    mock_subprocess.side_effect = TimeoutError()
    with pytest.raises(VPNError, match="Command timed out"):
        run_subprocess_safely(["/usr/local/bin/nordvpn", "status"])

    # Test unexpected error
    mock_subprocess.side_effect = Exception("Unexpected error")
    with pytest.raises(VPNError, match="Failed to run command"):
        run_subprocess_safely(["/usr/local/bin/nordvpn", "status"])


@pytest.mark.asyncio
async def test_run_subprocess_safely_with_path(mock_subprocess):
    """Test subprocess execution with Path objects."""
    # Test with Path objects
    cmd_path = Path("/usr/local/bin/nordvpn")
    config_path = Path("/etc/nordvpn/config.conf")
    result = run_subprocess_safely(
        [cmd_path, "--config", config_path],
        timeout=10,
    )
    assert result.returncode == 0
    mock_subprocess.assert_called_once()
    assert all(isinstance(arg, str) for arg in mock_subprocess.call_args[0][0])
