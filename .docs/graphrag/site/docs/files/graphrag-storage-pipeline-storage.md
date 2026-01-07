---
sidebar_position: 219
---

# graphrag/storage/pipeline_storage.py

## Overview

Pipeline storage interface and helpers for the pipeline.

This module defines PipelineStorage, an abstract base class that specifies a key-value storage API used by the pipeline. It includes methods for existence checks, pattern-based discovery, retrieval with optional byte/encoding handling, listing keys, obtaining creation dates, and deletion. It also exposes a small helper to format timestamps in the local time zone.

Key exports
- PipelineStorage: Abstract base class for storage backends.
- has(key: str) -&gt; bool: Return True if the given key exists in the storage.
- find(file_pattern: re.Pattern[str], base_dir: str | None = None, file_filter: dict[str, Any] | None = None, max_count: int = -1) -&gt; Iterator[tuple[str, dict[str, Any]]]: Find files in the storage that match a compiled pattern, with optional base_dir and metadata-based filtering.
- get_timestamp_formatted_with_local_tz(timestamp: datetime) -&gt; str: Get the formatted timestamp with the local time zone.
- get_creation_date(key: str) -&gt; str: Get the creation date for the given key.
- clear() -&gt; None: Synchronously clear all entries from the storage.
- set(key: str, value: Any, encoding: str | None = None) -&gt; None: Set the value for the given key.
- keys() -&gt; list[str]: List all keys currently stored.
- get(key: str, as_bytes: bool | None = None, encoding: str | None = None) -&gt; Any: Get the value for the given key.
- child(name: str | None) -&gt; "PipelineStorage": Create or return a child storage instance.
- delete(key: str) -&gt; None: Delete the given key from the storage.

Brief summary
The interface supports in-memory, filesystem, database, or remote backends, enabling interchangeable storage implementations for the pipeline’s data needs. Implementations should document the exact exception behavior (e.g., invalid keys, I/O errors) and compatibility constraints for Python versions lacking newer typing constructs.

## Classes

- [`PipelineStorage`](../api/classes/graphrag-storage-pipeline-storage-pipelinestorage)

## Functions

- [`has`](../api/functions/graphrag-storage-pipeline-storage-has)
- [`get_timestamp_formatted_with_local_tz`](../api/functions/graphrag-storage-pipeline-storage-get-timestamp-formatted-with-local-tz)
- [`find`](../api/functions/graphrag-storage-pipeline-storage-find)
- [`get_creation_date`](../api/functions/graphrag-storage-pipeline-storage-get-creation-date)
- [`clear`](../api/functions/graphrag-storage-pipeline-storage-clear)
- [`set`](../api/functions/graphrag-storage-pipeline-storage-set)
- [`keys`](../api/functions/graphrag-storage-pipeline-storage-keys)
- [`get`](../api/functions/graphrag-storage-pipeline-storage-get)
- [`child`](../api/functions/graphrag-storage-pipeline-storage-child)
- [`delete`](../api/functions/graphrag-storage-pipeline-storage-delete)

