---
sidebar_position: 307
---

# progress_iterable

**File:** `graphrag/logger/progress.py` (lines 81-95)

## Signature

```python
def progress_iterable(
    iterable: Iterable[T],
    progress: ProgressHandler | None,
    num_total: int | None = None,
    description: str = "",
) -> Iterable[T]
```

## Description

Wrap an iterable with a progress reporter. After each item is yielded, the progress callback will be called with a Progress object describing the total number of items and how many have been completed so far. If the callback is None, no updates will be emitted.

The Progress object provides:
- total_items: total number of items (as given by num_total)
- completed_items: number of items yielded so far
- description: optional description included with updates

Note: If num_total is None, the total will be inferred by consuming the iterable (via list(iterable)), which may exhaust inputs that cannot be re-iterated. To avoid this, pass a known num_total or ensure the iterable can be iterated multiple times.

Args:
    iterable (Iterable[T]): The input iterable to wrap. Each item yielded is unchanged.
    progress (ProgressHandler | None): Callback invoked with a Progress instance after each item is yielded. If None, updates are suppressed.
    num_total (int | None): Total number of items. If None, inferred by consuming the iterable (may exhaust it).
    description (str): Optional description to attach to progress updates.

Returns:
    Iterable[T]: A generator that yields the same items as the input iterable, while updating progress after each item is yielded.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_local_context`

