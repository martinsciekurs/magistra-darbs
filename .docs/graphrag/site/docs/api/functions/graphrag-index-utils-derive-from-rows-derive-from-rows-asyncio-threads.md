---
sidebar_position: 193
---

# derive_from_rows_asyncio_threads

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 61-88)

## Signature

```python
def derive_from_rows_asyncio_threads(
    input: pd.DataFrame,
    transform: Callable[[pd.Series], Awaitable[ItemType]],
    callbacks: WorkflowCallbacks,
    num_threads: int | None = 4,
    progress_msg: str = "",
) -> list[ItemType | None]
```

## Description

Threaded (IO-bound) variant: derive results from DataFrame rows by dispatching per-row work to a thread pool via asyncio.to_thread. The transform is expected to be an asynchronous function that operates on the row's pandas Series and returns an ItemType (or None). Internally, rows are passed to the executor as a tuple (index, row); the transform should use only the Series, not the full tuple.

This function constrains concurrency with a semaphore using num_threads (default 4).

Args:
  input: pandas.DataFrame
      The input data to process, where each row will be transformed.
  transform: Callable[[pd.Series], Awaitable[ItemType]]
      Async function applied to the row's Series to produce an ItemType. The function should
      operate on the Series alone and not expect the full (index, Series) tuple.
  callbacks: WorkflowCallbacks
      Callbacks used to report progress and handle workflow lifecycle events.
  num_threads: int | None
      Maximum number of concurrent threads to use; if None, a default of 4 is used.
  progress_msg: str
      Optional message to display for progress tracking.

Returns:
  list[ItemType | None]
      A list containing the result for each input row. Each element is either the ItemType
      produced by transform or None if the row could not be transformed.

Raises:
  Propagates exceptions raised by the per-row transform or by callbacks. If multiple errors
  occur during parallel execution, a summary exception may be raised by the internal error
  aggregator.

Notes:
  This function is the threaded variant of derive_from_rows and relies on asyncio.to_thread to
  execute transforms in a thread pool while an asyncio event loop drives orchestration.

## Dependencies

This function calls:

- `graphrag/index/utils/derive_from_rows.py::_derive_from_rows_base`

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::derive_from_rows`

