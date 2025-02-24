"""OpenVPN command construction and management.

this_file: src/nyord_vpn/network/vpn_commands.py

This module provides utilities for constructing and managing OpenVPN commands.
It centralizes all OpenVPN-related command construction to ensure consistency
and proper configuration across the application.
"""

import platform
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

    # Base command with common options
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
        # Add script security for up/down scripts
        "--script-security",
        "2",
        # Network setup
        "--persist-tun",  # Keep tun device between restarts
        "--persist-key",  # Keep keys between restarts
        "--nobind",  # Don't bind to a specific local port
        "--fast-io",  # Optimize I/O operations
        # Cipher configuration
        "--data-ciphers",
        "AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305",
        "--data-ciphers-fallback",
        "AES-256-CBC",
    ]

    # Platform-specific options
    system = platform.system().lower()
    if system == "darwin":  # macOS
        # On macOS, we don't use external DNS scripts
        cmd.extend([
            # Enable routing
            "--redirect-gateway",  # Redirect all traffic through VPN
            "def1",  # Use default gateway
            "autolocal",  # Automatically handle local routing
            # DNS handling is done by the system
            "--dhcp-option",
            "DNS",
            "103.86.96.100",  # NordVPN DNS
            "--dhcp-option",
            "DNS",
            "103.86.99.100",  # NordVPN DNS backup
        ])
    else:  # Linux and others
        # Use standard Linux DNS update scripts if available
        resolv_conf_script = Path("/etc/openvpn/update-resolv-conf")
        if resolv_conf_script.exists():
            cmd.extend([
                "--up",
                str(resolv_conf_script),
                "--down",
                str(resolv_conf_script),
            ])
        
        cmd.extend([
            # Enable routing
            "--redirect-gateway",  # Redirect all traffic through VPN
            "def1",  # Use default gateway
            "bypass-dhcp",  # Don't redirect DHCP
            "bypass-dns",  # Don't redirect DNS
        ])

    # Add log file if specified
    if log_path:
        cmd.extend(["--log", str(log_path)])

    return cmd
