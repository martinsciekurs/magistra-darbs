---
sidebar_position: 301
---

# _wrapped_with_retries_async

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_retries.py` (lines 49-52)

## Signature

```python
def _wrapped_with_retries_async(
        **kwargs: Any,
    ) -> Any
```

## Description

Wrap the asynchronous request function with retries using the configured retry service.

Args:
    kwargs: Keyword arguments passed to the underlying asynchronous request function.

Returns:
    Any: The value returned by the underlying asynchronous request function when called with the provided kwargs.

Raises:
    Exception: Propagated from the underlying asynchronous function or the retry service.

