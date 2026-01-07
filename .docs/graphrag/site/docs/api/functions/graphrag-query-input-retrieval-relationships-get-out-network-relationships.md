---
sidebar_position: 386
---

# get_out_network_relationships

**File:** `graphrag/query/input/retrieval/relationships.py` (lines 34-54)

## Signature

```python
def get_out_network_relationships(
    selected_entities: list[Entity],
    relationships: list[Relationship],
    ranking_attribute: str = "rank",
) -> list[Relationship]
```

## Description

Get relationships that connect the selected entities to other entities, considering both directions (outgoing from and incoming to the selected set). The other endpoint may lie outside the selected set. The resulting relationships are sorted by the specified ranking_attribute.

Args:
  selected_entities (list[Entity]): The selected entities; used as one end of the relationships to consider.
  relationships (list[Relationship]): The pool of relationships to search within.
  ranking_attribute (str): The attribute name used for sorting; defaults to "rank".

Returns:
  list[Relationship]: The relationships where either the source is in the selected_entities and the target is outside the selected set, or the target is in the selected_entities and the source is outside the selected set; i.e., relationships connected to the selected entities but with the other endpoint possibly outside the set. The list is sorted by ranking_attribute.

Notes:
  If the input is empty, an empty list is returned.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/relationships.py::sort_relationships_by_rank`

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::_filter_relationships`

