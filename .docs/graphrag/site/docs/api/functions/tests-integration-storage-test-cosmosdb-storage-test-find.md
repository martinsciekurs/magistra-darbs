---
sidebar_position: 431
---

# test_find

**File:** `tests/integration/storage/test_cosmosdb_storage.py` (lines 24-67)

## Signature

```python
def test_find()
```

## Description

Test the integration behavior of CosmosDBPipelineStorage.find() in a test container. This test creates a storage instance, verifies an empty result set, adds JSON files, verifies the listing order, reads content, checks existence, deletes a file, and clears storage at the end.

Returns:
    None

Raises:
    None

## Dependencies

This function calls:

- `graphrag/storage/cosmosdb_pipeline_storage.py::CosmosDBPipelineStorage`

