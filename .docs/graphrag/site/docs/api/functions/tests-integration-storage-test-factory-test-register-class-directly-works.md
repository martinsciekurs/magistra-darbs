---
sidebar_position: 432
---

# test_register_class_directly_works

**File:** `tests/integration/storage/test_factory.py` (lines 104-160)

## Signature

```python
def test_register_class_directly_works()
```

## Description

Test that StorageFactory allows direct class registration and can instantiate the registered class.

This test registers a concrete CustomStorage class directly with StorageFactory, verifies it is registered and reported as supported, and creates an instance to ensure the registration path works.

Args:
- None: This test has no parameters.

Returns:
- None: This test does not return a value; it uses assertions to verify StorageFactory behavior.

Notes:
- Scope: direct class registration via StorageFactory for StorageFactory behavior verification.

## Example 💡 Generated

```python
from module import test_register_class_directly_works
# Import and run the test to verify StorageFactory path
test_register_class_directly_works()  # Run; should pass
```

