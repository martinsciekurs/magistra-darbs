---
sidebar_position: 288
---

# _create_embeddings

**File:** `graphrag/language_model/providers/litellm/embedding_model.py` (lines 100-172)

## Signature

```python
def _create_embeddings(
    model_config: "LanguageModelConfig",
    cache: "PipelineCache | None",
    cache_key_prefix: str,
) -> tuple[FixedModelEmbedding, AFixedModelEmbedding]
```

## Description

Wrap the base litellm embedding function with the model configuration and additional features.

Wrap the base litellm embedding function with instance variables based on the model configuration. Then wrap additional features such as rate limiting, retries, and caching, if enabled.

Final function composition order:
- Logging(Cache(Retries(RateLimiter(ModelEmbedding()))))

Args:
  model_config: LanguageModelConfig. The configuration for the language model.
  cache: PipelineCache | None. Optional cache for storing responses.
  cache_key_prefix: str. Prefix for cache keys.

Returns:
  tuple[FixedModelEmbedding, AFixedModelEmbedding]. A tuple containing the synchronous and asynchronous embedding functions.

Raises:
  ValueError: Azure Managed Identity authentication is only supported for Azure models.

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/embedding_model.py::_create_base_embeddings`
- `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py::with_cache`
- `graphrag/language_model/providers/litellm/request_wrappers/with_logging.py::with_logging`
- `graphrag/language_model/providers/litellm/request_wrappers/with_rate_limiter.py::with_rate_limiter`
- `graphrag/language_model/providers/litellm/request_wrappers/with_retries.py::with_retries`

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/embedding_model.py::LitellmEmbeddingModel.__init__`

