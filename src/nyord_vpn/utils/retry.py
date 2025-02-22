"""Retry utilities for VPN operations."""

import asyncio
import functools
from typing import Any, TypeVar
from collections.abc import Callable, Awaitable

from nyord_vpn.core.exceptions import VPNError

T = TypeVar("T")


def with_retry(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable[[Callable[..., Awaitable[T]]], Callable[..., Awaitable[T]]]:
    """Decorator to retry async functions with exponential backoff.

    Args:
        max_retries: Maximum number of retries
        delay: Initial delay between retries in seconds
        backoff: Backoff multiplier for each retry

    Returns:
        Decorated function
    """

    def decorator(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> T:
            last_error = None
            current_delay = delay

            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except (VPNError, asyncio.TimeoutError, OSError) as e:
                    last_error = e
                    if attempt < max_retries - 1:
                        await asyncio.sleep(current_delay)
                        current_delay *= backoff
                    continue

            if last_error:
                raise last_error

            # This should never happen, but makes the type checker happy
            msg = "Retry failed with no error"
            raise VPNError(msg)

        return wrapper

    return decorator


def with_fallback(
    primary_func: Callable[..., Awaitable[T]],
    fallback_func: Callable[..., Awaitable[T]],
) -> Callable[..., Awaitable[T]]:
    """Create a function that falls back to a secondary implementation.

    Args:
        primary_func: Primary function to try first
        fallback_func: Fallback function to try if primary fails

    Returns:
        Combined function that tries primary then fallback
    """

    @functools.wraps(primary_func)
    async def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return await primary_func(*args, **kwargs)
        except (VPNError, asyncio.TimeoutError, OSError):
            return await fallback_func(*args, **kwargs)

    return wrapper
