---
sidebar_position: 242
---

# get_summarized_entities_relationships

**File:** `graphrag/index/workflows/extract_graph.py` (lines 135-159)

## Signature

```python
def get_summarized_entities_relationships(
    extracted_entities: pd.DataFrame,
    extracted_relationships: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    summarization_strategy: dict[str, Any] | None = None,
    summarization_num_threads: int = 4,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Summarize the entities and relationships using the provided summarization strategy.

Args:
    extracted_entities: DataFrame containing extracted entity nodes to be summarized.
    extracted_relationships: DataFrame containing extracted relationships to be summarized.
    callbacks: WorkflowCallbacks providing progress reporting hooks for long-running operations.
    cache: PipelineCache used to cache results from the summarization strategy.
    summarization_strategy: dictionary configuring the summarization approach; may be None to use defaults.
    summarization_num_threads: number of threads to use for summarization.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A tuple containing:
        - entities: DataFrame with entity summaries merged on "title" (after dropping the original "description" column).
        - relationships: DataFrame with relationship summaries merged on ["source", "target"] (after dropping the original "description" column).

Raises:
    Exception: If summarization or subsequent DataFrame operations fail, propagating exceptions from summarize_descriptions or pandas."&#125;

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::summarize_descriptions`

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph.py::extract_graph`
- `graphrag/index/workflows/update_entities_relationships.py::_update_entities_and_relationships`

