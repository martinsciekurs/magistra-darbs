---
sidebar_position: 298
---

# _wrapped_with_rate_limiter_async

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_rate_limiter.py` (lines 79-95)

## Signature

```python
def _wrapped_with_rate_limiter_async(
        **kwargs: Any,
    ) -> Any
```

## Description

Asynchronous wrapper that applies rate limiting to a request function.

Args:
    kwargs: Any
        Arbitrary keyword arguments forwarded to the wrapped asynchronous function.
        The wrapper computes the rate-limiting token count from max_tokens plus
        a token count derived from the provided 'messages' or 'input' in kwargs.

Returns:
    Any
        The result of the wrapped asynchronous function after acquiring the rate
        limiter.

Raises:
    Propagates exceptions raised by the rate limiter or by the wrapped asynchronous
    function.

## Example 💡 Generated

```python
from module import _wrapped_with_rate_limiter_async
import asyncio
async def main():
    messages = [{"role":"user","content":"Hello"}]
    result = await _wrapped_with_rate_limiter_async(
        messages=messages
    )
    print(result)
asyncio.run(main())
```

