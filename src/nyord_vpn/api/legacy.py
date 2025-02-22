"""Legacy VPN API implementation."""

from typing import TypedDict, Any
import shutil
import asyncio
import aiohttp
import shlex
from pathlib import Path

from nyord_vpn.api.base import BaseAPI
from nyord_vpn.core.exceptions import VPNError
from nyord_vpn.utils.system import run_subprocess_safely


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
            VPNError: If nordvpn command is not found
        """
        self.username = username
        self.password = password

        # Check if nordvpn command exists
        nordvpn_path = shutil.which("nordvpn")
        if not nordvpn_path:
            msg = "nordvpn command not found in PATH"
            raise VPNError(msg)
        self.nordvpn_path = Path(nordvpn_path).resolve()

    async def _get_servers(self, country: str) -> list[ServerInfo]:
        """Get list of servers for a country.

        Args:
            country: Country name or code

        Returns:
            List of server information

        Raises:
            VPNError: If server list cannot be retrieved
        """
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                    f"https://api.nordvpn.com/v1/servers/{shlex.quote(country)}",
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response:
                    response.raise_for_status()
                    servers = await response.json()
                    return [{"name": s["name"], "id": s["id"]} for s in servers]
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                msg = f"Failed to get server list: {e}"
                raise VPNError(msg) from e

    async def connect(self, country: str | None = None) -> bool:
        """Connect to NordVPN.

        Args:
            country: Optional country to connect to

        Returns:
            True if connection successful

        Raises:
            VPNError: If connection fails
        """
        cmd = [str(self.nordvpn_path), "connect"]
        if country:
            # Sanitize country input
            safe_country = shlex.quote(country)
            if not safe_country.strip("'\""):
                msg = "Invalid country name"
                raise VPNError(msg)
            cmd.append(safe_country)

        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=30)

            if process.returncode != 0:
                msg = f"Failed to connect: {stderr.decode()}"
                raise VPNError(msg)
            return True
        except asyncio.TimeoutError as e:
            msg = "Connection timed out after 30 seconds"
            raise VPNError(msg) from e
        except Exception as e:
            msg = f"Failed to connect: {e}"
            raise VPNError(msg) from e

    async def disconnect(self) -> bool:
        """Disconnect from NordVPN.

        Returns:
            True if disconnection successful

        Raises:
            VPNError: If disconnection fails
        """
        try:
            process = await asyncio.create_subprocess_exec(
                str(self.nordvpn_path),
                "disconnect",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=10)

            if process.returncode != 0:
                msg = f"Failed to disconnect: {stderr.decode()}"
                raise VPNError(msg)
            return True
        except asyncio.TimeoutError as e:
            msg = "Disconnect timed out after 10 seconds"
            raise VPNError(msg) from e
        except Exception as e:
            msg = f"Failed to disconnect: {e}"
            raise VPNError(msg) from e

    async def status(self) -> dict[str, Any]:
        """Get current connection status.

        Returns:
            Dictionary with status information

        Raises:
            VPNError: If status cannot be retrieved
        """
        try:
            # Get current IP
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    "https://api.nordvpn.com/v1/helpers/ip",
                    timeout=aiohttp.ClientTimeout(total=10),
                    ssl=True,
                ) as response:
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
                msg = f"Failed to get status: {stderr.decode()}"
                raise VPNError(msg)

            return {
                "ip": ip_info.get("ip"),
                "country": ip_info.get("country"),
                "status": stdout.decode(),
            }
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            msg = f"Failed to get status: {e}"
            raise VPNError(msg) from e
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
                msg = f"Failed to get country list: {e}"
                raise VPNError(msg) from e

    async def get_credentials(self) -> tuple[str, str]:
        """Get stored credentials.

        Returns:
            Tuple of (username, password)
        """
        return self.username, self.password
