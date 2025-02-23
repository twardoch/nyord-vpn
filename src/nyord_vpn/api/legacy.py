"""Legacy VPN API implementation based on shell script."""

import subprocess
import tempfile
from pathlib import Path
from typing import Any

import requests
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from nyord_vpn.core.base import BaseVPNClient, VPNStatus
from nyord_vpn.core.exceptions import VPNConfigError, VPNConnectionError, VPNServerError

# API endpoints
API_BASE = "https://api.nordvpn.com/v1"
RECOMMENDATIONS_URL = f"{API_BASE}/servers/recommendations"
CONFIGS_URL = "https://downloads.nordcdn.com/configs/files/ovpn_tcp/servers"

# Country ID mapping from shell script
COUNTRY_IDS = {
    "albania": 2,
    "algeria": 3,
    "andorra": 5,
    "argentina": 10,
    "armenia": 11,
    "australia": 13,
    "austria": 14,
    # ... more countries to be added
    "united_states": 228,
    "united_kingdom": 227,
}


class LegacyVPNClient(BaseVPNClient):
    """Legacy VPN client implementation."""

    def __init__(self) -> None:
        """Initialize legacy VPN client."""
        super().__init__()
        self._openvpn_pid: int | None = None
        self._current_server: str | None = None
        logger.debug("Initializing legacy VPN client")
        self._ensure_openvpn()
        self._config_dir = Path(tempfile.mkdtemp(prefix="nyord_vpn_"))
        self._config_dir.chmod(0o700)  # Secure permissions
        logger.debug(f"Created config directory: {self._config_dir}")

    def _ensure_openvpn(self) -> None:
        """Ensure OpenVPN is installed."""
        try:
            result = subprocess.run(
                ["openvpn", "--version"], check=True, capture_output=True
            )
            version = result.stdout.decode().split()[1]
            logger.debug(f"Found OpenVPN version {version}")
        except (subprocess.SubprocessError, FileNotFoundError) as e:
            logger.error("OpenVPN not found")
            msg = "OpenVPN not found. Install with: brew install openvpn"
            raise VPNConfigError(msg) from e

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def _get_server(self, country: str | None = None) -> str:
        """Get recommended server for country.

        Args:
            country: Optional country name or code

        Returns:
            str: Server hostname

        Raises:
            VPNServerError: If no servers found
        """
        try:
            # Build query params
            params = {
                "filters[servers_technologies][identifier]": "openvpn_tcp",
                "filters[servers_groups][identifier]": "legacy_standard",
                "limit": 1,
            }

            if country:
                params["filters[country_id]"] = country.lower()
                logger.debug(f"Getting server recommendation for country: {country}")
            else:
                logger.debug("Getting server recommendation for fastest server")

            # Get server recommendation
            response = requests.get(
                RECOMMENDATIONS_URL,
                params=params,
                timeout=10,
                headers={"User-Agent": "nyord-vpn/1.0"},
            )
            response.raise_for_status()

            servers = response.json()
            if not servers:
                logger.error(f"No servers found for country: {country}")
                msg = f"No servers found for country: {country}"
                raise VPNServerError(msg)

            server = servers[0]["hostname"]
            logger.debug(f"Selected server: {server}")
            return server

        except requests.RequestException as e:
            logger.error(f"Failed to get server recommendation: {e}")
            msg = f"Failed to get server recommendation: {e}"
            raise VPNServerError(msg) from e

    def _get_config(self, server: str) -> Path:
        """Download OpenVPN config for server.

        Args:
            server: Server hostname

        Returns:
            Path: Path to config file

        Raises:
            VPNConfigError: If config download fails
        """
        try:
            # Download config file
            config_file = self._config_dir / f"{server}.ovpn"
            if not config_file.exists():
                logger.debug(f"Downloading config for server: {server}")
                response = requests.get(
                    f"{CONFIGS_URL}/{server}.tcp.ovpn",
                    timeout=10,
                    headers={"User-Agent": "nyord-vpn/1.0"},
                )
                response.raise_for_status()

                # Save config
                config_file.write_text(response.text)
                config_file.chmod(0o600)  # Secure permissions
                logger.debug(f"Saved config to: {config_file}")
            else:
                logger.debug(f"Using cached config: {config_file}")

            return config_file

        except requests.RequestException as e:
            logger.error(f"Failed to download config for {server}: {e}")
            msg = f"Failed to download config for {server}: {e}"
            raise VPNConfigError(msg) from e

    def connect(self, country: str | None = None) -> bool:
        """Connect to VPN using legacy implementation."""
        try:
            # Disconnect if connected
            if self._openvpn_pid:
                logger.debug("Disconnecting existing connection")
                self.disconnect()

            # Get server and config
            logger.info("Initializing VPN connection...")
            server = self._get_server(country)
            config_file = self._get_config(server)

            # Create temp auth file
            auth_file = Path(tempfile.mkstemp(prefix="nordvpn_", suffix=".auth")[1])
            auth_file.write_text(f"{self.username}\n{self.password}")
            auth_file.chmod(0o600)
            logger.debug(f"Created auth file: {auth_file}")

            try:
                # Start OpenVPN
                logger.debug("Starting OpenVPN process")
                process = subprocess.Popen(
                    [
                        "sudo",
                        "openvpn",
                        "--config",
                        str(config_file),
                        "--auth-user-pass",
                        str(auth_file),
                        "--daemon",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT,
                )
                self._openvpn_pid = process.pid
                self._current_server = server
                logger.debug(f"OpenVPN process started with PID: {self._openvpn_pid}")

                # Wait for connection
                logger.info(f"Connecting to {server}...")

                # Monitor connection status
                retries = 0
                max_retries = 12  # 60 seconds total
                while retries < max_retries:
                    if self.protected():
                        logger.info("VPN connection established")
                        return True
                    retries += 1
                    logger.debug(
                        f"Waiting for connection... attempt {retries}/{max_retries}"
                    )
                    subprocess.run(["sleep", "5"], check=False)  # Wait 5 seconds between checks

                # Connection failed
                logger.error("Failed to establish VPN connection after 60 seconds")
                msg = "Failed to establish VPN connection after 60 seconds"
                raise VPNConnectionError(msg)

            finally:
                # Cleanup auth file
                logger.debug("Cleaning up auth file")
                auth_file.unlink()
        except Exception as e:
            # Cleanup on failure
            logger.error(f"Connection failed: {e}")
            self.disconnect()
            msg = f"Failed to connect: {e}"
            raise VPNConnectionError(msg) from e

    def disconnect(self) -> bool:
        """Disconnect from VPN."""
        try:
            if self._openvpn_pid:
                logger.debug(f"Stopping OpenVPN process {self._openvpn_pid}")
                # Try graceful shutdown first
                try:
                    subprocess.run(
                        ["sudo", "kill", "-SIGTERM", str(self._openvpn_pid)],
                        check=True,
                        timeout=5,
                    )
                    logger.debug("OpenVPN process terminated gracefully")
                except subprocess.SubprocessError:
                    # Force kill if graceful shutdown fails
                    logger.warning("Graceful shutdown failed, force killing process")
                    subprocess.run(
                        ["sudo", "kill", "-9", str(self._openvpn_pid)], check=True
                    )
                self._openvpn_pid = None
                self._current_server = None

            # Cleanup any stray processes
            try:
                logger.debug("Cleaning up stray OpenVPN processes")
                subprocess.run(["sudo", "pkill", "-f", "openvpn"], check=True)
            except subprocess.SubprocessError:
                pass  # Ignore if no processes found

            return True
        except subprocess.SubprocessError as e:
            logger.error(f"Failed to disconnect: {e}")
            msg = f"Failed to disconnect: {e}"
            raise VPNConnectionError(msg) from e
        finally:
            # Cleanup config directory
            if self._config_dir.exists():
                logger.debug("Cleaning up config directory")
                for f in self._config_dir.glob("*"):
                    try:
                        f.unlink()
                        logger.debug(f"Removed config file: {f}")
                    except OSError as e:
                        logger.warning(f"Failed to remove config file {f}: {e}")
                try:
                    self._config_dir.rmdir()
                    logger.debug("Removed config directory")
                except OSError as e:
                    logger.warning(f"Failed to remove config directory: {e}")

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def protected(self) -> bool:
        """Check if VPN is active."""
        try:
            # Check OpenVPN process
            if not self._openvpn_pid:
                logger.debug("No OpenVPN process found")
                return False

            try:
                # Check if process is running
                subprocess.run(
                    ["ps", "-p", str(self._openvpn_pid)],
                    check=True,
                    capture_output=True,
                )
                logger.debug(f"OpenVPN process {self._openvpn_pid} is running")
            except subprocess.SubprocessError:
                logger.debug(f"OpenVPN process {self._openvpn_pid} not found")
                return False

            # Verify IP is from NordVPN
            logger.debug("Checking if IP belongs to NordVPN")
            response = requests.get(
                "https://ipinfo.io/json",
                timeout=5,
                headers={"User-Agent": "nyord-vpn/1.0"},
            )
            response.raise_for_status()
            data = response.json()

            is_protected = (
                "nordvpn" in data.get("org", "").lower()
                or "nord" in data.get("org", "").lower()
            )
            logger.debug(f"VPN protection status: {is_protected}")
            return is_protected
        except Exception as e:
            logger.error(f"Failed to check VPN status: {e}")
            return False

    @retry(
        stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def status(self) -> VPNStatus:
        """Get VPN status."""
        try:
            # Get IP info
            logger.debug("Getting IP information")
            response = requests.get(
                "https://ipinfo.io/json",
                timeout=5,
                headers={"User-Agent": "nyord-vpn/1.0"},
            )
            response.raise_for_status()
            data = response.json()

            # Check if connected to NordVPN
            is_connected = self.protected()
            logger.debug(f"VPN connection status: {is_connected}")

            status = VPNStatus(
                connected=is_connected,
                ip=data.get("ip", ""),
                country=data.get("country", ""),
                server=self._current_server or "",
            )
            logger.debug(f"VPN status: {status}")
            return status
        except Exception as e:
            logger.error(f"Failed to get status: {e}")
            msg = f"Failed to get status: {e}"
            raise VPNConnectionError(msg) from e

    def list_countries(self) -> list[dict[str, Any]]:
        """Get list of available countries."""
        try:
            logger.debug("Getting country list")
            response = requests.get(
                f"{API_BASE}/servers/countries",
                timeout=10,
                headers={"User-Agent": "nyord-vpn/1.0"},
            )
            response.raise_for_status()

            countries = []
            for country in response.json():
                name = country.get("name", "").replace("_", " ").title()
                code = str(country.get("id", ""))
                if name and code:
                    countries.append({"name": name, "code": code})

            countries = sorted(countries, key=lambda x: x["name"])
            logger.debug(f"Found {len(countries)} countries")
            return countries

        except requests.RequestException as e:
            logger.error(f"Failed to get country list: {e}")
            msg = f"Failed to get country list: {e}"
            raise VPNConfigError(msg) from e
