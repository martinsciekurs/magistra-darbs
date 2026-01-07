---
sidebar_position: 335
---

# _filter_relationships

**File:** `graphrag/query/context_builder/local_context.py` (lines 232-317)

## Signature

```python
def _filter_relationships(
    selected_entities: list[Entity],
    relationships: list[Relationship],
    top_k_relationships: int = 10,
    relationship_ranking_attribute: str = "rank",
) -> list[Relationship]
```

## Description

Filter and sort relationships based on a set of selected entities and a ranking attribute.

First priority: in-network relationships (i.e. relationships between selected entities). Second priority: out-of-network relationships (i.e. relationships between selected entities and other entities not in the selected set). Within out-of-network relationships, mutual relationships (shared with multiple selected entities) are prioritized by counting links per out-network entity.

Args:
    selected_entities (list[Entity]): The selected entities to consider.
    relationships (list[Relationship]): The pool of relationships to search within.
    top_k_relationships (int): The maximum number of out-of-network relationships to include per selected entity (default 10).
    relationship_ranking_attribute (str): The attribute name used for ranking; defaults to "rank".

Returns:
    list[Relationship]: The filtered and sorted relationships. The result is the concatenation of in-network relationships and the top-ranked out-of-network relationships, truncated to a budget equal to top_k_relationships * len(selected_entities).

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/relationships.py::get_in_network_relationships`
- `graphrag/query/input/retrieval/relationships.py::get_out_network_relationships`

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::build_relationship_context`

