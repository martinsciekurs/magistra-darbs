---
sidebar_position: 226
---

# graphrag/utils/storage.py

## Overview

Utilities for storing and retrieving parquet-backed pandas DataFrames in a PipelineStorage backend.

This module provides helper functions to write a DataFrame to storage as a parquet file, check for the existence of a table, load a table from storage, and delete a table from storage. The storage backend is any implementation of PipelineStorage.

Exports:
- write_table_to_storage(table, name, storage): Write a DataFrame to storage as &#123;name&#125;.parquet.
- storage_has_table(name, storage): Return True if &#123;name&#125;.parquet exists in storage.
- load_table_from_storage(name, storage): Load and return the DataFrame stored at &#123;name&#125;.parquet.
- delete_table_from_storage(name, storage): Delete the parquet file &#123;name&#125;.parquet from storage.

## Functions

- [`write_table_to_storage`](../api/functions/graphrag-utils-storage-write-table-to-storage)
- [`storage_has_table`](../api/functions/graphrag-utils-storage-storage-has-table)
- [`load_table_from_storage`](../api/functions/graphrag-utils-storage-load-table-from-storage)
- [`delete_table_from_storage`](../api/functions/graphrag-utils-storage-delete-table-from-storage)

