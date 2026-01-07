---
sidebar_position: 446
---

# test_vector_store_operations

**File:** `tests/integration/vector_stores/test_cosmosdb.py` (lines 25-76)

## Signature

```python
def test_vector_store_operations()
```

## Description

Test basic vector store operations with CosmosDB.

Args:
    None: The function does not accept any parameters.

Returns:
    None: The test does not return a value.

Rises:
    Exception: Exceptions may be raised during test execution.

## Dependencies

This function calls:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`
- `graphrag/vector_stores/base.py::VectorStoreDocument`
- `graphrag/vector_stores/cosmosdb.py::CosmosDBVectorStore`

