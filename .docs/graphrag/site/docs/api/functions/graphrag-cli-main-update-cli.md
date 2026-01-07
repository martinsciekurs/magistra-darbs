---
sidebar_position: 30
---

# _update_cli

**File:** `graphrag/cli/main.py` (lines 207-285)

## Signature

```python
def _update_cli(
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
        help="Run the indexing pipeline with verbose logging.",
    ),
    memprofile: bool = typer.Option(
        False,
        "--memprofile",
        help="Run the indexing pipeline with memory profiling.",
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

Update an existing knowledge graph index.

Applies a default output configuration (if not provided by config), saving the new index to the local file system in the update_output folder. If an explicit output path is provided, it overrides the base output directory specified in the configuration.

Args:
    config: Path | None - The configuration file to use. If None, the configuration is located via the project root.
    root: Path - The project root directory. Directory containing the configuration and output structure; used to locate the config when not provided.
    method: IndexingMethod - The indexing method to use. Defaults to Standard.
    verbose: bool - Run the indexing pipeline with verbose logging for detailed output.
    memprofile: bool - Run the indexing pipeline with memory profiling.
    cache: bool - Use LLM cache during processing.
    skip_validation: bool - Skip any preflight validation. Useful when running no LLM steps.
    output: Path | None - Output directory for the indexing pipeline. Overrides output.base_dir in the configuration file. If None, the configuration’s defaults are used.

Returns:
    None

Raises:
    FileNotFoundError - If the specified config or root path does not exist.
    PermissionError - If the configured or chosen output locations are not writable.
    ValueError - If an invalid combination of options is provided.
    OSError - For generic I/O errors encountered during update.
    Other exceptions may propagate from the underlying update_cli call.

## Dependencies

This function calls:

- `graphrag/cli/index.py::update_cli`

