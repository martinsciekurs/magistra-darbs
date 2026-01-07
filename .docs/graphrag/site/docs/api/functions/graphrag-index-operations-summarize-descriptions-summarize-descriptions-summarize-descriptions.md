---
sidebar_position: 164
---

# summarize_descriptions

**File:** `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py` (lines 23-108)

## Signature

```python
def summarize_descriptions(
    entities_df: pd.DataFrame,
    relationships_df: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    strategy: dict[str, Any] | None = None,
    num_threads: int = 4,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Summarize entity and relationship descriptions from an entity graph, using a language model.

Args:
    entities_df: DataFrame containing entity nodes with at least a title and a description per node.
    relationships_df: DataFrame containing edge information with at least source, target, and a description per edge.
    callbacks: WorkflowCallbacks providing progress reporting hooks for long-running operations.
    cache: PipelineCache used to cache results from strategy execution.
    strategy: dict[str, Any] | None: Strategy configuration for the summarization strategy. If None, defaults are applied.
    num_threads: int: Number of concurrent workers to use for summarization.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A tuple containing the entity descriptions DataFrame and the relationship descriptions DataFrame.

Raises:
    ValueError: If an unknown strategy type is provided.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::get_summarized`
- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::load_strategy`

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph.py::get_summarized_entities_relationships`

