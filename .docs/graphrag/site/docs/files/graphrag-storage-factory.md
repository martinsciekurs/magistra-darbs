---
sidebar_position: 216
---

# graphrag/storage/factory.py

## Overview

Registry-based factory for pipeline storage backends.

Purpose
Provides a central registry (StorageFactory) that maps storage type identifiers to creator callables for concrete PipelineStorage implementations (BlobPipelineStorage, CosmosDBPipelineStorage, FilePipelineStorage, MemoryPipelineStorage). It enables checking supported types, creating storage instances, registering new types, and listing registered types.

Public interfaces
- StorageFactory: Registry-based factory class offering:
  - is_supported_type(storage_type: str) -&gt; bool
  - create_storage(storage_type: str, kwargs: dict) -&gt; PipelineStorage
  - register(storage_type: str, creator: Callable[..., PipelineStorage]) -&gt; None
  - get_storage_types() -&gt; list[str]

Key exports
- StorageFactory: The registry-based factory for pipeline storage backends, mapping storage type keys to creator callables and providing methods to query, instantiate, register, and enumerate storage types.

Summary
This module centralizes creation and management of storage backends for pipeline storage, enabling pluggable implementations and runtime registration of new storage types.

## Classes

- [`StorageFactory`](../api/classes/graphrag-storage-factory-storagefactory)

## Functions

- [`is_supported_type`](../api/functions/graphrag-storage-factory-is-supported-type)
- [`create_storage`](../api/functions/graphrag-storage-factory-create-storage)
- [`register`](../api/functions/graphrag-storage-factory-register)
- [`get_storage_types`](../api/functions/graphrag-storage-factory-get-storage-types)

