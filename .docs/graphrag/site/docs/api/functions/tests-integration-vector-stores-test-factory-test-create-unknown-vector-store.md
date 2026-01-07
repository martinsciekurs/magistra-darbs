---
sidebar_position: 447
---

# test_create_unknown_vector_store

**File:** `tests/integration/vector_stores/test_factory.py` (lines 105-110)

## Signature

```python
def test_create_unknown_vector_store()
```

## Description

Test that creating an unknown vector store type raises a ValueError.

Returns:
    None

Raises:
    ValueError: Unknown vector store type: unknown

## Dependencies

This function calls:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`

