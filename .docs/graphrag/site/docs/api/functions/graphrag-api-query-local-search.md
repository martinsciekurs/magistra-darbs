---
sidebar_position: 12
---

# local_search

**File:** `graphrag/api/query.py` (lines 342-406)

## Signature

```python
def local_search(
    config: GraphRagConfig,
    entities: pd.DataFrame,
    communities: pd.DataFrame,
    community_reports: pd.DataFrame,
    text_units: pd.DataFrame,
    relationships: pd.DataFrame,
    covariates: pd.DataFrame | None,
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

Perform a local search and return the aggregated response and any context data captured during streaming.

This function initializes logging, wires a context-capturing callback, and streams results via local_search_streaming. Chunks yielded by the streaming engine are concatenated into a single full_response string. The latest context data emitted during streaming is returned as context_data.

Args:
  config: GraphRagConfig
      A graphrag configuration (from settings.yaml).
  entities: pandas.DataFrame
      The final entities (from entities.parquet).
  communities: pandas.DataFrame
      The final communities (from communities.parquet).
  community_reports: pandas.DataFrame
      The final community reports (from community_reports.parquet).
  text_units: pandas.DataFrame
      The final text units (from text_units.parquet).
  relationships: pandas.DataFrame
      The final relationships (from relationships.parquet).
  covariates: pandas.DataFrame | None
      The final covariates (from covariates.parquet), or None if not available.
  community_level: int
      The community level to search at.
  response_type: str
      The response type to return.
  query: str
      The user query to search for.
  callbacks: list[QueryCallbacks] | None
      Optional list of callback handlers. Defaults to None.
  verbose: bool
      Whether to enable verbose logging. Defaults to False.

Returns:
  tuple[str, dict[str, Any] | list[dict[str, Any]] | dict[str, pd.DataFrame] | list[pd.DataFrame]]
      A tuple containing:
      - full_response: the aggregated response string produced by streaming.
      - context_data: the latest context data captured from streaming (structure depends on the engine; commonly a dict).

Examples:
  result, ctx = local_search(
      config=config,
      entities=entities_df,
      communities=communities_df,
      community_reports=reports_df,
      text_units=text_units_df,
      relationships=relationships_df,
      covariates=covariates_df,
      community_level=2,
      response_type="full",
      query="quantum computing",
      verbose=True,
  )

Raises:
  pydantic.ValidationError: If the input arguments do not satisfy the declared types.
  Exception: Any exception raised by the underlying streaming engine or callback processing.

## Dependencies

This function calls:

- `graphrag/api/query.py::local_search_streaming`
- `graphrag/callbacks/noop_query_callbacks.py::NoopQueryCallbacks`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`

## Called By

This function is called by:

- `graphrag/api/query.py::multi_index_local_search`

