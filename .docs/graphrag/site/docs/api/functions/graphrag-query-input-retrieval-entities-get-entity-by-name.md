---
sidebar_position: 378
---

# get_entity_by_name

**File:** `graphrag/query/input/retrieval/entities.py` (lines 40-42)

## Signature

```python
def get_entity_by_name(entities: Iterable[Entity], entity_name: str) -> list[Entity]
```

## Description

Get entities by name.

Args:
    entities: Iterable[Entity], the collection of entities to search.
    entity_name: str, the name to match against the entity.title attribute.

Returns:
    list[Entity], a list of entities whose title matches the given name.

Raises:
    AttributeError: if any entity in entities does not have a 'title' attribute.

## Called By

This function is called by:

- `graphrag/query/context_builder/entity_extraction.py::map_query_to_entities`

