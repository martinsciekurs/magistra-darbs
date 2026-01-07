---
sidebar_position: 284
---

# _create_completions

**File:** `graphrag/language_model/providers/litellm/chat_model.py` (lines 114-186)

## Signature

```python
def _create_completions(
    model_config: "LanguageModelConfig",
    cache: "PipelineCache | None",
    cache_key_prefix: str,
) -> tuple[FixedModelCompletion, AFixedModelCompletion]
```

## Description

Wrap the base litellm completion function with the model configuration and additional features.

Wrap the base litellm completion function with instance variables based on the model configuration.
Then wrap additional features such as rate limiting, retries, and caching, if enabled.

Final function composition order:
- Logging(Cache(Retries(RateLimiter(ModelCompletion()))))

Args:
    model_config: The configuration for the language model.
    cache: Optional cache for storing responses.
    cache_key_prefix: Prefix for cache keys.

Returns:
    A tuple containing the synchronous and asynchronous completion functions.

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/chat_model.py::_create_base_completions`
- `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py::with_cache`
- `graphrag/language_model/providers/litellm/request_wrappers/with_logging.py::with_logging`
- `graphrag/language_model/providers/litellm/request_wrappers/with_rate_limiter.py::with_rate_limiter`
- `graphrag/language_model/providers/litellm/request_wrappers/with_retries.py::with_retries`

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/chat_model.py::LitellmChatModel.__init__`

