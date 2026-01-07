---
sidebar_position: 131
---

# graphrag/index/workflows/load_update_documents.py

## Overview

Module for loading and updating documents in the GraphRag update workflow.

This module defines two public functions that power the update-document loading workflow: loading update-only input documents, computing deltas against previously stored documents, and writing results to storage.

Key exports:
- load_update_documents(config: InputConfig, input_storage: PipelineStorage, previous_storage: PipelineStorage) -&gt; pd.DataFrame
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

load_update_documents:
    Args:
        config: InputConfig containing input configuration (such as file_type and input source details)
        input_storage: PipelineStorage from which input documents will be loaded
        previous_storage: PipelineStorage containing previously stored documents for delta computation
    Returns:
        pd.DataFrame: The new input documents after delta computation
    Raises:
        Exception: If loading or delta computation fails

run_workflow:
    Args:
        config: GraphRagConfig containing input configuration and related settings
        context: PipelineRunContext providing access to input_storage, output_storage, and runtime statistics
    Returns:
        WorkflowFunctionOutput: The output containing the loaded update documents and related workflow metadata
    Raises:
        Exception: If loading, writing to storage, or orchestration fails

Brief summary:
The load_update_documents function loads documents using create_input(config, input_storage),
computes deltas using get_delta_docs with previous_storage, and returns the new inputs as a DataFrame.
The run_workflow function orchestrates loading, storage writing, and returns a workflow-compatible output.

## Functions

- [`load_update_documents`](../api/functions/graphrag-index-workflows-load-update-documents-load-update-documents)
- [`run_workflow`](../api/functions/graphrag-index-workflows-load-update-documents-run-workflow)

