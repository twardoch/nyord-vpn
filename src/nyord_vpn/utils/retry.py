"""Retry utilities for VPN operations."""

from functools import wraps
from typing import TypeVar, ParamSpec
from collections.abc import Callable, Awaitable

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from nyord_vpn.core.exceptions import VPNError

# Type variables for generic functions
T = TypeVar("T")
P = ParamSpec("P")


def with_retry(
    max_attempts: int = 3,
    min_wait: int = 4,
    max_wait: int = 10,
) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]:
    """Decorator to retry async operations with exponential backoff.

    Args:
        max_attempts: Maximum number of retry attempts
        min_wait: Minimum wait time between retries in seconds
        max_wait: Maximum wait time between retries in seconds

    Returns:
        Decorated function
    """
    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=min_wait, max=max_wait),
        retry=retry_if_exception_type(VPNError),
    )


def with_fallback(
    primary: Callable[P, Awaitable[T]],
    fallback: Callable[P, Awaitable[T]],
) -> Callable[P, Awaitable[T]]:
    """Create a function that falls back to a secondary implementation on failure.

    Args:
        primary: Primary async function to try first
        fallback: Fallback async function to try on failure

    Returns:
        Combined function with fallback
    """

    @wraps(primary)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return await primary(*args, **kwargs)
        except Exception as e:
            try:
                return await fallback(*args, **kwargs)
            except Exception as e2:
                msg = f"Both primary and fallback failed: {e}, {e2}"
                raise VPNError(msg) from e2

    return wrapper
