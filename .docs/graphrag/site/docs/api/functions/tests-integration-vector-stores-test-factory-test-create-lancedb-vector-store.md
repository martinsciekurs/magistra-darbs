---
sidebar_position: 454
---

# test_create_lancedb_vector_store

**File:** `tests/integration/vector_stores/test_factory.py` (lines 19-31)

## Signature

```python
def test_create_lancedb_vector_store()
```

## Description

Test creating a LanceDB vector store via the VectorStoreFactory.

Args:
    None: This test takes no input parameters.

Returns:
    None: The test does not return a value.

Raises:
    AssertionError: If the created vector_store is not an instance of LanceDBVectorStore, or if the vector_store's index_name does not match the expected value.

## Dependencies

This function calls:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`

