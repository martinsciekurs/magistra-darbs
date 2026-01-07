---
sidebar_position: 140
---

# _prepare_reports_at_level

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 63-188)

## Signature

```python
def _prepare_reports_at_level(
    node_df: pd.DataFrame,
    edge_df: pd.DataFrame,
    claim_df: pd.DataFrame | None,
    tokenizer: Tokenizer,
    level: int,
    max_context_tokens: int = 16_000,
) -> pd.DataFrame
```

## Description

Prepare reports at a given level.

Args:
    node_df: pd.DataFrame
        DataFrame containing node details; filtered to the specified level using schemas.COMMUNITY_LEVEL.
    edge_df: pd.DataFrame
        DataFrame containing edge details between nodes.
    claim_df: pd.DataFrame | None
        Optional DataFrame containing claims related to nodes; may be None.
    tokenizer: Tokenizer
        Tokenizer used to compute context token counts for context generation.
    level: int
        Target community level for which to prepare reports.
    max_context_tokens: int
        Maximum number of tokens allowed for the generated context strings (default 16_000).

Returns:
    pd.DataFrame
        DataFrame containing prepared reports at the given level, with node and edge details
        aggregated, optional claim details merged, ALL_CONTEXT populated, and context strings
        generated for each community by parallel_sort_context_batch.

Raises:
    Exception
        If an error occurs during processing (for example, due to missing expected columns or invalid data).

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::parallel_sort_context_batch`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_local_context`

