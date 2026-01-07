---
sidebar_position: 14
---

# multi_index_basic_search

**File:** `graphrag/api/query.py` (lines 1152-1226)

## Signature

```python
def multi_index_basic_search(
    config: GraphRagConfig,
    text_units_list: list[pd.DataFrame],
    index_names: list[str],
    streaming: bool,
    query: str,
    callbacks: list[QueryCallbacks] | None = None,
    verbose: bool = False,
) -> tuple[
    str | dict[str, Any] | list[dict[str, Any]],
    str | list[pd.DataFrame] | dict[str, pd.DataFrame],
]
```

## Description

Perform a basic search across multiple indexes and return the search results and associated context data.

Args:
    config (GraphRagConfig): A graphrag configuration (from settings.yaml).
    text_units_list (list[pd.DataFrame]): A list of DataFrames containing the final text units (from text_units.parquet).
    index_names (list[str]): A list of index names.
    streaming (bool): Whether to stream the results or not. Streaming is not implemented for this function.
    query (str): The user query to search for.
    callbacks (list[QueryCallbacks] | None): Optional callbacks for processing the search.
    verbose (bool): If True, enable verbose logging.

Returns:
    tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]: A tuple containing the search response and the context data. The first element can be a string, a dict, or a list of dicts. The second element can be a string, a list of DataFrames, or a dict mapping strings to DataFrames.

Raises:
    NotImplementedError: If streaming is True; streaming is not yet implemented for multi_index_basic_search.

## Dependencies

This function calls:

- `graphrag/api/query.py::basic_search`
- `graphrag/logger/standard_logging.py::init_loggers`

