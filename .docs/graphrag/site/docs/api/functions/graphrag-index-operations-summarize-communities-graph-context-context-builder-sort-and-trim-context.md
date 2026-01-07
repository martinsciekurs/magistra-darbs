---
sidebar_position: 137
---

# _sort_and_trim_context

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 279-289)

## Signature

```python
def _sort_and_trim_context(
    df: pd.DataFrame, tokenizer: Tokenizer, max_context_tokens: int
) -> pd.Series
```

## Description

Sort and trim the context to fit the token limit.

Args:
    df: DataFrame containing the contexts, with a column named by schemas.ALL_CONTEXT that holds the per-row context data to be processed.
    tokenizer: Tokenizer. Tokenizer used to count tokens when trimming.
    max_context_tokens: int. Maximum number of tokens allowed for each context after trimming.

Returns:
    pd.Series. A Series containing the processed contexts after sorting and trimming per entry.

Raises:
    Exception: Propagates any exception raised by the transformation (e.g., via transform_series or sort_context) when processing the contexts.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::sort_context`
- `graphrag/index/utils/dataframes.py::transform_series`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_level_context`

