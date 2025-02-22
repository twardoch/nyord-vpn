"""System utilities for VPN operations."""

import os
import shutil
import subprocess
from pathlib import Path
from collections.abc import Sequence

from nyord_vpn.core.exceptions import VPNError


def check_command(cmd: str) -> tuple[bool, str]:
    """Check if a command exists in the system and return its absolute path.

    Args:
        cmd: Command name to check

    Returns:
        tuple[bool, str]: (exists, absolute_path)
    """
    cmd_path = shutil.which(cmd)
    return (bool(cmd_path), cmd_path or "")


def run_subprocess_safely(
    cmd: Sequence[str | Path],
    *,
    check: bool = True,
    timeout: int = 30,
    text: bool = True,
) -> subprocess.CompletedProcess:
    """Run a subprocess command safely with proper validation.

    Args:
        cmd: Command and arguments as a sequence
        check: Whether to check the return code
        timeout: Timeout in seconds
        text: Whether to return text output

    Returns:
        CompletedProcess instance

    Raises:
        VPNError: If the command fails or times out
    """
    try:
        # Validate all arguments are strings or Path objects
        if not all(isinstance(arg, str | Path) for arg in cmd):
            msg = "All command arguments must be strings or Path objects"
            raise VPNError(msg)

        # Convert all arguments to strings
        cmd_str = [str(arg) for arg in cmd]

        # Validate executable path
        if not os.path.isabs(cmd_str[0]):
            msg = f"Executable path must be absolute: {cmd_str[0]}"
            raise VPNError(msg)

        return subprocess.run(
            cmd_str,
            check=check,
            capture_output=True,
            timeout=timeout,
            text=text,
        )
    except subprocess.CalledProcessError as e:
        msg = f"Command failed: {e.stderr}"
        raise VPNError(msg) from e
    except subprocess.TimeoutExpired as e:
        msg = f"Command timed out after {timeout} seconds"
        raise VPNError(msg) from e
    except Exception as e:
        msg = f"Failed to run command: {e}"
        raise VPNError(msg) from e
