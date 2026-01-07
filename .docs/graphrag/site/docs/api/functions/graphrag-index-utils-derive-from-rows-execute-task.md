---
sidebar_position: 188
---

# execute_task

**File:** `graphrag/index/utils/derive_from_rows.py` (lines 78-82)

## Signature

```python
def execute_task(task: Coroutine) -> ItemType | None
```

## Description

Execute a coroutine task under a concurrency-limiting semaphore and return the awaited result.

Args:
- task: Coroutine. The coroutine to be awaited to obtain a thread-like awaitable, which is then awaited to produce the final ItemType result.

Returns:
- ItemType | None: The result produced by awaiting the retrieved thread from the task. May be None if the thread yields no value.

Raises:
- Propagates any exception raised by awaiting the input task or the retrieved thread (no error handling is performed here).

## Called By

This function is called by:

- `graphrag/index/utils/derive_from_rows.py::gather`

