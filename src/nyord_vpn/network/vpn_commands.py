"""OpenVPN command construction and management.

this_file: src/nyord_vpn/network/vpn_commands.py

This module provides utilities for constructing and managing OpenVPN commands.
It centralizes all OpenVPN-related command construction to ensure consistency
and proper configuration across the application.

Key Features:
1. OpenVPNConfig dataclass for configuration management
2. Platform-specific command customization
3. Secure defaults for encryption and TLS
4. DNS leak prevention
5. Configuration validation
"""

import contextlib
import platform
import shutil
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

from loguru import logger

from nyord_vpn.exceptions import VPNConfigError

# Error message constants to avoid TRY003 linting issues
CONFIG_FILE_NOT_FOUND = "OpenVPN config file not found"
AUTH_FILE_NOT_FOUND = "OpenVPN auth file not found"
CANNOT_READ_FILES = "Cannot read OpenVPN files"
INVALID_VERBOSITY = "Invalid verbosity level (must be 1-6)"
INVALID_CONNECT_RETRY = "Invalid connect_retry value (must be >= 1)"
INVALID_CONNECT_TIMEOUT = "Invalid connect_timeout value (must be >= 1)"
INVALID_PING_INTERVAL = "Invalid ping_interval value (must be >= 1)"
INVALID_PING_RESTART = "Invalid ping_restart value (must be > ping_interval)"
OPENVPN_NOT_FOUND = "OpenVPN executable not found in PATH"


class OpenVPNVerbosity(Enum):
    """OpenVPN verbosity levels.

    These levels determine the amount of logging output from the OpenVPN process:
    - SILENT: Minimal output (errors only)
    - ERROR: Basic error information
    - WARNING: Errors and warnings
    - NORMAL: Standard connection information
    - DETAIL: Detailed connection information (default)
    - DEBUG: Comprehensive debugging information
    """

    SILENT = 1
    ERROR = 2
    WARNING = 3
    NORMAL = 4
    DETAIL = 5
    DEBUG = 6


