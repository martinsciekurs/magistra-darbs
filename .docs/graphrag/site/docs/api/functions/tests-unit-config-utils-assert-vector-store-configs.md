---
sidebar_position: 487
---

# assert_vector_store_configs

**File:** `tests/unit/config/utils.py` (lines 109-126)

## Signature

```python
def assert_vector_store_configs(
    actual: dict[str, VectorStoreConfig],
    expected: dict[str, VectorStoreConfig],
)
```

## Description

Assert that two dictionaries of VectorStoreConfig objects are equal.

Args:
    actual: dict[str, VectorStoreConfig]
        Actual mapping of vector store names to VectorStoreConfig objects to validate.
    expected: dict[str, VectorStoreConfig]
        Expected mapping of vector store names to VectorStoreConfig objects.

Returns:
    None
        This function does not return a value; it raises AssertionError on mismatches.

Raises:
    AssertionError
        If actual and expected do not match in type, length, keys, or any VectorStoreConfig attributes
        (type, db_uri, url, api_key, audience, container_name, overwrite, database_name).

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

