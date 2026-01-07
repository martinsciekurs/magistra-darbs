---
sidebar_position: 380
---

# get_entity_by_key

**File:** `graphrag/query/input/retrieval/entities.py` (lines 23-37)

## Signature

```python
def get_entity_by_key(
    entities: Iterable[Entity], key: str, value: str | int
) -> Entity | None
```

## Description

Get an entity by key from a collection.

Args:
    entities: Iterable[Entity]. The collection of Entity objects to search.
    key: str. The attribute name on the Entity to compare.
    value: str or int. The value to compare against the attribute. If value is a string UUID, also compare the same UUID with dashes removed.

Returns:
    Entity | None: The first matching Entity if found, otherwise None.

Raises:
    AttributeError: If any entity in the iterable does not have the attribute named by 'key'.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/entities.py::is_valid_uuid`

## Called By

This function is called by:

- `graphrag/query/context_builder/entity_extraction.py::map_query_to_entities`
- `tests/unit/query/input/retrieval/test_entities.py::test_get_entity_by_key`

