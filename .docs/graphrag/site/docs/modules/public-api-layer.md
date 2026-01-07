---
sidebar_position: 1
---

# Public API Layer

Public interfaces for indexing, prompt tuning, and querying GraphRAG. These define the library-facing API used by clients and other subsystems.

## Overview

Public API surface for GraphRAG. This module defines the library-facing entry points that enable clients to index data, generate indexing prompts, and perform queries against GraphRAG. It coordinates the public interfaces exposed by graphrag.api.index, graphrag.api.prompt_tune, and graphrag.api.query, providing a cohesive surface for library users.

Architectural purpose
- Expose and coordinate the GraphRAG public API across indexing, prompt tuning, and querying subsystems.
- Re-export and document the primary entry points so clients interact with a stable surface rather than internal implementations.
- Centralize high-level orchestration while delegating concrete work to the underlying submodules.

Key components and responsibilities
- graphrag.api.index: Utilities to configure and run the GraphRAG indexing pipeline. Responsibilities include resolving the final indexing method (_get_method) and executing the indexing workflow against a GraphRagConfig (build_index).
- graphrag.api.prompt_tune: Utilities to generate indexing prompts for GraphRAG prompt tuning. Exposes generate_indexing_prompts to assemble prompts from domain content, entity types, entity relationships, and community reports.
- graphrag.api.query: Query interfaces for the GraphRAG API. Provides high-level entry points to perform global, local, and drift searches, with both streaming and non-streaming variants, coordinating with a GraphRagConfig and related data structures.

Main entry points / public APIs
- _get_method, build_index (from graphrag.api.index): determine and execute the appropriate indexing workflow.
- generate_indexing_prompts (from graphrag.api.prompt_tune): construct indexing prompts by coordinating multiple prompt-generation components.
- on_context, global_search_streaming, global_search, multi_index_global_search, basic_search, basic_search_streaming, drift_search, drift_search_streaming (from graphrag.api.query): provide diverse query capabilities across contexts, global and drift searches, with streaming and non-streaming variants.

Usage notes / side effects
- APIs rely on GraphRagConfig and related data structures; they may perform I/O, streaming, and data transformations as part of their operations.
- Functions may raise library-defined runtime errors to signal misconfiguration or invalid usage.

Args
- This module does not accept module-level arguments. Client usage occurs via the exported functions described above.

Returns
- This module itself returns no value. Public API functions return results appropriate to their operations (results, streams, or data structures) as implemented in their respective components.

Raises
- RuntimeError and library-specific exceptions defined by graphrag.api may be raised to indicate misconfiguration, invalid inputs, or usage errors.

## Files in this Module

- [`graphrag/api/__init__.py`](../files/graphrag-api-init)
- [`graphrag/api/index.py`](../files/graphrag-api-index)
- [`graphrag/api/prompt_tune.py`](../files/graphrag-api-prompt-tune)
- [`graphrag/api/query.py`](../files/graphrag-api-query)
