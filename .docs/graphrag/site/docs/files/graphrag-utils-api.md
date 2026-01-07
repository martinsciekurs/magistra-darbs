---
sidebar_position: 224
---

# graphrag/utils/api.py

## Overview

Utilities for coordinating text and vector-based search, storage creation, and caching across multiple embedding stores. This module exposes a MultiVectorStore abstraction and a set of helper functions that implement end-to-end search workflows, document loading, storage configuration, and cache management used by graphrag to work with multiple embedding stores and backends.

Public API:
- similarity_search_by_text(text, text_embedder, k=10, **kwargs) -&gt; list[VectorStoreSearchResult]
  Performs a text-based similarity search by computing an embedding for the input text with the provided text_embedder. If the embedding is truthy, delegates to similarity_search_by_vector; otherwise returns an empty list.
- load_search_prompt(root_dir, prompt_config) -&gt; str | None
  Load the search prompt from disk if configured; otherwise returns None.
- similarity_search_by_vector(query_embedding, k=10, **kwargs) -&gt; list[VectorStoreSearchResult]
  Performs a vector-based similarity search across all configured embedding stores and merges results.
- search_by_id(id) -&gt; VectorStoreDocument
  Searches for a document by id across the configured vector stores and returns the matching VectorStoreDocument.
- update_context_data(context_data, links) -&gt; Any
  Updates context data with index_name and index_id fields derived from the links mapping.
- MultiVectorStore(...)
  Unified interface that combines multiple vector stores for cross-store search and retrieval. Constructor details depend on embedding stores and index names.
- reformat_context_data(context_data) -&gt; dict
  Reformats context data for all query responses, returning a dict suitable for downstream consumption.
- load_documents(documents, overwrite=True) -&gt; None
  Loads a list of VectorStoreDocument objects into the underlying stores; overwrite controls replacement of existing docs.
- create_storage_from_config(output) -&gt; PipelineStorage
  Creates a storage object from a StorageConfig.
- filter_by_id(include_ids) -&gt; Any
  Builds a query filter to restrict results to the provided IDs.
- connect(**kwargs) -&gt; Any
  Connects to the configured vector storage backends.
- create_cache_from_config(cache, root_dir) -&gt; PipelineCache
  Creates a PipelineCache from a CacheConfig by delegating to CacheFactory, merging the root_dir context.
- truncate(text, max_length) -&gt; str
  Truncates a string to max_length characters, appending a truncation indicator when needed.
- get_embedding_store(config_args, embedding_name) -&gt; BaseVectorStore
  Retrieves and connects the embedding store for the specified embedding name based on the given configuration.

Notes:
- This module imports core types and classes such as BaseVectorStore, VectorStoreDocument, VectorStoreSearchResult, TextEmbedder, PipelineStorage, CacheConfig, StorageConfig, VectorStoreSchemaConfig, and factory classes for storage, cache, and vector stores.

## Classes

- [`MultiVectorStore`](../api/classes/graphrag-utils-api-multivectorstore)

## Functions

- [`similarity_search_by_text`](../api/functions/graphrag-utils-api-similarity-search-by-text)
- [`load_search_prompt`](../api/functions/graphrag-utils-api-load-search-prompt)
- [`similarity_search_by_vector`](../api/functions/graphrag-utils-api-similarity-search-by-vector)
- [`search_by_id`](../api/functions/graphrag-utils-api-search-by-id)
- [`update_context_data`](../api/functions/graphrag-utils-api-update-context-data)
- [`__init__`](../api/functions/graphrag-utils-api-init)
- [`reformat_context_data`](../api/functions/graphrag-utils-api-reformat-context-data)
- [`load_documents`](../api/functions/graphrag-utils-api-load-documents)
- [`create_storage_from_config`](../api/functions/graphrag-utils-api-create-storage-from-config)
- [`filter_by_id`](../api/functions/graphrag-utils-api-filter-by-id)
- [`connect`](../api/functions/graphrag-utils-api-connect)
- [`create_cache_from_config`](../api/functions/graphrag-utils-api-create-cache-from-config)
- [`truncate`](../api/functions/graphrag-utils-api-truncate)
- [`get_embedding_store`](../api/functions/graphrag-utils-api-get-embedding-store)

