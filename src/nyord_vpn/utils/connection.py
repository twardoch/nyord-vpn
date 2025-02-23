from typing import Optional
import psutil


def is_openvpn_running() -> bool:
    """Check if any OpenVPN process is running."""
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
    """
    Compute if the VPN connection is active.

    Args:
        current_ip: Current IP address.
        initial_ip: The initial IP before VPN activation.
        connected_ip: The recorded VPN IP.
        openvpn_running: Whether an OpenVPN process is running.
        nord_status: Optional flag from NordVPN API indicating VPN status.

    Returns:
        True if VPN is active, False otherwise.
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
