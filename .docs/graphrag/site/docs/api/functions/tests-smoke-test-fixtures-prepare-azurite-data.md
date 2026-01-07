---
sidebar_position: 458
---

# prepare_azurite_data

**File:** `tests/smoke/test_fixtures.py` (lines 92-119)

## Signature

```python
def prepare_azurite_data(input_path: str, azure: dict) -> Callable[[], None]
```

## Description

Prepare Azurite test data for the fixtures.

This coroutine uses the azure configuration to create or reset a blob storage
container, uploads test data from the local input directory (txt and csv files),
and returns a callable that will delete the container when invoked.

Args:
  input_path: Path on disk containing test input data. The function looks for an
    input subdirectory with .txt and .csv files to upload.
  azure: Dictionary with Azure/Azurite configuration. Expected keys include:
    input_container: name of the blob container to use
    input_base_dir: optional base directory inside the container for the uploaded files

Returns:
  A callable with no arguments that deletes the blob container when called.

Raises:
  Exceptions raised by BlobPipelineStorage operations or file I/O

## Dependencies

This function calls:

- `graphrag/storage/blob_pipeline_storage.py::BlobPipelineStorage`

## Called By

This function is called by:

- `tests/smoke/test_fixtures.py::TestIndexer.test_fixture`

