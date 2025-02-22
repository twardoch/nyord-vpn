"""Logging utilities for VPN operations."""

import logging
import sys
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler

# Console for rich output
console = Console()


def setup_logging(
    level: str | int = logging.INFO,
    log_file: Path | None = None,
    rich_output: bool = True,
) -> logging.Logger:
    """Setup logging configuration.

    Args:
        level: Logging level
        log_file: Optional file to log to
        rich_output: Whether to use rich output

    Returns:
        Logger instance
    """
    # Create logger
    logger = logging.getLogger("nyord_vpn")
    logger.setLevel(level)

    # Remove existing handlers
    logger.handlers.clear()

    if rich_output:
        # Rich console handler
        console_handler = RichHandler(console=console, show_time=True, show_path=False)
    else:
        # Basic console handler
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    if log_file:
        # File handler
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_operation(operation: str) -> None:
    """Log VPN operation with rich formatting.

    Args:
        operation: Operation description
    """
    console.print(f"[bold blue]{operation}[/bold blue]")


def log_success(message: str) -> None:
    """Log success message with rich formatting.

    Args:
        message: Success message
    """
    console.print(f"[bold green]✓ {message}[/bold green]")


def log_error(message: str) -> None:
    """Log error message with rich formatting.

    Args:
        message: Error message
    """
    console.print(f"[bold red]✗ {message}[/bold red]")


def log_warning(message: str) -> None:
    """Log warning message with rich formatting.

    Args:
        message: Warning message
    """
    console.print(f"[bold yellow]! {message}[/bold yellow]")
