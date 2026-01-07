---
sidebar_position: 9
---

# Storage & Vector Stores

GraphRAG uses pluggable storage backends for both pipeline data and results, along with vector stores that enable semantic retrieval in tandem with the knowledge graph.

Storage abstractions
- File-based storage: A filesystem-backed pipeline storage that manages a root directory for artifacts and outputs.
- Blob storage: BlobPipelineStorage for cloud-based blob storage integration.
- Factory and adapters: A storage factory to create endpoints based on configuration, allowing users to plug in their own storage backend.

Vector stores and retrieval backends
- LanceDB: Local vector store backend optimized for fast experimentation and small to medium datasets.
- Cosmos DB: Cloud-based vector store integration for scalable deployments.
- Azure AI Search: Cloud-based search service integration for hybrid text/semantic search.

Where these are defined
- graphrag/storage/file_pipeline_storage.py
- graphrag/graphrag/storage/blob_pipeline_storage.py
- graphrag/graphrag/vector_stores/__init__.py
- graphrag/graphrag/vector_stores/factory.py
- graphrag/graphrag/vector_stores/lancedb.py
- graphrag/graphrag/vector_stores/cosmosdb.py
- graphrag/graphrag/vector_stores/azure_ai_search.py

Configuration hints
- Storage type and base_dir are configured in settings.yaml or environment variables as part of the Storage configuration section.
- Vector store configuration is similarly supplied as part of the index/query settings, enabling the system to write embeddings directly to the chosen vector store during indexing.
