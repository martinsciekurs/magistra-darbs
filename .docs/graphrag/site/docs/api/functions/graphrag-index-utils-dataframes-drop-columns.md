---
sidebar_position: 183
---

# drop_columns

**File:** `graphrag/index/utils/dataframes.py` (lines 13-15)

## Signature

```python
def drop_columns(df: pd.DataFrame, *column: str) -> pd.DataFrame
```

## Description

Drop specified columns from a DataFrame.

Args:
    df (pd.DataFrame): The DataFrame from which to drop columns.
    column (str): One or more column names to drop from the DataFrame.

Returns:
    pd.DataFrame: The DataFrame with the specified columns dropped.

Raises:
    KeyError: If any of the specified column names do not exist in df.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_drop_community_level`

