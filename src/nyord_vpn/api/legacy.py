"""Legacy VPN API implementation."""

from typing import TypedDict, Any
import shutil
import asyncio
import aiohttp
import shlex

from nyord_vpn.api.base import BaseAPI
from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.validation import (
    validate_country,
    validate_credentials,
    validate_command,
    validate_hostname,
)
from nyord_vpn.utils.log_utils import log_error


class ServerInfo(TypedDict):
    name: str
    id: str


class CountryInfo(TypedDict):
    name: str
    id: str


class LegacyAPI(BaseAPI):
    """Legacy NordVPN API implementation."""

    def __init__(self, username: str, password: str):
        """Initialize the API with NordVPN credentials.

        Args:
            username: NordVPN username
            password: NordVPN password

        Raises:
            VPNError: If nordvpn command is not found or credentials are invalid
        """
        # Validate credentials
        self.username, self.password = validate_credentials(username, password)

        # Check if nordvpn command exists and validate it
        nordvpn_path = shutil.which("nordvpn")
        if not nordvpn_path:
            msg = "nordvpn command not found in PATH"
            raise VPNError(msg)
        self.nordvpn_path = validate_command(nordvpn_path)

    async def _get_servers(self, country: str) -> list[ServerInfo]:
        """Get list of servers for a country.

        Args:
            country: Country name or code

        Returns:
            List of server information

        Raises:
            VPNError: If server list cannot be retrieved
        """

        def handle_error(e: Exception) -> list[ServerInfo]:
            msg = f"Failed to get server list: {e}"
            raise VPNError(msg) from e

        # Validate country
        country = validate_country(country)

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"https://api.nordvpn.com/v1/servers/{shlex.quote(country)}",
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response:
                    response.raise_for_status()
                    servers = await response.json()
                    return [
                        {
                            "name": validate_hostname(s["name"]),
                            "id": str(s["id"]),
                        }
                        for s in servers
                    ]
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                return handle_error(e)

    async def connect(self, country: str | None = None) -> bool:
        """Connect to VPN using legacy API.

        Args:
            country: Optional country to connect to

        Returns:
            bool: True if connection successful
        """

        def handle_error(e: Exception, message: str | None = None) -> bool:
            error_msg = message or str(e)
            log_error(f"Legacy API connection failed: {error_msg}")
            return False

        try:
            # Get server
            servers = await self._get_servers(country or "United States")
            if not servers:
                return handle_error(Exception("No servers found"))
            # Build command
            server = servers[0]["name"]
            cmd = [
                "openvpn",
                "--config",
                f"{server}.ovpn",
                "--auth-user-pass",
                "auth.txt",
                "--daemon",
            ]

            # Start OpenVPN process
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=30)

            if process.returncode != 0:
                return handle_error(Exception(stderr.decode()))
            return True
        except asyncio.TimeoutError as e:
            return handle_error(e, "Connection timed out after 30 seconds")
        except Exception as e:
            return handle_error(e)

    async def disconnect(self) -> bool:
        """Disconnect from VPN using legacy API.

        Returns:
            bool: True if disconnection successful
        """

        def handle_error(e: Exception, message: str | None = None) -> bool:
            error_msg = message or str(e)
            log_error(f"Legacy API disconnection failed: {error_msg}")
            return False

        try:
            # Kill OpenVPN process
            cmd = ["pkill", "openvpn"]
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=5)

            if process.returncode != 0:
                return handle_error(Exception(stderr.decode()))
            return True
        except asyncio.TimeoutError as e:
            return handle_error(e, "Disconnection timed out after 5 seconds")
        except Exception as e:
            return handle_error(e)

    async def status(self) -> dict[str, Any]:
        """Get current connection status.

        Returns:
            Dictionary with status information

        Raises:
            VPNError: If status cannot be retrieved
        """

        def handle_error(e: Exception, operation: str) -> dict[str, Any]:
            msg = f"Failed to {operation}: {e}"
            raise VPNError(msg) from e

        try:
            # Get current IP
            async with (
                aiohttp.ClientSession() as session,
                session.get(
                    "https://api.nordvpn.com/v1/helpers/ip",
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response,
            ):
                response.raise_for_status()
                ip_info = await response.json()

            # Get connection status
            process = await asyncio.create_subprocess_exec(
                str(self.nordvpn_path),
                "status",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=10)

            if process.returncode != 0:
                return handle_error(Exception(stderr.decode()), "get status")

            return {
                "ip": ip_info.get("ip"),
                "country": ip_info.get("country"),
                "status": stdout.decode(),
            }
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            return handle_error(e, "get IP info")
        except Exception as e:
            return handle_error(e, "get status")

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
