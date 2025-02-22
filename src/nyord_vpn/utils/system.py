"""System utilities for VPN operations."""

import os
import shutil
import subprocess
from pathlib import Path
from collections.abc import Sequence
from typing import Any

from nyord_vpn.core.exceptions import VPNError

SHELL_METACHARACTERS = ";|&`$(){}[]<>\\'"


def check_command(cmd: str | Path) -> tuple[bool, str]:
    """Check if a command exists and is executable.

    Args:
        cmd: Command to check

    Returns:
        Tuple of (exists, path)
    """
    try:
        cmd_str = str(cmd)
        if os.path.isabs(cmd_str):
            # If absolute path, check directly
            if os.access(cmd_str, os.X_OK):
                return True, cmd_str
            return False, ""

        # Otherwise search in PATH
        cmd_path = shutil.which(cmd_str)
        if cmd_path:
            return True, cmd_path
        return False, ""
    except Exception as e:
        msg = f"Failed to check command: {e}"
        raise VPNError(msg) from e


def validate_command(cmd: Sequence[str | Path]) -> list[str]:
    """Validate a command and its arguments for safe execution.

    Args:
        cmd: Command and arguments as a sequence

    Returns:
        list[str]: Validated command list

    Raises:
        VPNError: If command is invalid or unsafe
    """
    if not cmd:
        msg = "Empty command"
        raise VPNError(msg)

    try:
        # Convert all arguments to strings
        cmd_list = [str(arg) for arg in cmd]

        # Validate executable
        exists, command_path = check_command(cmd_list[0])
        if not exists:
            msg = f"Command {cmd_list[0]} not found"
            raise VPNError(msg)

        # Check for shell metacharacters
        unsafe_chars = {
            ";",
            "&",
            "|",
            ">",
            "<",
            "`",
            "$",
            "(",
            ")",
            "{",
            "}",
            "[",
            "]",
            "\\",
            "'",
            '"',
            "\n",
        }
        for arg in cmd_list:
            if any(char in arg for char in unsafe_chars):
                msg = f"Command argument contains unsafe characters: {arg}"
                raise VPNError(msg)

        # Use absolute path for executable
        cmd_list[0] = command_path
        return cmd_list

    except VPNError:
        raise
    except Exception as e:
        msg = f"Failed to validate command: {e}"
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
            shell=False,  # Never use shell
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
