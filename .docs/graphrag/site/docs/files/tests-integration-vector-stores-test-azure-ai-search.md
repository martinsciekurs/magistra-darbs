---
sidebar_position: 240
---

# tests/integration/vector_stores/test_azure_ai_search.py

## Overview

Integration tests for Azure AI Search backed vector store using mocks.

This module defines integration-style tests for the AzureAISearchVectorStore using mocked Azure Cognitive Search clients. It provides fixtures and helpers (vector_store, vector_store_custom, mock_search_client, mock_index_client, sample_documents, none_embedder, mock_embedder) and test cases to verify embedding handling, indexing interactions, and basic vector-store operations without requiring live services. The tests reside in tests/integration/vector_stores/test_azure_ai_search.py and rely on top-level configuration constants TEST_AZURE_AI_SEARCH_URL and TEST_AZURE_AI_SEARCH_KEY (defaulting to "test_api_key").

Public methods:
- vector_store
- none_embedder
- vector_store_custom
- mock_embedder
- test_vector_store_customization
- test_vector_store_operations
- mock_search_client
- sample_documents

## Classes

- [`TestAzureAISearchVectorStore`](../api/classes/tests-integration-vector-stores-test-azure-ai-search-testazureaisearchvectorstore)

## Functions

- [`vector_store`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-vector-store)
- [`none_embedder`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-none-embedder)
- [`vector_store_custom`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-vector-store-custom)
- [`mock_embedder`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-mock-embedder)
- [`test_vector_store_customization`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-test-vector-store-customization)
- [`test_vector_store_operations`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-test-vector-store-operations)
- [`mock_search_client`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-mock-search-client)
- [`sample_documents`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-sample-documents)
- [`test_empty_embedding`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-test-empty-embedding)
- [`mock_index_client`](../api/functions/tests-integration-vector-stores-test-azure-ai-search-mock-index-client)

