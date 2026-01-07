---
sidebar_position: 182
---

# select

**File:** `graphrag/index/utils/dataframes.py` (lines 51-53)

## Signature

```python
def select(df: pd.DataFrame, *columns: str) -> pd.DataFrame
```

## Description

Select columns from a DataFrame.

Args:
    df: The DataFrame to select columns from.
    columns: The names of the columns to select from df.

Returns:
    pd.DataFrame: A DataFrame containing only the specified columns, in the order provided.

Raises:
    KeyError: If any of the provided column names do not exist in df.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_community_df`

