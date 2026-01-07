---
sidebar_position: 241
---

# tests/integration/vector_stores/test_cosmosdb.py

## Overview

CosmosDB integration tests for Graphrag vector stores.

Purpose:
Tests for the CosmosDBVectorStore integration, covering customization, clearing, embedding, and basic vector store operations against a Cosmos DB instance.

Key exports:
- CosmosDBVectorStore: The Cosmos DB backed vector store class under test.
- VectorStoreDocument: Base document type used with the vector store.
- VectorStoreSchemaConfig: Configuration model for vector store schemas.
- test_vector_store_customization
- test_clear
- mock_embedder
- test_vector_store_operations

Summary:
The tests provide integration scenarios for verifying that the CosmosDBVectorStore can be customized, loaded, cleared, and perform standard vector store operations. A mock_embedder is used to produce deterministic embeddings. The test_clear scenario connects to Cosmos DB using WELL_KNOWN_COSMOS_CONNECTION_STRING and database_name \"testclear\" to validate existence before and after clearing.

## Functions

- [`test_vector_store_customization`](../api/functions/tests-integration-vector-stores-test-cosmosdb-test-vector-store-customization)
- [`test_clear`](../api/functions/tests-integration-vector-stores-test-cosmosdb-test-clear)
- [`mock_embedder`](../api/functions/tests-integration-vector-stores-test-cosmosdb-mock-embedder)
- [`test_vector_store_operations`](../api/functions/tests-integration-vector-stores-test-cosmosdb-test-vector-store-operations)

