---
sidebar_position: 229
---

# graphrag/vector_stores/cosmosdb.py

## Overview

Cosmos DB backed vector store for GraphRAG.

This module implements a Cosmos DB-backed storage backend that conforms to GraphRAG's vector store interface. It stores document vectors and associated metadata in Azure Cosmos DB, supports loading documents, text-based similarity search, and vector-based similarity search, and manages the creation and deletion of the underlying database and container along with indexing configuration.

Public API
- CosmosDBVectorStore(vector_store_schema_config: VectorStoreSchemaConfig, **kwargs: Any) -&gt; None
  Initialize the Cosmos DB vector store using the provided schema configuration.

- connect(connection_string: str | None = None, url: str | None = None, database_name: str, **kwargs: Any) -&gt; None
  Establish a connection to the Cosmos DB account and initialize internal clients. If neither connection_string nor url is provided, a ValueError is raised. May raise CosmosHttpResponseError on HTTP errors.

- load_documents(documents: list[VectorStoreDocument], overwrite: bool = True) -&gt; None
  Load or upsert the given documents into the store. If overwrite is True, the container may be reset prior to loading. Documents with non-null vectors are stored, with fields mapped according to the configured id_field, vector_field, text_field, and attributes_field.

- similarity_search_by_text(text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any) -&gt; list[VectorStoreSearchResult]
  Perform a text-based similarity search and return up to k matching results as VectorStoreSearchResult objects.

- similarity_search_by_vector(query_embedding: list[float], k: int = 10, **kwargs: Any) -&gt; list[VectorStoreSearchResult]
  Perform a vector-based similarity search against the stored embeddings and return up to k top results as VectorStoreSearchResult objects.

- search_by_id(id: str) -&gt; VectorStoreDocument
  Retrieve a document by its identifier, returning its id, vector, text, and attributes.

- clear() -&gt; None
  Delete the vector store container and the database to reset the store.

Notes on internals (implementation detail, not required for typical usage)
- Internal helpers such as _database_exists, _container_exists, _create_database, _create_container, _delete_database, _delete_container, filter_by_id, and cosine_similarity support lifecycle management and search operations. These are intended for internal use and may change without breaking the public API.

Credentials and configuration
- VectorStoreSchemaConfig (graphrag.config.models.vector_store_schema_config.VectorStoreSchemaConfig) defines mappings for id_field, vector_field, text_field, and attributes_field, as well as the database and container naming and indexing options used by Cosmos DB.
- Cosmos DB credentials: a Cosmos DB account accessible via account URL or a connection string. Use connect(connection_string=...) or connect(url=..., database_name=...) accordingly. Authentication is typically performed via DefaultAzureCredential or other Azure Identity credentials in your environment.

Error handling
- CosmosHttpResponseError is raised for HTTP or Cosmos DB service errors.
- ValueError is raised for invalid arguments (for example, missing required connection details).

Usage example
- Instantiate: store = CosmosDBVectorStore(vector_store_schema_config)
- Connect: store.connect(url="https://&lt;account&gt;.documents.azure.com:443/", database_name="&lt;db&gt;")
- Load documents: store.load_documents(documents, overwrite=True)
- Text search: results = store.similarity_search_by_text("query text", text_embedder, k=5)
- Vector search: results = store.similarity_search_by_vector([0.12, -0.34, ...], k=5)
- Retrieve by id: doc = store.search_by_id("doc1")
- Clear store: store.clear()

## Classes

- [`CosmosDBVectorStore`](../api/classes/graphrag-vector-stores-cosmosdb-cosmosdbvectorstore)

## Functions

- [`_database_exists`](../api/functions/graphrag-vector-stores-cosmosdb-database-exists)
- [`similarity_search_by_text`](../api/functions/graphrag-vector-stores-cosmosdb-similarity-search-by-text)
- [`_delete_database`](../api/functions/graphrag-vector-stores-cosmosdb-delete-database)
- [`filter_by_id`](../api/functions/graphrag-vector-stores-cosmosdb-filter-by-id)
- [`__init__`](../api/functions/graphrag-vector-stores-cosmosdb-init)
- [`cosine_similarity`](../api/functions/graphrag-vector-stores-cosmosdb-cosine-similarity)
- [`_create_database`](../api/functions/graphrag-vector-stores-cosmosdb-create-database)
- [`_create_container`](../api/functions/graphrag-vector-stores-cosmosdb-create-container)
- [`connect`](../api/functions/graphrag-vector-stores-cosmosdb-connect)
- [`load_documents`](../api/functions/graphrag-vector-stores-cosmosdb-load-documents)
- [`_container_exists`](../api/functions/graphrag-vector-stores-cosmosdb-container-exists)
- [`search_by_id`](../api/functions/graphrag-vector-stores-cosmosdb-search-by-id)
- [`_delete_container`](../api/functions/graphrag-vector-stores-cosmosdb-delete-container)
- [`clear`](../api/functions/graphrag-vector-stores-cosmosdb-clear)
- [`similarity_search_by_vector`](../api/functions/graphrag-vector-stores-cosmosdb-similarity-search-by-vector)

