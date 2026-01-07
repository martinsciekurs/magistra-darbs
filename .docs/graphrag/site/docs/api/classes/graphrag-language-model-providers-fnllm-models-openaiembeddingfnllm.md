---
sidebar_position: 33
---

# OpenAIEmbeddingFNLLM

**File:** `graphrag/language_model/providers/fnllm/models.py`

## Overview

OpenAI Embedding FNLLM provider that generates text embeddings using the FNLLM OpenAI embeddings LLM.

Args:
  name: The name to assign to the internal cache provider and model instance.
  config: LanguageModelConfig used to derive the OpenAI configuration.
  callbacks: Optional WorkflowCallbacks; if provided, used for workflow event handling.
  cache: Optional PipelineCache; if provided, used to cache results.

Returns:
  OpenAIEmbeddingFNLLM: An initialized instance of the provider.

Raises:
  Exception: If initialization fails due to configuration issues or internal errors.

## Methods

### `aembed_batch`

```python
def aembed_batch(self, text_list: list[str], **kwargs) -> list[list[float]]
```

### `aembed`

```python
def aembed(self, text: str, **kwargs) -> list[float]
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

