---
sidebar_position: 382
---

# get_candidate_relationships

**File:** `graphrag/query/input/retrieval/relationships.py` (lines 57-68)

## Signature

```python
def get_candidate_relationships(
    selected_entities: list[Entity],
    relationships: list[Relationship],
) -> list[Relationship]
```

## Description

Get candidate relationships associated with the selected entities.

Args:
    selected_entities: The selected entities for which to retrieve candidate relationships.
    relationships: The pool of relationships to filter.

Returns:
    list[Relationship]: Relationships involving any of the selected entities, i.e., where the relationship's source or target matches a selected entity's title.

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::get_candidate_context`

