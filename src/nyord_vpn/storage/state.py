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
            - current_ip (str, optional): Current IP after disconnection

    Note:
        The state file is used for connection recovery
        and status monitoring. Failed saves are logged
        but don't raise exceptions to prevent disrupting
        VPN operations.

    """
    try:
        # Load existing state to preserve important info
        existing = {}
        if STATE_FILE.exists():
            try:
                existing = json.loads(STATE_FILE.read_text())
            except json.JSONDecodeError:
                pass

        # Handle IP updates
        current_ip = state.get("current_ip")
        
        # If we're disconnected and have a current_ip, that's definitely our normal_ip
        # This happens after a disconnect operation (bye command)
        if not state.get("connected") and current_ip:
            state["normal_ip"] = current_ip  # Decisively update normal_ip
            state["connected_ip"] = None     # Clear VPN IP
        # If we're connected and have a current_ip, it's our VPN IP
        elif state.get("connected") and current_ip:
            state["connected_ip"] = current_ip
            # Keep existing normal_ip while connected
            if not state.get("normal_ip") and existing.get("normal_ip"):
                state["normal_ip"] = existing.get("normal_ip")

        # Ensure timestamp is updated
        state["timestamp"] = time.time()

        # Write state atomically using temp file
        temp_state = STATE_FILE.with_suffix(".tmp")
        temp_state.write_text(json.dumps(state, indent=2))
        temp_state.replace(STATE_FILE)

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
            # Even if state is stale, preserve IPs
            default = {
                "connected": False,
                "normal_ip": state.get("normal_ip"),
                "connected_ip": None,
                "server": None,
                "country": None,
                "timestamp": time.time(),
            }
            return default
    except Exception as e:
        logger.warning(f"Failed to load VPN state: {e}")

    return {
        "connected": False,
        "normal_ip": None,
        "connected_ip": None,
        "server": None,
        "country": None,
        "timestamp": time.time(),
    }
