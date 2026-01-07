---
sidebar_position: 228
---

# graphrag/vector_stores/base.py

## Overview

Base vector store abstraction used by GraphRAG to store and retrieve documents via vector representations.

Purpose
- Provide the core interface and common lifecycle for vector stores used by GraphRAG. Concrete backends should implement storage and search logic for both vector and text queries, while sharing initialization surface and metadata.

Key exports
- BaseVectorStore: Abstract base class defining the interface for vector store backends, including similarity_search_by_vector, similarity_search_by_text, connect, filter_by_id, load_documents, search_by_id, and __init__.

Summary
- This module defines the BaseVectorStore and the associated schema/config types it relies on, enabling consistent integration of different vector store implementations.

Args
- None: This module does not take parameters.

Returns
- None: This module does not return a value.

Raises
- None: This module does not raise exceptions on its own.

## Classes

- [`BaseVectorStore`](../api/classes/graphrag-vector-stores-base-basevectorstore)

## Functions

- [`similarity_search_by_vector`](../api/functions/graphrag-vector-stores-base-similarity-search-by-vector)
- [`connect`](../api/functions/graphrag-vector-stores-base-connect)
- [`filter_by_id`](../api/functions/graphrag-vector-stores-base-filter-by-id)
- [`load_documents`](../api/functions/graphrag-vector-stores-base-load-documents)
- [`__init__`](../api/functions/graphrag-vector-stores-base-init)
- [`search_by_id`](../api/functions/graphrag-vector-stores-base-search-by-id)
- [`similarity_search_by_text`](../api/functions/graphrag-vector-stores-base-similarity-search-by-text)

