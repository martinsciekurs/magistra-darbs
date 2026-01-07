---
sidebar_position: 277
---

# tests/verbs/test_pipeline_state.py

## Overview

Module for tests that verify updating a Graphrag pipeline's run context state via workflows. Purpose: This module defines two asynchronous workflow functions, run_workflow_1 and run_workflow_2, and two tests, test_pipeline_state and test_pipeline_existing_state, to ensure PipelineRunContext.state is updated correctly when workflows are executed by a PipelineFactory-based pipeline.

Key exports:
- run_workflow_1(_config: GraphRagConfig, context: PipelineRunContext)
- run_workflow_2(_config: GraphRagConfig, context: PipelineRunContext)
- test_pipeline_state()
- test_pipeline_existing_state()

Summary:
- run_workflow_1 initializes context.state["count"] to 1 and returns a WorkflowFunctionOutput with result=None.
- run_workflow_2 increments context.state["count"] by 1 and may raise KeyError if 'count' is not present.
- test_pipeline_state registers both workflows and asserts the final state count equals 2.
- test_pipeline_existing_state initializes count to 4, runs only run_workflow_2, and asserts final count equals 5.

Returns:
- None

Raises:
- KeyError: If 'count' is not present when run_workflow_2 is invoked.

## Functions

- [`run_workflow_1`](../api/functions/tests-verbs-test-pipeline-state-run-workflow-1)
- [`run_workflow_2`](../api/functions/tests-verbs-test-pipeline-state-run-workflow-2)
- [`test_pipeline_state`](../api/functions/tests-verbs-test-pipeline-state-test-pipeline-state)
- [`test_pipeline_existing_state`](../api/functions/tests-verbs-test-pipeline-state-test-pipeline-existing-state)

