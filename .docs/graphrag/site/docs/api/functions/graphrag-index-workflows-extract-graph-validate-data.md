---
sidebar_position: 241
---

# _validate_data

**File:** `graphrag/index/workflows/extract_graph.py` (lines 162-164)

## Signature

```python
def _validate_data(df: pd.DataFrame) -> bool
```

## Description

Validate that the dataframe has data.

Args:
    df (pd.DataFrame): DataFrame to validate.

Returns:
    bool: True if the DataFrame contains at least one row, False otherwise.

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph.py::extract_graph`

