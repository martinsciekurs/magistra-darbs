---
sidebar_position: 37
---

# run_drift_search

**File:** `graphrag/cli/query.py` (lines 268-386)

## Signature

```python
def run_drift_search(
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

Perform a local drift search for a given query across either a multi-index or single-index dataset, with optional streaming of results.

Loads index files required for local search and calls the appropriate Query API depending on the loaded index layout.

Args:
    config_filepath (Path | None): Path to the configuration file to use, or None to use the default configuration.
    data_dir (Path | None): Optional directory containing precomputed data to override the base output directory.
    root_dir (Path): Root directory of the project.
    community_level (int): Target community level for the drift search.
    response_type (str): The type of response to request from the API.
    streaming (bool): If True, stream results as they are produced. Streaming prints each received chunk to stdout (without buffering) and may update the context data during streaming.
    query (str): The drift search query string used to perform the local search.
    verbose (bool): If True, print verbose progress and diagnostic information.

Returns:
    tuple[str, dict[str, Any]]: A pair consisting of the final response as a string and a dictionary containing context data captured during the operation.

Raises:
    FileNotFoundError: If the configuration file cannot be found.
    ValueError: If the configuration is invalid or required configuration data are missing.
    Exceptions propagated from the underlying API calls or asyncio operations may occur (e.g., during streaming or remote calls).

Notes on behavior:
    - Internal flow depends on the index layout loaded by _resolve_output_files:
      • If dataframe_dict["multi-index"] is True, this function uses the Multi-Index Drift Search API
        and returns the API response along with context data. The response is printed to stdout.
      • Otherwise, a Single-Index Drift Search workflow is used:
        - If streaming is enabled, an asynchronous streaming search is performed. Chunks are printed as they arrive,
          and a final full response string along with context data is returned.
        - If streaming is disabled, a single non-streaming search is performed; the final response is printed and
          returned with context data.

Notes on side effects:
    - Printing: In both multi-index and non-streaming single-index paths, the final response is printed to stdout.
    - Streaming path: Each streamed chunk is printed immediately as it is received, followed by a newline at the end.
    - Context data: The context data is captured via an on_context callback during streaming and returned with the response.

## Dependencies

This function calls:

- `graphrag.api::drift_search`
- `graphrag.api::multi_index_drift_search`
- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/cli/query.py::run_streaming_search`
- `graphrag/config/load_config.py::load_config`

## Called By

This function is called by:

- `graphrag/cli/main.py::_query_cli`

