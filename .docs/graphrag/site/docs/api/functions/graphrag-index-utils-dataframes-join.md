---
sidebar_position: 184
---

# join

**File:** `graphrag/index/utils/dataframes.py` (lines 39-43)

## Signature

```python
def join(
    left: pd.DataFrame, right: pd.DataFrame, key: str, strategy: MergeHow = "left"
) -> pd.DataFrame
```

## Description

Perform a table join.

Args:
    left: The left DataFrame.
    right: The right DataFrame.
    key: The column name to join on.
    strategy: The merge strategy to use (how parameter for pandas merge). Defaults to left.

Returns:
    pd.DataFrame: The joined DataFrame resulting from left.merge(right, on=key, how=strategy).

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_subcontext_df`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_community_df`

