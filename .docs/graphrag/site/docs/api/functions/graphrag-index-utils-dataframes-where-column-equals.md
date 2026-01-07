---
sidebar_position: 187
---

# where_column_equals

**File:** `graphrag/index/utils/dataframes.py` (lines 18-20)

## Signature

```python
def where_column_equals(df: pd.DataFrame, column: str, value: Any) -> pd.DataFrame
```

## Description

Return a filtered DataFrame where a column equals a value.

Args:
    df (pd.DataFrame): The DataFrame to filter.
    column (str): The column name to compare.
    value (Any): The value to compare against.

Returns:
    pd.DataFrame: A DataFrame containing only rows where df[column] == value.

Raises:
    KeyError: If the specified column is not in df.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_at_level`

