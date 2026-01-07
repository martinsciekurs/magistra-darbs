---
sidebar_position: 7
---

# Storage & Vector Store Integrations

Storage abstractions and concrete implementations for file/blob storage and vector stores (LanceDB, Cosmos, Azure AI Search, etc.).

## Overview

Storage and vector store integrations for GraphRAG.

Architectural purpose
Provide pluggable storage backends for pipeline data and results, including filesystem-based and Azure Blob Storage-backed storage, together with vector store backends that support text- and vector-based retrieval for GraphRAG.

Key components and responsibilities
- graphrag.storage.file_pipeline_storage.FilePipelineStorage: filesystem-backed implementation of the PipelineStorage interface. Manages a root directory (creating it if necessary) and offers operations to read, write, clear, list keys, and filter or traverse items.
- graphrag.storage.blob_pipeline_storage.BlobPipelineStorage: Azure Blob Storage-backed implementation of the PipelineStorage interface used to cache pipeline results and data. Stores dataframe exports as JSON (and Parquet) where applicable; provides helpers like _abfs_url, _set_df_json, _set_df_parquet, and operations such as find, clear, get, and _create_container.
- graphrag.vector_stores.lancedb.LanceDBVectorStore: LanceDB-backed vector store for GraphRAG. Supports similarity search by text and by vector, loading documents, filtering by id, and connection management.
- graphrag.vector_stores.cosmosdb.CosmosDBVectorStore: Cosmos DB-backed vector store. Supports text- and vector-based retrieval, loading documents, filtering by id, and internal utilities like cosine_similarity, _create_database, _create_container.
- graphrag.vector_stores.azure_ai_search.AzureAISearchVectorStore: Azure AI Search-backed vector store. Supports similarity search by vector and text, loading documents, and id-based filtering; connects to the Azure Cognitive Search index.

- graphrag.vector_stores.factory.VectorStoreFactory: registry-based factory to construct vector store instances from registered implementations. Maintains a registry mapping vector_store_type keys to creator callables. Provides create_vector_store, get_vector_store_types, is_supported_type, and register.

Main entry points / public APIs
- FilePipelineStorage and BlobPipelineStorage as storage backends for GraphRAG pipelines.
- LanceDBVectorStore, CosmosDBVectorStore, AzureAISearchVectorStore as concrete vector store implementations.
- VectorStoreFactory (and its public methods) to instantiate vector stores from registered types.

## Files in this Module

- [`graphrag/storage/__init__.py`](../files/graphrag-storage-init)
- [`graphrag/storage/file_pipeline_storage.py`](../files/graphrag-storage-file-pipeline-storage)
- [`graphrag/storage/blob_pipeline_storage.py`](../files/graphrag-storage-blob-pipeline-storage)
- [`graphrag/vector_stores/__init__.py`](../files/graphrag-vector-stores-init)
- [`graphrag/vector_stores/factory.py`](../files/graphrag-vector-stores-factory)
- [`graphrag/vector_stores/lancedb.py`](../files/graphrag-vector-stores-lancedb)
- [`graphrag/vector_stores/cosmosdb.py`](../files/graphrag-vector-stores-cosmosdb)
- [`graphrag/vector_stores/azure_ai_search.py`](../files/graphrag-vector-stores-azure-ai-search)
