---
sidebar_position: 3
---

# Indexing Engine Core & Workflows

Core indexing pipeline, graph construction, embedding, and update workflows that build and maintain the knowledge graph index.

## Overview

Indexing Engine Core & Workflows: Core indexing pipeline, graph construction, embedding, and update workflows that build and maintain the knowledge graph index.

Architectural purpose
- This package implements the end-to-end GraphRAG-based indexing platform, including the core pipeline, graph construction, embedding, and incremental update workflows to build and maintain a knowledge graph index.

Key components and responsibilities
- graphrag/index/run/run_pipeline.py: Utilities for running the GraphRag index run pipeline, including execution helpers, run state persistence, and output transfer between storages. Public: run_pipeline; private: _dump_json, _copy_previous_output, _run_pipeline.
- graphrag/index/run/utils.py: Utilities to assemble a run context, create a callback chain, and derive update-related storage objects. Exports: create_callback_chain, create_run_context, get_update_storages.
- graphrag/index/workflows/factory.py: GraphRag workflows factory for building pipelines of workflow functions. Coordinates registration and construction of pipelines, maintains a class-level registry of named WorkflowFunction callables, and can assemble pipelines. Public: register, register_all, create_pipeline, register_pipeline; Class: PipelineFactory.
- graphrag/index/workflows/load_input_documents.py: Load and manage input documents for the GraphRag index workflow; supports multi-format ingestion (Plain Text, CSV, JSON) with schema validation via InputConfig; parses into a standard pandas DataFrame and persists to storage. Public API: load_input_documents, run_workflow.
- graphrag/index/workflows/update_text_embeddings.py: Module for updating text embeddings during incremental index runs; defines run_workflow to update embeddings based on incremental updates and persists results to storage, leveraging generate_text_embeddings and write_table_to_storage.
- graphrag/index/workflows/create_base_text_units.py: Module to generate base text units for GraphRAG indexing; utilities to convert input documents into base text units by grouping texts, chunking, and applying optional metadata preprocessing; exposes run_workflow.
- graphrag/index/workflows/update_entities_relationships.py: Utilities to update entities and relationships during incremental index runs; defines _update_entities_and_relationships and run_workflow to merge previous state with delta updates and update/merge relationships.
- graphrag/index/operations/create_graph.py: Utilities to construct NetworkX graphs from tabular data; create_graph builds a Graph from a DataFrame of edges and optional node attributes, with support for edge attributes and a node identifier column parameter.
- graphrag/index/operations/embed_graph/embed_graph.py: Embed graphs into vector space using node2vec; exposes embed_graph to map a NetworkX graph to embedding vectors, with configuration support.
- graphrag/index/operations/embed_graph/embed_node2vec.py: Node2Vec-based embedding for NetworkX graphs; function embed_node2vec computes node embeddings for Graphs suitable for downstream tasks.
- graphrag/index/operations/compute_degree.py: Compute the degree of each node in a NetworkX graph and return a pandas DataFrame.
- graphrag/index/operations/prune_graph.py: Prune graphs by filtering nodes and edges by frequency, degree, and edge weights; exports _get_upper_threshold_by_std and prune_graph.
- graphrag/index/validate_config.py: GraphRag configuration validation utility; function validate_config_names.
- graphrag/index/typing/state.py: Typing/state module describing common state representations used by the workflows.
- graphrag/index/operations/snapshot_graphml.py: Snapshot GraphMLs of graphs to a storage backend; function snapshot_graphml.

Public entry points / main APIs
- Public entry points include run_pipeline (graphrag/index/run/run_pipeline.py) and internal helpers (_dump_json, _copy_previous_output, _run_pipeline).
- Run utilities: create_callback_chain, create_run_context, get_update_storages (graphrag/index/run/utils.py).
- Workflow factory and assembly: PipelineFactory and functions in graphrag/index/workflows/factory.py (register, register_all, create_pipeline, register_pipeline).
- Public workflow entry points: load_input_documents.run_workflow, create_base_text_units.run_workflow, update_text_embeddings.run_workflow, update_entities_relationships.run_workflow.
- Graph construction and embeddings: create_graph, embed_graph, embed_node2vec.
- Graph analysis: compute_degree.
- Graph pruning: prune_graph and helper _get_upper_threshold_by_std.
- Configuration validation: validate_config_names.
- GraphML snapshot: snapshot_graphml.

## Files in this Module

- [`graphrag/index/run/run_pipeline.py`](../files/graphrag-index-run-run-pipeline)
- [`graphrag/index/run/utils.py`](../files/graphrag-index-run-utils)
- [`graphrag/index/workflows/factory.py`](../files/graphrag-index-workflows-factory)
- [`graphrag/index/workflows/load_input_documents.py`](../files/graphrag-index-workflows-load-input-documents)
- [`graphrag/index/workflows/update_text_embeddings.py`](../files/graphrag-index-workflows-update-text-embeddings)
- [`graphrag/index/workflows/create_base_text_units.py`](../files/graphrag-index-workflows-create-base-text-units)
- [`graphrag/index/workflows/update_entities_relationships.py`](../files/graphrag-index-workflows-update-entities-relationships)
- [`graphrag/index/operations/create_graph.py`](../files/graphrag-index-operations-create-graph)
- [`graphrag/index/operations/embed_graph/embed_graph.py`](../files/graphrag-index-operations-embed-graph-embed-graph)
- [`graphrag/index/operations/embed_graph/embed_node2vec.py`](../files/graphrag-index-operations-embed-graph-embed-node2vec)
- [`graphrag/index/operations/compute_degree.py`](../files/graphrag-index-operations-compute-degree)
- [`graphrag/index/operations/prune_graph.py`](../files/graphrag-index-operations-prune-graph)
- [`graphrag/index/validate_config.py`](../files/graphrag-index-validate-config)
- [`graphrag/index/typing/state.py`](../files/graphrag-index-typing-state)
- [`graphrag/index/operations/snapshot_graphml.py`](../files/graphrag-index-operations-snapshot-graphml)
