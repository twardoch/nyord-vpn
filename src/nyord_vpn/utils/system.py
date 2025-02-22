"""System utilities for VPN operations."""

import os
import shutil
import subprocess
import stat
from pathlib import Path
from collections.abc import Sequence
from typing import Any

from nyord_vpn.core.exceptions import VPNError


def check_command(cmd: str) -> tuple[bool, str]:
    """Check if a command exists in the system and return its absolute path.

    Args:
        cmd: Command name to check

    Returns:
        tuple[bool, str]: (exists, absolute_path)

    Raises:
        VPNError: If the command exists but has invalid permissions
    """
    cmd_path = shutil.which(cmd)
    if cmd_path:
        # Check file permissions
        try:
            st = os.stat(cmd_path)
            if bool(st.st_mode & (stat.S_IWGRP | stat.S_IWOTH)):
                msg = f"Command {cmd_path} has unsafe permissions"
                raise VPNError(msg)
            return True, cmd_path
        except OSError as e:
            msg = f"Failed to check command permissions: {e}"
            raise VPNError(msg) from e
    return False, ""


def validate_command(cmd: Sequence[str | Path]) -> list[str]:
    """Validate command arguments for safety.

    Args:
        cmd: Command and arguments as a sequence

    Returns:
        list[str]: Validated command arguments

    Raises:
        VPNError: If command validation fails
    """
    if not cmd:
        msg = "Empty command"
        raise VPNError(msg)

    # Validate all arguments are strings or Path objects
    if not all(isinstance(arg, (str, Path)) for arg in cmd):
        msg = "All command arguments must be strings or Path objects"
        raise VPNError(msg)

    # Convert all arguments to strings
    cmd_str = [str(arg) for arg in cmd]

    # Validate executable path
    if not os.path.isabs(cmd_str[0]):
        msg = f"Executable path must be absolute: {cmd_str[0]}"
        raise VPNError(msg)

    # Check executable permissions
    try:
        st = os.stat(cmd_str[0])
        if not bool(st.st_mode & stat.S_IXUSR):
            msg = f"File is not executable: {cmd_str[0]}"
            raise VPNError(msg)
        if bool(st.st_mode & (stat.S_IWGRP | stat.S_IWOTH)):
            msg = f"Executable {cmd_str[0]} has unsafe permissions"
            raise VPNError(msg)
    except OSError as e:
        msg = f"Failed to check executable permissions: {e}"
        raise VPNError(msg) from e

    # Check for shell injection patterns
    for arg in cmd_str[1:]:
        if any(char in arg for char in "|&;$<>(){}[]"):
            msg = f"Invalid characters in argument: {arg}"
            raise VPNError(msg)

    return cmd_str


def run_subprocess_safely(
    cmd: Sequence[str | Path],
    *,
    check: bool = True,
    timeout: int = 30,
    text: bool = True,
    max_output_size: int = 1024 * 1024,  # 1MB
) -> subprocess.CompletedProcess[Any]:
    """Run a subprocess command safely with proper validation.

    Args:
        cmd: Command and arguments as a sequence
        check: Whether to check the return code
        timeout: Timeout in seconds
        text: Whether to return text output
        max_output_size: Maximum size of output in bytes

    Returns:
        CompletedProcess instance

    Raises:
        VPNError: If the command fails or times out
    """
    try:
        # Validate command
        cmd_str = validate_command(cmd)

        # Create a new process group
        process = subprocess.Popen(
            cmd_str,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=text,
            start_new_session=True,  # Isolate process group
            close_fds=True,  # Close inherited file descriptors
        )

        try:
            # Wait for process with timeout
            stdout, stderr = process.communicate(timeout=timeout)

            # Check output size
            if len(stdout) > max_output_size or len(stderr) > max_output_size:
                process.kill()
                msg = "Process output exceeded maximum size"
                raise VPNError(msg)

            # Check return code if requested
            if check and process.returncode != 0:
                msg = f"Command failed with code {process.returncode}: {stderr}"
                raise subprocess.CalledProcessError(
                    process.returncode, cmd_str, stdout, stderr
                )

            return subprocess.CompletedProcess(
                cmd_str, process.returncode, stdout, stderr
            )

        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
            msg = f"Command timed out after {timeout} seconds"
            raise VPNError(msg)

        finally:
            # Ensure process is terminated
            if process.poll() is None:
                process.kill()
                process.wait()

    except subprocess.CalledProcessError as e:
        # Sanitize error message
        error_msg = str(e.stderr)
        if len(error_msg) > 1024:  # Limit error message size
            error_msg = error_msg[:1021] + "..."
        msg = f"Command failed: {error_msg}"
        raise VPNError(msg) from e

    except Exception as e:
        msg = f"Failed to run command: {e}"
        raise VPNError(msg) from e
