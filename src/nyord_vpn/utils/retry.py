"""Retry utilities for VPN operations."""

from functools import wraps
from typing import TypeVar, Any
from collections.abc import Callable
from collections.abc import Coroutine

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from nyord_vpn.core.exceptions import VPNError

T = TypeVar("T")


def with_fallback(
    primary: Callable[..., Coroutine[Any, Any, T]],
    fallback: Callable[..., Coroutine[Any, Any, T]],
) -> Callable[..., Coroutine[Any, Any, T]]:
    """Decorator to fallback to secondary implementation on failure.

    Args:
        primary: Primary implementation to try first
        fallback: Fallback implementation to use on failure

    Returns:
        Wrapped function that tries primary then falls back
    """

    @retry(
        stop=stop_after_attempt(2),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(VPNError),
    )
    async def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return await primary(*args, **kwargs)
        except Exception:
            return await fallback(*args, **kwargs)

    return wrapper


def with_retry(
    func: Callable[..., Coroutine[Any, Any, T]] | None = None,
    *,
    max_attempts: int = 3,
    min_wait: float = 1,
    max_wait: float = 30,
) -> Callable[..., Coroutine[Any, Any, T]]:
    """Retry decorator for VPN operations.

    Args:
        func: Async function to retry
        max_attempts: Maximum number of retry attempts
        min_wait: Minimum wait time between retries in seconds
        max_wait: Maximum wait time between retries in seconds

    Returns:
        Decorated async function that will retry on failure
    """

    def decorator(
        f: Callable[..., Coroutine[Any, Any, T]],
    ) -> Callable[..., Coroutine[Any, Any, T]]:
        @retry(
            stop=stop_after_attempt(max_attempts),
            wait=wait_exponential(multiplier=1, min=min_wait, max=max_wait),
            retry=retry_if_exception_type(VPNError),
        )
        @wraps(f)
        async def wrapper(*args: Any, **kwargs: Any) -> T:
            return await f(*args, **kwargs)

        return wrapper

    if func is None:
        return decorator
    return decorator(func)
