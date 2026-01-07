---
sidebar_position: 568
---

# test_create_community_reports

**File:** `tests/verbs/test_create_community_reports.py` (lines 42-81)

## Signature

```python
def test_create_community_reports()
```

## Description

Test the create_community_reports workflow by generating community reports and validating the produced output against a test dataset.

The test loads test data into a test context, configures a mock language model with predefined responses, runs the workflow to generate community reports, and asserts that the resulting community_reports table matches the expected test data, including specific checks for mock-driven fields and the presence of all final columns.

Returns:
  None: The test does not return a value; it performs assertions to verify correctness.

Raises:
  Exception: Exceptions raised by the helper utilities used in this test (load_test_table, create_test_context, load_table_from_storage) may propagate.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_community_reports.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`

