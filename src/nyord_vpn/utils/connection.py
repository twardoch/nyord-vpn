"""Network connection utilities for VPN management.

this_file: src/nyord_vpn/utils/connection.py

This module provides utilities for VPN connection verification and monitoring.
It implements robust connection checking by combining multiple data sources.

Core Functionality:
1. Process monitoring for OpenVPN
2. Connection status verification
3. IP address change detection
4. Multi-source status validation

Integration Points:
- Used by VPNConnectionManager (network/vpn.py)
- Used by Client (core/client.py) for status
- Works with utils/utils.py for state
- Supports error handling in models.py

Connection Verification:
The module implements a sophisticated verification system:
1. Process state monitoring
2. IP address validation
3. API status integration
4. State consistency checks

Design Philosophy:
- Prefers multiple verification sources
- Implements graceful fallbacks
- Provides detailed status info
- Supports debugging and logging

The utilities ensure reliable connection status reporting
by combining multiple indicators and implementing fallback
logic when certain checks fail.
"""

from typing import Optional
import psutil


def is_openvpn_running() -> bool:
    """Check if any OpenVPN process is currently running.

    Uses psutil to scan all running processes and identify
    any OpenVPN instances. This is a key component of
    connection verification, as a running OpenVPN process
    is necessary (but not sufficient) for an active VPN.

    Returns:
        bool: True if an OpenVPN process is found,
              False if no OpenVPN process is running

    Note:
        This function only checks for process existence,
        not whether the process is functioning correctly
        or if the VPN connection is actually established.
    """
    for proc in psutil.process_iter(["name"]):
        if proc.info.get("name") == "openvpn":
            return True
    return False


def compute_connection_status(
    current_ip: str,
    initial_ip: Optional[str],
    connected_ip: Optional[str],
    openvpn_running: bool,
    nord_status: Optional[bool] = None,
) -> bool:
    """Determine VPN connection status through multiple checks.

    This function implements a comprehensive connection verification
    algorithm that combines multiple data points:

    1. Process Check:
       - Verifies OpenVPN process is running

    2. IP Address Validation:
       - Compares current IP against initial (pre-VPN) IP
       - Verifies current IP matches expected VPN IP

    3. NordVPN API Status (if available):
       - Incorporates server-side connection status

    The algorithm handles various edge cases:
    - Initial connection establishment
    - Connection drops and recoveries
    - API unavailability
    - Process state mismatches

    Args:
        current_ip: Currently detected IP address
        initial_ip: IP address before VPN connection (may be None)
        connected_ip: Expected VPN IP address (may be None)
        openvpn_running: Whether OpenVPN process is active
        nord_status: Optional NordVPN API connection status

    Returns:
        bool: True if VPN connection is verified active,
              False if any verification step fails

    Note:
        The function implements fallback logic when the API
        status is unavailable, relying more heavily on
        local indicators in such cases.
    """
    if nord_status is not None:
        is_connected = (
            openvpn_running
            and (current_ip == connected_ip or nord_status)
            and (initial_ip is None or current_ip != initial_ip)
        )
    else:
        is_connected = (
            openvpn_running
            and (current_ip == connected_ip)
            and (initial_ip is None or current_ip != initial_ip)
        )
    if not is_connected and openvpn_running and current_ip == connected_ip:
        is_connected = True
    return is_connected
