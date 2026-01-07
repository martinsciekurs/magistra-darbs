---
sidebar_position: 219
---

# chunker_with_logging

**File:** `graphrag/index/workflows/create_base_text_units.py` (lines 134-138)

## Signature

```python
def chunker_with_logging(row: pd.Series, row_index: int) -> Any
```

## Description

Log chunker progress for a row during chunking.

Executes the chunker on the given row and logs progress using total_rows from the surrounding scope.

Args:
    row (pd.Series): The input row to be chunked.
    row_index (int): The index of the row being processed (0-based).

Returns:
    Any: The result of the chunker applied to the row.

Raises:
    Exception: Propagates any exception raised by chunker(row).

## Dependencies

This function calls:

- `graphrag/index/workflows/create_base_text_units.py::chunker`

## Called By

This function is called by:

- `graphrag/index/workflows/create_base_text_units.py::create_base_text_units`

