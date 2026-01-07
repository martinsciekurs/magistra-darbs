---
sidebar_position: 5
---

# API Reference

Public interfaces for indexing, prompt tuning, and querying GraphRAG are organized under the Public API Layer. These interfaces define the library-facing API used by clients and subsystems. The primary entry points are:

- Indexing API (graphrag/graphrag/api/index.py): Public interfaces for ingesting documents, creating text units, and building the knowledge graph index. This layer abstracts the end-to-end indexing workflow so that researchers and applications can programmatically drive indexing with custom data sources.
- Prompt Tuning API (graphrag/graphrag/api/prompt_tune.py): Public interfaces for generating and applying prompt-tuning configurations. This enables domain-specific tuning of prompts used during query time or during index-time prompts.
- Query API (graphrag/graphrag/api/query.py): Public interfaces for composing and executing questions against the knowledge graph. This layer orchestrates the creation of retrieval contexts, optional global/local DRIFT reasoning, and LLM-backed answers.

Usage patterns (high level)
- Initialize or obtain an API client, configure data sources, and call the indexing API to ingest documents and build the graph.
- Provide tuning configurations or prompts, and use the prompt tuning API to adapt prompts for specific domains.
- Use the query API to run questions against the index, leveraging context from the graph and vector store for augmented reasoning.

Notes
- The exact function names and signatures are provided in the corresponding files: graphrag/graphrag/api/index.py, graphrag/graphrag/api/prompt_tune.py, graphrag/graphrag/api/query.py. This section documents the public API surface and its intended usage rather than concrete implementation details.
