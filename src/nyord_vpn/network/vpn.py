"""VPN connection manager for NordVPN."""

import os
import subprocess
import time
from pathlib import Path
from typing import Any

import requests
from loguru import logger
from rich.progress import Progress, SpinnerColumn, TextColumn

from src.nyord_vpn.models import VPNError
from src.nyord_vpn.utils.utils import API_HEADERS, OPENVPN_AUTH


class VPNConnectionManager:
    """Manages VPN connections using OpenVPN."""

    def __init__(
        self, openvpn_path: str = "/usr/local/sbin/openvpn", verbose: bool = False
    ):
        """Initialize VPN connection manager.

        Args:
            openvpn_path: Path to OpenVPN executable
            verbose: Whether to enable verbose logging
        """
        self.openvpn_path = openvpn_path
        self.logger = logger
        self.verbose = verbose
        self.process: subprocess.Popen | None = None
        self.config_dir = Path(os.path.expanduser("~/.config/nyord-vpn/configs"))
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Connection state
        self._initial_ip: str | None = None
        self._connected_ip: str | None = None
        self._server: str | None = None
        self._country_name: str | None = None

    def get_current_ip(self) -> str | None:
        """Get current IP address."""
        try:
            response = requests.get("https://api.ipify.org?format=json", timeout=5)
            response.raise_for_status()
            return response.json().get("ip")
        except Exception:
            return None

    def check_openvpn_installation(self) -> str:
        """Verify OpenVPN is installed and return its path."""
        try:
            result = subprocess.run(
                ["which", "openvpn"], capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            raise VPNError(
                "OpenVPN not found. Please install OpenVPN first:\n"
                "  macOS: brew install openvpn\n"
                "  Linux: sudo apt install openvpn\n"
                "  Windows: Download from https://openvpn.net/community-downloads/"
            )

    def connect(self, server: dict[str, Any]) -> None:
        """Connect to a VPN server.

        Args:
            server: Server info dictionary

        Raises:
            VPNError: If connection fails
        """
        try:
            hostname = server.get("hostname")
            if not hostname:
                raise VPNError("Invalid server info - missing hostname")

            if self.verbose:
                self.logger.debug(f"Connecting to {hostname}")

            # Store initial IP
            self._initial_ip = self.get_current_ip()

            # Generate OpenVPN config
            config_path = self._generate_config(hostname)

            # Verify auth file exists and has correct format
            if not OPENVPN_AUTH.exists():
                raise VPNError(
                    "Authentication file not found. Please create ~/.cache/nyord-vpn/openvpn.auth with your NordVPN credentials:\n"
                    "  1. Set your credentials as environment variables:\n"
                    "     export NORD_USER='your_nordvpn_username'\n"
                    "     export NORD_PASSWORD='your_nordvpn_password'\n"
                    "  2. Create the auth file:\n"
                    '     echo "$NORD_USER" > ~/.cache/nyord-vpn/openvpn.auth\n'
                    '     echo "$NORD_PASSWORD" >> ~/.cache/nyord-vpn/openvpn.auth\n'
                    "\nThe file should contain your username on the first line and password on the second line."
                )

            try:
                auth_lines = OPENVPN_AUTH.read_text().strip().splitlines()
                if len(auth_lines) != 2 or not all(line.strip() for line in auth_lines):
                    raise VPNError(
                        "Invalid auth file format. The file should contain exactly two non-empty lines:\n"
                        "  Line 1: Your NordVPN username\n"
                        "  Line 2: Your NordVPN password"
                    )
            except Exception as e:
                if isinstance(e, VPNError):
                    raise
                raise VPNError(f"Failed to read auth file: {e}")

            # Start OpenVPN process
            cmd = [
                "sudo",
                "openvpn",
                "--config",
                str(config_path),
                "--auth-user-pass",
                str(OPENVPN_AUTH),
                "--verb",
                "5",  # Increased verbosity for more detailed logs
            ]

            if self.verbose:
                self.logger.debug(f"Running OpenVPN command: {' '.join(cmd)}")

            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                progress.add_task(description="Connecting...", total=None)
                self.process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,  # Line buffered
                )

            # Wait for initial connection and capture output
            time.sleep(5)
            if self.process.poll() is not None:
                stdout, stderr = self.process.communicate()
                if self.verbose:
                    self.logger.debug(f"OpenVPN stdout:\n{stdout}")
                    self.logger.debug(f"OpenVPN stderr:\n{stderr}")
                if "AUTH_FAILED" in stderr:
                    raise VPNError(f"Authentication failed. Full error:\n{stderr}")
                raise VPNError(f"OpenVPN process failed:\n{stderr}\nOutput:\n{stdout}")

            # Verify connection
            if not self.verify_connection():
                raise VPNError("Failed to establish VPN connection")

            # Update connection info
            self._server = hostname
            self._connected_ip = self.get_current_ip()

            if self.verbose:
                self.logger.info(f"Connected to {hostname}")

        except Exception as e:
            raise VPNError(f"Failed to connect to VPN: {e}")

    def disconnect(self) -> None:
        """Disconnect from VPN."""
        if self.process:
            try:
                # Try graceful shutdown first
                self.process.terminate()
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Force kill if graceful shutdown fails
                    self.process.kill()
                    self.process.wait()
            except Exception as e:
                if self.verbose:
                    self.logger.warning(f"Error during VPN disconnect: {e}")
            finally:
                self.process = None

        # Clean up any lingering OpenVPN processes
        try:
            subprocess.run(
                ["sudo", "pkill", "-f", "openvpn"],
                check=False,
                capture_output=True,
            )
        except Exception as e:
            if self.verbose:
                self.logger.warning(f"Error cleaning up OpenVPN processes: {e}")

        # Reset connection state
        self._initial_ip = None
        self._connected_ip = None
        self._server = None
        self._country_name = None

    def verify_connection(self) -> bool:
        """Verify VPN connection is active."""
        try:
            # Check if process is running
            if not self.is_connected():
                return False

            # Get current IP
            current_ip = self.get_current_ip()
            if not current_ip:
                return False

            # Check if IP has changed from initial
            if current_ip == self._initial_ip:
                return False

            # Check NordVPN API for connection status
            try:
                response = requests.get(
                    "https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data",
                    headers=API_HEADERS,
                    timeout=5,
                )
                response.raise_for_status()
                nord_data = response.json()
                if not nord_data.get("status", False):
                    return False
            except Exception:
                # If API check fails, just verify IP change
                pass

            return True

        except Exception:
            return False

    def _generate_config(self, hostname: str) -> Path:
        """Generate OpenVPN config file for server.

        Args:
            hostname: Server hostname

        Returns:
            Path: Path to generated config file
        """
        config_path = self.config_dir / f"{hostname}.ovpn"

        # Basic OpenVPN config
        config = f"""client
dev tun
proto tcp
remote {hostname} 443
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
auth SHA512
verify-x509-name CN={hostname}
auth-nocache
pull
tls-client
key-direction 1
verb 3

<ca>
-----BEGIN CERTIFICATE-----
MIIFCjCCAvKgAwIBAgIBATANBgkqhkiG9w0BAQ0FADA5MQswCQYDVQQGEwJQQTEQ
MA4GA1UEChMHTm9yZFZQTjEYMBYGA1UEAxMPTm9yZFZQTiBSb290IENBMB4XDTE2
MDEwMTAwMDAwMFoXDTM1MTIzMTIzNTk1OVowOTELMAkGA1UEBhMCUEExEDAOBgNV
BAoTB05vcmRWUE4xGDAWBgNVBAMTD05vcmRWUE4gUm9vdCBDQTCCAiIwDQYJKoZ
IhvcNAQEBBQADggIPADCCAgoCggIBAMkr/BYhyo0F2upsIMXwC6QvkZps3NN2/eQF
kfQIS1gql0aejsKsEnmY0Kaon8uZCTXPsRH1gQNgg5D2gixdd1mJUvV3dE3y9FJr
XMoDkXdCGBodvKJyU6lcfEVF6/UxHcbBguZK9UtRHS9eJYm3rpL/5huQMCppX7kU
eQ8dpCwd3iKITqwd1ZudDqsWaU0vqzC2H55IyaZ/5/TnCk31Q1UP6BksbbuRcwOV
skEDsm6YoWDnn/IIzGOYnFJRzQH5jTz3j1QBvRIuQuBuvUkfhx1FEwhwZigrcxXu
MP+QgM54kezgziJUaZcOM2zF3lvrwMvXDMfNeIoJABv9ljw969xQ8czQCU5lMVmA
37ltv5Ec9U5hZuwk/9QO1Z+d/r6Jx0mlurS8gnCAKJgwa3kyZw6e4FZ8mYL4vpRR
hPdvRTWCMJkeB4yBHyhxUmTRgJHm6YR3D6hcFAc9cQcTEl/I60tMdz33G6m0O42s
Qt/+AR3YCY/RusWVBJB/qNS94EtNtj8iaebCQW1jHAhvGmFILVR9lzD0EzWKHkvy
WEjmUVRgCDd6Ne3eFRNS73gdv/C3l5boYySeu4exkEYVxVRn8DhCxs0MnkMHWFK6
MyzXCCn+JnWFDYPfDKHvpff/kLDobtPBf+Lbch5wQy9quY27xaj0XwLyjOltpiST
LWae/Q4vAgMBAAGjHTAbMAwGA1UdEwQFMAMBAf8wCwYDVR0PBAQDAgEGMA0GCSqG
SIb3DQEBDQUAA4ICAQC9fUL2sZPxIN2mD32VeNySTgZlCEdVmlq471o/bDMP4B8g
nQesFRtXY2ZCjs50Jm73B2LViL9qlREmI6vE5IC8IsRBJSV4ce1WYxyXro5rmVg/
k6a10rlsbK/eg//GHoJxDdXDOokLUSnxt7gk3QKpX6eCdh67p0PuWm/7WUJQxH2S
DxsT9vB/iZriTIEe/ILoOQF0Aqp7AgNCcLcLAmbxXQkXYCCSB35Vp06u+eTWjG0/
pyS5V14stGtw+fA0DJp5ZJV4eqJ5LqxMlYvEZ/qKTEdoCeaXv2QEmN6dVqjDoTAo
k0t5u4YRXzEVCfXAC3ocplNdtCA72wjFJcSbfif4BSC8bDACTXtnPC7nD0VndZLp
+RiNLeiENhk0oTC+UVdSc+n2nJOzkCK0vYu0Ads4JGIB7g8IB3z2t9ICmsWrgnhd
NdcOe15BincrGA8avQ1cWXsfIKEjbrnEuEk9b5jel6NfHtPKoHc9mDpRdNPISeVa
wDBM1mJChneHt59Nh8Gah74+TM1jBsw4fhJPvoc7Atcg740JErb904mZfkIEmojC
VPhBHVQ9LHBAdM8qFI2kRK0IynOmAZhexlP/aT/kpEsEPyaZQlnBn3An1CRz8h0S
PApL8PytggYKeQmRhl499+6jLxcZ2IegLfqq41dzIjwHwTMplg+1pKIOVojpWA==
-----END CERTIFICATE-----
</ca>

<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
e685bdaf659a25a200e2b9e39e51ff03
0fc72cf1ce07232bd8b2be5e6c670143
f51e937e670eee09d4f2ea5a6e4e6996
5db852c275351b86fc4ca892d78ae002
d6f70d029bd79c4d1c26cf14e9588033
cf639f8a74809f29f72b9d58f9b8f5fe
fc7938eade40e9fed6cb92184abb2cc1
0eb1a296df243b251df0643d53724cdb
5a92a1d6cb817804c4a9319b57d53be5
80815bcfcb2df55018cc83fc43bc7ff8
2d51f9b88364776ee9d12fc85cc7ea5b
9741c4f598c485316db066d52db4540e
212e1518a9bd4828219e24b20d88f598
a196c9de96012090e333519ae18d3509
9427e7b372d348d352dc4c85e18cd4b9
3f8a56ddb2e64eb67adfc9b337157ff4
-----END OpenVPN Static key V1-----
</tls-auth>
"""

        config_path.write_text(config)
        return config_path

    def is_connected(self) -> bool:
        """Check if VPN is currently connected.

        Returns:
            bool: True if connected
        """
        return self.process is not None and self.process.poll() is None

    def update_connection_info(self, server_hostname: str, country_name: str) -> None:
        """Update connection information."""
        self._server = server_hostname
        self._country_name = country_name
        self._connected_ip = self.get_current_ip()

    def setup_connection(
        self, server_hostname: str, username: str, password: str
    ) -> None:
        """Set up OpenVPN configuration files.

        Args:
            server_hostname: Server hostname
            username: NordVPN username
            password: NordVPN password
        """
        # Generate OpenVPN config
        config_path = self._generate_config(server_hostname)

        # Create auth file
        OPENVPN_AUTH.write_text(f"{username}\n{password}")

        if self.verbose:
            self.logger.debug(f"Created auth file at {OPENVPN_AUTH}")
