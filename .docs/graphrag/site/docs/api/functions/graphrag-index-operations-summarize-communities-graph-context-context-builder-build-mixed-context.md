---
sidebar_position: 139
---

# _build_mixed_context

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 292-302)

## Signature

```python
def _build_mixed_context(
    df: pd.DataFrame, tokenizer: Tokenizer, max_context_tokens: int
) -> pd.Series
```

## Description

Build mixed context for each row by applying build_mixed_context to the ALL_CONTEXT data and trimming to the token limit.

Args:
    df: DataFrame containing ALL_CONTEXT column to be processed.
    tokenizer: Tokenizer used to count tokens during trimming.
    max_context_tokens: int Maximum number of tokens allowed for the resulting context.

Returns:
    pd.Series: A Series of processed mixed contexts per row.

Raises:
    Exception: Any exception raised by the transformation function will be propagated to the caller.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/build_mixed_context.py::build_mixed_context`
- `graphrag/index/utils/dataframes.py::transform_series`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_community_df`

