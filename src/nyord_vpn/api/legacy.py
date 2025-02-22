"""Legacy VPN API implementation."""

import json
import os
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import TypedDict, Any
import asyncio
import aiohttp
import shlex
import pycountry

from nyord_vpn.api.base import BaseAPI
from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.validation import (
    validate_country,
    validate_credentials,
    validate_hostname,
)
from nyord_vpn.utils.log_utils import log_error
from nyord_vpn.utils.system import run_subprocess_safely


# Constants
OVPN_CONFIG_URL = "https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"
NORDVPN_CONFIG_DIR = Path("/etc/nordvpn_file")


class ServerInfo(TypedDict):
    name: str
    id: str


class CountryInfo(TypedDict):
    name: str
    id: str


def normalize_country(country: str) -> str:
    """Normalize country name or code to full name.

    Args:
        country: Country name or ISO code (e.g. 'de', 'germany', 'Germany')

    Returns:
        str: Full country name

    Raises:
        VPNError: If country not found
    """
    try:
        # Try as alpha_2 code first
        c = pycountry.countries.get(alpha_2=country.upper())
        if c:
            return c.name

        # Try as full name
        c = pycountry.countries.get(name=country)
        if c:
            return c.name

        # Try fuzzy search
        matches = pycountry.countries.search_fuzzy(country)
        if matches:
            return matches[0].name

        msg = f"Country not found: {country}"
        raise VPNError(msg)

    except LookupError as e:
        msg = f"Invalid country: {country}"
        raise VPNError(msg) from e


