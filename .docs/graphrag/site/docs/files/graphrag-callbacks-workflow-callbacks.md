---
sidebar_position: 9
---

# graphrag/callbacks/workflow_callbacks.py

## Overview

Workflow callbacks for observing workflow and pipeline lifecycle events.

Purpose: This module defines a Protocol named WorkflowCallbacks that observers can implement to react to progress updates and to the start/end signals emitted by the orchestration layer. It relies on Progress for progress updates and PipelineRunResult for representing pipeline results.

Key exports:
- WorkflowCallbacks: a Protocol describing the observer interface with the following methods:
  - progress(progress: Progress) -&gt; None
  - workflow_start(name: str, instance: object) -&gt; None
  - pipeline_start(names: list[str]) -&gt; None
  - pipeline_end(results: list[PipelineRunResult]) -&gt; None
  - workflow_end(name: str, instance: object) -&gt; None

Brief summary:
Stateless observers that react to progress updates and lifecycle events for workflows and pipelines.

## Classes

- [`WorkflowCallbacks`](../api/classes/graphrag-callbacks-workflow-callbacks-workflowcallbacks)

## Functions

- [`progress`](../api/functions/graphrag-callbacks-workflow-callbacks-progress)
- [`workflow_start`](../api/functions/graphrag-callbacks-workflow-callbacks-workflow-start)
- [`pipeline_start`](../api/functions/graphrag-callbacks-workflow-callbacks-pipeline-start)
- [`pipeline_end`](../api/functions/graphrag-callbacks-workflow-callbacks-pipeline-end)
- [`workflow_end`](../api/functions/graphrag-callbacks-workflow-callbacks-workflow-end)

