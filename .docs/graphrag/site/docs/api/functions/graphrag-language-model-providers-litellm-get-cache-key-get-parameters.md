---
sidebar_position: 289
---

# _get_parameters

**File:** `graphrag/language_model/providers/litellm/get_cache_key.py` (lines 81-135)

## Signature

```python
def _get_parameters(
    model_config: "LanguageModelConfig",
    **kwargs: Any,
) -> dict[str, Any]
```

## Description

Pluck out the parameters that define a cache key.

Use the same parameters as fnllm except request timeout.
- embeddings: https://github.com/microsoft/essex-toolkit/blob/main/python/fnllm/fnllm/openai/types/embeddings/parameters.py#L12
- chat: https://github.com/microsoft/essex-toolkit/blob/main/python/fnllm/fnllm/openai/types/chat/parameters.py#L25

Args:
    model_config: The configuration of the language model.
    kwargs: Additional model input parameters.

Returns:
    dict[str, Any]: A dictionary of parameters that define the cache key.

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/get_cache_key.py::get_cache_key`

