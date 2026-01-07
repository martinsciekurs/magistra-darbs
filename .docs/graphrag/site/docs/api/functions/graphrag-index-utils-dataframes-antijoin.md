---
sidebar_position: 186
---

# antijoin

**File:** `graphrag/index/utils/dataframes.py` (lines 23-31)

## Signature

```python
def antijoin(df: pd.DataFrame, exclude: pd.DataFrame, column: str) -> pd.DataFrame
```

## Description

Return an anti-joined dataframe.

Args:
    df (pd.DataFrame): The DataFrame to apply the exclusion to.
    exclude (pd.DataFrame): The DataFrame containing rows to remove.
    column (str): The join-on column.

Returns:
    pd.DataFrame: The rows from df whose value in column is not present in exclude[column].

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_antijoin_reports`

