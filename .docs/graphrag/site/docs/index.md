---
sidebar_position: 1
slug: /
---

# graphrag Documentation

GraphRAG is a Python-based data pipeline and knowledge-graph augmentation framework designed to help you index unstructured private text, extract entities and relations, and build a hierarchical knowledge graph. It then uses large language models (LLMs) to answer questions with context-augmented prompts, enabling retrieval-augmented reasoning over private datasets. The project provides modular components for indexing, prompt tuning, querying, and visualization, making it suitable for researchers...

## Navigation

- **[Guide](guide/)** - Introduction, Quick Start, and How-To guides
- **[Modules](modules/)** - High-level architectural components
- **[Files](files/)** - File-level documentation  
- **[API Reference](api/)** - Classes and functions

## Modules

This codebase is organized into the following architectural modules:

### [Public API Layer](modules/public-api-layer)

Public interfaces for indexing, prompt tuning, and querying GraphRAG. These define the library-facing API used by clients and other subsystems.

### [GraphRAG Command-Line Interface](modules/graphrag-command-line-interface)

CLI entry points and tooling to run indexing, querying, and prompt tuning workflows via uv/poethepoet.

### [Indexing Engine Core & Workflows](modules/indexing-engine-core-workflows)

Core indexing pipeline, graph construction, embedding, and update workflows that build and maintain the knowledge graph index.

### [Query Engine Core & Interfaces](modules/query-engine-core-interfaces)

Query-time context construction, data retrieval, and LLM orchestration utilities used to answer questions against the knowledge graph.

### [Knowledge Graph Data Model](modules/knowledge-graph-data-model)

Core data structures and schemas that represent documents, entities, relationships, communities, and associated metadata in the knowledge graph.

### [AI Orchestration & LLM Providers](modules/ai-orchestration-llm-providers)

Abstractions and backends for language models, tokenization, and LLM service management used across indexing and querying.

### [Storage & Vector Store Integrations](modules/storage-vector-store-integrations)

Storage abstractions and concrete implementations for file/blob storage and vector stores (LanceDB, Cosmos, Azure AI Search, etc.).

### [Unified Search App (Demo UI)](modules/unified-search-app-demo-ui)

Demo UI and data loading components for Unified Search, built around the GraphRAG index and results visualization.

