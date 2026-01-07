---
sidebar_position: 94
---

# PipelineFactory

**File:** `graphrag/index/workflows/factory.py`

## Overview

PipelineFactory coordinates registration and construction of pipelines composed of workflow functions. It maintains a class-level registry of named WorkflowFunction callables and can assemble these into reusable Pipeline objects for GraphRag-based workflows. A Pipeline is a sequence of WorkflowFunction objects executed in order to process GraphRag data.

Attributes:
  registry: ClassVar[dict[str, WorkflowFunction]] - class-level mapping of names to workflow callables used to build pipelines and validate references.

Methods:
  register(cls, name: str, workflow: WorkflowFunction)
    Register a custom workflow function.
    Args:
      cls: The class that provides access to the registry (PipelineFactory).
      name: The name under which the workflow will be registered.
      workflow: The workflow function to register for the given name.
    Returns:
      None
    Raises:
      TypeError: If the provided name or workflow are of incorrect types.

  register_all(cls, workflows: dict[str, WorkflowFunction])
    Register a dict of custom workflow functions.
    Args:
      cls: The class that provides access to the registry (PipelineFactory).
      workflows: A dictionary mapping workflow names to workflow functions.
    Returns:
      None
    Raises:
      TypeError: If the mapping is not of the expected type or contains invalid entries.

  create_pipeline(
        cls,
        config: GraphRagConfig,
        method: IndexingMethod | str = IndexingMethod.Standard,
    ) -&gt; Pipeline
    Create a pipeline for executing a sequence of workflows.
    Args:
      cls: The class reference (provided automatically for classmethod).
      config: GraphRagConfig describing the graph/rag indexing setup.
      method: The indexing method or key to select a predefined pipeline. Defaults to IndexingMethod.Standard.
    Returns:
      Pipeline: The constructed Pipeline object.
    Raises:
      KeyError: If any workflow name in the selected workflows is not registered.
      TypeError: If the provided config or method have invalid types.
      ValueError: If the resolved workflow list is empty or otherwise invalid.

  register_pipeline(cls, name: str, workflows: list[str])
    Register a new pipeline method as a list of workflow names.
    Args:
      cls: The class reference (PipelineFactory).
      name: The name of the pipeline to register.
      workflows: A list of workflow names that constitute the pipeline.
    Returns:
      None
    Raises:
      TypeError: If inputs have incorrect types.
      KeyError: If any referenced workflow name is not registered.
      ValueError: If the workflows list is empty.

## Methods

### `register`

```python
def register(cls, name: str, workflow: WorkflowFunction)
```

### `register_all`

```python
def register_all(cls, workflows: dict[str, WorkflowFunction])
```

### `create_pipeline`

```python
def create_pipeline(
        cls,
        config: GraphRagConfig,
        method: IndexingMethod | str = IndexingMethod.Standard,
    ) -> Pipeline
```

### `register_pipeline`

```python
def register_pipeline(cls, name: str, workflows: list[str])
```