class LegacyAPI(BaseAPI):
    """Legacy NordVPN API implementation."""

    def __init__(self, username: str, password: str):
        """Initialize the API with NordVPN credentials.

        Args:
            username: NordVPN username
            password: NordVPN password

        Raises:
            VPNError: If OpenVPN is not found
        """
        self.username = username
        self.password = password

        # Check if openvpn command exists
        openvpn_path = shutil.which("openvpn")
        if not openvpn_path:
            msg = "openvpn command not found in PATH. Install it with 'brew install openvpn' on macOS"
            raise VPNError(msg)
        self.openvpn_path = Path(openvpn_path).resolve()

        # Ensure config directory exists
        self._setup_config_dir()

    def _setup_config_dir(self) -> None:
        """Set up NordVPN configuration directory."""
        try:
            # Create config directory if it doesn't exist
            if not NORDVPN_CONFIG_DIR.exists():
                os.makedirs(NORDVPN_CONFIG_DIR, mode=0o700, exist_ok=True)

            # Download and extract config files if they don't exist
            ovpn_dir = NORDVPN_CONFIG_DIR / "ovpn_tcp"
            if not ovpn_dir.exists():
                # Create temporary directory for download
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    zip_path = temp_path / "ovpn.zip"

                    # Download config files
                    cmd = [
                        "curl",
                        "-sSL",
                        OVPN_CONFIG_URL,
                        "-o",
                        str(zip_path),
                    ]
                    run_subprocess_safely(cmd, timeout=30)

                    # Extract config files
                    with zipfile.ZipFile(zip_path) as zf:
                        zf.extractall(NORDVPN_CONFIG_DIR)

        except Exception as e:
            msg = f"Failed to setup config directory: {e}"
            raise VPNError(msg) from e

    async def _get_servers(self, country: str) -> list[dict[str, Any]]:
        """Get list of servers for a country.

        Args:
            country: Country name or code

        Returns:
            List of server information

        Raises:
            VPNError: If server list cannot be retrieved
        """
        # Normalize country name
        country = normalize_country(country)

        async with aiohttp.ClientSession() as session:
            try:
                # Get country ID first
                async with session.get(
                    "https://api.nordvpn.com/v1/servers/countries",
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response:
                    response.raise_for_status()
                    countries = await response.json()
                    country_id = None
                    for c in countries:
                        if c["name"].lower() == country.lower():
                            country_id = c["id"]
                            break
                    if not country_id:
                        msg = f"Country not found in NordVPN: {country}"
                        raise VPNError(msg)

                # Get recommended servers
                async with session.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php",
                    params={
                        "action": "servers_recommendations",
                        "filters": json.dumps({"country_id": country_id}),
                    },
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response:
                    response.raise_for_status()
                    servers = await response.json()
                    return [
                        {"name": s["hostname"], "id": str(s["id"])} for s in servers
                    ]
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                msg = f"Failed to get server list: {e}"
                raise VPNError(msg) from e

    async def connect(self, country: str | None = None) -> bool:
        """Connect to VPN.

        Args:
            country: Optional country to connect to

        Returns:
            True if connection successful

        Raises:
            VPNError: If connection fails
        """
        try:
            # Get server
            servers = await self._get_servers(country or "United States")
            if not servers:
                msg = "No servers found"
                raise VPNError(msg)

            # Create temp auth file
            auth_file = Path(tempfile.mkstemp(prefix="nordvpn_", suffix=".auth")[1])
            auth_file.write_text(f"{self.username}\n{self.password}")
            auth_file.chmod(0o600)

            try:
                # Get config file
                server = servers[0]["name"]
                config_file = NORDVPN_CONFIG_DIR / "ovpn_tcp" / f"{server}.tcp.ovpn"
                if not config_file.exists():
                    msg = f"Config file not found: {config_file}"
                    raise VPNError(msg)

                # Build OpenVPN command with verbose logging
                cmd = [
                    "sudo",  # Run as root
                    str(self.openvpn_path),
                    "--config",
                    str(config_file),
                    "--auth-user-pass",
                    str(auth_file),
                    "--daemon",
                    "--verb",
                    "4",  # Verbose logging
                    "--log",
                    "/var/log/openvpn.log",  # Log to file
                ]

                # Check sudo access first
                try:
                    run_subprocess_safely(["sudo", "-n", "true"], timeout=5)
                except Exception:
                    print(
                        "\nNeed sudo access to run OpenVPN. Please enter your password:"
                    )
                    run_subprocess_safely(["sudo", "-v"], timeout=30)

                # Now run OpenVPN
                print(f"\nConnecting to {server}...")
                run_subprocess_safely(cmd, timeout=30)

                # Wait for connection and show log
                print("\nChecking connection status (log at /var/log/openvpn.log)...")
                run_subprocess_safely(
                    ["sudo", "tail", "-n", "20", "-f", "/var/log/openvpn.log"],
                    timeout=5,
                )
                return True

            finally:
                # Clean up auth file
                if auth_file.exists():
                    auth_file.unlink()

        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNError(msg) from e

    async def disconnect(self) -> bool:
        """Disconnect from VPN.

        Returns:
            True if disconnection successful

        Raises:
            VPNError: If disconnection fails
        """
        try:
            # Find and kill OpenVPN processes
            ps_output = run_subprocess_safely(["ps", "-ax"], timeout=5).stdout
            openvpn_procs = [
                line.split()[0]
                for line in ps_output.splitlines()
                if "openvpn" in line.lower()
            ]

            if not openvpn_procs:
                return True

            for pid in openvpn_procs:
                run_subprocess_safely(["kill", pid], timeout=5)

            return True

        except Exception as e:
            msg = f"Failed to disconnect: {e}"
            raise VPNError(msg) from e

    async def status(self) -> dict[str, Any]:
        """Get current connection status.

        Returns:
            Dictionary with connection status

        Raises:
            VPNError: If status cannot be retrieved
        """
        try:
            # Check if OpenVPN is running
            ps_output = run_subprocess_safely(["ps", "-ax"], timeout=5).stdout
            connected = any(
                "openvpn" in line.lower() for line in ps_output.splitlines()
            )

            # Get public IP info
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://ipinfo.io/json",
                    timeout=aiohttp.ClientTimeout(total=5),
                ) as response:
                    response.raise_for_status()
                    ip_info = await response.json()

            return {
                "connected": connected,
                "ip": ip_info.get("ip"),
                "country": ip_info.get("country"),
                "city": ip_info.get("city"),
                "hostname": ip_info.get("hostname"),
            }

        except Exception as e:
            msg = f"Failed to get status: {e}"
            raise VPNError(msg) from e

    async def list_countries(self) -> list[str]:
        """Get list of available countries.

        Returns:
            List of country names

        Raises:
            VPNError: If country list cannot be retrieved
        """

        def handle_error(e: Exception) -> list[str]:
            msg = f"Failed to get country list: {e}"
            raise VPNError(msg) from e

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    "https://api.nordvpn.com/v1/servers/countries",
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response:
                    response.raise_for_status()
                    countries: list[CountryInfo] = await response.json()
                    return [c["name"] for c in countries]
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                return handle_error(e)

    async def get_credentials(self) -> tuple[str, str]:
        """Get stored credentials.

        Returns:
            Tuple of (username, password)
        """
        return self.username, self.password
