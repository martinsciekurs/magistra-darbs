---
sidebar_position: 377
---

# is_valid_uuid

**File:** `graphrag/query/input/retrieval/entities.py` (lines 95-102)

## Signature

```python
def is_valid_uuid(value: str) -> bool
```

## Description

Determine if a string is a valid UUID.

Args:
    value: str. The string to validate as a UUID.

Returns:
    bool: True if the string is a valid UUID, False otherwise.

## Called By

This function is called by:

- `graphrag/query/input/retrieval/entities.py::get_entity_by_id`
- `graphrag/query/input/retrieval/entities.py::get_entity_by_key`

