---
sidebar_position: 79
---

# AzureOpenAIEmbeddingFNLLM

**File:** `graphrag/language_model/providers/fnllm/models.py`

## Overview

Azure OpenAI Embedding FNLLM provider for generating text embeddings.

This class provides embedding capabilities using an Azure OpenAI embedding model via FNLLM and exposes methods to embed single texts and batches, with both asynchronous and synchronous variants. It is initialized with a name, a LanguageModelConfig used to derive the OpenAI configuration, and optional components such as callbacks and a cache.

Args:
  name: The name to assign to the internal cache provider and model instance.
  config: The LanguageModelConfig used to derive the OpenAI configuration.
  callbacks: Optional WorkflowCallbacks; if provided, an error handler will be used.
  cache: Optional PipelineCache.

Returns:
  None

Raises:
  ValueError: If no embeddings are found in the response.

## Methods

### `aembed`

```python
def aembed(self, text: str, **kwargs) -> list[float]
```

### `aembed_batch`

```python
def aembed_batch(self, text_list: list[str], **kwargs) -> list[list[float]]
```

### `embed_batch`

```python
def embed_batch(self, text_list: list[str], **kwargs) -> list[list[float]]
```

### `embed`

```python
def embed(self, text: str, **kwargs) -> list[float]
```

### `__init__`

```python
def __init__(
        self,
        *,
        name: str,
        config: LanguageModelConfig,
        callbacks: WorkflowCallbacks | None = None,
        cache: PipelineCache | None = None,
    ) -> None
```

