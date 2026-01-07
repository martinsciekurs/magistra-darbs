---
sidebar_position: 10
---

# drift_search

**File:** `graphrag/api/query.py` (lines 708-769)

## Signature

```python
def drift_search(
    config: GraphRagConfig,
    entities: pd.DataFrame,
    communities: pd.DataFrame,
    community_reports: pd.DataFrame,
    text_units: pd.DataFrame,
    relationships: pd.DataFrame,
    community_level: int,
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

Perform a DRIFT search and return the context data and response.

Parameters
----------
- config (GraphRagConfig): A graphrag configuration (from settings.yaml).
- entities (pd.DataFrame): A DataFrame containing the final entities (from entities.parquet).
- communities (pd.DataFrame): A DataFrame containing the final communities (from communities.parquet).
- community_reports (pd.DataFrame): A DataFrame containing the final community reports (from community_reports.parquet).
- text_units (pd.DataFrame): A DataFrame containing the final text units (from text_units.parquet).
- relationships (pd.DataFrame): A DataFrame containing the final relationships (from relationships.parquet).
- community_level (int): The community level to search at.
- response_type (str): The type of response to generate (e.g., full, compact).
- query (str): The user query to search for.
- callbacks (list[QueryCallbacks] | None): Optional list of callback handlers to receive streaming and context information.
- verbose (bool): Enable verbose logging for debugging.

Returns
----------
tuple[str | dict[str, Any] | list[dict[str, Any]], str | list[pd.DataFrame] | dict[str, pd.DataFrame]]: A tuple containing the search response and the context data. The first element is the generated response, which can be a string, a dictionary, or a list of dictionaries depending on the response_type. The second element is the context data, which may be a string, a list of DataFrames, or a mapping of strings to DataFrames.

Raises
----------
pydantic.ValidationError: If input arguments fail validation via the validate_call decorator.

## Dependencies

This function calls:

- `graphrag/api/query.py::drift_search_streaming`
- `graphrag/callbacks/noop_query_callbacks.py::NoopQueryCallbacks`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`

## Called By

This function is called by:

- `graphrag/api/query.py::multi_index_drift_search`

