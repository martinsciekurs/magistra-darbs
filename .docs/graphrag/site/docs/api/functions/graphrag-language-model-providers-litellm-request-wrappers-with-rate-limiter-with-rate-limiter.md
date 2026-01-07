---
sidebar_position: 299
---

# with_rate_limiter

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_rate_limiter.py` (lines 22-97)

## Signature

```python
def with_rate_limiter(
    *,
    sync_fn: LitellmRequestFunc,
    async_fn: AsyncLitellmRequestFunc,
    model_config: "LanguageModelConfig",
    rpm: int | None = None,
    tpm: int | None = None,
) -> tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]
```

## Description

Wrap the synchronous and asynchronous Litellm request functions with rate limiting.

Args
----
sync_fn: The synchronous chat/embedding request function to wrap.
async_fn: The asynchronous chat/embedding request function to wrap.
model_config: LanguageModelConfig containing rate_limit_strategy and related model parameters.
rpm: Optional rate limit in requests per minute. If None or 0, the RPM limit is disabled.
tpm: Optional rate limit in tokens per minute. If None or 0, the TPM limit is disabled.

Returns
-------
tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]
    The wrapped synchronous and asynchronous request functions.

Raises
------
ValueError
    If the rate limiter strategy in model_config is None or not registered with the RateLimiterFactory.

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/services/rate_limiter/rate_limiter_factory.py::RateLimiterFactory`

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/chat_model.py::_create_completions`
- `graphrag/language_model/providers/litellm/embedding_model.py::_create_embeddings`

