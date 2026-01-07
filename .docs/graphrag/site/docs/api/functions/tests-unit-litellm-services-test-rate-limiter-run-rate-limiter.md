---
sidebar_position: 541
---

# _run_rate_limiter

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 236-248)

## Signature

```python
def _run_rate_limiter(
    rate_limiter: RateLimiter,
    # Acquire cost
    input_queue: Queue[int | None],
    # time value
    output_queue: Queue[float | None],
)
```

## Description

Run the RateLimiter and record timestamps for each acquired token count.

Continuously reads token_count from input_queue; when a token_count is None, the function exits. For each non-None token_count, it enters the rate limiter with acquire(token_count=token_count) and, after a successful acquisition, pushes the current time (time.time()) to output_queue.

Args:
    rate_limiter: The RateLimiter instance used to enforce rate limits.
    input_queue: Queue[int | None]. Each non-None value represents the number of tokens to acquire; None signals termination.
    output_queue: Queue[float | None]. Timestamps (time.time()) are put here after acquisition; may contain None values.

Returns:
    None: This function does not return a value.

Raises:
    Exceptions propagated from the underlying RateLimiter or queue operations.

