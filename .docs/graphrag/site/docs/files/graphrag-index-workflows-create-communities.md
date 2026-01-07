---
sidebar_position: 119
---

# graphrag/index/workflows/create_communities.py

## Overview

Create final communities from entities and relationships using graph-based clustering and metadata enrichment.

This module exposes the core workflow for constructing a graph from relationships, applying Leiden-based clustering to identify hierarchical communities, and aggregating related entities and relationships into a metadata-rich final DataFrame aligned to COMMUNITIES_FINAL_COLUMNS. It also provides a workflow entry point that orchestrates the process using a GraphRagConfig and a storage context.

Key exports:
- create_communities(entities: pd.DataFrame, relationships: pd.DataFrame, max_cluster_size: int, use_lcc: bool, seed: int | None = None) -&gt; pd.DataFrame
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Brief summary:
The create_communities function constructs a graph from the input relationships, performs Leiden clustering to derive communities, and aggregates related entities and relationships into a final, schema-aligned DataFrame. The run_workflow function executes this process using the provided configuration and storage context to read inputs and write outputs.

## Functions

- [`create_communities`](../api/functions/graphrag-index-workflows-create-communities-create-communities)
- [`run_workflow`](../api/functions/graphrag-index-workflows-create-communities-run-workflow)

