---
sidebar_position: 4
---

# WorkflowCallbacks

**File:** `graphrag/callbacks/workflow_callbacks.py`

## Overview

WorkflowCallbacks defines a Protocol for observers of workflow and pipeline lifecycle events. Implementations act as stateless observers that react to progress updates and the start/end signals emitted by the orchestration layer.

Methods

progress(self, progress: Progress) -&gt; None
    Called when a progress update occurs.
    progress: Progress object representing the current progress event.
    Returns: None

workflow_start(self, name: str, instance: object) -&gt; None
    Invoked when a workflow starts.
    name: The name of the workflow starting.
    instance: The workflow instance object associated with the start event.
    Returns: None

pipeline_start(self, names: list[str]) -&gt; None
    Invoked to signal that the entire pipeline starts.
    names: The names of the pipelines that started.
    Returns: None

pipeline_end(self, results: list[PipelineRunResult]) -&gt; None
    Invoked to signal that the entire pipeline ends.
    results: A list of PipelineRunResult objects representing the pipeline results.
    Returns: None

workflow_end(self, name: str, instance: object) -&gt; None
    Invoked when a workflow ends.
    name: The name of the workflow.
    instance: The workflow instance object.
    Returns: None

Usage
Observers implement this Protocol and register with the orchestration system to receive these callbacks during workflow and pipeline lifecycle events.

## Methods

### `progress`

```python
def progress(self, progress: Progress) -> None
```

### `workflow_start`

```python
def workflow_start(self, name: str, instance: object) -> None
```

### `pipeline_start`

```python
def pipeline_start(self, names: list[str]) -> None
```

### `pipeline_end`

```python
def pipeline_end(self, results: list[PipelineRunResult]) -> None
```

### `workflow_end`

```python
def workflow_end(self, name: str, instance: object) -> None
```

