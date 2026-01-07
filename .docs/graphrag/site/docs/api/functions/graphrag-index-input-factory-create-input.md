---
sidebar_position: 54
---

# create_input

**File:** `graphrag/index/input/factory.py` (lines 27-56)

## Signature

```python
def create_input(
    config: InputConfig,
    storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Instantiate input data for a pipeline.

Args:
    config: InputConfig containing input configuration (such as file_type and metadata) and storage base_dir information.
    storage: PipelineStorage used to access the input data.

Returns:
    pandas.DataFrame: The loaded input data as a DataFrame. If config.metadata is provided and all metadata columns exist in the DataFrame, a new column named "metadata" is added containing a JSON object per row built from the metadata columns, and the original metadata columns are converted to strings.

Raises:
    ValueError: If one or more metadata columns listed in config.metadata are not found in the DataFrame, or if the input type specified in config.file_type is unknown.

## Called By

This function is called by:

- `graphrag/index/workflows/load_input_documents.py::load_input_documents`
- `graphrag/index/workflows/load_update_documents.py::load_update_documents`
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

