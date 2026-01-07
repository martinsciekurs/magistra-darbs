---
sidebar_position: 146
---

# parallel_sort_context_batch

**File:** `graphrag/index/operations/summarize_communities/graph_context/sort_context.py` (lines 129-164)

## Signature

```python
def parallel_sort_context_batch(
    community_df, tokenizer: Tokenizer, max_context_tokens, parallel=False
)
```

## Description

Calculate context strings for each community entry, optionally using parallel execution, and populate related context columns.

Args:
  community_df: DataFrame containing community data to be enriched with context strings.
  tokenizer: Tokenizer used to count tokens for context strings.
  max_context_tokens: Maximum number of tokens allowed for a context string.
  parallel: Whether to enable parallel computation of context strings using ThreadPoolExecutor.

Returns:
  The input DataFrame with additional context-related columns populated:
  - CONTEXT_STRING: the computed context string for each row.
  - CONTEXT_SIZE: token length of CONTEXT_STRING.
  - CONTEXT_EXCEED_FLAG: whether CONTEXT_SIZE exceeds max_context_tokens.

Raises:
  Exceptions raised by sort_context or by the parallel execution machinery if parallel is enabled.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::sort_context`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_prepare_reports_at_level`

