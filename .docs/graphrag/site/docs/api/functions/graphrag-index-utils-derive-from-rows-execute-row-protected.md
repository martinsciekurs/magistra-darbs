---
sidebar_position: 190
---

# execute_row_protected

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 109-113)

## Signature

```python
def execute_row_protected(
            row: tuple[Hashable, pd.Series],
        ) -> ItemType | None
```

## Description

Execute the provided row transformation in a protected asynchronous context using a shared semaphore.

This wrapper acquires the shared semaphore before invoking the underlying transform (execute) on the given row and returns its result. It does not perform any casting; the return value is whatever execute(row) returns (which may be None).

Args:
    row (tuple[Hashable, pd.Series]): A row, where row[1] is the pd.Series passed to the transform.

Returns:
    ItemType | None: The result of execute(row); may be None if the underlying transform returns None.

Raises:
    Propagates any exception raised by execute(row); exceptions may bubble up to upstream callers.

## Dependencies

This function calls:

- `graphrag/index/utils/derive_from_rows.py::execute`

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::gather`

