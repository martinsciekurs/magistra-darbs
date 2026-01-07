---
sidebar_position: 6
---

# global_search

**File:** `graphrag/api/query.py` (lines 64-124)

## Signature

```python
def global_search(
    config: GraphRagConfig,
    entities: pd.DataFrame,
    communities: pd.DataFrame,
    community_reports: pd.DataFrame,
    community_level: int | None,
    dynamic_community_selection: bool,
    response_type: str,
    query: str,
    callbacks: list[QueryCallbacks] | None = None,
    verbose: bool = False,
) -> tuple[
    str | dict[str, Any] | list[dict[str, Any]],
    str | list[pd.DataFrame] | dict[str, pd.DataFrame],
]
```

## Description

Perform a global search and return the full response and context data.

Args:
    config: GraphRagConfig. A graphrag configuration (from settings.yaml).
    entities: pd.DataFrame. A DataFrame containing the final entities (from entities.parquet).
    communities: pd.DataFrame. A DataFrame containing the final communities (from communities.parquet).
    community_reports: pd.DataFrame. A DataFrame containing the final community reports (from community_reports.parquet).
    community_level: int | None. The community level to search at.
    dynamic_community_selection: bool. Enable dynamic community selection instead of using all community reports at a fixed level. Note that you can still provide a community_level to cap the maximum level to search.
    response_type: str. The type of response to return.
    query: str. The user query to search for.
    callbacks: list[QueryCallbacks] | None. Optional list of QueryCallbacks to be invoked during the search.
    verbose: bool. Enable verbose logging during the search.

Returns:
    tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]: 
        The first element is the aggregated response produced by the search. This can be a string or a structured object (e.g., dict or list) depending on response_type.
        The second element is the context data captured during the search. This may be a string, a list of DataFrames, or a dictionary of DataFrames depending on how context was populated.

Raises:
    pydantic.ValidationError: If input arguments fail type validation.
    Exception: If an unexpected error occurs during streaming or processing.

## Dependencies

This function calls:

- `graphrag/api/query.py::global_search_streaming`
- `graphrag/callbacks/noop_query_callbacks.py::NoopQueryCallbacks`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`

## Called By

This function is called by:

- `graphrag/api/query.py::multi_index_global_search`

