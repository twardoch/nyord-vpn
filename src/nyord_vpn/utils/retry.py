"""Retry utilities for VPN operations."""

from functools import wraps
from typing import TypeVar, Any, cast
from collections.abc import Callable, Coroutine

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from nyord_vpn.core.exceptions import VPNError

T = TypeVar("T")


def with_fallback(primary: Callable[..., T], fallback: Callable[..., T]):
    """Decorator to fallback to secondary implementation on failure.

    Args:
        primary: Primary implementation to try first
        fallback: Fallback implementation to use on failure

    Returns:
        Wrapped function that tries primary then falls back
    """

    @backoff.on_exception(backoff.expo, Exception, max_tries=2, jitter=None)
    async def wrapper(*args, **kwargs) -> T:
        try:
            return await primary(*args, **kwargs)
        except Exception:
            return await fallback(*args, **kwargs)

    return wrapper


def with_retry(
    func: Callable[..., Coroutine[Any, Any, T]],
) -> Callable[..., Coroutine[Any, Any, T]]:
    """Retry decorator for VPN operations.

    Args:
        func: Async function to retry

    Returns:
        Decorated async function that will retry on failure
    """

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(VPNError),
    )
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> T:
        """Wrapper function that adds retry logic.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Result of decorated function

        Raises:
            VPNError: If all retries fail
        """
        result = await func(*args, **kwargs)
        return cast(T, result)

    return cast(Callable[..., Coroutine[Any, Any, T]], wrapper)
