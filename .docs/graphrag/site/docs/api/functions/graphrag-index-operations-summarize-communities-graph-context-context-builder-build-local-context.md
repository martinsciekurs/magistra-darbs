---
sidebar_position: 142
---

# build_local_context

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 38-60)

## Signature

```python
def build_local_context(
    nodes,
    edges,
    claims,
    tokenizer: Tokenizer,
    callbacks: WorkflowCallbacks,
    max_context_tokens: int = 16_000,
)
```

## Description

Prepare initial local context for all communities, processing level-by-level.

This function computes per-level local context data and concatenates the results. It determines the processing levels with get_levels, iterates through them with progress_iterable using callbacks.progress, and for each level builds a per-level DataFrame by calling _prepare_reports_at_level with the provided inputs and the max_context_tokens budget. The resulting per-level DataFrame has its COMMUNITY_LEVEL column set to the corresponding level, and all per-level DataFrames are concatenated into a single DataFrame that represents the initial local context for all communities.

Args:
  nodes: DataFrame containing community node details, including a COMMUNITY_LEVEL column.
  edges: DataFrame containing edge details between nodes.
  claims: DataFrame or None containing claims related to communities.
  tokenizer: Tokenizer used to compute context token counts during per-level processing.
  callbacks: WorkflowCallbacks used for progress reporting.
  max_context_tokens: int, maximum number of tokens allocated for per-level processing; defaults to 16,000.

Returns:
  pd.DataFrame: A concatenated DataFrame with prepared local context for all levels; each row includes COMMUNITY_LEVEL indicating its level.

Raises:
  None.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_prepare_reports_at_level`
- `graphrag/index/operations/summarize_communities/utils.py::get_levels`
- `graphrag/logger/progress.py::progress_iterable`

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`

