---
sidebar_position: 586
---

# update_document_metadata

**File:** `tests/verbs/util.py` (lines 89-95)

## Signature

```python
def update_document_metadata(metadata: list[str], context: PipelineRunContext)
```

## Description

Asynchronously load the documents table from storage, create a new metadata column containing per-row dictionaries built from the selected metadata columns, and write the updated table back to storage.

This function loads the documents table from the provided storage backend, builds a dictionary for each row from the specified metadata columns, assigns it to a new 'metadata' column, and persists the changes back to storage.

Args:
  metadata: List[str] - Names of the columns to include in each per-row metadata dictionary.
  context: PipelineRunContext - Runtime context containing the output_storage used to load and write the documents table.

Returns:
  None

Raises:
  Exception: Exceptions raised by the storage backend during load or write operations may propagate.

## Dependencies

This function calls:

- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata_included_in_chunk`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents_with_metadata_column`

