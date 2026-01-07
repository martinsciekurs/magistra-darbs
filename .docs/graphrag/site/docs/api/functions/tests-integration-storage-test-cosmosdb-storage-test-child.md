---
sidebar_position: 430
---

# test_child

**File:** `tests/integration/storage/test_cosmosdb_storage.py` (lines 70-80)

## Signature

```python
def test_child()
```

## Description

Test that a child CosmosDBPipelineStorage can be created from a parent storage.

The test initializes a CosmosDBPipelineStorage, uses the child() method to obtain a child storage, and asserts that the returned object is a CosmosDBPipelineStorage.

Returns:
    None

## Dependencies

This function calls:

- `graphrag/storage/cosmosdb_pipeline_storage.py::CosmosDBPipelineStorage`

