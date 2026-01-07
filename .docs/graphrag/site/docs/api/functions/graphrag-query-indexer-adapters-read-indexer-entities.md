---
sidebar_position: 348
---

# read_indexer_entities

**File:** `graphrag/query/indexer_adapters.py` (lines 139-178)

## Signature

```python
def read_indexer_entities(
    entities: pd.DataFrame,
    communities: pd.DataFrame,
    community_level: int | None,
) -> list[Entity]
```

## Description

Read in the Entities from the raw indexing outputs.

This function joins the entity records with their associated communities, optionally filters by a
specified community_level, aggregates community memberships per entity, and converts the resulting
records into Entity objects using read_entities.

Args:
    entities (pd.DataFrame): DataFrame containing entity information with at least an "id" column.
    communities (pd.DataFrame): DataFrame containing community information including "entity_ids",
        "community", and "level".
    community_level (int | None): If not None, keep entities with associated communities at or below this level.

Returns:
    list[Entity]: The list of Entity objects constructed from the input data.

Raises:
    AttributeError: If community_level is not None and the intermediate DataFrame does not contain a
        "level" column (as expected by _filter_under_community_level).

## Dependencies

This function calls:

- `graphrag/query/indexer_adapters.py::_filter_under_community_level`
- `graphrag/query/input/loaders/dfs.py::read_entities`

## Called By

This function is called by:

- `graphrag/api/query.py::global_search_streaming`
- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`

