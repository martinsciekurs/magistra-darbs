---
sidebar_position: 7
---

# multi_index_global_search

**File:** `graphrag/api/query.py` (lines 196-338)

## Signature

```python
def multi_index_global_search(
    config: GraphRagConfig,
    entities_list: list[pd.DataFrame],
    communities_list: list[pd.DataFrame],
    community_reports_list: list[pd.DataFrame],
    index_names: list[str],
    community_level: int | None,
    dynamic_community_selection: bool,
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

Perform a global search across multiple indexes and return the results and associated context data.

Deprecated: Multi-index global search is deprecated and will be removed in GraphRAG v3.

Parameters
    config: GraphRagConfig. A graphrag configuration (from settings.yaml).
    entities_list: list[pd.DataFrame]. A list of DataFrames containing the final entities (from entities.parquet).
    communities_list: list[pd.DataFrame]. A list of DataFrames containing the final communities (from communities.parquet).
    community_reports_list: list[pd.DataFrame]. A list of DataFrames containing the final community reports (from community_reports.parquet).
    index_names: list[str]. A list of index names.
    community_level: int | None. The community level to search at.
    dynamic_community_selection: bool. Enable dynamic community selection instead of using all community reports at a fixed level. Note that you can still provide a community_level cap to the maximum level to search.
    response_type: str. The type of response to return.
    streaming: bool. Whether to stream the results or not. Streaming is currently not supported and will raise NotImplementedError.
    query: str. The user query to search for.
    callbacks: list[QueryCallbacks] | None. Optional callbacks to handle streaming results or events.
    verbose: bool. Verbose logging.

Returns
    tuple[
        str | dict[str, Any] | list[dict[str, Any]],
        str | list[pd.DataFrame] | dict[str, pd.DataFrame],
    ]
    The first element is the search response payload, which may be a plain string, a structured payload (dict), or a list of dicts depending on the response_type. The second element is the updated context payload, which can be a string, a list of DataFrames, or a mapping of keys to DataFrames representing the contextual data for the response.

Raises
    NotImplementedError: If streaming is requested (streaming == True).

Example
    Typical usage:
    result, context = await multi_index_global_search(
        config=config,
        entities_list=entities_list,
        communities_list=communities_list,
        community_reports_list=community_reports_list,
        index_names=index_names,
        community_level=community_level,
        dynamic_community_selection=dynamic_community_selection,
        response_type="default",
        streaming=False,
        query="example query",
        callbacks=None,
        verbose=False,
    )

    Streaming usage (not implemented):
        streaming=True currently raises NotImplementedError.

## Dependencies

This function calls:

- `graphrag/api/query.py::global_search`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/api.py::truncate`
- `graphrag/utils/api.py::update_context_data`

