---
sidebar_position: 231
---

# graphrag/vector_stores/lancedb.py

## Overview

LanceDB-backed vector store implementation for GraphRAG.

This module provides a LanceDB-backed implementation of the vector store interface
used by GraphRAG. It stores document embeddings in a LanceDB collection and
supports similarity search by input text or by embedding vector, loading
documents, optional filtering by document IDs, and connecting to a LanceDB
database.

Key exports:
- LanceDBVectorStore: LanceDB-backed vector store class implementing the vector store
  interface. Public methods include similarity_search_by_text, similarity_search_by_vector,
  load_documents, search_by_id, filter_by_id, and connect.
- VectorStoreDocument: type used to represent stored documents.
- VectorStoreSearchResult: type used to represent search results.
- VectorStoreSchemaConfig: configuration model describing the vector store schema.

Brief summary:
The module adapts GraphRAG's vector store abstractions to LanceDB, enabling scalable
embedding storage and retrieval with LanceDB's indexing capabilities.

## Classes

- [`LanceDBVectorStore`](../api/classes/graphrag-vector-stores-lancedb-lancedbvectorstore)

## Functions

- [`similarity_search_by_text`](../api/functions/graphrag-vector-stores-lancedb-similarity-search-by-text)
- [`search_by_id`](../api/functions/graphrag-vector-stores-lancedb-search-by-id)
- [`load_documents`](../api/functions/graphrag-vector-stores-lancedb-load-documents)
- [`similarity_search_by_vector`](../api/functions/graphrag-vector-stores-lancedb-similarity-search-by-vector)
- [`filter_by_id`](../api/functions/graphrag-vector-stores-lancedb-filter-by-id)
- [`__init__`](../api/functions/graphrag-vector-stores-lancedb-init)
- [`connect`](../api/functions/graphrag-vector-stores-lancedb-connect)

