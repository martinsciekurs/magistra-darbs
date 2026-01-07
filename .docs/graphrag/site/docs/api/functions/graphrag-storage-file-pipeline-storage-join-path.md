---
sidebar_position: 394
---

# join_path

**File:** `graphrag/storage/file_pipeline_storage.py` (lines 169-171)

## Signature

```python
def join_path(file_path: str, file_name: str) -> Path
```

## Description

Join a base path with the relative components of a file name to form a new pathlib.Path.

This function uses the parent directory and the file name from file_name and joins them with file_path to produce the final path. Note that if file_name is an absolute path, pathlib will discard the leading path components of file_path and the result will correspond to the absolute path described by file_name's components.

Args:
    file_path (str): Base path to join with the file's relative components (parent and name).
    file_name (str): Path-like string; its parent directory and file name are used for the join.

Returns:
    pathlib.Path: The resulting Path object.

## Called By

This function is called by:

- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage.get`
- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage.set`
- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage.has`
- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage.delete`
- `graphrag/storage/file_pipeline_storage.py::FilePipelineStorage.get_creation_date`

