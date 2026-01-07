---
sidebar_position: 139
---

# graphrag/index/workflows/update_text_embeddings.py

## Overview

Module for updating text embeddings during incremental index runs.

This module defines the run_workflow function, which updates text embeddings based on incremental updates from an index run and persists results to storage. It leverages generate_text_embeddings and write_table_to_storage to perform embedding generation and storage writes, coordinating with get_update_storages and the run context.

Key exports:
- run_workflow

Args:
- config: GraphRagConfig containing configuration for embedding and storage behavior.
- context: PipelineRunContext carrying the state for the run, including update_timestamp and incremental update data.

Returns:
- WorkflowFunctionOutput: The outcome of the workflow function execution.

Raises:
- Exception: If an unexpected error occurs during embedding generation or storage write.

## Functions

- [`run_workflow`](../api/functions/graphrag-index-workflows-update-text-embeddings-run-workflow)

