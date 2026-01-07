---
sidebar_position: 16
---

# multi_index_local_search

**File:** `graphrag/api/query.py` (lines 476-704)

## Signature

```python
def multi_index_local_search(
    config: GraphRagConfig,
    entities_list: list[pd.DataFrame],
    communities_list: list[pd.DataFrame],
    community_reports_list: list[pd.DataFrame],
    text_units_list: list[pd.DataFrame],
    relationships_list: list[pd.DataFrame],
    covariates_list: list[pd.DataFrame] | None,
    index_names: list[str],
    community_level: int,
    response_type: str,
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

Perform a local search across multiple indexes and return the rendered response and updated context data.

Args:
  config: GraphRagConfig
      A graphrag configuration (from settings.yaml).
  entities_list: list[pd.DataFrame]
      A list of DataFrames containing the final entities (from entities.parquet).
  communities_list: list[pd.DataFrame]
      A list of DataFrames containing the final communities (from communities.parquet).
  community_reports_list: list[pd.DataFrame]
      A list of DataFrames containing the final community reports (from community_reports.parquet).
  text_units_list: list[pd.DataFrame]
      A list of DataFrames containing the final text units (from text_units.parquet).
  relationships_list: list[pd.DataFrame]
      A list of DataFrames containing the final relationships (from relationships.parquet).
  covariates_list: list[pd.DataFrame] | None
      Optional; A list of DataFrames containing the final covariates (from covariates.parquet).
  index_names: list[str]
      A list of index names.
  community_level: int
      The community level to search at.
  response_type: str
      The response type to return.
  streaming: bool
      Whether to stream the results or not. Streaming is not yet implemented for this multi-index search.
  query: str
      The user query to search for.
  callbacks: list[QueryCallbacks] | None
      Optional; Callbacks to customize query handling.
  verbose: bool
      Enable verbose logging.

Returns:
  tuple[
      str | dict[str, Any] | list[dict[str, Any]],
      str | list[pd.DataFrame] | dict[str, pd.DataFrame],
  ]
  A tuple containing the rendered response and the updated context data. The first element is
  the response as a string or a structured object (dict or list of dicts) depending on the
  requested format. The second element is the context data, which may be a string, a list of DataFrames,
  or a dict mapping string keys to DataFrames.

Raises:
  NotImplementedError
      If streaming is requested (streaming == True), as streaming is not yet implemented for this
      multi-index local search.

## Dependencies

This function calls:

- `graphrag/api/query.py::local_search`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`
- `graphrag/utils/api.py::update_context_data`

