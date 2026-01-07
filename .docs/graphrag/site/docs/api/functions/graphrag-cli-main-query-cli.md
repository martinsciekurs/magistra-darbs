---
sidebar_position: 27
---

# _query_cli

**File:** `graphrag/cli/main.py` (lines 414-545)

## Signature

```python
def _query_cli(
    method: SearchMethod = typer.Option(
        ...,
        "--method",
        "-m",
        help="The query algorithm to use.",
    ),
    query: str = typer.Option(
        ...,
        "--query",
        "-q",
        help="The query to execute.",
    ),
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
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Run the query with verbose logging.",
    ),
    data: Path | None = typer.Option(
        None,
        "--data",
        "-d",
        help="Index output directory (contains the parquet files).",
        exists=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        autocompletion=ROOT_AUTOCOMPLETE,
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
    community_level: int = typer.Option(
        2,
        "--community-level",
        help=(
            "Leiden hierarchy level from which to load community reports. "
            "Higher values represent smaller communities."
        ),
    ),
    dynamic_community_selection: bool = typer.Option(
        False,
        "--dynamic-community-selection/--no-dynamic-selection",
        help="Use global search with dynamic community selection.",
    ),
    response_type: str = typer.Option(
        "Multiple Paragraphs",
        "--response-type",
        help=(
            "Free-form description of the desired response format "
            "(e.g. 'Single Sentence', 'List of 3-7 Points', etc.)."
        ),
    ),
    streaming: bool = typer.Option(
        False,
        "--streaming/--no-streaming",
        help="Print the response in a streaming manner.",
    ),
) -> None
```

## Description

Query a knowledge graph index.

Args:
    method: The query algorithm to use.
    query: The query to execute.
    config: The configuration to use.
    verbose: Run the query with verbose logging.
    data: Index output directory (contains the parquet files).
    root: The project root directory.
    community_level: Leiden hierarchy level from which to load community reports. Higher values represent smaller communities.
    dynamic_community_selection: Use global search with dynamic community selection.
    response_type: Free-form description of the desired response format (e.g. 'Single Sentence', 'List of 3-7 Points', etc.).
    streaming: Print the response in a streaming manner.

Returns:
    None

Raises:
    ValueError

## Dependencies

This function calls:

- `graphrag/cli/query.py::run_basic_search`
- `graphrag/cli/query.py::run_drift_search`
- `graphrag/cli/query.py::run_global_search`
- `graphrag/cli/query.py::run_local_search`

