---
sidebar_position: 38
---

# run_basic_search

**File:** `graphrag/cli/query.py` (lines 389-474)

## Signature

```python
def run_basic_search(
    config_filepath: Path | None,
    data_dir: Path | None,
    root_dir: Path,
    streaming: bool,
    query: str,
    verbose: bool,
)
```

## Description

Perform a basics search with a given query.

Loads index files required for basic search and calls the Query API.

Args:
    config_filepath: Path | None
        Path to a config file to use, or None to locate one in root_dir.
    data_dir: Path | None
        Optional directory containing precomputed data to override the base output directory.
    root_dir: Path
        Root directory of the project.
    streaming: bool
        If True, perform a streaming search and print chunks as they are produced.
    query: str
        The search query string used to perform the basic search.
    verbose: bool
        If True, enable verbose output from the API calls.

Returns:
    tuple[str, dict[str, Any]]
        The full response string and the context data collected during the search.

Raises:
    FileNotFoundError
        If the config file cannot be found.
    ValueError
        If the config is invalid.
    Exception
        Exceptions raised by the underlying streaming or non-streaming API calls may propagate to the caller.

## Dependencies

This function calls:

- `graphrag.api::basic_search`
- `graphrag.api::multi_index_basic_search`
- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/cli/query.py::run_streaming_search`
- `graphrag/config/load_config.py::load_config`

## Called By

This function is called by:

- `graphrag/cli/main.py::_query_cli`

