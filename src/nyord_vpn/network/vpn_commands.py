"""OpenVPN command construction and management.

this_file: src/nyord_vpn/network/vpn_commands.py

This module provides utilities for constructing and managing OpenVPN commands.
It centralizes all OpenVPN-related command construction to ensure consistency
and proper configuration across the application.
"""

from pathlib import Path

from nyord_vpn.exceptions import VPNConfigError


def get_openvpn_command(
    config_path: Path,
    auth_path: Path,
    log_path: Path | None = None,
    verbosity: int = 5,
    connect_retry: int = 2,
    connect_timeout: int = 10,
    ping_interval: int = 10,
    ping_restart: int = 60,
) -> list[str]:
    """Construct OpenVPN command with all necessary arguments.

    This is the central place for OpenVPN command construction. It provides
    a comprehensive set of options for connection management, monitoring,
    and error handling.

    Args:
        config_path: Path to OpenVPN config file
        auth_path: Path to authentication file
        log_path: Optional path to log file
        verbosity: Logging verbosity level (1-6)
        connect_retry: Number of connection retry attempts
        connect_timeout: Connection timeout in seconds
        ping_interval: Interval between ping tests in seconds
        ping_restart: Time without ping response before restart

    Returns:
        List of command arguments for OpenVPN

    Raises:
        VPNConfigError: If required files don't exist or aren't accessible

    Note:
        The command includes security-focused defaults and robust
        error handling parameters to ensure stable VPN connections.

    """
    # Validate required files
    if not config_path.exists():
        raise VPNConfigError(f"OpenVPN config file not found: {config_path}")
    if not auth_path.exists():
        raise VPNConfigError(f"OpenVPN auth file not found: {auth_path}")

    # Validate file permissions (should be readable)
    try:
        config_path.read_bytes()
        auth_path.read_bytes()
    except (PermissionError, OSError) as e:
        raise VPNConfigError(f"Cannot read OpenVPN files: {e}")

    # Create log directory if needed
    if log_path:
        log_path.parent.mkdir(parents=True, exist_ok=True)

    # Validate verbosity level
    if not 1 <= verbosity <= 6:
        raise VPNConfigError(f"Invalid verbosity level: {verbosity} (must be 1-6)")

    cmd = [
        "openvpn",
        "--config",
        str(config_path),
        "--auth-user-pass",
        str(auth_path),
        "--verb",
        str(verbosity),
        "--connect-retry",
        str(connect_retry),
        "--connect-timeout",
        str(connect_timeout),
        "--resolv-retry",
        "infinite",
        "--ping",
        str(ping_interval),
        "--ping-restart",
        str(ping_restart),
    ]

    if log_path:
        cmd.extend(["--log", str(log_path)])

    return cmd
