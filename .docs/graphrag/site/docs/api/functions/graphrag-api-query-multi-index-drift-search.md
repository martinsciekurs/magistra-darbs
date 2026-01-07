---
sidebar_position: 15
---

# multi_index_drift_search

**File:** `graphrag/api/query.py` (lines 845-1053)

## Signature

```python
def multi_index_drift_search(
    config: GraphRagConfig,
    entities_list: list[pd.DataFrame],
    communities_list: list[pd.DataFrame],
    community_reports_list: list[pd.DataFrame],
    text_units_list: list[pd.DataFrame],
    relationships_list: list[pd.DataFrame],
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

Perform a DRIFT search across multiple indexes and return the search result and updated context data.

Args:
    config (GraphRagConfig): A graphrag configuration (from settings.yaml).
    entities_list (list[pd.DataFrame]): A list of DataFrames containing the final entities (from entities.parquet).
        Each DataFrame is expected to include columns such as human_readable_id, id, title, and text_unit_ids.
    communities_list (list[pd.DataFrame]): A list of DataFrames containing the final communities (from communities.parquet).
        Each DataFrame is expected to include columns such as community, entity_ids, and human_readable_id.
    community_reports_list (list[pd.DataFrame]): A list of DataFrames containing the final community reports (from community_reports.parquet).
        Each DataFrame is expected to include columns such as community, id, and human_readable_id.
    text_units_list (list[pd.DataFrame]): A list of DataFrames containing the final text units (from text_units.parquet).
        Each DataFrame should include at least id and human_readable_id.
    relationships_list (list[pd.DataFrame]): A list of DataFrames containing the final relationships (from relationships.parquet).
        Each DataFrame is expected to include human_readable_id, source, target, and text_unit_ids.
    index_names (list[str]): A list of index names.
    community_level (int): The community level to search at.
    response_type (str): The type of response to return.
    streaming (bool): Whether to stream the results or not. Streaming is not yet implemented; if True a NotImplementedError will be raised.
    query (str): The user query to search for.
    callbacks (list[QueryCallbacks] | None): Optional callbacks to apply to the search.
    verbose (bool): Enable verbose logging.

Returns:
    tuple[
        str | dict[str, Any] | list[dict[str, Any]],
        str | list[pd.DataFrame] | dict[str, pd.DataFrame],
    ]: A tuple consisting of the search result payload and the updated context data.
        - The first element (result) may be a string, a dictionary mapping string keys to result data, or a list of result dictionaries.
        - The second element (context) is either a string, a list of DataFrames, or a dictionary mapping keys to DataFrames.

Raises:
    NotImplementedError: If streaming is requested, as streaming is not yet implemented for multi_index_drift_search.

Examples:
    result, context = await multi_index_drift_search(
        config=cfg,
        entities_list=entities_per_index,
        communities_list=communities_per_index,
        community_reports_list=reports_per_index,
        text_units_list=text_units_per_index,
        relationships_list=relationships_per_index,
        index_names=["idx_a", "idx_b"],
        community_level=1,
        response_type="full",
        streaming=False,
        query="find drift",
        callbacks=None,
        verbose=True,
    )

## Dependencies

This function calls:

- `graphrag/api/query.py::drift_search`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`
- `graphrag/utils/api.py::update_context_data`

