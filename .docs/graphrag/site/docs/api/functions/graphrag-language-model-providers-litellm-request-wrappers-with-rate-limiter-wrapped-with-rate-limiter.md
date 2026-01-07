---
sidebar_position: 300
---

# _wrapped_with_rate_limiter

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_rate_limiter.py` (lines 63-77)

## Signature

```python
def _wrapped_with_rate_limiter(**kwargs: Any) -> Any
```

## Description

Wrapped synchronous request function with rate limiting.

Args:
    kwargs: Any
        Arbitrary keyword arguments forwarded to the wrapped synchronous function.
        The wrapper computes the rate-limiting token count from max_tokens plus
        a token count derived from the provided 'messages' or 'input' in kwargs.

Returns:
    Any
        The result of the wrapped synchronous request function.

Raises:
    Exception
        Propagates exceptions raised by the rate limiter or by the wrapped function.

