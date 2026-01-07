---
sidebar_position: 379
---

# get_entity_by_id

**File:** `graphrag/query/input/retrieval/entities.py` (lines 15-20)

## Signature

```python
def get_entity_by_id(entities: dict[str, Entity], value: str) -> Entity | None
```

## Description

Get entity by id.

Args:
    entities: dict[str, Entity]. Mapping of entity IDs to Entity objects.
    value: str. The id value to look up. If value is a valid UUID, also try the same value with dashes removed.

Returns:
    Entity | None. The matching Entity if found, otherwise None.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/entities.py::is_valid_uuid`

## Called By

This function is called by:

- `graphrag/query/context_builder/entity_extraction.py::map_query_to_entities`
- `tests/unit/query/input/retrieval/test_entities.py::test_get_entity_by_id`

