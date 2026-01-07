---
sidebar_position: 276
---

# _create_cache

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 33-37)

## Signature

```python
def _create_cache(cache: PipelineCache | None, name: str) -> FNLLMCacheProvider | None
```

## Description

Create an FNLLM cache provider from a pipeline cache.

Args:
    cache: PipelineCache | None - The pipeline cache to wrap. If None, returns None.
    name: str - The name to assign to the child cache provider.

Returns:
    FNLLMCacheProvider | None - The created cache provider, or None if cache is None.

## Dependencies

This function calls:

- `graphrag/language_model/providers/fnllm/cache.py::FNLLMCacheProvider`

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/models.py::OpenAIChatFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::OpenAIEmbeddingFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIChatFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIEmbeddingFNLLM.__init__`

