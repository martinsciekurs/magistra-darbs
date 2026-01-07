---
sidebar_position: 151
---

# LitellmRequestFunc

**File:** `graphrag/language_model/providers/litellm/types.py`

## Overview

Synchronous request function for Litellm that forwards calls to the underlying request function, capable of handling either chat completion or embedding.

Args:
    kwargs: Arbitrary keyword arguments forwarded to the underlying request function. Specific accepted keys depend on the concrete implementation.

Returns:
    Any: The result of the underlying request function.

Raises:
    Exception: Exceptions raised by the underlying request function.

## Methods

### `__call__`

```python
def __call__(self, /, **kwargs: Any) -> Any
```

