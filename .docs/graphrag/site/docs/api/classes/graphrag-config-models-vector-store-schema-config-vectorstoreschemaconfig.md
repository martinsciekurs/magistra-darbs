---
sidebar_position: 76
---

# VectorStoreSchemaConfig

**File:** `graphrag/config/models/vector_store_schema_config.py`

## Overview

VectorStoreSchemaConfig defines and validates the mapping of schema field names used by the vector store.

Purpose: Centralizes the configuration of field names for id, vector, text, and attributes and provides validation to ensure field names are safe and valid.

Key attributes:
- id_field: The field name used for the unique identifier in the schema.
- vector_field: The field name containing the vector data.
- text_field: The field name containing associated text data.
- attributes_field: The field name containing additional attributes.

Args:
- id_field: The field name used as the unique identifier (must be a valid identifier).
- vector_field: The field name for the vector data (must be a valid identifier).
- text_field: The field name for the associated text (must be a valid identifier).
- attributes_field: The field name for additional attributes (must be a valid identifier).

Returns:
- None

Raises:
- ValueError: If an unsafe or invalid field name is encountered during validation.

## Methods

### `_validate_model`

```python
def _validate_model(self)
```

### `_validate_schema`

```python
def _validate_schema(self) -> None
```

