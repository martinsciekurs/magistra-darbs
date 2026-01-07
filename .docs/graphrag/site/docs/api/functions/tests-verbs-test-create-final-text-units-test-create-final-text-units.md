---
sidebar_position: 571
---

# test_create_final_text_units

**File:** `tests/verbs/test_create_final_text_units.py` (lines 19-41)

## Signature

```python
def test_create_final_text_units()
```

## Description

Test the asynchronous creation of final text units and validate the produced output against the expected test table.

Returns:
    None. This test does not return a value; it asserts correctness by comparing actual output to expected data.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_final_text_units.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`

