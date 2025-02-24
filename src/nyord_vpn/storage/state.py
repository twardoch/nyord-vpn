import json
import time

from nyord_vpn.utils.utils import STATE_FILE, logger


def save_vpn_state(state: dict) -> None:
    """Save VPN connection state to persistent storage.

    Maintains a record of the VPN connection state including:
    1. Connection status and timing
    2. IP address information (original and VPN)
    3. Server details and location
    4. State metadata

    Args:
        state: Dictionary containing state information:
            - connected (bool): Current connection status
            - normal_ip (str): IP address when not connected to VPN
            - connected_ip (str): VPN-assigned IP
            - server (str): Connected server hostname
            - country (str): Server country
            - timestamp (float): State update time

    Note:
        The state file is used for connection recovery
        and status monitoring. Failed saves are logged
        but don't raise exceptions to prevent disrupting
        VPN operations.
    """
    try:
        # If we're saving a disconnected state, update normal_ip
        if not state.get("connected"):
            current_ip = state.get("current_ip")
            if current_ip:
                state["normal_ip"] = current_ip

        # Load existing state to preserve normal_ip if not present
        if STATE_FILE.exists():
            try:
                existing = json.loads(STATE_FILE.read_text())
                if not state.get("normal_ip"):
                    state["normal_ip"] = existing.get("normal_ip")
            except json.JSONDecodeError:
                pass

        # Ensure timestamp is updated
        state["timestamp"] = time.time()

        STATE_FILE.write_text(json.dumps(state, indent=2))
    except Exception as e:
        logger.warning(f"Failed to save VPN state: {e}")


def load_vpn_state() -> dict:
    """Load VPN connection state from storage.

    Retrieves and validates the stored VPN state:
    1. Checks state file existence
    2. Validates state freshness (5 minute TTL)
    3. Provides default state if needed

    Returns:
        dict: State information containing:
            - connected (bool): Connection status
            - normal_ip (str|None): IP when not connected to VPN
            - connected_ip (str|None): VPN IP
            - server (str|None): Server hostname
            - country (str|None): Server country
            - timestamp (float): Update time

    Note:
        The state is considered stale after 5 minutes
        to prevent using outdated connection information.
        Failed loads return a safe default state.
    """
    try:
        if STATE_FILE.exists():
            state = json.loads(STATE_FILE.read_text())
            # State is valid for 5 minutes
            if time.time() - state.get("timestamp", 0) < 300:
                return state
    except Exception as e:
        logger.warning(f"Failed to load VPN state: {e}")

    return {
        "connected": False,
        "normal_ip": None,  # IP address when not connected to VPN
        "connected_ip": None,  # IP address when connected to VPN
        "server": None,
        "country": None,
        "timestamp": time.time(),
    }
