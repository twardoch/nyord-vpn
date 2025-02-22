"""Network utilities for VPN operations."""

import asyncio
import time
from typing import Any

import aiohttp
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from nyord_vpn.core.exceptions import VPNError, VPNConnectionError


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(aiohttp.ClientError),
)
async def get_public_ip() -> dict[str, Any]:
    """Get public IP information.

    Returns:
        dict: IP information including:
            - ip: Public IP address
            - country: Country name
            - city: City name
            - hostname: Hostname
            - org: Organization name

    Raises:
        VPNError: If IP information cannot be retrieved
    """
    # List of IP info services to try
    services = [
        "https://ipinfo.io/json",
        "https://ip-api.com/json",
        "https://ipapi.co/json",
    ]

    async with aiohttp.ClientSession() as session:
        for service in services:
            try:
                async with session.get(
                    service,
                    timeout=aiohttp.ClientTimeout(total=5),
                    ssl=True,
                ) as response:
                    response.raise_for_status()
                    return await response.json()
            except (aiohttp.ClientError, asyncio.TimeoutError):
                continue

        msg = "All IP info services failed"
        raise VPNError(msg)


async def wait_for_connection(
    server_name: str,
    *,
    timeout: int = 60,
    check_interval: int = 2,
) -> dict[str, Any]:
    """Wait for VPN connection to be established.

    Args:
        server_name: Expected VPN server name
        timeout: Maximum time to wait in seconds
        check_interval: Time between checks in seconds

    Returns:
        dict: IP information when connected

    Raises:
        VPNConnectionError: If connection is not established within timeout
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            ip_info = await get_public_ip()
            if ip_info.get("hostname", "").endswith("nordvpn.com"):
                return ip_info
        except VPNError:
            pass
        await asyncio.sleep(check_interval)

    msg = f"Failed to connect to {server_name} after {timeout} seconds"
    raise VPNConnectionError(msg)
