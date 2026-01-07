---
sidebar_position: 163
---

# get_summarized

**File:** `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py` (lines 39-93)

## Signature

```python
def get_summarized(
        nodes: pd.DataFrame, edges: pd.DataFrame, semaphore: asyncio.Semaphore
    )
```

## Description

Summarize descriptions for nodes and edges and return summary dataframes.

Args:
    nodes: pd.DataFrame
        DataFrame containing node information with at least a title and a description per node.
    edges: pd.DataFrame
        DataFrame containing edge information with at least source, target, and a description per edge.
    semaphore: asyncio.Semaphore
        Semaphore used to limit concurrent summarization operations.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]
        A tuple containing:
        - entity_descriptions: DataFrame with columns 'title' and 'description' summarizing each node.
        - relationship_descriptions: DataFrame with columns 'source', 'target', and 'description' summarizing each edge.

Raises:
    Exceptions propagated from the underlying asynchronous summarization processes and tasks.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::do_summarize_descriptions`
- `graphrag/logger/progress.py::progress_ticker`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::summarize_descriptions`

