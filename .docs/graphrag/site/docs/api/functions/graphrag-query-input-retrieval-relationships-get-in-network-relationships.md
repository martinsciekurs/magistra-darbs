---
sidebar_position: 385
---

# get_in_network_relationships

**File:** `graphrag/query/input/retrieval/relationships.py` (lines 14-31)

## Signature

```python
def get_in_network_relationships(
    selected_entities: list[Entity],
    relationships: list[Relationship],
    ranking_attribute: str = "rank",
) -> list[Relationship]
```

## Description

Get all directed relationships between the selected entities, sorted by ranking_attribute.

Args:
  selected_entities: The selected entities to consider.
  relationships: The pool of relationships to search within.
  ranking_attribute: The attribute name used for sorting; defaults to "rank".

Returns:
  list[Relationship]: The relationships where both the source and target are in the selected entities; if more than one such relationship exists, they are returned sorted by ranking_attribute; otherwise the original list is returned.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/relationships.py::sort_relationships_by_rank`

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::_filter_relationships`

