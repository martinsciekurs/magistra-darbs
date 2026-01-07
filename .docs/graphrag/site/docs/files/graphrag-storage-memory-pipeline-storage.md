---
sidebar_position: 218
---

# graphrag/storage/memory_pipeline_storage.py

## Overview

MemoryPipelineStorage: In-memory, dictionary-backed implementation of the PipelineStorage interface.

Overview:
This module provides MemoryPipelineStorage, a fast, non-persistent storage backend that keeps pipeline data in a Python dictionary for the lifetime of the process. It implements the standard storage operations and supports creating child storages to establish isolated namespaces.

Key exports:
- MemoryPipelineStorage: In-memory storage backend conforming to the PipelineStorage interface with the following methods: clear, keys, delete, has, set, get, and child.

Initialization:
- __init__(self) -&gt; None
  Initializes the internal storage dictionary bound to self._storage. No parameters beyond self. Returns None.

Isolation and namespaces:
- The child(name) method returns a new MemoryPipelineStorage instance that operates within a named namespace. Keys used in the child are isolated from keys in other namespaces, ensuring namespace-level isolation guarantees for typical usage.

API summary:
- clear() -&gt; None: Remove all entries from the current namespace.
- keys() -&gt; list[str]: Return the keys currently stored in the current namespace.
- delete(key: str) -&gt; None: Delete the given key; raises KeyError if the key does not exist.
- has(key: str) -&gt; bool: Return True if the key exists in the current namespace.
- set(key: str, value: Any, encoding: str | None = None) -&gt; None: Store value under key; encoding is accepted for compatibility but ignored.
- get(key: str, as_bytes: bool | None = None, encoding: str | None = None) -&gt; Any: Retrieve value for key; as_bytes and encoding are ignored in this backend.
- child(name: str | None) -&gt; "PipelineStorage": Create and return a child storage scoped to the optional namespace; returns a MemoryPipelineStorage instance.

Remarks:
- This backend is intended for testing and runtime contexts where persistence is not required. Data does not survive process termination.

## Classes

- [`MemoryPipelineStorage`](../api/classes/graphrag-storage-memory-pipeline-storage-memorypipelinestorage)

## Functions

- [`clear`](../api/functions/graphrag-storage-memory-pipeline-storage-clear)
- [`keys`](../api/functions/graphrag-storage-memory-pipeline-storage-keys)
- [`delete`](../api/functions/graphrag-storage-memory-pipeline-storage-delete)
- [`has`](../api/functions/graphrag-storage-memory-pipeline-storage-has)
- [`set`](../api/functions/graphrag-storage-memory-pipeline-storage-set)
- [`__init__`](../api/functions/graphrag-storage-memory-pipeline-storage-init)
- [`get`](../api/functions/graphrag-storage-memory-pipeline-storage-get)
- [`child`](../api/functions/graphrag-storage-memory-pipeline-storage-child)

