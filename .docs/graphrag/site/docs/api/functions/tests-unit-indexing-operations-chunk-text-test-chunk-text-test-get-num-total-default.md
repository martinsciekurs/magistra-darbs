---
sidebar_position: 513
---

# test_get_num_total_default

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 23-27)

## Signature

```python
def test_get_num_total_default()
```

## Description

Compute the total number of elements in a DataFrame column.

Args:
    output: pandas.DataFrame The DataFrame containing the target column.
    column: str The name of the column to process.

Returns:
    int The total number of elements in the specified column; strings contribute 1 each, non-string entries contribute their length.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::_get_num_total`

