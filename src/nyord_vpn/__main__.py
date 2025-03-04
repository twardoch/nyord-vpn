"""Command line interface for nyord-vpn."""

import os
import sys

import fire
from dotenv import load_dotenv
from rich.console import Console

from nyord_vpn.core.client import Client, VPNError
from nyord_vpn.scripts.update_countries import fetch_countries
from nyord_vpn.utils.utils import check_root

console = Console()

# Load environment variables
load_dotenv()


class CLI:
    """NordVPN CLI interface."""

    def __init__(self, verbose: bool = False) -> None:
        """Initialize CLI.

        Args:
            verbose: Whether to show verbose output

        """
        try:
            # Get credentials from environment
            username = os.getenv("NORD_USER") or os.getenv("NORDVPN_LOGIN")
            password = os.getenv("NORD_PASSWORD") or os.getenv("NORDVPN_PASSWORD")

            if not username or not password:
                console.print("[red]Error: Missing credentials[/red]")
                console.print("Please set the following environment variables:")
                console.print("  NORD_USER or NORDVPN_LOGIN")
                console.print("  NORD_PASSWORD or NORDVPN_PASSWORD")
                sys.exit(1)

            # Initialize client with verbose flag
            self.client = Client(username, password, verbose=verbose)
            self.verbose = verbose
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def go(self, country_code: str) -> None:
        """Connect to VPN in specified country."""
        check_root()
        try:
            self.client.go(country_code)
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def bye(self) -> None:
        """Disconnect from VPN."""
        check_root()
        try:
            self.client.bye()
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def info(self) -> None:
        """Display current VPN status."""
        try:
            self.client.info()
        except VPNError as e:
            console.print(f"[red]Error:[/red] {e}")
            sys.exit(1)

    def update(self) -> None:
        """Update country information."""
        try:
            fetch_countries()
            if self.verbose:
                console.print("[green]Successfully updated country information[/green]")
        except Exception as e:
            console.print(f"[red]Error updating country information:[/red] {e}")
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
