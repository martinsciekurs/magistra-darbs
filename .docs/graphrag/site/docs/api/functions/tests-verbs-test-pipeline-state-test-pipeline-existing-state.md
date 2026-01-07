---
sidebar_position: 582
---

# test_pipeline_existing_state

**File:** `tests/verbs/test_pipeline_state.py` (lines 44-54)

## Signature

```python
def test_pipeline_existing_state()
```

## Description

Test that an existing state value in the pipeline run context can be updated by a workflow.

Only workflow_2 is registered and executed; the test initializes the run context with state=&#123;"count": 4&#125;, runs the pipeline, and asserts the final state count is 5.

Returns:
    None
        This test does not return a value.

Raises:
    AssertionError
        If the final state count is not 5.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/run/utils.py::create_run_context`

