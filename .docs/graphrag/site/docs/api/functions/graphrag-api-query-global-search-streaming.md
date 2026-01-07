---
sidebar_position: 5
---

# global_search_streaming

**File:** `graphrag/api/query.py` (lines 128-192)

## Signature

```python
def global_search_streaming(
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
) -> AsyncGenerator
```

## Description

Perform a global search and stream the response in chunks via an async generator.

Args:
  config: GraphRagConfig: A graphrag configuration (from settings.yaml).
  entities: pd.DataFrame: A DataFrame containing the final entities (from entities.parquet).
  communities: pd.DataFrame: A DataFrame containing the final communities (from communities.parquet).
  community_reports: pd.DataFrame: A DataFrame containing the final community reports (from community_reports.parquet).
  community_level: int | None: The community level to search at.
  dynamic_community_selection: bool: Enable dynamic community selection instead of using all community reports at a fixed level. Note that you can still provide community_level cap the maximum level to search.
  response_type: str: The type of response to return.
  query: str: The user query to search for.
  callbacks: list[QueryCallbacks] | None: Optional callbacks to receive streaming events.
  verbose: bool: If True, enable verbose logging.
Returns:
  AsyncGenerator: An asynchronous generator yielding strings; each yielded chunk is part of the streaming global search response.
Raises:
  pydantic.ValidationError: If input arguments fail validation via the validate_call decorator.

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/query/factory.py::get_global_search_engine`
- `graphrag/query/indexer_adapters.py::read_indexer_communities`
- `graphrag/query/indexer_adapters.py::read_indexer_entities`
- `graphrag/query/indexer_adapters.py::read_indexer_reports`
- `graphrag/utils/api.py::load_search_prompt`

## Called By

This function is called by:

- `graphrag/api/query.py::global_search`

