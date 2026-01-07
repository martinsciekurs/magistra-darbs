---
sidebar_position: 13
---

# LitellmEmbeddingModel

**File:** `graphrag/language_model/providers/litellm/embedding_model.py`

## Overview

LitellmEmbeddingModel wraps Litellm's embedding endpoints to generate vector representations for text inputs, with support for batch and single-input embeddings, and optional request-handling wrappers for caching, logging, rate limiting, and retries.

## Methods

### `_get_kwargs`

```python
def _get_kwargs(self, **kwargs: Any) -> dict[str, Any]
```

### `embed_batch`

```python
def embed_batch(self, text_list: list[str], **kwargs: Any) -> list[list[float]]
```

### `aembed_batch`

```python
def aembed_batch(
        self, text_list: list[str], **kwargs: Any
    ) -> list[list[float]]
```

### `aembed`

```python
def aembed(self, text: str, **kwargs: Any) -> list[float]
```

### `embed`

```python
def embed(self, text: str, **kwargs: Any) -> list[float]
```

### `__init__`

```python
def __init__(
        self,
        name: str,
        config: "LanguageModelConfig",
        cache: "PipelineCache | None" = None,
        **kwargs: Any,
    )
```

