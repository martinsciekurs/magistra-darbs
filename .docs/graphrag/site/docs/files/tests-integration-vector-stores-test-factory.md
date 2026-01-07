---
sidebar_position: 242
---

# tests/integration/vector_stores/test_factory.py

## Overview

Tests for the Vector Store Factory and related vector store implementations.

Summary:
This module contains integration tests for the VectorStoreFactory, covering creation of built-in vector stores (LanceDB, Azure AI Search, CosmosDB), registration and creation of custom vector stores, and utilities used by the tests. It relies on the Graphrag vector store abstractions and concrete implementations imported in the test module.

Key exports:
- CustomVectorStore: a test utility vector store that forwards initialization kwargs to BaseVectorStore.
- Test functions:
  - test_create_unknown_vector_store
  - test_create_cosmosdb_vector_store
  - test_get_vector_store_types
  - test_register_and_create_custom_vector_store
  - test_create_azure_ai_search_vector_store
  - test_is_supported_type
  - test_register_class_directly_works
  - test_create_lancedb_vector_store

Notes:
The module imports and references VectorStoreType, VectorStoreSchemaConfig, AzureAISearchVectorStore, CosmosDBVectorStore, LanceDBVectorStore, VectorStoreFactory, BaseVectorStore, and VectorStoreDocument for its tests.

## Classes

- [`CustomVectorStore`](../api/classes/tests-integration-vector-stores-test-factory-customvectorstore)

## Functions

- [`similarity_search_by_text`](../api/functions/tests-integration-vector-stores-test-factory-similarity-search-by-text)
- [`test_create_unknown_vector_store`](../api/functions/tests-integration-vector-stores-test-factory-test-create-unknown-vector-store)
- [`filter_by_id`](../api/functions/tests-integration-vector-stores-test-factory-filter-by-id)
- [`connect`](../api/functions/tests-integration-vector-stores-test-factory-connect)
- [`test_create_cosmosdb_vector_store`](../api/functions/tests-integration-vector-stores-test-factory-test-create-cosmosdb-vector-store)
- [`test_get_vector_store_types`](../api/functions/tests-integration-vector-stores-test-factory-test-get-vector-store-types)
- [`test_register_and_create_custom_vector_store`](../api/functions/tests-integration-vector-stores-test-factory-test-register-and-create-custom-vector-store)
- [`test_create_azure_ai_search_vector_store`](../api/functions/tests-integration-vector-stores-test-factory-test-create-azure-ai-search-vector-store)
- [`test_is_supported_type`](../api/functions/tests-integration-vector-stores-test-factory-test-is-supported-type)
- [`test_register_class_directly_works`](../api/functions/tests-integration-vector-stores-test-factory-test-register-class-directly-works)
- [`similarity_search_by_vector`](../api/functions/tests-integration-vector-stores-test-factory-similarity-search-by-vector)
- [`test_create_lancedb_vector_store`](../api/functions/tests-integration-vector-stores-test-factory-test-create-lancedb-vector-store)
- [`__init__`](../api/functions/tests-integration-vector-stores-test-factory-init)
- [`load_documents`](../api/functions/tests-integration-vector-stores-test-factory-load-documents)
- [`search_by_id`](../api/functions/tests-integration-vector-stores-test-factory-search-by-id)

