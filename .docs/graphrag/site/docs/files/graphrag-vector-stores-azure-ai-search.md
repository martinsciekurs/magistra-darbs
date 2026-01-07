---
sidebar_position: 227
---

# graphrag/vector_stores/azure_ai_search.py

## Overview

Azure AI Search vector store integration for GraphRag.

Purpose: This module provides an Azure AI Search backed vector store class used by GraphRag to perform vector-based and text-based retrieval, as well as loading documents into Azure Cognitive Search indices. It delegates initialization to the base vector store class and is configured via VectorStoreSchemaConfig.

Key exports:
- AzureAISearchVectorStore: Azure AI Search vector store class implementing vector search functionality using Azure Cognitive Search; exposes methods similarity_search_by_vector, connect, similarity_search_by_text, filter_by_id, search_by_id, load_documents; initialization delegates to the base class and config is provided via VectorStoreSchemaConfig.
- similarity_search_by_vector(query_embedding: list[float], k: int = 10, **kwargs: Any) -&gt; list[VectorStoreSearchResult]: Performs a vector-based similarity search using the provided embedding and returns top-k results as VectorStoreSearchResult.
- connect(**kwargs: Any) -&gt; Any: Establishes a connection to the Azure AI Search service; supports url, api_key (uses AzureKeyCredential if provided) and other options like audience and vector_search_profile_name; returns a client or connection handle.
- similarity_search_by_text(text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any) -&gt; list[VectorStoreSearchResult]: Performs a text-based similarity search using the given text and embedder.
- filter_by_id(include_ids: list[str] | list[int]) -&gt; Any: Builds a query filter to filter documents by the provided IDs; returns the filter string or None if no IDs provided.
- __init__(self, vector_store_schema_config: VectorStoreSchemaConfig, **kwargs: Any) -&gt; None: Initializes the Azure AI Search vector store by delegating to the base class constructor.
- search_by_id(id: str) -&gt; VectorStoreDocument: Fetches the document by id from the index; returns a VectorStoreDocument with id, text, vector, and attributes.
- load_documents(self, documents: list[VectorStoreDocument], overwrite: bool = True) -&gt; None: Uploads provided documents to the Azure AI Search index; if overwrite is True, the index is recreated prior to loading; only documents with non-null vectors are uploaded.

Raises:
- Exceptions raised by the base class __init__ are propagated.
- Underlying Azure SDK operations may raise their own exceptions during connection and indexing.

Brief summary: This module wires Azure AI Search into GraphRag as a pluggable vector store, enabling both vector and text search and document loading backed by Azure's search services.

## Classes

- [`AzureAISearchVectorStore`](../api/classes/graphrag-vector-stores-azure-ai-search-azureaisearchvectorstore)

## Functions

- [`similarity_search_by_vector`](../api/functions/graphrag-vector-stores-azure-ai-search-similarity-search-by-vector)
- [`connect`](../api/functions/graphrag-vector-stores-azure-ai-search-connect)
- [`similarity_search_by_text`](../api/functions/graphrag-vector-stores-azure-ai-search-similarity-search-by-text)
- [`filter_by_id`](../api/functions/graphrag-vector-stores-azure-ai-search-filter-by-id)
- [`__init__`](../api/functions/graphrag-vector-stores-azure-ai-search-init)
- [`search_by_id`](../api/functions/graphrag-vector-stores-azure-ai-search-search-by-id)
- [`load_documents`](../api/functions/graphrag-vector-stores-azure-ai-search-load-documents)

