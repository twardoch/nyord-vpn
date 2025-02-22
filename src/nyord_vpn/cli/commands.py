"""CLI interface for VPN client."""

import asyncio
from pathlib import Path
import sys
from typing import NoReturn

import fire
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from nyord_vpn.core.client import VPNClient
from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.logging import log_error, log_success, setup_logging

console = Console()


def exit_with_error(message: str, error: Exception | None = None) -> NoReturn:
    """Exit with error message and optional exception."""
    log_error(message)
    if error:
        console.print(f"[red]Details: {error}[/red]")
    sys.exit(1)


class CLI:
    """CLI interface for VPN operations."""

    def __init__(
        self,
        config: str | None = None,
        username: str | None = None,
        password: str | None = None,
        log_file: str | None = None,
    ):
        """Initialize CLI.

        Args:
            config: Optional path to config file
            username: Optional username
            password: Optional password
            log_file: Optional path to log file
        """
        self.config = Path(config) if config else None
        self.username = username
        self.password = password
        self.log_file = Path(log_file) if log_file else None
        self.logger = setup_logging(log_file=self.log_file)

    async def _get_client(self) -> VPNClient:
        """Get VPN client instance."""
        return VPNClient(
            config_file=self.config,
            username=self.username,
            password=self.password,
            log_file=self.log_file,
        )

    def connect(self, country: str | None = None) -> None:
        """Connect to VPN.

        Args:
            country: Optional country to connect to
        """

        async def _connect():
            async with await self._get_client() as client:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                ) as progress:
                    task = progress.add_task(
                        f"Connecting to VPN{f' in {country}' if country else ''}..."
                    )
                    await client.connect(country)
                    progress.update(task, completed=True)

                # Show status after connection
                status = await client.status()
                console.print(
                    Panel.fit(
                        f"[green]Connected to VPN[/green]\n"
                        f"IP: {status['ip']}\n"
                        f"Country: {status['country']}\n"
                        f"Server: {status['server']}"
                    )
                )

        try:
            asyncio.run(_connect())
        except VPNError as e:
            exit_with_error("Failed to connect", e)
        except asyncio.CancelledError as e:
            exit_with_error("Connection cancelled", e)
        except Exception as e:
            exit_with_error("Unexpected error during connection", e)

    def disconnect(self) -> None:
        """Disconnect from VPN."""

        async def _disconnect():
            async with await self._get_client() as client:
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                ) as progress:
                    task = progress.add_task("Disconnecting from VPN...")
                    await client.disconnect()
                    progress.update(task, completed=True)

        try:
            asyncio.run(_disconnect())
            log_success("Disconnected from VPN")
        except VPNError as e:
            exit_with_error("Failed to disconnect", e)
        except asyncio.CancelledError as e:
            exit_with_error("Disconnection cancelled", e)
        except Exception as e:
            exit_with_error("Unexpected error during disconnection", e)

    def status(self) -> None:
        """Show VPN connection status."""

        async def _status():
            async with await self._get_client() as client:
                status = await client.status()
                console.print(
                    Panel.fit(
                        f"VPN Status: [{'green' if status['connected'] else 'red'}]"
                        f"{'Connected' if status['connected'] else 'Disconnected'}[/]\n"
                        f"IP: {status['ip']}\n"
                        f"Country: {status['country']}\n"
                        f"Server: {status['server']}"
                    )
                )

        try:
            asyncio.run(_status())
        except VPNError as e:
            exit_with_error("Failed to get status", e)
        except asyncio.CancelledError as e:
            exit_with_error("Status check cancelled", e)
        except Exception as e:
            exit_with_error("Unexpected error while checking status", e)

    def list_countries(self) -> None:
        """List available countries."""

        async def _list():
            async with await self._get_client() as client:
                countries = await client.list_countries()
                console.print("\n[bold]Available Countries:[/bold]")
                for country in sorted(countries):
                    console.print(f"  • {country}")

        try:
            asyncio.run(_list())
        except VPNError as e:
            exit_with_error("Failed to list countries", e)
        except asyncio.CancelledError as e:
            exit_with_error("Country listing cancelled", e)
        except Exception as e:
            exit_with_error("Unexpected error while listing countries", e)


def main() -> None:
    """CLI entry point."""
    try:
        fire.Fire(CLI)
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        exit_with_error("Unexpected error", e)


if __name__ == "__main__":
    main()
