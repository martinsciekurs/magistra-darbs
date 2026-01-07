---
sidebar_position: 230
---

# graphrag/vector_stores/factory.py

## Overview

Module for a registry-based factory to construct vector store instances from registered implementations.

This module defines VectorStoreFactory, a registry-based factory that maintains a registry mapping vector_store_type keys (strings) to creator callables that return BaseVectorStore instances. It exposes classmethods to instantiate vector stores by type, list supported types, verify support for a type, and register new implementations.

Public API
- VectorStoreFactory: Registry-based factory for constructing vector store instances from registered implementations. Purpose: maintains a registry that maps vector_store_type keys (strings) to creator callables that return BaseVectorStore instances. It exposes classmethods to instantiate vector stores by type, list supported types, verify support for a type, and register new implementations.
- create_vector_store(vector_store_type: str, vector_store_schema_config: VectorStoreSchemaConfig, **kwargs: dict) -&gt; BaseVectorStore: Create a vector store object from the provided type via a registry lookup. This function looks up the registered vector store implementation by vector_store_type and instantiates it by passing vector_store_schema_config and any additional keyword arguments to the concrete vector store constructor. The concrete vector_store may require or accept additional kwargs; these are forwarded via kwargs.
- get_vector_store_types(cls) -&gt; list[str]: Get the registered vector store implementations. Args: cls: The class on which this classmethod is invoked. Returns: list[str]: The list of registered vector store type keys (i.e., the keys of cls._registry).
- is_supported_type(cls, vector_store_type: str) -&gt; bool: Check if the given vector_store_type is supported. Args: cls: type The class reference (classmethod parameter). vector_store_type: str The type identifier for the vector store. Returns: bool: True if vector_store_type is registered in the registry, False otherwise.
- register(cls, vector_store_type: str, creator: Callable[..., BaseVectorStore]) -&gt; None: Register a custom vector store implementation. Stores the provided creator in the internal registry under the given vector_store_type. The registration does not enforce any factory semantics; the creator is stored as-is and will be invoked at runtime by VectorStoreFactory.create_vector_store with vector_store_schema_config and any additional keyword arguments. Args: vector_store_type (str): ...

## Classes

- [`VectorStoreFactory`](../api/classes/graphrag-vector-stores-factory-vectorstorefactory)

## Functions

- [`create_vector_store`](../api/functions/graphrag-vector-stores-factory-create-vector-store)
- [`get_vector_store_types`](../api/functions/graphrag-vector-stores-factory-get-vector-store-types)
- [`is_supported_type`](../api/functions/graphrag-vector-stores-factory-is-supported-type)
- [`register`](../api/functions/graphrag-vector-stores-factory-register)

