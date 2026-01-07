---
sidebar_position: 128
---

# graphrag/index/workflows/finalize_graph.py

## Overview

Finalize graph data workflow.

This module implements the finalize_graph workflow used to finalize the entity and relationship data for the Graph Rag index. It coordinates the finalization steps by invoking operations such as create_graph, finalize_entities, finalize_relationships, and optional GraphML snapshotting via snapshot_graphml. It relies on configuration models EmbedGraphConfig and GraphRagConfig and interacts with storage helpers to load and persist updated tables.

Exports:
- finalize_graph(entities: pd.DataFrame, relationships: pd.DataFrame, embed_config: EmbedGraphConfig | None = None, layout_enabled: bool = False) -&gt; tuple[pd.DataFrame, pd.DataFrame]
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Brief summary:
- Orchestrates finalization of entity and relationship data, with optional embedding layout and GraphML snapshot, persisting changes to storage.

## Functions

- [`finalize_graph`](../api/functions/graphrag-index-workflows-finalize-graph-finalize-graph)
- [`run_workflow`](../api/functions/graphrag-index-workflows-finalize-graph-run-workflow)

