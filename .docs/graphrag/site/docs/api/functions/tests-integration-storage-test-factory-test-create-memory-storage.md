---
sidebar_position: 439
---

# test_create_memory_storage

**File:** `tests/integration/storage/test_factory.py` (lines 59-62)

## Signature

```python
def test_create_memory_storage()
```

## Description

Test creating a memory storage via StorageFactory using StorageType.memory.value with an empty kwargs dict, and verify the result is a MemoryPipelineStorage instance.

Args:
    None

Returns:
    None

Raises:
    AssertionError: if the created storage is not an instance of MemoryPipelineStorage.

