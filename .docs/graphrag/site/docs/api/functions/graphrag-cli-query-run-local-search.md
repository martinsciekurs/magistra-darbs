---
sidebar_position: 36
---

# run_local_search

**File:** `graphrag/cli/query.py` (lines 136-265)

## Signature

```python
def run_local_search(
    config_filepath: Path | None,
    data_dir: Path | None,
    root_dir: Path,
    community_level: int,
    response_type: str,
    streaming: bool,
    query: str,
    verbose: bool,
)
```

## Description

Perform a local search with a given query.

Loads index files required for local search and calls the Query API.

Args:
    config_filepath: Path | None
        Path to the configuration file to use, or None to use the default location.
    data_dir: Path | None
        Optional directory containing precomputed data to override the base output directory.
    root_dir: Path
        Root directory of the project.
    community_level: int
        Target community level for the search.
    response_type: str
        The type of response to return.
    streaming: bool
        If True, perform a streaming search; otherwise perform a non-streaming search.
    query: str
        The search query string used to perform the local search.
    verbose: bool
        If True, enable verbose logging output.

Returns:
    tuple[str, dict[str, Any]]
        The textual response and the context data dictionary produced by the search operation.

Raises:
    FileNotFoundError
        If the configuration file cannot be found.
    ValueError
        If the configuration is invalid or required components are missing.
    Exception
        Exceptions raised by the underlying API calls or asyncio operations may propagate to the caller.

## Dependencies

This function calls:

- `graphrag.api::local_search`
- `graphrag.api::multi_index_local_search`
- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/cli/query.py::run_streaming_search`
- `graphrag/config/load_config.py::load_config`

## Called By

This function is called by:

- `graphrag/cli/main.py::_query_cli`

