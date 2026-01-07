---
sidebar_position: 295
---

# _wrapped_with_logging

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_logging.py` (lines 36-43)

## Signature

```python
def _wrapped_with_logging(**kwargs: Any) -> Any
```

## Description

Wraps the synchronous request function with logging.

Args:
    kwargs: Keyword arguments passed to the underlying synchronous request function.

Returns:
    Any: The value returned by the underlying sync_fn when called with the provided kwargs.

Raises:
    Exception: Re-raised after logging the exception encountered during the call.

