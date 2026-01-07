---
sidebar_position: 235
---

# _join

**File:** `graphrag/index/workflows/create_final_text_units.py` (lines 121-127)

## Signature

```python
def _join(left, right)
```

## Description

Join two DataFrames on the id column using a left merge.

Args:
    left: pd.DataFrame
        Left DataFrame to join on id.
    right: pd.DataFrame
        Right DataFrame to join on id.

Returns:
    pd.DataFrame
        The result of merging left and right on 'id' with a left join, applying suffixes '_1' and '_2' to overlapping columns.

Raises:
    Exception: Propagates exceptions raised by pandas DataFrame.merge during the join operation.

## Called By

This function is called by:

- `graphrag/index/workflows/create_final_text_units.py::create_final_text_units`

