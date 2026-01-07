---
sidebar_position: 130
---

# graphrag/index/workflows/load_input_documents.py

## Overview

Load and manage input documents for the GraphRag index workflow.

This module provides functions to load input documents from configured sources, parse them into a standard pandas DataFrame, and persist them to storage as part of the GraphRag indexing workflow. The public API consists of load_input_documents and run_workflow. load_input_documents returns a DataFrame of the loaded inputs; run_workflow orchestrates loading and storage interactions, returning a WorkflowFunctionOutput that includes the loaded data.

Functions:
  - load_input_documents(config: InputConfig, storage: PipelineStorage) -&gt; pd.DataFrame
  - run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

load_input_documents:
  - Args:
      config: InputConfig containing input configuration (such as file_type and metadata) and storage base_dir information.
      storage: PipelineStorage used to access the input data.
  - Returns:
      pandas DataFrame: The loaded input data as a DataFrame.
  - Raises:
      Exceptions raised by loading/parsing inputs and storage interactions.

run_workflow:
  - Args:
      config: GraphRagConfig containing input configuration and related settings.
      context: PipelineRunContext providing access to input_storage, output_storage, and runtime statistics.
  - Returns:
      WorkflowFunctionOutput: The output containing the loaded input documents as a pandas DataFrame.
  - Raises:
      Exceptions raised during loading, writing to storage, or workflow execution.

## Functions

- [`load_input_documents`](../api/functions/graphrag-index-workflows-load-input-documents-load-input-documents)
- [`run_workflow`](../api/functions/graphrag-index-workflows-load-input-documents-run-workflow)

