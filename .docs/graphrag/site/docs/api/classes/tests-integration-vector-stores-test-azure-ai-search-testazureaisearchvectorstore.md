---
sidebar_position: 48
---

# TestAzureAISearchVectorStore

**File:** `tests/integration/vector_stores/test_azure_ai_search.py`

## Overview

TestAzureAISearchVectorStore: Test suite for AzureAISearchVectorStore integration with Azure Cognitive Search.

This class provides integration-style tests for the AzureAISearchVectorStore using mocked Azure Cognitive Search clients. It validates interaction with the search and indexing layers, embedding handling, and basic vector-store operations without requiring live services. The tests are driven by fixtures that configure a vector store instance, supply embedder behavior, and provide sample documents, while patching the SearchClient and SearchIndexClient to simulate Azure AI Search behavior.

Key fixtures and test coverage:
- vector_store: a configured AzureAISearchVectorStore instance bound to mocked search and index clients.
- none_embedder: a placeholder embedder that returns None to exercise edge cases.
- vector_store_custom: a vector store configured with custom field mappings.
- mock_embedder: a simple embedder returning a fixed embedding vector.
- mock_search_client: a mocked Azure AI Search SearchClient used in tests.
- mock_index_client: a mocked Azure AI Search SearchIndexClient used in tests.
- sample_documents: a small list of VectorStoreDocument objects used for load/search scenarios.
- test_empty_embedding: tests behavior when embedding yields an empty or None vector.
- test_vector_store_customization: tests that custom field mappings are honored during indexing/search.
- test_vector_store_operations: tests basic vector store operations (add/load/search) with mocks.

## Methods

### `vector_store`

```python
def vector_store(self, mock_search_client, mock_index_client)
```

### `none_embedder`

```python
def none_embedder(text: str) -> None
```

### `vector_store_custom`

```python
def vector_store_custom(self, mock_search_client, mock_index_client)
```

### `mock_embedder`

```python
def mock_embedder(text: str) -> list[float]
```

### `test_vector_store_customization`

```python
def test_vector_store_customization(
        self,
        vector_store_custom,
        sample_documents,
        mock_search_client,
        mock_index_client,
    )
```

### `test_vector_store_operations`

```python
def test_vector_store_operations(
        self, vector_store, sample_documents, mock_search_client, mock_index_client
    )
```

### `mock_search_client`

```python
def mock_search_client(self)
```

### `sample_documents`

```python
def sample_documents(self)
```

### `test_empty_embedding`

```python
def test_empty_embedding(self, vector_store, mock_search_client)
```

### `mock_index_client`

```python
def mock_index_client(self)
```

