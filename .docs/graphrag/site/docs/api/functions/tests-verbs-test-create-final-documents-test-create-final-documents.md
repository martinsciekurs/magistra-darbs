---
sidebar_position: 569
---

# test_create_final_documents

**File:** `tests/verbs/test_create_final_documents.py` (lines 20-36)

## Signature

```python
def test_create_final_documents()
```

## Description

Test the final documents creation workflow.

This asynchronous test loads the expected documents data, initializes a test context with text_units storage, constructs a Graphrag config, executes the final documents workflow, loads the produced documents from storage, and compares the actual output to the expected data. It also verifies that all columns listed in DOCUMENTS_FINAL_COLUMNS are present in the produced table.

Returns:
    None

Raises:
    Exception: If any step in setup, execution, or validation fails.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_final_documents.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`

