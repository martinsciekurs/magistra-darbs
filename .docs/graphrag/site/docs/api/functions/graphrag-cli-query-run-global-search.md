---
sidebar_position: 35
---

# run_global_search

**File:** `graphrag/cli/query.py` (lines 24-133)

## Signature

```python
def run_global_search(
    config_filepath: Path | None,
    data_dir: Path | None,
    root_dir: Path,
    community_level: int | None,
    dynamic_community_selection: bool,
    response_type: str,
    streaming: bool,
    query: str,
    verbose: bool,
)
```

## Description

Perform a global search with a given query.

Loads index files required for global search and calls the Query API.

Args:
    config_filepath: Path to a config file, or None.
    data_dir: Optional data directory to override output.base_dir, or None.
    root_dir: Root directory of the project.
    community_level: Optional integer indicating the target community level.
    dynamic_community_selection: Whether to dynamically select communities.
    response_type: Type of response to return.
    streaming: True to use streaming mode; False for a standard response.
    query: The search query.
    verbose: If True, enable verbose output.

Returns:
    tuple[str, dict[str, Any]]: The response as a string and a context data dictionary.

Raises:
    FileNotFoundError: If the config file cannot be found.
    ValueError: If the loaded configuration is invalid.
    Exception: Exceptions raised by the underlying API calls or asyncio operations may propagate to the caller.

## Dependencies

This function calls:

- `graphrag.api::global_search`
- `graphrag.api::multi_index_global_search`
- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/cli/query.py::run_streaming_search`
- `graphrag/config/load_config.py::load_config`

## Called By

This function is called by:

- `graphrag/cli/main.py::_query_cli`

