"""System utilities for VPN operations."""

import os
import shutil
import subprocess
from pathlib import Path
from collections.abc import Sequence
from typing import Any

from nyord_vpn.core.exceptions import VPNError

SHELL_METACHARACTERS = ";|&`$(){}[]<>\\'"


def check_command(command: str) -> tuple[bool, str]:
    """Check if a command exists in the system and validate its permissions."""
    try:
        command_path = shutil.which(command)
        if not command_path:
            return False, ""
        if not os.access(command_path, os.X_OK):
            msg = f"Command {command} exists but is not executable"
            raise VPNError(msg)
        return True, command_path
    except OSError as e:
        msg = f"Error checking command {command}: {e}"
        raise VPNError(msg) from e


def validate_command(cmd: Sequence[str | Path]) -> list[str]:
    """Validate a command and its arguments for safe execution."""
    if not cmd:
        msg = "Empty command"
        raise VPNError(msg)

    cmd_list = [str(arg) for arg in cmd]
    try:
        exists, command_path = check_command(cmd_list[0])
        if not exists:
            msg = f"Command {cmd_list[0]} not found"
            raise VPNError(msg)
        cmd_list[0] = command_path
        for arg in cmd_list[1:]:
            if any(char in arg for char in SHELL_METACHARACTERS):
                msg = f"Invalid character in argument: {arg}"
                raise VPNError(msg)
        return cmd_list
    except VPNError:
        raise
    except Exception as e:
        msg = f"Error validating command {cmd_list[0]}: {e}"
        raise VPNError(msg) from e


def run_subprocess_safely(
    cmd: Sequence[str | Path],
    *,
    check: bool = True,
    timeout: int = 30,
    text: bool = True,
    max_output_size: int = 1024 * 1024,  # 1MB
) -> subprocess.CompletedProcess[Any]:
    """Run a subprocess command safely.

    Args:
        cmd: Command and arguments as a sequence
        check: Whether to check return code
        timeout: Timeout in seconds
        text: Whether to return text output
        max_output_size: Maximum output size in bytes

    Returns:
        CompletedProcess: Subprocess result

    Raises:
        VPNError: If command execution fails
    """
    try:
        # Validate command
        cmd_list = validate_command(cmd)

        # Run command with safety measures
        result = subprocess.run(
            cmd_list,
            check=check,
            timeout=timeout,
            text=text,
            capture_output=True,
            env={"PATH": os.environ.get("PATH", "")},
        )

        # Check output size
        if len(result.stdout) > max_output_size or len(result.stderr) > max_output_size:
            msg = f"Command output exceeds maximum size of {max_output_size} bytes"
            raise VPNError(msg)
        return result

    except subprocess.CalledProcessError as e:
        msg = f"Command failed with exit code {e.returncode}: {e.stderr}"
        raise VPNError(msg) from e
    except subprocess.TimeoutExpired as e:
        msg = f"Command timed out after {timeout} seconds"
        raise VPNError(msg) from e
    except Exception as e:
        msg = f"Failed to run command: {e}"
        raise VPNError(msg) from e
