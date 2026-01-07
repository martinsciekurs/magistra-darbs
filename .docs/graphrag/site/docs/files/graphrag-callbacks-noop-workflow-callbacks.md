---
sidebar_position: 7
---

# graphrag/callbacks/noop_workflow_callbacks.py

## Overview

Noop implementation of workflow callbacks that performs no operations.

Purpose
Provide a safe, stateless no-op implementation of the WorkflowCallbacks interface for use in tests or scenarios where callbacks are required but should not alter program behavior.

Key exports
- NoopWorkflowCallbacks: Noop implementation of the WorkflowCallbacks interface.

Summary
This module exposes a NoopWorkflowCallbacks class that implements all callback methods as no-ops and maintains no internal state between calls. Public methods include: progress, pipeline_start, pipeline_end, workflow_start, and workflow_end.

## Classes

- [`NoopWorkflowCallbacks`](../api/classes/graphrag-callbacks-noop-workflow-callbacks-noopworkflowcallbacks)

## Functions

- [`progress`](../api/functions/graphrag-callbacks-noop-workflow-callbacks-progress)
- [`pipeline_end`](../api/functions/graphrag-callbacks-noop-workflow-callbacks-pipeline-end)
- [`workflow_end`](../api/functions/graphrag-callbacks-noop-workflow-callbacks-workflow-end)
- [`pipeline_start`](../api/functions/graphrag-callbacks-noop-workflow-callbacks-pipeline-start)
- [`workflow_start`](../api/functions/graphrag-callbacks-noop-workflow-callbacks-workflow-start)

