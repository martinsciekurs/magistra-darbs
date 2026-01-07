---
sidebar_position: 103
---

# ModelEventHandler

**File:** `graphrag/language_model/events/base.py`

## Overview

ModelEventHandler Protocol for handling model-related events, with a focus on error handling within the language model system.

Purpose:
Define the contract that concrete event handlers must follow to process and respond to errors raised by model operations.

Key attributes:
- on_error: The error-handling contract that implementations must provide.

on_error signature:
def on_error(self, error: BaseException | None, traceback: str | None = None, arguments: dict[str, Any] | None = None) -&gt; None

Notes:
- The Args described below correspond to the on_error method parameters; there are no separate class-level parameters.
- All parameters are optional to allow graceful handling when error information is incomplete.

Args:
- error: The error that occurred, or None if no error is provided.
- traceback: The traceback string associated with the error, or None if not available.
- arguments: Additional contextual arguments related to the error, or None.

Returns:
- None: The function does not return a value.

Raises:
- None

## Methods

### `on_error`

```python
def on_error(
        self,
        error: BaseException | None,
        traceback: str | None = None,
        arguments: dict[str, Any] | None = None,
    ) -> None
```

