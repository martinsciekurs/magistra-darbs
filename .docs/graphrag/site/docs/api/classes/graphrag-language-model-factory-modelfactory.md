---
sidebar_position: 56
---

# ModelFactory

**File:** `graphrag/language_model/factory.py`

## Overview

ModelFactory is a registry-based factory that creates chat and embedding language model backends.

Purpose:
- Maintain registries for embedding and chat model implementations.
- Provide a uniform API to register model backends and instantiate models by type.
- Offer utilities to query supported model types.

Attributes:
- _embedding_registry: ClassVar mapping[str, Callable[..., EmbeddingModel]] of model_type to a constructor for EmbeddingModel.
- _chat_registry: ClassVar mapping[str, Callable[..., ChatModel]] of model_type to a constructor for ChatModel.

Summary:
- Coordinates model backends from different providers (e.g., FNLLM, Litellm) by model type.

Returns:
- None

Raises:
- ValueError: If attempting to create a model for an unregistered model_type via create_chat_model or create_embedding_model.

## Methods

### `register_embedding`

```python
def register_embedding(
        cls, model_type: str, creator: Callable[..., EmbeddingModel]
    ) -> None
```

### `get_embedding_models`

```python
def get_embedding_models(cls) -> list[str]
```

### `create_chat_model`

```python
def create_chat_model(cls, model_type: str, **kwargs: Any) -> ChatModel
```

### `is_supported_model`

```python
def is_supported_model(cls, model_type: str) -> bool
```

### `is_supported_chat_model`

```python
def is_supported_chat_model(cls, model_type: str) -> bool
```

### `create_embedding_model`

```python
def create_embedding_model(cls, model_type: str, **kwargs: Any) -> EmbeddingModel
```

### `is_supported_embedding_model`

```python
def is_supported_embedding_model(cls, model_type: str) -> bool
```

### `get_chat_models`

```python
def get_chat_models(cls) -> list[str]
```

### `register_chat`

```python
def register_chat(cls, model_type: str, creator: Callable[..., ChatModel]) -> None
```

