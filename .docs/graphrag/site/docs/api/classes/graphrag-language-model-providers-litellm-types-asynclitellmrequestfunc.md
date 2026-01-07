---
sidebar_position: 145
---

# AsyncLitellmRequestFunc

**File:** `graphrag/language_model/providers/litellm/types.py`

## Overview

AsyncLitellmRequestFunc is a callable wrapper around an asynchronous Litellm request function used for chat completions or embeddings. It forwards all provided keyword arguments to the underlying request function, enabling flexible use with different backends.

Args:
    kwargs: Arbitrary keyword arguments forwarded to the underlying request function. Specific accepted keys depend on the concrete implementation.

Returns:
    The result produced by the underlying request function.

Raises:
    Exception: Exceptions raised by the underlying request function.

## Methods

### `__call__`

```python
def __call__(self, /, **kwargs: Any) -> Any
```

