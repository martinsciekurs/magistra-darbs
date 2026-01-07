---
sidebar_position: 428
---

# test_get_creation_date

**File:** `tests/integration/storage/test_cosmosdb_storage.py` (lines 113-133)

## Signature

```python
def test_get_creation_date()
```

## Description

Test that CosmosDBPipelineStorage.get_creation_date returns a correctly formatted creation timestamp.

This test creates a storage, writes a JSON file, retrieves its creation date using get_creation_date, and asserts that the returned string matches the expected format "%Y-%m-%d %H:%M:%S %z" when parsed as a datetime.

Returns:
None
Type: None

## Dependencies

This function calls:

- `graphrag/storage/cosmosdb_pipeline_storage.py::CosmosDBPipelineStorage`

