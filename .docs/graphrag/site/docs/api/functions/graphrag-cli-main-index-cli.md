---
sidebar_position: 28
---

# _index_cli

**File:** `graphrag/cli/main.py` (lines 120-203)

## Signature

```python
def _index_cli(
    config: Path | None = typer.Option(
        None,
        "--config",
        "-c",
        help="The configuration to use.",
        exists=True,
        file_okay=True,
        readable=True,
        autocompletion=CONFIG_AUTOCOMPLETE,
    ),
    root: Path = typer.Option(
        Path(),
        "--root",
        "-r",
        help="The project root directory.",
        exists=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        autocompletion=ROOT_AUTOCOMPLETE,
    ),
    method: IndexingMethod = typer.Option(
        IndexingMethod.Standard.value,
        "--method",
        "-m",
        help="The indexing method to use.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Run the indexing pipeline with verbose logging",
    ),
    memprofile: bool = typer.Option(
        False,
        "--memprofile",
        help="Run the indexing pipeline with memory profiling",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help=(
            "Run the indexing pipeline without executing any steps "
            "to inspect and validate the configuration."
        ),
    ),
    cache: bool = typer.Option(
        True,
        "--cache/--no-cache",
        help="Use LLM cache.",
    ),
    skip_validation: bool = typer.Option(
        False,
        "--skip-validation",
        help="Skip any preflight validation. Useful when running no LLM steps.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help=(
            "Indexing pipeline output directory. "
            "Overrides output.base_dir in the configuration file."
        ),
        dir_okay=True,
        writable=True,
        resolve_path=True,
    ),
) -> None
```

## Description

Build a knowledge graph index.

Args:
    config: The configuration to use.
    root: The project root directory.
    method: The indexing method to use.
    verbose: Run the indexing pipeline with verbose logging.
    memprofile: Run the indexing pipeline with memory profiling.
    dry_run: Run the indexing pipeline without executing any steps to inspect and validate the configuration.
    cache: Use LLM cache.
    skip_validation: Skip any preflight validation. Useful when running no LLM steps.
    output: Indexing pipeline output directory. Overrides output.base_dir in the configuration file.

Returns:
    None

Raises:
    Exceptions raised by graphrag.cli.index.index_cli may propagate.

## Dependencies

This function calls:

- `graphrag/cli/index.py::index_cli`

