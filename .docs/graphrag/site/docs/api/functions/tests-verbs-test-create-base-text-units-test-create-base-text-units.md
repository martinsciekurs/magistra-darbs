---
sidebar_position: 564
---

# test_create_base_text_units

**File:** `tests/verbs/test_create_base_text_units.py` (lines 17-28)

## Signature

```python
def test_create_base_text_units()
```

## Description

Test the creation of base text units by running the workflow and validating the produced text_units table against the expected test data.

Returns:
    None. This test does not return a value; it asserts correctness by comparing actual output to expected data.

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

