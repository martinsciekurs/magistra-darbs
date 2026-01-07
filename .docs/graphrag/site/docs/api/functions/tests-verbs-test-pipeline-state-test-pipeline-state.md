---
sidebar_position: 581
---

# test_pipeline_state

**File:** `tests/verbs/test_pipeline_state.py` (lines 29-41)

## Signature

```python
def test_pipeline_state()
```

## Description

Test that the pipeline run context state can be updated by workflows.

Two workflows are registered and executed in sequence, and the test asserts the state's count becomes 2.

Returns:
    None
        This test does not return a value.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/run/utils.py::create_run_context`

