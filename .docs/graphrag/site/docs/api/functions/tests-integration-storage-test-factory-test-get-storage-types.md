---
sidebar_position: 433
---

# test_get_storage_types

**File:** `tests/integration/storage/test_factory.py` (lines 90-96)

## Signature

```python
def test_get_storage_types()
```

## Description

Verify that StorageFactory.get_storage_types returns a collection containing the values of the built-in storage types.

The test asserts that StorageType.file.value, StorageType.memory.value, StorageType.blob.value, and StorageType.cosmosdb.value are present in the returned collection.

Returns:
    None

## Example 💡 Generated

```python
from storage_tests import test_get_storage_types
try:
    test_get_storage_types()
    print("OK: built-ins found")  # success
except AssertionError as e:
    print("FAIL:", e)  # expected if missing
```

