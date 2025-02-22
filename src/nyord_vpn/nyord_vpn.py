#!/usr/bin/env -S uv run
# /// script
# dependencies = ["rich", "fire", "requests", "pydantic", "pycountry"]
# ///

"""
NordVPN CLI for MacOS - Python Implementation

This script provides a command-line interface for NordVPN on MacOS.
It requires OpenVPN to be installed (brew install openvpn).
"""

import os
import shutil
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, NoReturn

import fire
import pycountry
import requests
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from nyord_vpn.utils.system import run_subprocess_safely

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
    """Get NordVPN country ID from country name."""
    try:
        country = pycountry.countries.lookup(country_name)
        if not country:
            return None
        return country.alpha_2.lower()
    except LookupError:
        return None


class VPNError(Exception):
    """Base exception for VPN-related errors."""


class ServerNotFoundError(VPNError):
    """Raised when a VPN server cannot be found."""


class VPNConnectionError(VPNError):
    """Raised when connection to VPN fails."""


class DisconnectionError(VPNError):
    """Raised when disconnection from VPN fails."""


class ServerResponse(BaseModel):
    """Model for server recommendation response."""

    hostname: str


def check_command(cmd: str) -> tuple[bool, str]:
    """Check if a command exists in the system and return its absolute path."""
    cmd_path = shutil.which(cmd)
    return (bool(cmd_path), cmd_path or "")


def _raise_ip_info_error(error: Exception) -> NoReturn:
    msg = f"Failed to get IP info: {error}"
    raise VPNConnectionError(msg) from error


def _raise_service_error() -> NoReturn:
    msg = "All IP info services failed"
    raise requests.RequestException(msg)


def get_public_ip() -> dict:
    """Get public IP information from various services."""
    services = [
        "https://ipinfo.io/json",
        "https://api.ipify.org?format=json",
        "https://api.myip.com",
    ]

    try:
        for service in services:
            try:
                response = requests.get(service, timeout=5, headers=HEADERS)
                response.raise_for_status()
                if not response.json():
                    continue
                return response.json()
            except requests.RequestException:
                continue
        return _raise_service_error()
    except requests.RequestException as e:
        return _raise_ip_info_error(e)


def _raise_server_not_found(country: str) -> NoReturn:
    msg = f"No servers found for country: {country}"
    raise ServerNotFoundError(msg)


def _raise_server_error(error: Exception) -> NoReturn:
    msg = f"Failed to get server recommendation: {error}"
    raise VPNConnectionError(msg) from error


def _raise_connection_error(error: Exception, server: str) -> NoReturn:
    msg = f"Failed to connect to {server}: {error}"
    raise VPNConnectionError(msg) from error


def _raise_disconnect_error(error: Exception) -> NoReturn:
    msg = f"Failed to disconnect: {error}"
    raise DisconnectionError(msg) from error


def _raise_config_error(error: Exception) -> NoReturn:
    msg = f"Failed to setup configuration: {error}"
    raise VPNError(msg) from error


def _raise_auth_error(error: Exception) -> NoReturn:
    msg = f"Failed to setup authentication: {error}"
    raise VPNError(msg) from error


def _raise_validation_error(error: Exception) -> NoReturn:
    msg = f"Failed to validate paths: {error}"
    raise VPNError(msg) from error


def _raise_config_file_error(path: Path) -> NoReturn:
    """Raise a VPNError with a descriptive message."""
    msg = f"Config file not found: {path}"
    raise VPNError(msg)


def get_nordvpn_server(country: str = "United States") -> str:
    """Get recommended NordVPN server for a country."""
    try:
        country_id = get_nordvpn_country_id(country)
        if not country_id:
            _raise_server_not_found(country)
        else:
            url = f"{RECOMMENDATIONS_URL}"
            params = {
                "filters[country_id]": country_id,
                "filters[servers_technologies][identifier]": "openvpn_udp",
                "filters[servers_groups][identifier]": "legacy_standard",
                "limit": 1,
            }

            response = requests.get(url, params=params, timeout=10, headers=HEADERS)
            response.raise_for_status()
            data = response.json()

            if not data:
                _raise_server_not_found(country)
            else:
                return data[0]["hostname"]
    except requests.RequestException as e:
        _raise_server_error(e)


