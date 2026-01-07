"""Beautiful logging using Rich - simple and out of the box."""

import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.panel import Panel
from rich import box
from docgen.utils.config import LOG_LEVEL

# Global console for direct printing
console = Console()

# Set up Rich handler once - it's beautiful by default!
_handler = RichHandler(
    console=console,
    show_time=False,
    show_path=False,
    rich_tracebacks=True,
    markup=True,
)


def setup_logger(name: str = "docgen", level: str = None) -> logging.Logger:
    """Set up logger with Rich - beautiful out of the box."""
    logger = logging.getLogger(name)
    log_level = getattr(logging, level or LOG_LEVEL, logging.INFO)
    logger.setLevel(log_level)
    logger.handlers.clear()
    _handler.setLevel(log_level)
    logger.addHandler(_handler)
    logger.propagate = False
    return logger


# Simple convenience functions for direct console output
def step(text: str) -> str:
    console.print(f"[bold blue]→[/bold blue] [bold]{text}[/bold]")
    return ""

def success(text: str) -> str:
    console.print(f"[bold green]✓[/bold green] {text}")
    return ""

def info(text: str) -> str:
    console.print(f"[cyan]ℹ[/cyan] {text}")
    return ""

def warning(text: str) -> str:
    console.print(f"[bold yellow]⚠[/bold yellow] [yellow]{text}[/yellow]")
    return ""

def error(text: str) -> str:
    console.print(f"[bold red]✗[/bold red] [red]{text}[/red]")
    return ""

def dim(text: str) -> str:
    console.print(f"[dim]{text}[/dim]")
    return ""

def header(text: str) -> str:
    console.print()
    console.print(Panel(f"[bold cyan]{text}[/bold cyan]", box=box.DOUBLE, border_style="cyan", padding=(1, 2)))
    console.print()
    return ""




