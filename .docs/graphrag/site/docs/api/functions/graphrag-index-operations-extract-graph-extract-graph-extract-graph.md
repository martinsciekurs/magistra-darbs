---
sidebar_position: 113
---

# extract_graph

**File:** `graphrag/index/operations/extract_graph/extract_graph.py` (lines 27-82)

## Signature

```python
def extract_graph(
    text_units: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    text_column: str,
    id_column: str,
    strategy: dict[str, Any] | None,
    async_mode: AsyncType = AsyncType.AsyncIO,
    entity_types=DEFAULT_ENTITY_TYPES,
    num_threads: int = 4,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Extract a graph from a piece of text using a language model.

Args:
    text_units: The input DataFrame containing the text data to process.
    callbacks: WorkflowCallbacks used for progress reporting and event handling.
    cache: PipelineCache instance used for caching results.
    text_column: Name of the column in text_units that contains the text to analyze.
    id_column: Name of the column in text_units that contains a unique identifier for each row.
    strategy: Strategy configuration dictionary; may be None to use defaults.
    async_mode: AsyncType controlling how tasks are scheduled.
    entity_types: List of entity types to extract; if None, defaults to DEFAULT_ENTITY_TYPES.
    num_threads: Number of worker threads to use for processing.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A pair of DataFrames: the first contains aggregated entities and the second contains aggregated relationships.

Raises:
    ValueError: If an unknown strategy type is provided.

## Dependencies

This function calls:

- `graphrag/index/operations/extract_graph/extract_graph.py::_load_strategy`
- `graphrag/index/operations/extract_graph/extract_graph.py::_merge_entities`
- `graphrag/index/operations/extract_graph/extract_graph.py::_merge_relationships`
- `graphrag/index/utils/derive_from_rows.py::derive_from_rows`

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph.py::run_workflow`