def wait_for_connection(server_name: str, timeout: int = 60) -> dict:
    """Wait for VPN connection to be established."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            ip_info = get_public_ip()
            if ip_info.get("hostname", "").endswith("nordvpn.com"):
                return ip_info
        except VPNConnectionError:
            pass
        time.sleep(2)
    msg = f"Failed to connect to {server_name} after {timeout} seconds"
    raise VPNConnectionError(msg)


def check_credential_file(path: Path) -> None:
    """Check if credential file exists and has correct permissions."""
    if not path.exists():
        msg = f"Credential file not found: {path}"
        raise VPNError(msg)

    # Check file permissions (600)
    current_mode = path.stat().st_mode & 0o777
    if current_mode != 0o600:
        try:
            path.chmod(0o600)
        except OSError as e:
            msg = f"Failed to set correct permissions on credential file: {e}"
            raise VPNError(msg) from e


def setup_config_directory() -> None:
    """Set up NordVPN configuration directory."""
    try:
        if not NORDVPN_CONFIG_DIR.exists():
            NORDVPN_CONFIG_DIR.mkdir(mode=0o700, parents=True)

        # Download and extract config files
        response = requests.get(OVPN_CONFIG_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(suffix=".zip") as temp_file:
            temp_file.write(response.content)
            temp_file.flush()

            # Use unzip command with list arguments
            unzip_exists, unzip_path = check_command("unzip")
            if not unzip_exists:
                msg = "unzip command not found"
                raise VPNError(msg)

            try:
                run_subprocess_safely(
                    [unzip_path, "-o", temp_file.name, "-d", str(NORDVPN_CONFIG_DIR)],
                    check=True,
                    timeout=30,
                )
            except VPNError as e:
                msg = f"Failed to extract config files: {e}"
                raise VPNError(msg) from e

    except (requests.RequestException, OSError) as e:
        msg = f"Failed to set up config directory: {e}"
        raise VPNError(msg) from e


def get_random_country() -> str:
    """Get a random country from the list of supported countries."""
    try:
        response = requests.get(
            "https://api.nordvpn.com/v1/servers/countries",
            headers=HEADERS,
            timeout=10,
        )
        response.raise_for_status()
        countries = response.json()
        if not countries:
            msg = "No countries found"
            raise VPNError(msg)

        # Use secrets for cryptographic random choice
        import secrets

        return countries[secrets.randbelow(len(countries))]["name"]
    except requests.RequestException as e:
        msg = f"Failed to get country list: {e}"
        raise VPNError(msg) from e


def create_temp_auth_file() -> tuple[Path, bool]:
    """Create a temporary file for VPN authentication."""
    try:
        temp_dir = Path(tempfile.gettempdir())
        auth_file = temp_dir / f"nordvpn_auth_{os.getpid()}"
        if not auth_file.touch(mode=0o600):
            msg = "Failed to create temporary auth file"
            raise VPNError(msg)
        return auth_file, True
    except OSError as e:
        msg = f"Failed to create temporary auth file: {e}"
        raise VPNError(msg) from e


def validate_paths(openvpn_path: str, config_file: Path, auth_file_path: Path) -> None:
    """Validate that all paths are absolute."""
    if not openvpn_path or not os.path.isabs(openvpn_path):
        msg = "OpenVPN path is not absolute"
        raise VPNError(msg)
    if not os.path.isabs(str(config_file)):
        msg = "Config file path is not absolute"
        raise VPNError(msg)
    if not os.path.isabs(str(auth_file_path)):
        msg = "Auth file path is not absolute"
        raise VPNError(msg)


def setup_auth(
    auth_file: str | Path | None,
    auth_login: str | None,
    auth_password: str | None,
) -> tuple[Path, Path | None]:
    """Set up authentication and return auth file path and temp file."""
    temp_auth_file = None
    if auth_login and auth_password:
        temp_auth_file, _ = create_temp_auth_file()
        temp_auth_file.write_text(f"{auth_login}\n{auth_password}")
        auth_file = temp_auth_file
    elif not auth_file:
        msg = "Either auth_file or auth_login/auth_password must be provided"
        raise VPNError(msg)
    else:
        auth_file_path = Path(auth_file)
        check_credential_file(auth_file_path)
        return auth_file_path, temp_auth_file

    auth_file_path = Path(auth_file)
    check_credential_file(auth_file_path)
    return auth_file_path, temp_auth_file


def run_openvpn(
    openvpn_path: str,
    config_file: Path,
    auth_file_path: Path,
) -> None:
    """Run OpenVPN with the given configuration."""
    cmd = [
        openvpn_path,
        "--config",
        str(config_file),
        "--auth-user-pass",
        str(auth_file_path),
        "--daemon",
    ]

    try:
        run_subprocess_safely(cmd, timeout=30)
    except VPNError as e:
        msg = f"Failed to connect to VPN: {e}"
        raise VPNConnectionError(msg) from e


def connect_nordvpn(
    *,  # Force keyword arguments
    country: str = "United States",
    auth_file: str | Path | None = None,
    auth_login: str | None = None,
    auth_password: str | None = None,
    random_country: bool = False,
) -> None:
    """Connect to NordVPN."""
    try:
        # Get server
        if random_country:
            country = get_random_country()

        server = get_nordvpn_server(country)
        if not server:
            _raise_server_error(VPNError("No server found"))
        else:
            # Setup config
            try:
                setup_config_directory()
            except (VPNError, OSError) as e:
                _raise_config_error(e)

            # Get config file path
            config_file = NORDVPN_CONFIG_DIR / f"{server}.ovpn"
            if not config_file.exists():
                _raise_config_file_error(config_file)
            else:
                # Setup auth
                try:
                    auth_file_path, temp_auth_file = setup_auth(
                        auth_file=auth_file,
                        auth_login=auth_login,
                        auth_password=auth_password,
                    )
                    if not auth_file_path:
                        _raise_auth_error(VPNError("No auth file created"))
                    else:
                        # Validate paths
                        try:
                            validate_paths(
                                openvpn_path="openvpn",
                                config_file=config_file,
                                auth_file_path=auth_file_path,
                            )
                        except (VPNError, OSError) as e:
                            _raise_validation_error(e)

                        # Connect
                        try:
                            run_openvpn(
                                openvpn_path="openvpn",
                                config_file=config_file,
                                auth_file_path=auth_file_path,
                            )
                            wait_for_connection(server)
                        except (VPNError, VPNConnectionError, OSError) as e:
                            _raise_connection_error(e, server)
                except (VPNError, OSError) as e:
                    _raise_auth_error(e)

    except (VPNError, VPNConnectionError, OSError) as e:
        _raise_connection_error(e, country)


def get_connection_status() -> None:
    """Get current VPN connection status."""
    try:
        ip_info = get_public_ip()
        if not ip_info:
            msg = "Failed to get IP info"
            raise VPNError(msg)
        is_vpn = ip_info.get("hostname", "").endswith("nordvpn.com")

        status_text = (
            f"IP: {ip_info.get('ip')}\n"
            f"Location: {ip_info.get('city', 'Unknown')}, {ip_info.get('country', 'Unknown')}\n"
            f"ISP: {ip_info.get('org', 'Unknown')}\n"
            f"VPN: {'Connected' if is_vpn else 'Not connected'}"
        )

        console.print(Panel(status_text))

    except (VPNError, requests.RequestException) as e:
        msg = f"Failed to get connection status: {e}"
        raise VPNError(msg) from e


def main():
    """Main entry point."""
    try:
        fire.Fire(
            {
                "connect": connect_nordvpn,
                "status": get_connection_status,
            }
        )
    except (VPNError, VPNConnectionError, requests.RequestException) as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
