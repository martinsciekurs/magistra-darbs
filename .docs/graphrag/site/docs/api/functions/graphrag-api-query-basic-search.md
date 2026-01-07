---
sidebar_position: 8
---

# basic_search

**File:** `graphrag/api/query.py` (lines 1057-1102)

## Signature

```python
def basic_search(
    config: GraphRagConfig,
    text_units: pd.DataFrame,
    query: str,
    callbacks: list[QueryCallbacks] | None = None,
    verbose: bool = False,
) -> tuple[
    str | dict[str, Any] | list[dict[str, Any]],
    str | list[pd.DataFrame] | dict[str, pd.DataFrame],
]
```

## Description

Perform a basic search and return the response and the context data.

Parameters
    config (GraphRagConfig): A graphrag configuration (from settings.yaml).
    text_units (pd.DataFrame): A DataFrame containing the final text units (from text_units.parquet).
    query (str): The user query to search for.
    callbacks (list[QueryCallbacks] | None): Optional callbacks for processing the search.
    verbose (bool): If True, enable verbose logging.

Returns
    tuple[str, dict[str, Any]]: The first element is the concatenated response string produced by streaming, and the second element is the context data dict collected from the streaming callbacks.

Notes
    - The function initializes logging via init_loggers and writes to query.log.
    - It attaches a local NoopQueryCallbacks that updates context_data through its on_context callback.
    - The returned context_data reflects the most recent context produced by the streaming process.

Raises
    pydantic.ValidationError: If input arguments fail validation by the validate_call decorator.

## Dependencies

This function calls:

- `graphrag/api/query.py::basic_search_streaming`
- `graphrag/callbacks/noop_query_callbacks.py::NoopQueryCallbacks`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`

## Called By

This function is called by:

- `graphrag/api/query.py::multi_index_basic_search`

