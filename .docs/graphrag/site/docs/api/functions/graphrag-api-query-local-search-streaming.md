---
sidebar_position: 13
---

# local_search_streaming

**File:** `graphrag/api/query.py` (lines 410-472)

## Signature

```python
def local_search_streaming(
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
) -> AsyncGenerator
```

## Description

Perform a local search and stream results via an asynchronous generator.

Args:
  config (GraphRagConfig): A graphrag configuration (from settings.yaml)
  entities (pd.DataFrame): A DataFrame containing the final entities (from entities.parquet)
  communities (pd.DataFrame): A DataFrame containing the final communities (from communities.parquet)
  community_reports (pd.DataFrame): A DataFrame containing the final community reports (from community_reports.parquet)
  text_units (pd.DataFrame): A DataFrame containing the final text units (from text_units.parquet)
  relationships (pd.DataFrame): A DataFrame containing the final relationships (from relationships.parquet)
  covariates (pd.DataFrame | None): A DataFrame containing the final covariates (from covariates.parquet) or None
  community_level (int): The community level to search at.
  response_type (str): The response type to return.
  query (str): The user query to search for.
  callbacks (list[QueryCallbacks] | None): Optional list of QueryCallbacks to customize streaming behavior.
  verbose (bool): Enable verbose logging when true.

Returns:
  AsyncGenerator[str, None]: An asynchronous generator yielding chunks of the streaming local search results as strings.

Edge cases:
  - If covariates is None, covariates are treated as an empty list for the search.

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/query/factory.py::get_local_search_engine`
- `graphrag/query/indexer_adapters.py::read_indexer_covariates`
- `graphrag/query/indexer_adapters.py::read_indexer_entities`
- `graphrag/query/indexer_adapters.py::read_indexer_relationships`
- `graphrag/query/indexer_adapters.py::read_indexer_reports`
- `graphrag/query/indexer_adapters.py::read_indexer_text_units`
- `graphrag/utils/api.py::get_embedding_store`
- `graphrag/utils/api.py::load_search_prompt`
- `graphrag/utils/cli.py::redact`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search`

