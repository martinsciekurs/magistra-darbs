---
sidebar_position: 449
---

# test_get_vector_store_types

**File:** `tests/integration/vector_stores/test_factory.py` (lines 97-102)

## Signature

```python
def test_get_vector_store_types()
```

## Description

Verify that VectorStoreFactory.get_vector_store_types returns a collection containing the values of built-in vector store types LanceDB, AzureAISearch, and CosmosDB.

Args:
    None

Returns:
    List[str] - a collection of built-in vector store type values from VectorStoreFactory.get_vector_store_types(). Note: The test function itself does not return a value; it asserts that the expected values are present in the collection.

Raises:
    None

