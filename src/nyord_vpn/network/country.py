import json
import time

from src.nyord_vpn.models import CountryCache
from src.nyord_vpn.utils.utils import COUNTRIES_CACHE, CACHE_EXPIRY


def get_cached_countries() -> CountryCache | None:
    """Get cached country list if available and not expired."""
    try:
        if not COUNTRIES_CACHE.exists():
            return None
        # Check if cache is expired
        if time.time() - COUNTRIES_CACHE.stat().st_mtime > CACHE_EXPIRY:
            return None
        return json.loads(COUNTRIES_CACHE.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def cache_countries(data: CountryCache) -> None:
    """Cache the country list to disk.

    Args:
        data: Dictionary containing countries list and last_updated timestamp
    """
    try:
        COUNTRIES_CACHE.parent.mkdir(parents=True, exist_ok=True)
        COUNTRIES_CACHE.write_text(json.dumps(data, indent=2, sort_keys=True))
        COUNTRIES_CACHE.chmod(0o644)  # Make readable for all users
    except OSError:
        pass
