---
sidebar_position: 302
---

# _wrapped_with_retries

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_retries.py` (lines 46-47)

## Signature

```python
def _wrapped_with_retries(**kwargs: Any) -> Any
```

## Description

Wrap the synchronous request function with retries using the configured retry service.

Args:
    kwargs: Keyword arguments passed to the underlying synchronous request function. (type: Any)

Returns:
    Any: The value returned by the underlying synchronous request function when called with the provided kwargs.

Raises:
    Exception: Propagated from the underlying synchronous function or the retry service.

