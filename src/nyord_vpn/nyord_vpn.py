#!/usr/bin/env -S uv run
# /// script
# dependencies = ["rich", "fire", "requests", "pydantic", "pycountry"]
# ///

"""
NordVPN CLI for MacOS - Python Implementation

This script provides a command-line interface for NordVPN on MacOS.
It requires OpenVPN to be installed (brew install openvpn).
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import random
from pathlib import Path
from typing import Any, cast

import fire
import pycountry
import requests
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
import contextlib

# Type definitions for pycountry
Country = Any  # pycountry doesn't expose proper types

# Constants
NORDVPN_CONFIG_DIR = Path("/etc/nordvpn_file")
OVPN_CONFIG_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"
RECOMMENDATIONS_URL = "https://api.nordvpn.com/v1/servers/recommendations"

# Browser-like headers to avoid 403
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://nordvpn.com/",
    "Origin": "https://nordvpn.com",
}

console = Console()

# Mapping of ISO 3166-1 alpha-2 codes to NordVPN country IDs
NORDVPN_COUNTRY_IDS: dict[str, str] = {
    "AL": "2",  # Albania
    "DZ": "3",  # Algeria
    "AD": "5",  # Andorra
    "AR": "10",  # Argentina
    "AM": "11",  # Armenia
    "AU": "13",  # Australia
    "AT": "14",  # Austria
    "AZ": "15",  # Azerbaijan
    "BS": "16",  # Bahamas
    "BD": "18",  # Bangladesh
    "BE": "21",  # Belgium
    "BZ": "22",  # Belize
    "BM": "24",  # Bermuda
    "BT": "25",  # Bhutan
    "BO": "26",  # Bolivia
    "BA": "27",  # Bosnia and Herzegovina
    "BR": "30",  # Brazil
    "BN": "32",  # Brunei
    "BG": "33",  # Bulgaria
    "KH": "36",  # Cambodia
    "CA": "38",  # Canada
    "KY": "40",  # Cayman Islands
    "CL": "43",  # Chile
    "CO": "47",  # Colombia
    "CR": "52",  # Costa Rica
    "HR": "54",  # Croatia
    "CY": "56",  # Cyprus
    "CZ": "57",  # Czech Republic
    "DK": "58",  # Denmark
    "DO": "61",  # Dominican Republic
    "EC": "63",  # Ecuador
    "EG": "64",  # Egypt
    "SV": "65",  # El Salvador
    "EE": "68",  # Estonia
    "FI": "73",  # Finland
    "FR": "74",  # France
    "GE": "80",  # Georgia
    "DE": "81",  # Germany
    "GH": "82",  # Ghana
    "GR": "84",  # Greece
    "GL": "85",  # Greenland
    "GU": "88",  # Guam
    "GT": "89",  # Guatemala
    "HN": "96",  # Honduras
    "HK": "97",  # Hong Kong
    "HU": "98",  # Hungary
    "IS": "99",  # Iceland
    "IN": "100",  # India
    "ID": "101",  # Indonesia
    "IE": "104",  # Ireland
    "IM": "243",  # Isle of Man
    "IL": "105",  # Israel
    "IT": "106",  # Italy
    "JM": "107",  # Jamaica
    "JP": "108",  # Japan
    "JE": "244",  # Jersey
    "KZ": "110",  # Kazakhstan
    "KE": "111",  # Kenya
    "LA": "118",  # Laos
    "LV": "119",  # Latvia
    "LB": "120",  # Lebanon
    "LI": "124",  # Liechtenstein
    "LT": "125",  # Lithuania
    "LU": "126",  # Luxembourg
    "MY": "131",  # Malaysia
    "MT": "134",  # Malta
    "MX": "140",  # Mexico
    "MD": "142",  # Moldova
    "MC": "143",  # Monaco
    "MN": "144",  # Mongolia
    "ME": "146",  # Montenegro
    "MA": "147",  # Morocco
    "MM": "149",  # Myanmar
    "NP": "152",  # Nepal
    "NL": "153",  # Netherlands
    "NZ": "156",  # New Zealand
    "NG": "159",  # Nigeria
    "MK": "128",  # North Macedonia
    "NO": "163",  # Norway
    "PK": "165",  # Pakistan
    "PA": "168",  # Panama
    "PG": "169",  # Papua New Guinea
    "PY": "170",  # Paraguay
    "PE": "171",  # Peru
    "PH": "172",  # Philippines
    "PL": "174",  # Poland
    "PT": "175",  # Portugal
    "PR": "176",  # Puerto Rico
    "RO": "179",  # Romania
    "RS": "192",  # Serbia
    "SG": "195",  # Singapore
    "SK": "196",  # Slovakia
    "SI": "197",  # Slovenia
    "ZA": "200",  # South Africa
    "KR": "114",  # South Korea
    "ES": "202",  # Spain
    "LK": "203",  # Sri Lanka
    "SE": "208",  # Sweden
    "CH": "209",  # Switzerland
    "TH": "214",  # Thailand
    "TT": "218",  # Trinidad and Tobago
    "TR": "220",  # Turkey
    "UA": "225",  # Ukraine
    "AE": "226",  # United Arab Emirates
    "GB": "227",  # United Kingdom
    "US": "228",  # United States
    "UY": "230",  # Uruguay
    "UZ": "231",  # Uzbekistan
    "VE": "233",  # Venezuela
    "VN": "234",  # Vietnam
}


def get_nordvpn_country_id(country_name: str) -> str | None:
    """Get NordVPN country ID from country name using pycountry."""
    # Try exact match first
    try:
        country = cast(Country, pycountry.countries.get(name=country_name))
        if country and hasattr(country, "alpha_2"):
            return NORDVPN_COUNTRY_IDS.get(country.alpha_2)

        # Try fuzzy search
        matches = pycountry.countries.search_fuzzy(country_name)
        if matches and hasattr(matches[0], "alpha_2"):
            return NORDVPN_COUNTRY_IDS.get(matches[0].alpha_2)
    except (LookupError, AttributeError):
        pass

    return None


class VPNError(Exception):
    """Base exception for VPN-related errors."""


class ServerNotFoundError(VPNError):
    """Raised when a VPN server cannot be found."""


class ConnectionError(VPNError):
    """Raised when connection to VPN fails."""


class DisconnectionError(VPNError):
    """Raised when disconnection from VPN fails."""


class ServerResponse(BaseModel):
    """Model for server recommendation response."""

    hostname: str


def check_command(cmd: str) -> bool:
    """Check if a command exists in the system."""
    return shutil.which(cmd) is not None


def get_public_ip() -> dict:
    """Get public IP information."""
    try:
        # Try multiple IP info services in case one fails
        services = [
            "https://ipinfo.io",
            "https://ip-api.com/json",
            "https://ipapi.co/json",
        ]
        for service in services:
            try:
                response = requests.get(service, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.RequestException:
                continue
        msg = "All IP info services failed"
        raise requests.RequestException(msg)
    except requests.RequestException as e:
        msg = f"Failed to get IP info: {e}"
        raise ConnectionError(msg)


def get_nordvpn_server(country: str = "United States") -> str:
    """Get recommended NordVPN server for a country."""
    # Check required commands
    if not check_command("curl"):
        msg = "curl not found. Install it with `brew install curl`"
        raise VPNError(msg)
    if not check_command("jq"):
        msg = "jq not found. Install it with `brew install jq`"
        raise VPNError(msg)

    country_id = get_nordvpn_country_id(country)
    if not country_id:
        console.print(
            "[yellow]Warning: Using server from closest location/country[/yellow]"
        )
        country_id = "US"

    # Parameters for the API request
    params: dict[str, str] = {
        "filters[country_id]": country_id,
        "filters[servers_technologies][identifier]": "openvpn_tcp",
        "limit": "5",  # Get top 5 servers to show stats
    }

    try:
        response = requests.get(
            RECOMMENDATIONS_URL, params=params, headers=HEADERS, timeout=10
        )
        response.raise_for_status()
    except requests.RequestException as e:
        msg = f"Failed to get server for {country}: {e}"
        raise ServerNotFoundError(msg)

    try:
        data = response.json()
        if not isinstance(data, list) or not data:
            msg = f"No servers available for {country}"
            raise ServerNotFoundError(msg)

        # Show server stats
        console.print(f"\n[blue]Available servers in {country}:[/blue]")
        for server in data:
            load = server.get("load", 0)
            hostname = server.get("hostname", "")
            console.print(
                f"[cyan]Server:[/cyan] {hostname}\n[cyan]Load:[/cyan] {load}%"
            )
        console.print()  # Empty line for readability

        # Select the server with lowest load
        server_data = min(data, key=lambda x: x.get("load", 100))
        hostname = server_data.get("hostname")
        if not isinstance(hostname, str) or not hostname:
            msg = f"Invalid server data received for {country}"
            raise ServerNotFoundError(msg)

        return f"{hostname}.tcp"
    except (json.JSONDecodeError, IndexError, KeyError, ValueError) as e:
        msg = f"Invalid response for {country}: {e}"
        raise ServerNotFoundError(msg)


def wait_for_connection(server_name: str, timeout: int = 60) -> dict:
    """Wait for VPN connection to be established and return IP info."""
    start_time = time.time()
    last_error = None
    console.print("[yellow]Waiting for connection to establish...[/yellow]")

    # Get initial IP info for comparison
    try:
        initial_ip = get_public_ip().get("ip")
    except requests.RequestException:
        initial_ip = None

    while time.time() - start_time < timeout:
        try:
            # Check OpenVPN process and its status
            openvpn_status = subprocess.run(
                ["ps", "aux"], capture_output=True, text=True, check=True
            ).stdout

            if "openvpn" not in openvpn_status:
                msg = "OpenVPN process died unexpectedly"
                raise ConnectionError(msg)

            # Check for OpenVPN errors in system log
            try:
                log_output = subprocess.run(
                    ["sudo", "grep", "openvpn", "/var/log/system.log", "-n", "10"],
                    capture_output=True,
                    text=True, check=False,
                ).stdout
                if "error" in log_output.lower():
                    console.print(
                        f"[yellow]OpenVPN reported errors: {log_output.strip()}[/yellow]"
                    )
            except subprocess.CalledProcessError:
                pass  # Ignore log reading errors

            # Then check IP info
            ip_info = get_public_ip()
            current_ip = ip_info.get("ip")

            # First success criterion: IP has changed
            if initial_ip and current_ip and initial_ip != current_ip:
                console.print(
                    "[green]IP address has changed - VPN appears active[/green]"
                )
                return ip_info

            # Second success criterion: ISP/Organization indicates NordVPN
            org = ip_info.get("org", "").lower()
            isp = ip_info.get("isp", "").lower()
            if any(x in (org + isp) for x in ["nordvpn", "nord", "tefincom"]):
                return ip_info

            # Check DNS resolution
            try:
                subprocess.run(
                    ["dig", "+short", "google.com"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=2,
                    check=True,
                )
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                console.print(
                    "[yellow]Warning: DNS resolution issues detected[/yellow]"
                )

            console.print("[yellow]Waiting for VPN connection...[/yellow]")
        except requests.RequestException as e:
            last_error = e
            console.print(f"[yellow]Still trying to connect: {e}[/yellow]")
        except ConnectionError as e:
            msg = f"OpenVPN connection failed: {e}"
            raise ConnectionError(msg)
        except KeyboardInterrupt:
            console.print("\n[red]Connection attempt interrupted by user[/red]")
            raise

        time.sleep(2)  # Sleep between checks

    msg = (
        f"Timeout waiting for connection to {server_name}. "
        f"Last error: {last_error if last_error else 'Could not verify VPN connection'}"
    )
    raise ConnectionError(
        msg
    )


def check_credential_file(path: Path) -> None:
    """Check if credential file exists and has secure permissions."""
    if not path.is_file():
        msg = f"Credential file not found: {path}"
        raise VPNError(msg)

    # Check file permissions (should be 600)
    stat = path.stat()
    if stat.st_mode & 0o777 != 0o600:
        msg = (
            f"Insecure permissions on credential file: {path}\n"
            "Please run: chmod 600 {path}"
        )
        raise VPNError(
            msg
        )

    # Check file ownership
    if stat.st_uid != os.getuid():
        msg = (
            f"Credential file {path} is not owned by the current user.\n"
            "Please ensure you own the file."
        )
        raise VPNError(
            msg
        )


def setup_config_directory() -> None:
    """Setup NordVPN configuration directory with proper permissions."""
    if NORDVPN_CONFIG_DIR.is_dir():
        return

    console.print("[yellow]Downloading OpenVPN configurations...[/yellow]")
    console.print("[blue]Please enter your system password (sudo) when prompted[/blue]")

    # Create directory with sudo
    try:
        subprocess.run(["sudo", "mkdir", "-p", str(NORDVPN_CONFIG_DIR)], check=True)
        subprocess.run(
            ["sudo", "chown", str(os.getuid()), str(NORDVPN_CONFIG_DIR)], check=True
        )
    except subprocess.CalledProcessError as e:
        msg = f"Failed to create config directory: {e}"
        raise VPNError(msg)

    # Download and extract configurations
    try:
        response = requests.get(OVPN_CONFIG_URL, timeout=30)
        response.raise_for_status()

        zip_path = NORDVPN_CONFIG_DIR / "ovpn.zip"
        zip_path.write_bytes(response.content)

        subprocess.run(
            ["unzip", "-qq", str(zip_path), "-d", str(NORDVPN_CONFIG_DIR)],
            check=True,
        )
        zip_path.unlink()

        udp_dir = NORDVPN_CONFIG_DIR / "ovpn_udp"
        if udp_dir.exists():
            shutil.rmtree(udp_dir)
    except (requests.RequestException, subprocess.CalledProcessError) as e:
        msg = f"Failed to download/extract configurations: {e}"
        raise VPNError(msg)


def get_random_country() -> str:
    """Get a random country from the available countries."""
    # Get a random country from pycountry that has a NordVPN ID
    available_countries = [
        cast(str, country.name)
        for country in pycountry.countries
        if hasattr(country, "alpha_2")
        and country.alpha_2 in NORDVPN_COUNTRY_IDS
    ]
    return random.choice(available_countries)


def create_temp_auth_file() -> tuple[Path, bool]:
    """Create a temporary auth file from environment variables.

    Returns:
        tuple[Path, bool]: (Path to auth file, True if temporary file was created)
    """
    login = os.environ.get("NORDVPN_LOGIN")
    password = os.environ.get("NORDVPN_PASSWORD")

    if not login or not password:
        return Path.home() / ".nordvpn_cred", False

    # Create a secure temporary file
    temp_auth = Path(tempfile.mkstemp(prefix="nordvpn_", suffix=".auth")[1])
    temp_auth.write_text(f"{login}\n{password}")
    temp_auth.chmod(0o600)

    return temp_auth, True


def connect_nordvpn(
    country: str = "United States",
    auth_file: str | Path | None = None,
    auth_login: str | None = None,
    auth_password: str | None = None,
    random_country: bool = False,
) -> None:
    """Connect to NordVPN using OpenVPN.

    Args:
        country: Country to connect to (default: United States)
        auth_file: Path to credentials file (default: ~/.nordvpn_cred)
        auth_login: NordVPN username (overrides auth_file)
        auth_password: NordVPN password (overrides auth_file)
        random_country: If True, connects to a random country (ignores country parameter)
    """
    # Handle authentication priority:
    # 1. Command line credentials (auth_login + auth_password)
    # 2. Environment variables (NORDVPN_LOGIN + NORDVPN_PASSWORD)
    # 3. Auth file (provided or default ~/.nordvpn_cred)

    temp_auth_created = False
    cred_file = None
    log_dir = None

    try:
        if auth_login and auth_password:
            # Create temporary file from command line credentials
            temp_auth = Path(tempfile.mkstemp(prefix="nordvpn_", suffix=".auth")[1])
            temp_auth.write_text(f"{auth_login}\n{auth_password}")
            temp_auth.chmod(0o600)
            cred_file = temp_auth
            temp_auth_created = True
        else:
            # Try environment variables or fall back to auth file
            cred_file, temp_auth_created = create_temp_auth_file()
            if not temp_auth_created:
                # Use provided auth file or default
                cred_file = Path(
                    str(auth_file) if auth_file else Path.home() / ".nordvpn_cred"
                )

        # Handle random country selection
        if random_country:
            country = get_random_country()
            console.print(f"[blue]Selected random country: {country}[/blue]")

        # Check required commands
        for cmd in ["openvpn", "ps"]:
            if not check_command(cmd):
                msg = f"{cmd} not found. Install it with `brew install {cmd}`"
                raise VPNError(msg)

        # Validate credential file
        check_credential_file(cred_file)

        # Disconnect any existing connection
        try:
            disconnect_nordvpn()
            time.sleep(2)  # Wait for cleanup
        except DisconnectionError:
            pass  # Ignore if not connected

        # Get server
        server_name = get_nordvpn_server(country)

        # Setup NordVPN files if needed
        setup_config_directory()

        # Verify config file exists
        config_file = NORDVPN_CONFIG_DIR / "ovpn_tcp" / f"{server_name}.ovpn"
        if not config_file.is_file():
            msg = f"Config file not found: {config_file}"
            raise VPNError(msg)

        # Create log file in a secure temporary directory
        log_dir = Path(tempfile.mkdtemp(prefix="nordvpn_"))
        log_file = log_dir / "openvpn.log"

        # Connect using OpenVPN
        console.print(f"[yellow]Connecting to {server_name}...[/yellow]")
        console.print(
            "[blue]Please enter your system password (sudo) when prompted[/blue]"
        )
        try:
            # Add verbosity to OpenVPN for better diagnostics
            subprocess.run(
                [
                    "sudo",
                    "openvpn",
                    "--config",
                    str(config_file),
                    "--auth-user-pass",
                    str(cred_file),
                    "--daemon",
                    "--verb",
                    "3",  # Increased verbosity
                    "--connect-retry",
                    "2",  # Retry connection twice
                    "--connect-timeout",
                    "10",  # 10 seconds connection timeout
                    "--resolv-retry",
                    "infinite",  # Keep trying to resolve DNS
                    "--log",
                    str(log_file),  # Log to file for debugging
                    "--ping",
                    "10",  # Send ping every 10 seconds
                    "--ping-restart",
                    "60",  # Restart if no ping response for 60 seconds
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            msg = f"Failed to connect to {server_name}: {e}"
            raise ConnectionError(msg)

        # Wait for connection and show IP
        try:
            ip_info = wait_for_connection(server_name)
            console.print(
                Panel.fit(
                    f"[green]Connected to {server_name}[/green]\n"
                    f"IP: {ip_info.get('ip')}\n"
                    f"Location: {ip_info.get('city', '')}, {ip_info.get('country', '')}\n"
                    f"ISP: {ip_info.get('org', '')}"
                )
            )
        except (ConnectionError, KeyboardInterrupt) as e:
            # Try to disconnect in case of timeout or interruption
            with contextlib.suppress(DisconnectionError):
                disconnect_nordvpn()
            if isinstance(e, KeyboardInterrupt):
                console.print("\n[red]Connection attempt cancelled by user[/red]")
                sys.exit(1)
            raise ConnectionError(str(e))
    except Exception as e:
        # Handle any unexpected errors
        if isinstance(e, ConnectionError | VPNError):
            raise
        msg = f"Unexpected error: {e}"
        raise VPNError(msg)
    finally:
        # Clean up temporary files
        if temp_auth_created and cred_file:
            with contextlib.suppress(OSError):
                cred_file.unlink()
        if log_dir:
            with contextlib.suppress(OSError):
                shutil.rmtree(log_dir)


def disconnect_nordvpn() -> None:
    """Disconnect from NordVPN."""
    try:
        subprocess.run(["sudo", "pkill", "openvpn"], check=True)
        console.print("[green]NordVPN disconnected successfully[/green]")
    except subprocess.CalledProcessError as e:
        msg = f"Failed to disconnect: {e}"
        raise DisconnectionError(msg)


def get_connection_status() -> None:
    """Get current VPN connection status."""
    try:
        # Check if OpenVPN is running
        openvpn_status = subprocess.run(
            ["ps", "aux"], capture_output=True, text=True, check=True
        ).stdout

        if "openvpn" not in openvpn_status:
            console.print("[yellow]Not connected to VPN[/yellow]")
            return

        # Get current IP info
        ip_info = get_public_ip()
        org = ip_info.get("org", "").lower()
        isp = ip_info.get("isp", "").lower()

        if any(x in (org + isp) for x in ["nordvpn", "nord", "tefincom"]):
            console.print(
                Panel.fit(
                    "[green]Connected to NordVPN[/green]\n"
                    f"IP: {ip_info.get('ip')}\n"
                    f"Location: {ip_info.get('city', '')}, {ip_info.get('country', '')}\n"
                    f"ISP: {ip_info.get('org', '')}"
                )
            )
        else:
            console.print("[yellow]Connected, but not through NordVPN[/yellow]")
            console.print(f"Current IP: {ip_info.get('ip')}")
    except Exception as e:
        console.print(f"[red]Error checking status: {e}[/red]")


def main():
    """CLI entry point."""
    try:
        fire.Fire(
            {
                "connect": lambda country="United States",
                auth_file=None,
                auth_login=None,
                auth_password=None,
                random=False: connect_nordvpn(
                    country=country,
                    auth_file=auth_file,
                    auth_login=auth_login,
                    auth_password=auth_password,
                    random_country=random,
                ),
                "disconnect": disconnect_nordvpn,
                "ip": lambda: console.print(get_public_ip()),
                "status": get_connection_status,
                "list-countries": lambda: console.print(
                    "\n".join(
                        sorted(
                            cast(str, country.name)
                            for country in pycountry.countries
                            if hasattr(country, "alpha_2")
                            and country.alpha_2 in NORDVPN_COUNTRY_IDS
                        )
                    )
                ),
            }
        )
    except KeyboardInterrupt:
        console.print("\n[red]Operation cancelled by user[/red]")
        with contextlib.suppress(DisconnectionError):
            disconnect_nordvpn()
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        with contextlib.suppress(DisconnectionError):
            disconnect_nordvpn()
        sys.exit(1)


if __name__ == "__main__":
    main()
