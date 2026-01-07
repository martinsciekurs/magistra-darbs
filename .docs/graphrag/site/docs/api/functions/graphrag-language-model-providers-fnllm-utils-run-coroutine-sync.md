---
sidebar_position: 274
---

# run_coroutine_sync

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 118-132)

## Signature

```python
def run_coroutine_sync(coroutine: Coroutine[Any, Any, T]) -> T
```

## Description

Run a coroutine synchronously.

Args:
    coroutine: Coroutine[Any, Any, T] The coroutine to run.

Returns:
    T: The result of the coroutine.

Raises:
    Exception: If the coroutine raises an exception, it will be propagated to the caller.

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/models.py::OpenAIChatFNLLM.chat`
- `graphrag/language_model/providers/fnllm/models.py::OpenAIEmbeddingFNLLM.embed_batch`
- `graphrag/language_model/providers/fnllm/models.py::OpenAIEmbeddingFNLLM.embed`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIChatFNLLM.chat`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIEmbeddingFNLLM.embed_batch`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIEmbeddingFNLLM.embed`

