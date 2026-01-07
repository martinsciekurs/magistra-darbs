---
sidebar_position: 9
---

# basic_search_streaming

**File:** `graphrag/api/query.py` (lines 1106-1148)

## Signature

```python
def basic_search_streaming(
    config: GraphRagConfig,
    text_units: pd.DataFrame,
    query: str,
    callbacks: list[QueryCallbacks] | None = None,
    verbose: bool = False,
) -> AsyncGenerator
```

## Description

Stream results from a local search as an asynchronous generator.

Args:
    config (GraphRagConfig): A graphrag configuration (from settings.yaml)
    text_units (pd.DataFrame): A DataFrame containing the final text units (from text_units.parquet)
    query (str): The user query to search for.
    callbacks (list[QueryCallbacks] | None): Optional list of QueryCallbacks to customize streaming behavior.
    verbose (bool): If True, enable verbose logging.

Returns:
    AsyncGenerator: An asynchronous generator yielding chunks of the search response as strings.

Raises:
    Exception: Propagates exceptions raised by underlying components (e.g., during embedding retrieval, prompt loading, or streaming).

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/query/factory.py::get_basic_search_engine`
- `graphrag/query/indexer_adapters.py::read_indexer_text_units`
- `graphrag/utils/api.py::get_embedding_store`
- `graphrag/utils/api.py::load_search_prompt`
- `graphrag/utils/cli.py::redact`

## Called By

This function is called by:

- `graphrag/api/query.py::basic_search`

