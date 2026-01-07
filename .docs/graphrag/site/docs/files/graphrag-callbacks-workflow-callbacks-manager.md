---
sidebar_position: 10
---

# graphrag/callbacks/workflow_callbacks_manager.py

## Overview

WorkflowCallbacksManager: registry and dispatcher for workflow lifecycle callbacks.

This module provides a single class, WorkflowCallbacksManager, which maintains an internal registry of WorkflowCallbacks instances and forwards lifecycle events to them. By centralizing registration and dispatch, it allows multiple callbacks to observe workflow and pipeline events without being tightly coupled to the core workflow logic.

Public API
- Class: WorkflowCallbacksManager
  - Attributes:
    - _callbacks: list[WorkflowCallbacks]; internal registry of callbacks to notify.
  - Methods:
    - __init__(): Initialize the manager with an empty callback registry.
    - register(callbacks: WorkflowCallbacks) -&gt; None: Register a new WorkflowCallbacks instance.
    - workflow_start(name: str, instance: object) -&gt; None: Dispatch the workflow_start event to all callbacks.
    - workflow_end(name: str, instance: object) -&gt; None: Dispatch the workflow_end event to all callbacks.
    - pipeline_start(names: list[str]) -&gt; None: Dispatch the pipeline_start event to all callbacks.
    - pipeline_end(results: list[PipelineRunResult]) -&gt; None: Dispatch the pipeline_end event to all callbacks.
    - progress(progress: Progress) -&gt; None: Forward Progress events to callbacks that implement a progress method.

Notes
- The manager forwards events to any registered callback that implements the corresponding method; if a callback does not implement a given method, it is skipped.

## Classes

- [`WorkflowCallbacksManager`](../api/classes/graphrag-callbacks-workflow-callbacks-manager-workflowcallbacksmanager)

## Functions

- [`workflow_start`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-workflow-start)
- [`__init__`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-init)
- [`workflow_end`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-workflow-end)
- [`pipeline_start`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-pipeline-start)
- [`progress`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-progress)
- [`register`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-register)
- [`pipeline_end`](../api/functions/graphrag-callbacks-workflow-callbacks-manager-pipeline-end)

