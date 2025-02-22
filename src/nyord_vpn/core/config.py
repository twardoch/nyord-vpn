"""Configuration management for VPN client."""

from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from nyord_vpn.core.exceptions import VPNConfigError


class VPNConfig(BaseSettings):
    """VPN configuration settings."""

    # Credentials
    username: str
    password: SecretStr

    # Connection settings
    default_country: str = "United States"
    retry_attempts: int = 3
    use_legacy_fallback: bool = True

    # Paths
    config_dir: Path = Path.home() / ".config" / "nyord-vpn"

    # API settings
    api_timeout: int = 30

    model_config = SettingsConfigDict(
        env_prefix="NORDVPN_",
        case_sensitive=False,
        env_file=None,
        env_file_encoding="utf-8",
    )

    def __init__(self, **kwargs):
        """Initialize config and ensure directories exist."""
        super().__init__(**kwargs)
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            self.config_dir.chmod(0o700)  # Secure permissions
        except Exception as e:
            msg = f"Failed to setup config directory: {e}"
            raise VPNConfigError(msg) from e


def load_config(config_file: Path | None = None) -> VPNConfig:
    """Load configuration from file and/or environment.

    Args:
        config_file: Optional path to config file

    Returns:
        VPNConfig: Configuration object

    Raises:
        VPNConfigError: If configuration is invalid
    """
    try:
        if config_file:
            return VPNConfig(_env_file=config_file)
        return VPNConfig()
    except Exception as e:
        msg = f"Failed to load configuration: {e}"
        raise VPNConfigError(msg) from e
