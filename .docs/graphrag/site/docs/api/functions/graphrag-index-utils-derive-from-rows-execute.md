---
sidebar_position: 189
---

# execute

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 148-159)

## Signature

```python
def execute(row: tuple[Any, pd.Series]) -> ItemType | None
```

## Description

Apply the provided transform to the row data and await if necessary.

Args:
    row: tuple[Any, pd.Series] - A row, where row[1] is the pd.Series passed to the transform.

Returns:
    ItemType | None - The transformed value cast to ItemType, or None if an error occurred during transformation.

Raises:
    None

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::execute_row_protected`

