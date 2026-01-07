---
sidebar_position: 51
---

# ModelManager

**File:** `graphrag/language_model/manager.py`

## Overview

Singleton manager for chat and embedding language models.

Overview:
ModelManager is a singleton responsible for creating, registering, retrieving, and listing ChatModel and EmbeddingModel instances. It delegates on-demand instantiation to ModelFactory and stores instances in internal registries for reuse. Access to the singleton is provided via __new__ or get_instance.

Attributes:
    chat_models (dict[str, ChatModel]): Registry of registered chat models keyed by name.
    embedding_models (dict[str, EmbeddingModel]): Registry of registered embedding models keyed by name.
    _initialized (bool): Initialization flag to prevent reinitialization.

Raises:
    ValueError: If attempting to retrieve a non-registered chat or embedding model.

## Methods

### `get_or_create_chat_model`

```python
def get_or_create_chat_model(
        self, name: str, model_type: str, **chat_kwargs: Any
    ) -> ChatModel
```

### `list_chat_models`

```python
def list_chat_models(self) -> dict[str, ChatModel]
```

### `remove_chat`

```python
def remove_chat(self, name: str) -> None
```

### `list_embedding_models`

```python
def list_embedding_models(self) -> dict[str, EmbeddingModel]
```

### `get_chat_model`

```python
def get_chat_model(self, name: str) -> ChatModel | None
```

### `get_or_create_embedding_model`

```python
def get_or_create_embedding_model(
        self, name: str, model_type: str, **embedding_kwargs: Any
    ) -> EmbeddingModel
```

### `get_instance`

```python
def get_instance(cls) -> ModelManager
```

### `register_embedding`

```python
def register_embedding(
        self, name: str, model_type: str, **embedding_kwargs: Any
    ) -> EmbeddingModel
```

### `__new__`

```python
def __new__(cls) -> Self
```

### `register_chat`

```python
def register_chat(
        self, name: str, model_type: str, **chat_kwargs: Any
    ) -> ChatModel
```

### `__init__`

```python
def __init__(self) -> None
```

### `remove_embedding`

```python
def remove_embedding(self, name: str) -> None
```

### `get_embedding_model`

```python
def get_embedding_model(self, name: str) -> EmbeddingModel | None
```

