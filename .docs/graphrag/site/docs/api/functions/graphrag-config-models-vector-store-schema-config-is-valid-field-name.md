---
sidebar_position: 50
---

# is_valid_field_name

**File:** `graphrag/config/models/vector_store_schema_config.py` (lines 15-17)

## Signature

```python
def is_valid_field_name(field: str) -> bool
```

## Description

Check if a field name is valid for CosmosDB.

Args:
    field: The field name to validate.

Returns:
    bool: True if the field name is valid for CosmosDB, False otherwise.

## Called By

This function is called by:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig._validate_schema`

