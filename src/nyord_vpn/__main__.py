"""CLI interface for VPN operations.

Usage:
    nyord-vpn [--api=<api>] [--verbose] <command> [<args>...]
    
Commands:
    connect [<country>]    Connect to VPN in specified country (optional). Requires administrator password.
    disconnect            Disconnect from VPN. Requires administrator password.
    status               Show current VPN connection status
    list-countries       List available countries

Options:
    --api=<api>         API to use: 'legacy' or 'njord' [default: legacy]
    --verbose           Enable debug logging [default: False]

Environment Variables:
    NORD_USER          NordVPN username (required)
    NORD_PASSWORD      NordVPN password (required)

Note:
    The connect and disconnect commands require administrator/sudo access to configure
    system networking. You will be prompted for your administrator password.
"""

import sys
from typing import Literal, cast

import fire
from loguru import logger
from rich.prompt import Prompt

from nyord_vpn.core.exceptions import VPNError, VPNConfigError
from nyord_vpn.core.factory import create_client


def setup_logging(verbose: bool = False) -> None:
    """Set up logging configuration.

    Args:
        verbose: Whether to enable debug logging
    """
    logger.remove()
    logger.add(
        sys.stderr,
        format="<level>{message}</level>",
        level="DEBUG" if verbose else "INFO",
    )


class CLI:
    """VPN CLI interface."""

    def __init__(self, api: str = "legacy", verbose: bool = False) -> None:
        """Initialize CLI.

        Args:
            api: API to use (legacy or njord)
            verbose: Enable verbose logging

        Raises:
            VPNConfigError: If API type is invalid
        """
        setup_logging(verbose)
        if api not in ("legacy", "njord"):
            msg = "API must be 'legacy' or 'njord'"
            raise VPNConfigError(msg)
        try:
            self._client = create_client(cast(Literal["legacy", "njord"], api))
        except VPNError as e:
            logger.error(f"Failed to initialize client: {e}")
            sys.exit(1)

    def connect(self, country: str | None = None) -> None:
        """Connect to VPN.

        Args:
            country: Optional country to connect to
        """
        try:
            logger.info(
                "Requesting administrator password to configure VPN connection..."
            )
            self._client.connect(country)
            status = self._client.status()
            logger.info(
                f"Connected to {status['server']} ({status['ip']}, {status['country']})"
            )
        except VPNError as e:
            if "RetryError" in str(e):
                logger.error(
                    "Failed to connect: VPN server is not responding. Please try again later or try a different server."
                )
            else:
                logger.error(f"Failed to connect: {e}")
            sys.exit(1)

    def disconnect(self) -> None:
        """Disconnect from VPN."""
        try:
            logger.info("Requesting administrator password to disconnect VPN...")
            self._client.disconnect()
            logger.info("Disconnected from VPN")
        except VPNError as e:
            logger.error(f"Failed to disconnect: {e}")
            sys.exit(1)

    def status(self) -> None:
        """Show VPN status."""
        try:
            status = self._client.status()
            if status["connected"]:
                logger.info(
                    f"Connected to {status['server']} "
                    f"({status['ip']}, {status['country']})"
                )
            else:
                logger.info("Not connected to VPN")
        except VPNError as e:
            logger.error(f"Failed to get status: {e}")
            sys.exit(1)

    def list_countries(self) -> None:
        """List available countries."""
        try:
            countries = self._client.list_countries()
            for country in countries:
                logger.info(f"{country['name']} ({country['code']})")
        except VPNError as e:
            logger.error(f"Failed to list countries: {e}")
            sys.exit(1)

    # Hide client attribute from Fire's command discovery
    @property
    def client(self) -> None:
        """Hide client attribute from Fire's command discovery."""
        return None


def main() -> None:
    """CLI entry point."""
    try:
        fire.Fire(CLI)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
