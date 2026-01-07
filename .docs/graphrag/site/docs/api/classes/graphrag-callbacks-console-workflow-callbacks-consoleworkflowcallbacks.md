---
sidebar_position: 45
---

# ConsoleWorkflowCallbacks

**File:** `graphrag/callbacks/console_workflow_callbacks.py`

## Overview

Console-based callback implementation that prints workflow and pipeline events to the console.

This class inherits NoopWorkflowCallbacks and provides a concrete, console-oriented implementation of the workflow callback interface. It prints status messages for pipeline and workflow lifecycle events and renders a live progress bar to stdout as progress updates are received. When verbose mode is enabled, additional diagnostic information may be emitted to aid debugging.

Args:
    verbose (bool): Enable verbose logging to the console.

Attributes:
    _verbose (bool): Internal flag controlling verbose output.

Returns:
    None

Raises:
    May raise OSError or other I/O-related exceptions raised by writing to stdout.

Methods:
    __init__(verbose: bool = False)
    pipeline_start(names: list[str]) -&gt; None
    pipeline_end(results: list[PipelineRunResult]) -&gt; None
    workflow_start(name: str, instance: object) -&gt; None
    progress(progress: Progress) -&gt; None
    workflow_end(name: str, instance: object) -&gt; None

## Methods

### `__init__`

```python
def __init__(self, verbose=False)
```

### `pipeline_end`

```python
def pipeline_end(self, results: list[PipelineRunResult]) -> None
```

### `pipeline_start`

```python
def pipeline_start(self, names: list[str]) -> None
```

### `workflow_start`

```python
def workflow_start(self, name: str, instance: object) -> None
```

### `progress`

```python
def progress(self, progress: Progress) -> None
```

### `workflow_end`

```python
def workflow_end(self, name: str, instance: object) -> None
```

