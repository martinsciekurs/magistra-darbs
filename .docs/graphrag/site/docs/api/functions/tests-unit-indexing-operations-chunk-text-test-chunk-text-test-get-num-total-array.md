---
sidebar_position: 514
---

# test_get_num_total_array

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 30-34)

## Signature

```python
def test_get_num_total_array()
```

## Description

Compute the total number of elements in a DataFrame column, counting strings as a single element and non-string entries by their length.

Args:
    output (pd.DataFrame): The DataFrame containing the target column.
    column (str): The name of the column to process.

Returns:
    int: The total number of elements in the specified column; strings contribute 1 each, non-string entries contribute their length.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::_get_num_total`

