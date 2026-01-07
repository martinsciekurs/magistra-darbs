---
sidebar_position: 411
---

# delete_table_from_storage

**File:** `graphrag/utils/storage.py` (lines 37-39)

## Signature

```python
def delete_table_from_storage(name: str, storage: PipelineStorage) -> None
```

## Description

Delete a table from storage.

Args:
  name (str): The base name of the parquet file to delete, without extension.
  storage (PipelineStorage): The storage backend to delete the parquet file from.

Returns:
  None

Raises:
  Exception: Exceptions raised by the storage backend during the delete operation may propagate.

