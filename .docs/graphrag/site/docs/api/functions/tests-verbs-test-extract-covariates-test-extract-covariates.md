---
sidebar_position: 572
---

# test_extract_covariates

**File:** `tests/verbs/test_extract_covariates.py` (lines 27-79)

## Signature

```python
def test_extract_covariates()
```

## Description

Test the covariates extraction workflow using a mocked language model response.

Returns:
    None: The test does not return a value.

Raises:
    Exception: Exceptions raised by underlying utilities (e.g., load_test_table or load_table_from_storage) may propagate during test execution.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/extract_covariates.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`

