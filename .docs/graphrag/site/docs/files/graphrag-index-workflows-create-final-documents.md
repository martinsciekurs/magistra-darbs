---
sidebar_position: 122
---

# graphrag/index/workflows/create_final_documents.py

## Overview

Final documents workflow for the GraphRAG index.

Purpose:
- Provide utilities to transform input documents and text units into final documents and to run the final documents transformation workflow by loading data from storage, applying transformations, and persisting results.

Key exports:
- create_final_documents(documents: pd.DataFrame, text_units: pd.DataFrame) -&gt; pd.DataFrame
  Transforms input documents and text units into final documents.
  Args:
    documents: pd.DataFrame - Input documents data frame. Expected to contain at least the columns referenced by DOCUMENTS_FINAL_COLUMNS.
    text_units: pd.DataFrame - Input text units data frame. Expected to contain an 'document_ids' column indicating related document ids.
  Returns:
    pd.DataFrame - Final documents data frame.

- run_workflow(_config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput
  Runs the final documents transformation workflow.
  Args:
    _config: GraphRagConfig - GraphRag configuration used by the workflow.
    context: PipelineRunContext - Pipeline context used to load input tables from storage via the given context.
  Returns:
    WorkflowFunctionOutput - Output wrapper containing the produced DataFrame.

## Functions

- [`create_final_documents`](../api/functions/graphrag-index-workflows-create-final-documents-create-final-documents)
- [`run_workflow`](../api/functions/graphrag-index-workflows-create-final-documents-run-workflow)

