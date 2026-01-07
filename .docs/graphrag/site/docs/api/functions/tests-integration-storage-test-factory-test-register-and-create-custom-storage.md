---
sidebar_position: 437
---

# test_register_and_create_custom_storage

**File:** `tests/integration/storage/test_factory.py` (lines 65-87)

## Signature

```python
def test_register_and_create_custom_storage()
```

## Description

Test registering and creating a custom storage type.

This test registers a custom storage type named "custom" using StorageFactory.register with a factory function, creates storage via StorageFactory.create_storage, and verifies that the factory was invoked and that the returned storage is the expected instance. It also asserts that the created instance has initialized set to True, and that "custom" appears in StorageFactory.get_storage_types() and is reported as a supported type by StorageFactory.is_supported_type.

Returns: None

