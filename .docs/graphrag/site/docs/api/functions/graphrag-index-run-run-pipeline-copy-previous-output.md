---
sidebar_position: 166
---

# _copy_previous_output

**File:** `graphrag/index/run/run_pipeline.py` (lines 160-167)

## Signature

```python
def _copy_previous_output(
    storage: PipelineStorage,
    copy_storage: PipelineStorage,
)
```

## Description

Copy parquet outputs from the source storage to the copy storage asynchronously.

This async function locates all parquet files in the source storage (matching the pattern ".parquet" at the end of the name), derives a base name by removing the ".parquet" extension from the path, loads the corresponding table from the source storage, and writes it to the copy storage under the same base name.

Args:
    storage (PipelineStorage): The storage backend to read parquet files from.
    copy_storage (PipelineStorage): The storage backend to which parquet files will be written.

Returns:
    None

Raises:
    ValueError: If a required parquet file cannot be found or if base name extraction yields an invalid name. The underlying load operation may raise ValueError.
    Exception: Exceptions raised by the storage backend or parquet reader/writer during the load or write operations may propagate to the caller.

Notes:
    - base_name is derived by removing the ".parquet" extension from the discovered file path. If a file name contains multiple occurrences of ".parquet", all occurrences will be removed, which may lead to an unexpected base name in rare cases.
    - This function processes all parquet files found in storage; if multiple files share the same base name, later files may overwrite earlier ones in copy_storage.

## Dependencies

This function calls:

- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/run/run_pipeline.py::run_pipeline`

