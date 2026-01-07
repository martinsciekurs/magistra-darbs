---
sidebar_position: 37
---

# StorageFactory

**File:** `graphrag/storage/factory.py`

## Overview

StorageFactory: Registry-based factory for pipeline storage backends.

Purpose:
Provides a centralized registry that maps storage type identifiers to creator callables for concrete PipelineStorage implementations (BlobPipelineStorage, CosmosDBPipelineStorage, FilePipelineStorage, MemoryPipelineStorage). It enables checking supported types, creating storage instances, registering new types, and listing available storage types.

Attributes:
    _registry: ClassVar[dict[str, Callable[..., PipelineStorage]]]
        Registry mapping storage type keys to their creator callables.

Methods:
    is_supported_type(cls, storage_type: str) -&gt; bool:
        Check if the given storage_type is registered.

    create_storage(cls, storage_type: str, kwargs: dict) -&gt; PipelineStorage:
        Create a storage object from the provided type.

    register(cls, storage_type: str, creator: Callable[..., PipelineStorage]) -&gt; None:
        Register a custom storage implementation.

    get_storage_types(cls) -&gt; list[str]:
        Get the registered storage implementations.

Returns:
    For is_supported_type: bool indicating support.
    For create_storage: a PipelineStorage instance.
    For register: None (side effect: registry updated).
    For get_storage_types: list of registered storage type keys.

Raises:
    ValueError: If the storage type is not registered when attempting to create storage.

## Methods

### `is_supported_type`

```python
def is_supported_type(cls, storage_type: str) -> bool
```

### `create_storage`

```python
def create_storage(cls, storage_type: str, kwargs: dict) -> PipelineStorage
```

### `register`

```python
def register(
        cls, storage_type: str, creator: Callable[..., PipelineStorage]
    ) -> None
```

### `get_storage_types`

```python
def get_storage_types(cls) -> list[str]
```

