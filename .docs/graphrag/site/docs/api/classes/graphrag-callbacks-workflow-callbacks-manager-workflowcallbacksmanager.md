---
sidebar_position: 58
---

# WorkflowCallbacksManager

**File:** `graphrag/callbacks/workflow_callbacks_manager.py`

## Overview

Manager that holds registered WorkflowCallbacks instances and dispatches lifecycle events to them.

Purpose:
To centralize the registration and dispatch of workflow and pipeline lifecycle events to all registered callbacks.

Key attributes:
- _callbacks: List[WorkflowCallbacks]
    Internal registry of callbacks to which events are forwarded.

Brief summary:
The manager maintains an internal registry of WorkflowCallbacks implementations and forwards events such as pipeline_start, pipeline_end, workflow_start, workflow_end, and progress to each registered callback that implements the corresponding method. There is no deduplication when registering callbacks; the same instance can be added multiple times.

Args:
- self: The WorkflowCallbacksManager instance. The constructor takes no external parameters.

Returns:
None

Raises:
None

## Methods

### `workflow_start`

```python
def workflow_start(self, name: str, instance: object) -> None
```

### `__init__`

```python
def __init__(self)
```

### `workflow_end`

```python
def workflow_end(self, name: str, instance: object) -> None
```

### `pipeline_start`

```python
def pipeline_start(self, names: list[str]) -> None
```

### `progress`

```python
def progress(self, progress: Progress) -> None
```

### `register`

```python
def register(self, callbacks: WorkflowCallbacks) -> None
```

### `pipeline_end`

```python
def pipeline_end(self, results: list[PipelineRunResult]) -> None
```

