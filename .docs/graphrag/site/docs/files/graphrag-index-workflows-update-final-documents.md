---
sidebar_position: 138
---

# graphrag/index/workflows/update_final_documents.py

## Overview

Module to update final documents from an incremental index run in GraphRag workflows.

Exports
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Summary
The run_workflow function orchestrates updating the final documents by consuming the results of an incremental index run. It retrieves the necessary update storages containing incremental document updates via get_update_storages and merges these updates into the final documents using concat_dataframes. The operation is side-effectful and returns a WorkflowFunctionOutput with result set to None, indicating that no explicit value is produced by this step.

Args:
- config: GraphRagConfig containing configuration for the workflow.
- context: PipelineRunContext carrying the state for the run.

Returns:
- WorkflowFunctionOutput: A WorkflowFunctionOutput instance where the result attribute is None, signifying that the workflow step updates final documents in place rather than returning a value. Additional metadata fields may be present depending on the WorkflowFunctionOutput type definition in the codebase.

Raises:
- KeyError: If the required update_timestamp metadata is missing from the update storages used by the update process. This path documents the direct consequence of missing the expected update_timestamp key during the update workflow.

Notes
- The KeyError path corresponds to missing update_timestamp in the update metadata supplied by upstream components. Ensure that the update metadata provides this key for the workflow to proceed.

## Functions

- [`run_workflow`](../api/functions/graphrag-index-workflows-update-final-documents-run-workflow)

