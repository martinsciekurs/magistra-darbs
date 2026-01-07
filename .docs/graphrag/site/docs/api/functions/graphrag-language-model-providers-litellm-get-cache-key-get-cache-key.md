---
sidebar_position: 291
---

# get_cache_key

**File:** `graphrag/language_model/providers/litellm/get_cache_key.py` (lines 33-78)

## Signature

```python
def get_cache_key(
    model_config: "LanguageModelConfig",
    prefix: str,
    messages: str | None = None,
    input: str | None = None,
    **kwargs: Any,
) -> str
```

## Description

Generate a cache key based on the model configuration, input arguments, and optional name.

Modeled after the fnllm cache key generation.
https://github.com/microsoft/essex-toolkit/blob/23d3077b65c0e8f1d89c397a2968fe570a25f790/python/fnllm/fnllm/caching/base.py#L50

Args:
    model_config: The configuration of the language model.
    prefix: A prefix for the cache key.
    messages: Optional messages input for the cache key.
    input: Optional single input for the cache key.
    **kwargs: Additional model input parameters. May include 'name', which, if present, is appended to the prefix after hashing.

Returns:
    str: The generated cache key in the form '&#123;prefix&#125;_&#123;data_hash&#125;_v&#123;version&#125;'. Note that the provided 'name' (via kwargs) is appended to the prefix after computing the data hash, not before.

Raises:
    ValueError: If both 'messages' and 'input' are provided. The exact message is: "Only one of 'messages' or 'input' should be provided."
    ValueError: If neither 'messages' nor 'input' is provided. The exact message is: "Either 'messages' or 'input' must be provided."

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/get_cache_key.py::_get_parameters`
- `graphrag/language_model/providers/litellm/get_cache_key.py::_hash`

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py::_wrapped_with_cache`
- `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py::_wrapped_with_cache_async`

