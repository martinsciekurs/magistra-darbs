---
sidebar_position: 565
---

# test_create_base_text_units_metadata

**File:** `tests/verbs/test_create_base_text_units.py` (lines 31-47)

## Signature

```python
def test_create_base_text_units_metadata()
```

## Description

Asynchronous test for creating base text units with metadata.

Args:
    None: This test does not take any parameters.

Returns:
    None

Raises:
    Exception: Exceptions raised by the underlying test utilities may propagate to the caller.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_base_text_units.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`
- `tests/verbs/util.py::update_document_metadata`

