"""Tests for system utilities."""

from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.system import run_subprocess_safely, check_command


@pytest.mark.asyncio
async def test_run_subprocess_safely(mocker: MockerFixture, mock_nordvpn_command: Path):
    """Test safe subprocess execution."""
    # Mock subprocess.run
    mock_run = mocker.patch("subprocess.run")
    mock_run.return_value.stdout = "test output"
    mock_run.return_value.stderr = ""

    # Test successful command
    result = run_subprocess_safely(
        [str(mock_nordvpn_command), "status"],
        timeout=10,
    )
    assert result.stdout == "test output"

    # Test command failure
    mock_run.side_effect = Exception("Command failed")
    with pytest.raises(VPNError, match="Failed to run command"):
        run_subprocess_safely(
            [str(mock_nordvpn_command), "invalid"],
            timeout=10,
        )


@pytest.mark.asyncio
async def test_run_subprocess_safely_with_path(
    mocker: MockerFixture, mock_nordvpn_command: Path
):
    """Test subprocess execution with Path objects."""
    # Mock subprocess.run
    mock_run = mocker.patch("subprocess.run")
    mock_run.return_value.stdout = "test output"
    mock_run.return_value.stderr = ""

    # Test with Path objects
    result = run_subprocess_safely(
        [mock_nordvpn_command, "--config", Path("/etc/nordvpn/config.conf")],
        timeout=10,
    )
    assert result.stdout == "test output"

    # Test command failure
    mock_run.side_effect = Exception("Command failed")
    with pytest.raises(VPNError, match="Failed to run command"):
        run_subprocess_safely(
            [mock_nordvpn_command, "--invalid"],
            timeout=10,
        )


@pytest.mark.asyncio
async def test_check_command(mock_nordvpn_command: Path):
    """Test command existence checking."""
    # Test existing command
    exists, path = check_command(str(mock_nordvpn_command))
    assert exists
    assert path == str(mock_nordvpn_command)

    # Test non-existent command
    exists, path = check_command("nonexistent_command")
    assert not exists
    assert path == ""
