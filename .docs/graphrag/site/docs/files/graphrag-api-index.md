---
sidebar_position: 1
---

# graphrag/api/index.py

## Overview

Utilities to configure and run the GraphRag indexing pipeline.

Purpose
- Provide small helpers to determine the final indexing method and to execute the indexing workflow against a GraphRagConfig.

Exports
- _get_method
- build_index

Summary
- The module coordinates method resolution, logging initialization, callback chain creation, pipeline construction, and execution to return results for GraphRag indexing runs.

Functions
- _get_method(method: IndexingMethod | str, is_update_run: bool) -&gt; str
  Args:
    method: IndexingMethod | str
      The indexing method. If an IndexingMethod is provided, its value is used; otherwise the string value is used directly.
    is_update_run: bool
      True if this is an update run; in which case the method name will be suffixed with "-update".
  Returns:
    str
      The final method name to use for the indexing pipeline.

- build_index(
    config: GraphRagConfig,
    method: IndexingMethod | str = IndexingMethod.Standard,
    is_update_run: bool = False,
    memory_profile: bool = False,
    callbacks: list[WorkflowCallbacks] | None = None,
    additional_context: dict[str, Any] | None = None,
    verbose: bool = False,
    input_documents: pd.DataFrame | None = None,
  ) -&gt; list[PipelineRunResult]
  Args:
    config: GraphRagConfig
      The configuration for the GraphRag indexing run.
    method: IndexingMethod | str
      The indexing method to use, or its string value if a simple string is provided.
    is_update_run: bool
      True if this is an update run; the final method name will incorporate this.
    memory_profile: bool
      Enable memory profiling during the run.
    callbacks: list[WorkflowCallbacks] | None
      Optional collection of workflow callbacks to wire into the run pipeline.
    additional_context: dict[str, Any] | None
      Additional contextual data to pass into the pipeline.
    verbose: bool
      Enable verbose logging/output.
    input_documents: pd.DataFrame | None
      Optional input documents to index instead of loading from a source.
  Returns:
    list[PipelineRunResult]
      The results of the indexing runs.
"""
&#125;  &gt;  None  // The final docstring content will be placed below as plain text. The system expects the actual docstring text here.

## Functions

- [`_get_method`](../api/functions/graphrag-api-index-get-method)
- [`build_index`](../api/functions/graphrag-api-index-build-index)

