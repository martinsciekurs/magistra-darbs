---
sidebar_position: 303
---

# with_retries

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_retries.py` (lines 20-54)

## Signature

```python
def with_retries(
    *,
    sync_fn: LitellmRequestFunc,
    async_fn: AsyncLitellmRequestFunc,
    model_config: "LanguageModelConfig",
) -> tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]
```

## Description

Wrap the synchronous and asynchronous request functions with retries.

This function constructs a retry service from model_config and returns two wrappers:
- a synchronous wrapper that uses retry to invoke the provided sync_fn
- an asynchronous wrapper that uses aretry to invoke the provided async_fn

Retry configuration is driven by model_config fields: retry_strategy, max_retries, and max_retry_wait.

Notes:
- The asynchronous wrapper uses aretry on the async_fn, while the synchronous wrapper uses retry on the sync_fn.

Args:
    sync_fn (LitellmRequestFunc): The synchronous chat/embedding request function to wrap.
    async_fn (AsyncLitellmRequestFunc): The asynchronous chat/embedding request function to wrap.
    model_config (LanguageModelConfig): Configuration for the language model, including retry parameters (retry_strategy, max_retries, max_retry_wait).

Returns:
    tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]: A tuple containing the wrapped synchronous and
        asynchronous chat/embedding request functions.

Raises:
    Propagates exceptions from the retry mechanism or the wrapped functions when retries are exhausted or an unrecoverable error occurs.

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/services/retry/retry_factory.py::RetryFactory`

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/chat_model.py::_create_completions`
- `graphrag/language_model/providers/litellm/embedding_model.py::_create_embeddings`

