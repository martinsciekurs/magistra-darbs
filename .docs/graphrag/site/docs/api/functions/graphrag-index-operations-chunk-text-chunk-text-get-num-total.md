---
sidebar_position: 71
---

# _get_num_total

**File:** `graphrag/index/operations/chunk_text/chunk_text.py` (lines 133-140)

## Signature

```python
def _get_num_total(output: pd.DataFrame, column: str) -> int
```

## Description

Compute the total number of elements in a DataFrame column, counting strings as a single element and non-string entries by their length.

Args:
output: pandas.DataFrame The DataFrame containing the target column.
column: str The name of the column to process.

Returns:
int The total number of elements in the specified column; strings contribute 1 each, non-string entries contribute their length.

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/chunk_text.py::chunk_text`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_get_num_total_default`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_get_num_total_array`

