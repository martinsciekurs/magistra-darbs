---
sidebar_position: 11
---

# drift_search_streaming

**File:** `graphrag/api/query.py` (lines 773-841)

## Signature

```python
def drift_search_streaming(
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
) -> AsyncGenerator
```

## Description

Perform a DRIFT streaming search and yield streaming response chunks.

Args:
    config (GraphRagConfig): A graphrag configuration (from settings.yaml).
    entities (pd.DataFrame): A DataFrame containing the final entities (from entities.parquet).
    communities (pd.DataFrame): A DataFrame containing the final communities (from communities.parquet).
    community_reports (pd.DataFrame): A DataFrame containing the final community reports (from community_reports.parquet).
    text_units (pd.DataFrame): A DataFrame containing the final text units (from text_units.parquet).
    relationships (pd.DataFrame): A DataFrame containing the final relationships (from relationships.parquet).
    community_level (int): The community level to search at.
    response_type (str): The response type to shape the drift search output.
    query (str): The user query to search for.
    callbacks (list[QueryCallbacks] | None): Optional list of callbacks to customize the streaming search behavior. If None, a default empty list is used.
    verbose (bool): Enable verbose logging of the streaming search process.

Returns:
    AsyncGenerator[str, None]: An asynchronous generator yielding string chunks that together form the streaming search response. Callers should consume chunks as they arrive and concatenate them to reconstruct the full response.

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/query/factory.py::get_drift_search_engine`
- `graphrag/query/indexer_adapters.py::read_indexer_entities`
- `graphrag/query/indexer_adapters.py::read_indexer_relationships`
- `graphrag/query/indexer_adapters.py::read_indexer_report_embeddings`
- `graphrag/query/indexer_adapters.py::read_indexer_reports`
- `graphrag/query/indexer_adapters.py::read_indexer_text_units`
- `graphrag/utils/api.py::get_embedding_store`
- `graphrag/utils/api.py::load_search_prompt`
- `graphrag/utils/cli.py::redact`

## Called By

This function is called by:

- `graphrag/api/query.py::drift_search`

