---
sidebar_position: 132
---

# graphrag/index/workflows/prune_graph.py

## Overview

Prune graph workflow orchestrator for Graphrag's indexing pipeline.

Purpose:
- Coordinates the prune-graph workflow by loading input data, delegating pruning to the prune_graph operation, and persisting the pruned results. The actual pruning logic resides in graphrag.index.operations.prune_graph and is invoked from this module via prune_graph_operation.

Args:
- config (GraphRagConfig): Configuration for pruning, including parameters exposed under prune_graph to control pruning behavior.
- context (PipelineRunContext): Runtime context for the workflow execution, containing metadata and runtime state.

Returns:
- WorkflowFunctionOutput: The result of the workflow, including the pruned entities and relationships and any associated metadata.

Raises:
- Exceptions raised by storage utilities, configuration validation, or the prune_graph operation are propagated to the caller.

Notes:
- The prune_graph operation expects input data in a specific shape (entities DataFrame with a 'title' column; relationships DataFrame with 'source' and 'target' columns; an optional 'weight' column may influence pruning).
- This module focuses on public API clarity and separates public orchestration from internal workflow orchestration.

## Functions

- [`prune_graph`](../api/functions/graphrag-index-workflows-prune-graph-prune-graph)
- [`run_workflow`](../api/functions/graphrag-index-workflows-prune-graph-run-workflow)

