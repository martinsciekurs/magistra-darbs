---
sidebar_position: 566
---

# test_create_base_text_units_metadata_included_in_chunk

**File:** `tests/verbs/test_create_base_text_units.py` (lines 50-68)

## Signature

```python
def test_create_base_text_units_metadata_included_in_chunk()
```

## Description

Asynchronous test for creating base text units with metadata included in a chunk when chunk_size_includes_metadata is True and metadata is prepended.

Returns:
    None: The test does not return a value.

Raises:
    Exception: Exceptions raised by the underlying test utilities or storage backends may propagate to the caller.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_base_text_units.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`
- `tests/verbs/util.py::update_document_metadata`

