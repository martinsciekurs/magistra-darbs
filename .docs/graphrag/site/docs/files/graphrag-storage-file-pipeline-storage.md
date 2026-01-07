---
sidebar_position: 217
---

# graphrag/storage/file_pipeline_storage.py

## Overview

File-based storage backend for a pipeline that stores items as individual files under a root directory.

Purpose:
This module provides a filesystem-backed implementation of the PipelineStorage interface. It manages a root directory (creating it if necessary) and offers operations to read, write, delete, list keys, clear storage, and find files by pattern. It supports a configurable text encoding for file I/O and relies on aiofiles for asynchronous-like filesystem interactions.

Exports:
- FilePipelineStorage: The File-based storage backend class implementing the PipelineStorage interface.

Summary:
The FilePipelineStorage class exposes methods to clear storage, enumerate keys, obtain child storages, filter items, perform file pattern searches, and perform standard CRUD operations (get, set, has, delete) along with utility helpers for path joining and reading files. The storage root is created if missing, and the encoding for file operations can be customized via initialization parameters.

## Classes

- [`FilePipelineStorage`](../api/classes/graphrag-storage-file-pipeline-storage-filepipelinestorage)

## Functions

- [`clear`](../api/functions/graphrag-storage-file-pipeline-storage-clear)
- [`keys`](../api/functions/graphrag-storage-file-pipeline-storage-keys)
- [`child`](../api/functions/graphrag-storage-file-pipeline-storage-child)
- [`item_filter`](../api/functions/graphrag-storage-file-pipeline-storage-item-filter)
- [`find`](../api/functions/graphrag-storage-file-pipeline-storage-find)
- [`__init__`](../api/functions/graphrag-storage-file-pipeline-storage-init)
- [`_read_file`](../api/functions/graphrag-storage-file-pipeline-storage-read-file)
- [`join_path`](../api/functions/graphrag-storage-file-pipeline-storage-join-path)
- [`get`](../api/functions/graphrag-storage-file-pipeline-storage-get)
- [`set`](../api/functions/graphrag-storage-file-pipeline-storage-set)
- [`has`](../api/functions/graphrag-storage-file-pipeline-storage-has)
- [`delete`](../api/functions/graphrag-storage-file-pipeline-storage-delete)
- [`get_creation_date`](../api/functions/graphrag-storage-file-pipeline-storage-get-creation-date)

