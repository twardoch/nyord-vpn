"""Command line interface for nyord-vpn."""

import os
import sys
from typing import List, Optional
import json
from datetime import datetime
import subprocess

import fire
from rich.console import Console
from rich.table import Table

from .client import Client, VPNError
from .scripts.update_countries import fetch_countries

console = Console()


def _check_root() -> None:
    """Request root privileges using sudo."""
    if os.geteuid() != 0:
        try:
            # Re-run the script with sudo
            args = ["sudo", sys.executable] + sys.argv
            subprocess.run(args, check=True)
            sys.exit(0)
        except subprocess.CalledProcessError:
            console.print("[red]Error: This command requires root privileges.[/red]")
            console.print("[yellow]Please run the command again with sudo:[/yellow]")
            console.print(f"[blue]sudo {' '.join(sys.argv)}[/blue]")
            sys.exit(1)


class CLI:
    """NordVPN CLI interface."""

    def __init__(self, verbose: bool = False):
        """Initialize CLI."""
        try:
            self.client = Client(verbose=verbose)
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def go(self, country_code: str) -> None:
        """Connect to VPN in specified country.

        Args:
            country_code: Two-letter country code (e.g. 'us', 'uk')
        """
        _check_root()
        try:
            self.client.go(country_code)
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def bye(self) -> None:
        """Disconnect from VPN."""
        _check_root()
        try:
            self.client.disconnect()
            console.print("[green]Successfully disconnected from VPN[/green]")
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def info(self) -> None:
        """Show current connection info."""
        try:
            status = self.client.status()
            if status:
                console.print(f"[green]Connected to:[/green] {status}")
            else:
                console.print("[yellow]Not connected to VPN[/yellow]")
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def where(self, live: bool = False) -> None:
        """List available countries.

        Args:
            live: If True, fetch fresh data from API instead of using cache
        """
        try:
            if live:
                countries = fetch_countries()
            else:
                countries = self.client.countries

            table = Table(title="Available Countries")
            table.add_column("Country", style="cyan")
            table.add_column("Code", style="yellow")
            table.add_column("Servers", justify="right", style="green")

            for country in sorted(countries, key=lambda x: x["name"]):
                table.add_row(
                    country["name"],
                    country["code"].lower(),
                    str(country["serverCount"]),
                )

            console.print(table)
            total_servers = sum(country["serverCount"] for country in countries)
            console.print(
                f"\nTotal: [cyan]{len(countries)}[/cyan] countries, [green]{total_servers}[/green] servers"
            )

        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def update(self) -> None:
        """Update country list from NordVPN API."""
        try:
            countries = fetch_countries()
            with open(self.client.cache_file, "w") as f:
                json.dump(
                    {"countries": countries, "last_updated": str(datetime.now())},
                    f,
                    indent=2,
                )
            console.print("[green]Successfully updated country list[/green]")
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)


def main() -> None:
    """Main entry point."""
    try:
        fire.Fire(CLI)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
