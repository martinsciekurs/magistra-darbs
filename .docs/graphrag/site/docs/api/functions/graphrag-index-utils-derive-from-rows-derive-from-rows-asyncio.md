---
sidebar_position: 194
---

# derive_from_rows_asyncio

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 94-122)

## Signature

```python
def derive_from_rows_asyncio(
    input: pd.DataFrame,
    transform: Callable[[pd.Series], Awaitable[ItemType]],
    callbacks: WorkflowCallbacks,
    num_threads: int = 4,
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
    num_threads: int
        Number of concurrent workers to use. This limits the degree of parallelism; default is 4.
    progress_msg: str
        Description shown in the progress ticker during processing.

Returns:
    list[ItemType | None]
        A list of results corresponding to each input row; each element is either an ItemType or None if a row could not be processed.

## Dependencies

This function calls:

- `graphrag/index/utils/derive_from_rows.py::_derive_from_rows_base`

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::derive_from_rows`

