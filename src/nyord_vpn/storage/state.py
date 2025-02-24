import json
import time

from nyord_vpn.utils.utils import STATE_FILE, logger


def save_vpn_state(state: dict) -> None:
    """Save VPN connection state to file.

    Args:
        state: Dictionary with VPN state information.

    """
    try:
        STATE_FILE.write_text(json.dumps(state, indent=2))
    except Exception as e:
        logger.warning(f"Failed to save VPN state: {e}")


def load_vpn_state() -> dict:
    """Load VPN connection state from file.

    Returns:
        Dictionary with VPN state; defaults if state is missing or expired.

    """
    try:
        if STATE_FILE.exists():
            state = json.loads(STATE_FILE.read_text())
            # Consider state valid for 5 minutes
            if time.time() - state.get("timestamp", 0) < 300:
                return state
    except Exception as e:
        logger.warning(f"Failed to load VPN state: {e}")
    return {
        "connected": False,
        "initial_ip": None,
        "connected_ip": None,
        "server": None,
        "country": None,
        "timestamp": time.time(),
    }
