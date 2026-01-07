---
sidebar_position: 191
---

# gather

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 108-118)

## Signature

```python
def gather(execute: ExecuteFn[ItemType]) -> list[ItemType | None]
```

## Description

Gather results by applying the given execute function to each row of the input DataFrame and returning the results as a list.

Args:
    execute: ExecuteFn[ItemType] - A function that accepts a tuple[Hashable, pd.Series] representing a DataFrame row and returns an ItemType or None. This may be an awaitable.

Returns:
    list[ItemType | None]: A list of results corresponding to each input row. Each element is either an ItemType or None.

Raises:
    Exception: If the underlying execute raises an exception, it will propagate to the caller.

## Dependencies

This function calls:

- `graphrag/index/utils/derive_from_rows.py::execute_row_protected`

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::_derive_from_rows_base`

