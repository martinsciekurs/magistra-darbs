---
sidebar_position: 451
---

# test_create_azure_ai_search_vector_store

**File:** `tests/integration/vector_stores/test_factory.py` (lines 35-47)

## Signature

```python
def test_create_azure_ai_search_vector_store()
```

## Description

Test creating an Azure AI Search vector store using the VectorStoreFactory.

Args:
    None: The test function has no input parameters.

Returns:
    None: The test does not return a value.

Raises:
    AssertionError: If the created vector_store is not an instance of AzureAISearchVectorStore.

## Dependencies

This function calls:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`

