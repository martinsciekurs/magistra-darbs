---
sidebar_position: 86
---

# LitellmChatModel

**File:** `graphrag/language_model/providers/litellm/chat_model.py`

## Overview

LitellmChatModel is a Graphrag wrapper around a Litellm chat model with streaming, caching, and resilience features.

Args:
  name: The name of the model instance.
  config: LanguageModelConfig containing configuration for the language model.
  cache: Optional PipelineCache to use for responses; if provided, a child cache scoped to this model's name is created.
  kwargs: Arbitrary keyword arguments forwarded to the underlying Litellm client.

Returns:
  LitellmChatModel: The initialized model instance.

Raises:
  May raise exceptions from underlying libraries (e.g., authentication or network errors) during initialization or operation.

## Methods

### `_get_kwargs`

```python
def _get_kwargs(self, **kwargs: Any) -> dict[str, Any]
```

### `achat_stream`

```python
def achat_stream(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> AsyncGenerator[str, None]
```

### `chat`

```python
def chat(self, prompt: str, history: list | None = None, **kwargs: Any) -> "MR"
```

### `chat_stream`

```python
def chat_stream(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> Generator[str, None]
```

### `achat`

```python
def achat(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> "MR"
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

