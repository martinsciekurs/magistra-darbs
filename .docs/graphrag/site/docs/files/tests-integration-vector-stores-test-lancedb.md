---
sidebar_position: 243
---

# tests/integration/vector_stores/test_lancedb.py

## Overview

LanceDB-backed vector store integration tests.

Purpose:
This module contains integration tests for the LanceDBVectorStore implementation, exercising creation and deletion of collections, loading documents, vector similarity searches, filtering, and basic vector store operations in an integration test context.

Key exports:
- TestLanceDBVectorStore: Integration test class for LanceDBVectorStore.
- mock_embedder(text) -&gt; list[float]: Deterministic embedding function used by tests.

Summary:
The TestLanceDBVectorStore class provides test methods such as sample_documents and sample_documents_categories to generate test data, along with tests like test_empty_collection, test_vector_store_customization, test_filter_search, and test_vector_store_operations to validate vector store behavior.

## Classes

- [`TestLanceDBVectorStore`](../api/classes/tests-integration-vector-stores-test-lancedb-testlancedbvectorstore)

## Functions

- [`sample_documents_categories`](../api/functions/tests-integration-vector-stores-test-lancedb-sample-documents-categories)
- [`sample_documents`](../api/functions/tests-integration-vector-stores-test-lancedb-sample-documents)
- [`test_empty_collection`](../api/functions/tests-integration-vector-stores-test-lancedb-test-empty-collection)
- [`test_vector_store_customization`](../api/functions/tests-integration-vector-stores-test-lancedb-test-vector-store-customization)
- [`test_filter_search`](../api/functions/tests-integration-vector-stores-test-lancedb-test-filter-search)
- [`test_vector_store_operations`](../api/functions/tests-integration-vector-stores-test-lancedb-test-vector-store-operations)
- [`mock_embedder`](../api/functions/tests-integration-vector-stores-test-lancedb-mock-embedder)