@dataclass
class OpenVPNConfig:
    """Configuration for OpenVPN connection.

    This dataclass encapsulates all configuration parameters needed for establishing
    an OpenVPN connection, ensuring type safety and validation. It serves as a central
    place for all OpenVPN configuration parameters.

    Attributes:
        config_path: Path to OpenVPN config file
        auth_path: Path to authentication file
        log_path: Optional path to log file
        verbosity: Logging verbosity level (1-6)
        connect_retry: Number of connection retry attempts
        connect_timeout: Connection timeout in seconds
        ping_interval: Interval between ping tests in seconds
        ping_restart: Time without ping response before restart
        ciphers: List of encryption ciphers to use
        tls_ciphers: List of TLS cipher suites to use
        tls_min_version: Minimum TLS version to use
        auth_retry_behavior: Authentication retry behavior
        dns_servers: DNS servers to use (platform-specific)
        extra_options: Additional OpenVPN command-line options

    """

    # Required paths
    config_path: Path
    auth_path: Path

    # Optional paths
    log_path: Path | None = None

    # Connection parameters
    verbosity: OpenVPNVerbosity | int = OpenVPNVerbosity.DETAIL
    connect_retry: int = 2
    connect_timeout: int = 10
    ping_interval: int = 10
    ping_restart: int = 60

    # Security parameters
    ciphers: list[str] = field(
        default_factory=lambda: [
            "AES-256-GCM",
            "AES-128-GCM",
            "CHACHA20-POLY1305",
            "AES-256-CBC",
        ]
    )
    tls_ciphers: list[str] = field(
        default_factory=lambda: [
            "TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384",
            "TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256",
        ]
    )
    tls_min_version: str = "1.2"
    auth_retry_behavior: str = "nointeract"

    # DNS configuration
    dns_servers: list[str] = field(
        default_factory=lambda: [
            "103.86.96.100",  # NordVPN DNS
            "103.86.99.100",  # NordVPN DNS backup
        ]
    )

    # Additional options
    extra_options: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the configuration after initialization.

        Performs various validation checks on the configuration to ensure it is valid,
        including checking file existence, permissions, and parameter constraints.

        Raises:
            VPNConfigError: If any validation check fails

        """
        # Validate paths
        self._validate_paths()

        # Validate verbosity
        self._validate_verbosity()

        # Validate numeric parameters
        self._validate_numeric_params()

    def _validate_paths(self) -> None:
        """Validate file paths.

        Checks that required files exist and are accessible.

        Raises:
            VPNConfigError: If any path validation fails

        """
        # Convert to Path objects if strings were provided
        if isinstance(self.config_path, str):
            self.config_path = Path(self.config_path)
        if isinstance(self.auth_path, str):
            self.auth_path = Path(self.auth_path)
        if isinstance(self.log_path, str):
            self.log_path = Path(self.log_path)

        # Check if config file exists
        if not self.config_path.exists():
            raise VPNConfigError(f"{CONFIG_FILE_NOT_FOUND}: {self.config_path}")

        # Check if auth file exists
        if not self.auth_path.exists():
            raise VPNConfigError(f"{AUTH_FILE_NOT_FOUND}: {self.auth_path}")

        # Validate file permissions (should be readable)
        try:
            self.config_path.read_bytes()
            self.auth_path.read_bytes()
        except (PermissionError, OSError) as e:
            raise VPNConfigError(f"{CANNOT_READ_FILES}: {e}") from e

        # Create log directory if needed
        if self.log_path:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def _validate_verbosity(self) -> None:
        """Validate verbosity level.

        Ensures the verbosity level is either a valid enum value or an integer in the range 1-6.

        Raises:
            VPNConfigError: If verbosity validation fails

        """
        # Convert integer to enum if needed
        if isinstance(self.verbosity, int):
            if not 1 <= self.verbosity <= 6:
                raise VPNConfigError(f"{INVALID_VERBOSITY}: {self.verbosity}")
            # Convert to enum for consistent handling
            with contextlib.suppress(ValueError):
                self.verbosity = OpenVPNVerbosity(self.verbosity)

    def _validate_numeric_params(self) -> None:
        """Validate numeric parameters.

        Ensures that numeric parameters are within acceptable ranges.

        Raises:
            VPNConfigError: If any numeric parameter validation fails

        """
        # Connect retry should be positive
        if self.connect_retry < 1:
            raise VPNConfigError(f"{INVALID_CONNECT_RETRY}: {self.connect_retry}")

        # Connect timeout should be positive
        if self.connect_timeout < 1:
            raise VPNConfigError(f"{INVALID_CONNECT_TIMEOUT}: {self.connect_timeout}")

        # Ping interval should be positive
        if self.ping_interval < 1:
            raise VPNConfigError(f"{INVALID_PING_INTERVAL}: {self.ping_interval}")

        # Ping restart should be greater than ping interval
        if self.ping_restart <= self.ping_interval:
            raise VPNConfigError(
                f"{INVALID_PING_RESTART}: {self.ping_restart} (ping_interval: {self.ping_interval})"
            )


def get_openvpn_command(config: OpenVPNConfig) -> list[str]:
    """Construct OpenVPN command with all necessary arguments.

    This is the central place for OpenVPN command construction. It provides
    a comprehensive set of options for connection management, monitoring,
    and error handling.

    Args:
        config: OpenVPN configuration object

    Returns:
        List of command arguments for OpenVPN

    Raises:
        VPNConfigError: If OpenVPN executable is not found in PATH

    """
    # Check if openvpn is installed
    if not shutil.which("openvpn"):
        raise VPNConfigError(f"{OPENVPN_NOT_FOUND}. Please install OpenVPN first.")

    # Base command with common options
    cmd = [
        "openvpn",
        "--config",
        str(config.config_path),
        "--auth-user-pass",
        str(config.auth_path),
        "--verb",
        str(
            config.verbosity.value
            if isinstance(config.verbosity, OpenVPNVerbosity)
            else config.verbosity
        ),
        "--connect-retry",
        str(config.connect_retry),
        "--connect-timeout",
        str(config.connect_timeout),
        "--resolv-retry",
        "infinite",
        "--ping",
        str(config.ping_interval),
        "--ping-restart",
        str(config.ping_restart),
        "--script-security",
        "2",
        "--persist-tun",
        "--persist-key",
        "--nobind",
        "--fast-io",
    ]

    # Add security parameters
    cmd.extend(
        [
            "--data-ciphers",
            ":".join(config.ciphers),
            "--data-ciphers-fallback",
            config.ciphers[-1],  # Last cipher as fallback
            "--auth-retry",
            config.auth_retry_behavior,
            "--auth-nocache",
            "--pull-filter",
            "ignore",
            "auth-token",
            "--tls-version-min",
            config.tls_min_version,
            "--tls-cipher",
            ":".join(config.tls_ciphers),
        ]
    )

    # Platform-specific options
    system = platform.system().lower()
    if system == "darwin":  # macOS
        # Add macOS-specific options
        _add_macos_options(cmd, config)
    elif system == "linux":  # Linux
        # Add Linux-specific options
        _add_linux_options(cmd, config)
    elif system == "windows":  # Windows
        # Add Windows-specific options
        _add_windows_options(cmd, config)
    else:
        logger.warning(f"Unsupported platform: {system}. Using generic options.")
        # Add generic options for other platforms
        _add_generic_options(cmd, config)

    # Add log file if specified
    if config.log_path:
        cmd.extend(["--log", str(config.log_path)])

    # Add any extra options
    for key, value in config.extra_options.items():
        if value is True:
            # Boolean flag (--flag)
            cmd.append(f"--{key}")
        elif value is not None:
            # Option with value (--option value)
            cmd.append(f"--{key}")
            cmd.append(str(value))

    return cmd


def _add_macos_options(cmd: list[str], config: OpenVPNConfig) -> None:
    """Add macOS-specific OpenVPN options.

    Args:
        cmd: Command list to extend
        config: OpenVPN configuration

    """
    cmd.extend(
        [
            # Basic routing
            "--redirect-gateway",
            "def1",
        ]
    )

    # Add DNS configuration
    for dns_server in config.dns_servers:
        cmd.extend(["--dhcp-option", "DNS", dns_server])


def _add_linux_options(cmd: list[str], config: OpenVPNConfig) -> None:
    """Add Linux-specific OpenVPN options.

    Args:
        cmd: Command list to extend
        config: OpenVPN configuration

    """
    # Use standard Linux DNS update scripts if available
    resolv_conf_script = Path("/etc/openvpn/update-resolv-conf")
    if resolv_conf_script.exists():
        cmd.extend(
            [
                "--up",
                str(resolv_conf_script),
                "--down",
                str(resolv_conf_script),
            ]
        )

    cmd.extend(
        [
            # Enable routing
            "--redirect-gateway",  # Redirect all traffic through VPN
            "def1",  # Use default gateway
            "bypass-dhcp",  # Don't redirect DHCP
            "bypass-dns",  # Don't redirect DNS
        ]
    )

    # Add DNS configuration (if update-resolv-conf is not available)
    if not resolv_conf_script.exists():
        for dns_server in config.dns_servers:
            cmd.extend(["--dhcp-option", "DNS", dns_server])


def _add_windows_options(cmd: list[str], config: OpenVPNConfig) -> None:
    """Add Windows-specific OpenVPN options.

    Args:
        cmd: Command list to extend
        config: OpenVPN configuration

    """
    cmd.extend(
        [
            # Basic routing
            "--redirect-gateway",
            "def1",
        ]
    )

    # Add DNS configuration
    for dns_server in config.dns_servers:
        cmd.extend(["--dhcp-option", "DNS", dns_server])


def _add_generic_options(cmd: list[str], config: OpenVPNConfig) -> None:
    """Add generic OpenVPN options for unsupported platforms.

    Args:
        cmd: Command list to extend
        config: OpenVPN configuration

    """
    cmd.extend(
        [
            # Basic routing
            "--redirect-gateway",
            "def1",
        ]
    )

    # Add DNS configuration
    for dns_server in config.dns_servers:
        cmd.extend(["--dhcp-option", "DNS", dns_server])


# Example usage
def create_default_config(
    config_path: Path, auth_path: Path, log_path: Path | None = None
) -> OpenVPNConfig:
    """Create a default OpenVPN configuration.

    This is a helper function to create a default configuration with reasonable values.

    Args:
        config_path: Path to OpenVPN config file
        auth_path: Path to authentication file
        log_path: Optional path to log file

    Returns:
        A configured OpenVPNConfig object

    Raises:
        VPNConfigError: If validation fails

    """
    return OpenVPNConfig(
        config_path=config_path,
        auth_path=auth_path,
        log_path=log_path,
        verbosity=OpenVPNVerbosity.DETAIL,
        connect_retry=2,
        connect_timeout=10,
        ping_interval=10,
        ping_restart=60,
    )
