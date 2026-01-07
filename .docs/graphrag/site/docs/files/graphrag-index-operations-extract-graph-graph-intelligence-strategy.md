---
sidebar_position: 71
---

# graphrag/index/operations/extract_graph/graph_intelligence_strategy.py

## Overview

Graph intelligence strategy utilities for graph-based extraction in Graphrag. This module coordinates a language model, a graph extractor, and a caching layer to produce an EntityExtractionResult from input documents and a requested set of entity types. It provides two entry points used by the extraction workflow:
- run_extract_graph(model, docs, entity_types, args) (async)
- run_graph_intelligence(docs, entity_types, cache, args)

Key exports:
- run_extract_graph: coroutine to run the entity extraction chain.
- run_graph_intelligence: function to perform graph intelligence-based extraction.

Summary:
Wires together GraphExtractor, language model interfaces, and PipelineCache to perform entity extraction and graph intelligence-based enhancements, returning an EntityExtractionResult with extracted entities and related metadata.

Functions:

run_extract_graph
- Description: Asynchronous entry point that orchestrates the extraction chain using the provided language model, documents, target entity types, and strategy configuration.
- Args:
  - model: ChatModel - The chat model instance used to invoke the extraction.
  - docs: list[Document] - The input documents from which to extract entities.
  - entity_types: EntityTypes - The set of entity types to extract and consider for graph construction.
  - args: StrategyConfig - Strategy configuration, including prompts, llm settings, and defaults.
- Returns: EntityExtractionResult - The result containing extracted entities and metadata.
- Raises: ValueError, TypeError, RuntimeError, KeyError (as appropriate for invalid input or failure in model/cache).

run_graph_intelligence
- Description: Synchronous entry point that applies graph intelligence enhancements to the document set, using the entity types, a cache, and strategy configuration.
- Args:
  - docs: list[Document] - The input documents to process.
  - entity_types: EntityTypes - The types of entities to extract.
  - cache: PipelineCache - Cache instance used for language model interactions and intermediate results.
  - args: StrategyConfig - Strategy configuration, including prompts and settings.
- Returns: EntityExtractionResult - The result including entities and related metadata after graph intelligence processing.
- Raises: ValueError, TypeError, RuntimeError, KeyError (as appropriate for invalid input or failure in model/cache).

Edge cases:
- Empty or None docs should be handled gracefully, typically returning an empty or minimal EntityExtractionResult.
- Unsupported or missing entity types should raise a clear error.
- Failures in the language model or cache should surface as RuntimeError with contextual information.

Notes:
- The docstring aligns with actual code signatures and imports; the run_extract_graph function is asynchronous, and both functions return EntityExtractionResult.

## Functions

- [`run_extract_graph`](../api/functions/graphrag-index-operations-extract-graph-graph-intelligence-strategy-run-extract-graph)
- [`run_graph_intelligence`](../api/functions/graphrag-index-operations-extract-graph-graph-intelligence-strategy-run-graph-intelligence)

