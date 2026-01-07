---
sidebar_position: 400
---

# create_storage_from_config

**File:** `graphrag/utils/api.py` (lines 264-270)

## Signature

```python
def create_storage_from_config(output: StorageConfig) -> PipelineStorage
```

## Description

Create a storage object from the config.

Args:
    output: StorageConfig The storage configuration to create a storage object from.

Returns:
    PipelineStorage: The created storage object.

Raises:
    ValueError: If the storage type is not registered.

## Dependencies

This function calls:

- `graphrag/storage/factory.py::StorageFactory`

## Called By

This function is called by:

- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/index/run/run_pipeline.py::run_pipeline`
- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/prompt_tune/loader/input.py::load_docs_in_chunks`
- `tests/unit/indexing/input/test_csv_loader.py::test_csv_loader_one_file`
- `tests/unit/indexing/input/test_csv_loader.py::test_csv_loader_one_file_with_title`
- `tests/unit/indexing/input/test_csv_loader.py::test_csv_loader_one_file_with_metadata`
- `tests/unit/indexing/input/test_csv_loader.py::test_csv_loader_multiple_files`
- `tests/unit/indexing/input/test_json_loader.py::test_json_loader_one_file_one_object`
- `tests/unit/indexing/input/test_json_loader.py::test_json_loader_one_file_multiple_objects`
- `tests/unit/indexing/input/test_json_loader.py::test_json_loader_one_file_with_title`
- `tests/unit/indexing/input/test_json_loader.py::test_json_loader_one_file_with_metadata`
- `tests/unit/indexing/input/test_json_loader.py::test_json_loader_multiple_files`
- `tests/unit/indexing/input/test_txt_loader.py::test_txt_loader_one_file`
- `tests/unit/indexing/input/test_txt_loader.py::test_txt_loader_one_file_with_metadata`
- `tests/unit/indexing/input/test_txt_loader.py::test_txt_loader_multiple_files`

