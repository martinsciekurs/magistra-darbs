---
sidebar_position: 115
---

# FNLLMEvents

**File:** `graphrag/language_model/providers/fnllm/events.py`

## Overview

FNLLMEvents handles FNLLM-specific events and delegates error processing to a provided error handler.

Args:
    on_error: ErrorHandlerFn to be invoked on errors.

Returns:
    None

Raises:
    Exception: If the configured error handler raises an exception.

## Methods

### `__init__`

```python
def __init__(self, on_error: ErrorHandlerFn)
```

### `on_error`

```python
def on_error(
        self,
        error: BaseException | None,
        traceback: str | None = None,
        arguments: dict[str, Any] | None = None,
    ) -> None
```

