"""Configuration management for VPN client."""

from pathlib import Path
import json

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

    @classmethod
    def from_file(cls, config_file: Path) -> "VPNConfig":
        """Load configuration from a JSON file.

        Args:
            config_file: Path to the configuration file

        Returns:
            VPNConfig: Configuration object

        Raises:
            FileNotFoundError: If the config file doesn't exist
            json.JSONDecodeError: If the config file is invalid JSON
            ValueError: If the configuration is invalid
        """
        if not config_file.exists():
            msg = f"Config file not found: {config_file}"
            raise FileNotFoundError(msg)

        try:
            config_data = json.loads(config_file.read_text())
            return cls(**config_data)
        except json.JSONDecodeError as e:
            msg = f"Invalid JSON in config file: {e}"
            raise json.JSONDecodeError(
                msg, e.doc, e.pos
            ) from e
        except Exception as e:
            msg = f"Failed to load config from file: {e}"
            raise ValueError(msg) from e

    @classmethod
    def from_env(cls) -> "VPNConfig":
        """Load configuration from environment variables.

        Returns:
            VPNConfig: Configuration object

        Raises:
            ValueError: If required environment variables are missing or invalid
        """
        try:
            return cls()
        except Exception as e:
            msg = f"Failed to load config from environment: {e}"
            raise ValueError(msg) from e


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
            return VPNConfig.from_file(config_file)
        return VPNConfig.from_env()
    except Exception as e:
        msg = f"Failed to load configuration: {e}"
        raise VPNConfigError(msg) from e
