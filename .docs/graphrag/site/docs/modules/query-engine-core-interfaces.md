---
sidebar_position: 4
---

# Query Engine Core & Interfaces

Query-time context construction, data retrieval, and LLM orchestration utilities used to answer questions against the knowledge graph.

## Overview

Query Engine Core & Interfaces for Graphrag: query-time context construction, data retrieval, and LLM orchestration utilities used to answer questions against the knowledge graph.

Architectural overview
- Provides a cohesive framework to construct DRIFT-ready context, extract and map entities from queries, orchestrate structured global search workflows, and support LLM-based answer generation against a knowledge graph.
- Comprises builders, utilities, and prompts that together enable end-to-end query answering from context construction to result synthesis. It relies on pandas for context representation (DataFrame) where appropriate.

Key components and responsibilities
- graphrag/query/context_builder/builders.py: Module for constructing DRIFT context used to prime downstream search actions for a given query. This module defines an abstract interface and concrete builders that assemble the context required by DRIFT-based search processes. It relies on pandas for context representation (DataFrame).
- graphrag/query/context_builder/local_context.py: Utilities for constructing context data for graph-based prompt systems. Purpose: This module provides helper functions to assemble context data tables (entities, covariates, and relationships) into text blocks and structured DataFrames suitable for inclusion in system prompts.
  Functions: build_entity_context, build_covariates_context, get_candidate_context, _filter_relationships, build_relationship_context
- graphrag/query/context_builder/entity_extraction.py: Graphrag query context: entity extraction utilities for mapping user queries to Entity objects using vector stores and a relationship graph. Overview This module provides utilities to extract entities from a user query and map them to Entity objects within Graphrag's query context.
  Functions: from_string, find_nearest_neighbors_by_entity_rank, map_query_to_entities
  Classes: EntityVectorStoreKey
- graphrag/query/structured_search/global_search/search.py: Module implementing a structured global search workflow that orchestrates parallel batches of community report summaries, maps each batch to an answer, and reduces the results into a final user-facing response using a language model. This module exposes the GlobalSearch class, which coordinates initialization, streaming, and reduction of search results.
  Functions: __init__, search, _map_response_single_batch, _stream_reduce_response, stream_search, _reduce_response, _parse_search_response
  Classes: GlobalSearch
- graphrag/query/llm/text_utils.py: Utilities for batching, JSON cleaning/parsing, and token-based text chunking to support LLM workflows. This module provides helpers to: - batch data into fixed-size chunks for batched LLM prompts or processing (batched) - repair and parse JSON-like content produced by language models into native Py...
  Functions: batched, try_parse_json_object, chunk_text
- graphrag/prompts/query/global_search_knowledge_system_prompt.py: Prompt definition for the knowledge system in global search scenarios.
- graphrag/prompts/query/local_search_system_prompt.py: Prompt definition for local search system prompts.
- graphrag/prompts/query/question_gen_system_prompt.py: Prompt definition for question generation to guide LLMs.

Main entry points / public APIs
- Context builders
  - DRIFTContextBuilder, BasicContextBuilder, GlobalContextBuilder, LocalContextBuilder (graphrag/query/context_builder/builders.py)
  - build_context (as part of the DRIFT context construction workflow)
- Local context utilities
  - build_entity_context, build_covariates_context, get_candidate_context, _filter_relationships, build_relationship_context (graphrag/query/context_builder/local_context.py)
- Entity extraction and mapping
  - from_string, find_nearest_neighbors_by_entity_rank, map_query_to_entities (graphrag/query/context_builder/entity_extraction.py)
  - EntityVectorStoreKey (graphrag/query/context_builder/entity_extraction.py)
- Structured global search orchestration
  - GlobalSearch class (graphrag/query/structured_search/global_search/search.py)
  - __init__, search, stream_search, _parse_search_response, _map_response_single_batch, _reduce_response, _stream_reduce_response (graphrag/query/structured_search/global_search/search.py)
- LLM text utilities
  - batched, try_parse_json_object, chunk_text (graphrag/query/llm/text_utils.py)
- Prompts
  - graphrag/prompts/query/global_search_knowledge_system_prompt.py
  - graphrag/prompts/query/local_search_system_prompt.py
  - graphrag/prompts/query/question_gen_system_prompt.py

This module serves as the architectural hub for the Graphrag query experience, wiring together context construction, entity grounding, structured search orchestration, and LLM-driven response synthesis for answering questions against the knowledge graph.

## Files in this Module

- [`graphrag/query/__init__.py`](../files/graphrag-query-init)
- [`graphrag/query/context_builder/builders.py`](../files/graphrag-query-context-builder-builders)
- [`graphrag/query/context_builder/local_context.py`](../files/graphrag-query-context-builder-local-context)
- [`graphrag/query/context_builder/entity_extraction.py`](../files/graphrag-query-context-builder-entity-extraction)
- [`graphrag/query/structured_search/global_search/search.py`](../files/graphrag-query-structured-search-global-search-search)
- [`graphrag/query/llm/text_utils.py`](../files/graphrag-query-llm-text-utils)
- [`graphrag/prompts/query/global_search_knowledge_system_prompt.py`](../files/graphrag-prompts-query-global-search-knowledge-system-prompt)
- [`graphrag/prompts/query/local_search_system_prompt.py`](../files/graphrag-prompts-query-local-search-system-prompt)
- [`graphrag/prompts/query/question_gen_system_prompt.py`](../files/graphrag-prompts-query-question-gen-system-prompt)
