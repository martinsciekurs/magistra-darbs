---
sidebar_position: 438
---

# test_create_cosmosdb_storage

**File:** `tests/integration/storage/test_factory.py` (lines 42-50)

## Signature

```python
def test_create_cosmosdb_storage()
```

## Description

Test creating a CosmosDB storage via the StorageFactory.

This test is skipped on non-Windows platforms because the Cosmos DB emulator is only available on Windows runners.

Returns:
    None

Raises:
    AssertionError: If the created storage is not an instance of CosmosDBPipelineStorage.

