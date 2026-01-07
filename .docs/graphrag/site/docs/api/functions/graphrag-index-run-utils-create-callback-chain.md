---
sidebar_position: 169
---

# create_callback_chain

**File:** `graphrag/index/run/utils.py` (lines 41-48)

## Signature

```python
def create_callback_chain(
    callbacks: list[WorkflowCallbacks] | None,
) -> WorkflowCallbacks
```

## Description

Create a callback manager that encompasses multiple callbacks.

Args:
    callbacks: list[WorkflowCallbacks] | None. The callbacks to register on the manager. If None, an empty list is used.

Returns:
    WorkflowCallbacks: A manager that aggregates the provided callbacks.

## Dependencies

This function calls:

- `graphrag/callbacks/workflow_callbacks_manager.py::WorkflowCallbacksManager`

## Called By

This function is called by:

- `graphrag/api/index.py::build_index`

