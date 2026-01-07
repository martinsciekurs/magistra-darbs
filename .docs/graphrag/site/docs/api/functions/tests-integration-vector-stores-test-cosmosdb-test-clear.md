---
sidebar_position: 444
---

# test_clear

**File:** `tests/integration/vector_stores/test_cosmosdb.py` (lines 79-105)

## Signature

```python
def test_clear()
```

## Description

Test clearing the vector store.

Initializes a CosmosDBVectorStore with index_name "testclear", connects to the Cosmos DB instance using WELL_KNOWN_COSMOS_CONNECTION_STRING and database_name "testclear", loads a VectorStoreDocument, verifies it can be retrieved by its id, clears the store, and asserts that the underlying database no longer exists via _database_exists().

Returns:
None

## Dependencies

This function calls:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`
- `graphrag/vector_stores/base.py::VectorStoreDocument`
- `graphrag/vector_stores/cosmosdb.py::CosmosDBVectorStore`

