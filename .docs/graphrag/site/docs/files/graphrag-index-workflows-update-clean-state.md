---
sidebar_position: 133
---

# graphrag/index/workflows/update_clean_state.py

## Overview

Cleanup state after an update in the GraphRag index workflows.

This module provides the workflow function that performs post-update cleanup of internal state in the GraphRag index workflow.

Key exports:
- run_workflow(_config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Exports details:
run_workflow
  Args:
    _config: GraphRagConfig: GraphRag configuration.
    context: PipelineRunContext: Runtime context for the workflow execution.
  Returns:
    WorkflowFunctionOutput: Output object for the workflow function; the result is None.

Summary:
The run_workflow function accepts the GraphRag configuration and a runtime context to perform cleanup after an update, returning a WorkflowFunctionOutput. It is intended for use within the GraphRag index workflow to ensure proper state hygiene post-update.

## Functions

- [`run_workflow`](../api/functions/graphrag-index-workflows-update-clean-state-run-workflow)

