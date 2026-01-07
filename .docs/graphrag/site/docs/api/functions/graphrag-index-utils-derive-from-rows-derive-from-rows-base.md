---
sidebar_position: 192
---

# _derive_from_rows_base

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 131-173)

## Signature

```python
def _derive_from_rows_base(
    input: pd.DataFrame,
    transform: Callable[[pd.Series], Awaitable[ItemType]],
    callbacks: WorkflowCallbacks,
    gather: GatherFn[ItemType],
    progress_msg: str = "",
) -> list[ItemType | None]
```

## Description

Derive from rows asynchronously.

This is useful for IO bound operations.

Args:
    input: pd.DataFrame
        The input data to process, where each row will be transformed.
    transform: Callable[[pd.Series], Awaitable[ItemType]]
        Async function applied to a row's Series to produce an ItemType.
    callbacks: WorkflowCallbacks
        Callbacks used to report progress and handle workflow events.
    gather: GatherFn[ItemType]
        Function that gathers results by applying the given execute function to each row.
    progress_msg: str
        Optional description to accompany progress updates.

Returns:
    list[ItemType | None]
        A list of results corresponding to each input row; elements may be ItemType or None if an error occurred for that row.

Raises:
    ParallelizationError
        If any errors were encountered during processing.

## Dependencies

This function calls:

- `graphrag/index/utils/derive_from_rows.py::gather`
- `graphrag/logger/progress.py::progress_ticker`

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::derive_from_rows_asyncio_threads`
- `graphrag/index/utils/derive_from_rows.py::derive_from_rows_asyncio`

