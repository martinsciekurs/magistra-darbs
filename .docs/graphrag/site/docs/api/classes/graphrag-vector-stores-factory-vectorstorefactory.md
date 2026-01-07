---
sidebar_position: 74
---

# VectorStoreFactory

**File:** `graphrag/vector_stores/factory.py`

## Overview

VectorStoreFactory is a registry-based factory for constructing vector store instances from a registry of concrete implementations.

Purpose
This class maintains a registry that maps vector_store_type keys (strings) to creator callables that return BaseVectorStore instances. It exposes classmethods to instantiate vector stores by type, list supported types, verify support for a type, and register new implementations.

Class Attributes
  _registry (ClassVar[dict[str, Callable[..., BaseVectorStore]]]): Internal registry mapping vector_store_type keys to creator callables. Each creator should return a BaseVectorStore when invoked with a VectorStoreSchemaConfig and any forwarded keyword arguments.

Methods
  create_vector_store(
      cls,
      vector_store_type: str,
      vector_store_schema_config: VectorStoreSchemaConfig,
      **kwargs: dict
  ) -&gt; BaseVectorStore
  Create a vector store instance by looking up the registered creator for the given vector_store_type and invoking it with vector_store_schema_config and any additional keyword arguments. If the type is not registered, raises an error (e.g., KeyError or ValueError). Exceptions raised by the concrete vector store constructor are propagated.

  get_vector_store_types(cls) -&gt; list[str]
  Return a list of registered vector_store_type keys.

  is_supported_type(cls, vector_store_type: str) -&gt; bool
  Return True if vector_store_type is registered; otherwise False.

  register(cls, vector_store_type: str, creator: Callable[..., BaseVectorStore]) -&gt; None
  Register a new vector store implementation under the given vector_store_type. The provided creator is stored and invoked by create_vector_store. Raises ValueError if vector_store_type is already registered.

Notes
 The factory delegates all construction details to the registered creators. The concrete creators may require or accept additional kwargs, which are forwarded by create_vector_store.

## Methods

### `create_vector_store`

```python
def create_vector_store(
        cls,
        vector_store_type: str,
        vector_store_schema_config: VectorStoreSchemaConfig,
        **kwargs: dict,
    ) -> BaseVectorStore
```

### `get_vector_store_types`

```python
def get_vector_store_types(cls) -> list[str]
```

### `is_supported_type`

```python
def is_supported_type(cls, vector_store_type: str) -> bool
```

### `register`

```python
def register(
        cls, vector_store_type: str, creator: Callable[..., BaseVectorStore]
    ) -> None
```

