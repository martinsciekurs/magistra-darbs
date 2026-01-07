---
sidebar_position: 296
---

# _wrapped_with_logging_async

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_logging.py` (lines 45-54)

## Signature

```python
def _wrapped_with_logging_async(
        **kwargs: Any,
    ) -> Any
```

## Description

Wraps the asynchronous request function with logging.

Args:
    kwargs: Keyword arguments passed to the underlying asynchronous request function.

Returns:
    Any: The value returned by the underlying async_fn when called with the provided kwargs.

Raises:
    Exception: Re-raised after logging the exception encountered during the call.

