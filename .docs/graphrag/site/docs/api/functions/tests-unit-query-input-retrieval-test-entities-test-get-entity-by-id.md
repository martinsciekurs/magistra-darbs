---
sidebar_position: 557
---

# test_get_entity_by_id

**File:** `tests/unit/query/input/retrieval/test_entities.py` (lines 11-89)

## Signature

```python
def test_get_entity_by_id()
```

## Description

Get entity by id.

Args:
    entities (dict[str, Entity]): Mapping of entity IDs to Entity objects.
    value (str): The id value to look up. If value is a valid UUID, also try the same value with dashes removed.

Returns:
    Entity | None: The matching Entity if found, otherwise None.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/data_model/entity.py::Entity`
- `graphrag/query/input/retrieval/entities.py::get_entity_by_id`

