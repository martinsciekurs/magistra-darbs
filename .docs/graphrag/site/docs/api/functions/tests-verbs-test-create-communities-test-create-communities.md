---
sidebar_position: 567
---

# test_create_communities

**File:** `tests/verbs/test_create_communities.py` (lines 19-48)

## Signature

```python
def test_create_communities()
```

## Description

Test the create_communities workflow by generating final communities and validating the produced output against the test dataset.

Args:
    None: This test function does not accept any parameters.

Returns:
    None: The test does not return a value; it performs assertions to verify correctness.

Raises:
    Exception: Exceptions raised by the helper utilities used in this test (load_test_table, create_test_context, create_graphrag_config, run_workflow, load_table_from_storage, or compare_outputs) may propagate.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/create_communities.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::compare_outputs`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`

