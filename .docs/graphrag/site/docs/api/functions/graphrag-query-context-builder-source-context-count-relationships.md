---
sidebar_position: 338
---

# count_relationships

**File:** `graphrag/query/context_builder/source_context.py` (lines 82-100)

## Signature

```python
def count_relationships(
    entity_relationships: list[Relationship], text_unit: TextUnit
) -> int
```

## Description

Count the number of relationships of the selected entity that are associated with the text unit.

Args:
    entity_relationships: list[Relationship]
        The relationships for the selected entity.
    text_unit: TextUnit
        The text unit for which to count related relationships.

Returns:
    int
        The number of relationships in entity_relationships that are associated with the given text_unit. If the text_unit has no relationship_ids, this is the count of relationships whose text_unit_ids contain the text_unit's id; otherwise it is the count of relationships whose id appears in text_unit.relationship_ids.

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_text_unit_context`

