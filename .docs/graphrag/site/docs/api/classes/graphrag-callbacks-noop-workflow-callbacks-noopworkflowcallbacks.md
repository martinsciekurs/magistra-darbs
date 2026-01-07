---
sidebar_position: 102
---

# NoopWorkflowCallbacks

**File:** `graphrag/callbacks/noop_workflow_callbacks.py`

## Overview

Noop implementation of the WorkflowCallbacks interface that performs no operations.

Purpose:
Provide a safe, no-op callback implementation that conforms to the WorkflowCallbacks
interface, suitable for tests or scenarios where callbacks are required but should
not alter behavior.

Attributes:
- Stateless: This class does not maintain internal state between calls.

Summary:
All callback methods implemented by this class return None and perform no side effects.

## Methods

### `progress`

```python
def progress(self, progress: Progress) -> None
```

### `pipeline_end`

```python
def pipeline_end(self, results: list[PipelineRunResult]) -> None
```

### `workflow_end`

```python
def workflow_end(self, name: str, instance: object) -> None
```

### `pipeline_start`

```python
def pipeline_start(self, names: list[str]) -> None
```

### `workflow_start`

```python
def workflow_start(self, name: str, instance: object) -> None
```

