---
sidebar_position: 330
---

# find_nearest_neighbors_by_entity_rank

**File:** `graphrag/query/context_builder/entity_extraction.py` (lines 95-121)

## Signature

```python
def find_nearest_neighbors_by_entity_rank(
    entity_name: str,
    all_entities: list[Entity],
    all_relationships: list[Relationship],
    exclude_entity_names: list[str] | None = None,
    k: int | None = 10,
) -> list[Entity]
```

## Description

Retrieve entities that have direct connections with the target entity, sorted by their rank.

Args:
    entity_name: The name of the target entity.
    all_entities: The list of all Entity objects to search.
    all_relationships: The list of Relationship objects to consider for connections.
    exclude_entity_names: Optional list of entity titles to exclude from results.
    k: Optional number of neighbors to return; if provided, at most k items are returned; if None, all related entities are returned.

Returns:
    list[Entity]: A list of Entity objects representing neighboring entities connected to the target entity, sorted by rank in descending order. If k is provided, at most k entities are returned; otherwise all related entities are returned.

