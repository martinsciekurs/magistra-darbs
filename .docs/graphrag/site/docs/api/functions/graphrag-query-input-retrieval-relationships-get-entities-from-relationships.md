---
sidebar_position: 384
---

# get_entities_from_relationships

**File:** `graphrag/query/input/retrieval/relationships.py` (lines 71-78)

## Signature

```python
def get_entities_from_relationships(
    relationships: list[Relationship], entities: list[Entity]
) -> list[Entity]
```

## Description

Get all entities that are associated with the selected relationships.

Args:
    relationships (list[Relationship]): The relationships to inspect.
    entities (list[Entity]): The pool of entities to filter from.

Returns:
    list[Entity]: The subset of entities whose title matches the source or target of any relationship in relationships.

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::get_candidate_context`

