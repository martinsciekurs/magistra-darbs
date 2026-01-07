---
sidebar_position: 92
---

# ProgressTicker

**File:** `graphrag/logger/progress.py`

## Overview

ProgressTicker tracks progress toward a known total and optionally notifies a callback with progress updates.

This class maintains an internal counter of completed items out of a known total and, on demand, emits progress events to an optional callback. A progress event is represented as an object with at least total_items and completed_items fields, and may also include the description provided at construction.

Args:
- callback: ProgressHandler | None - A function to handle progress reports, or None to disable updates. Default: None. The callback receives a progress-like object describing current progress.
- num_total: int - Total number of items to track.
- description: str - Optional description for the progress updates. Default: "".

Returns:
- None

Raises:
- None

Attributes:
- _callback: ProgressHandler | None - The function to call with progress updates, or None to suppress updates.
- _num_total: int - Total number of items to track.
- _description: str - Optional description for display.
- _completed_items: int - Count of completed ticks.

Behavior:
- __call__(self, num_ticks: int = 1) - Advances the internal counter by num_ticks. If a callback is set, invokes it with a progress-like object containing total_items (equal to _num_total) and completed_items (updated value).
- done(self) - Marks the progress as done. If a callback is provided, invokes it with a progress-like object whose total_items and completed_items both equal _num_total, preserving the description from initialization.

Example:
A minimal usage example:
Define a callback function that prints the progress, create a ProgressTicker with a total, and advance it by calling the instance. Call done() to report completion.

## Methods

### `__call__`

```python
def __call__(self, num_ticks: int = 1) -> None
```

### `__init__`

```python
def __init__(
        self, callback: ProgressHandler | None, num_total: int, description: str = ""
    )
```

### `done`

```python
def done(self) -> None
```

