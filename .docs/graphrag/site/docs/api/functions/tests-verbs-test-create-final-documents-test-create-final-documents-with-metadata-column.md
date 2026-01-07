---
sidebar_position: 570
---

# test_create_final_documents_with_metadata_column

**File:** `tests/verbs/test_create_final_documents.py` (lines 39-59)

## Signature

```python
def test_create_final_documents_with_metadata_column()
```

## Description

Test the final documents workflow when a metadata column is provided.

The test builds a test context with storage for text_units, creates a Graphrag config, enables metadata extraction by setting config.input.metadata = ["title"], simulates the metadata construction during initial input loading by calling update_document_metadata, captures the expected documents table from storage, runs the final documents workflow, then loads the actual documents table from storage, and compares the two results. It also asserts that every column listed in DOCUMENTS_FINAL_COLUMNS is present in the produced final documents table.

Returns:
    None
Raises:
    Exception: Exceptions raised by the utilities used in the test (e.g., load_table_from_storage, update_document_metadata, run_workflow) may propagate.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_final_documents.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::update_document_metadata`

