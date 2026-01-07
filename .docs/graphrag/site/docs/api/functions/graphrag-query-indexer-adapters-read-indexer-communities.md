---
sidebar_position: 352
---

# read_indexer_communities

**File:** `graphrag/query/indexer_adapters.py` (lines 181-216)

## Signature

```python
def read_indexer_communities(
    final_communities: pd.DataFrame,
    final_community_reports: pd.DataFrame,
) -> list[Community]
```

## Description

Read in the Communities from the raw indexing outputs and reconstruct the community hierarchy information.

The function explodes the entity_ids per community to propagate entity membership, validates that the communities present in final_communities are covered by final_community_reports, logs a warning and filters if any are missing, and finally builds Community objects via read_communities with a mapping of columns.

Args:
  final_communities (pd.DataFrame): The final communities DataFrame produced by the indexer. Expected to contain at minimum id, community, title, level, and entity_ids (a list of related entity IDs) for proper expansion.
  final_community_reports (pd.DataFrame): The DataFrame containing community reports used to validate and align the community structure. Must include a community column used for matching.

Returns:
  list[Community]: A list of reconstructed Community objects, including hierarchy information and sub-community relations, as produced by read_communities. The input communities are filtered to align with reported communities when necessary.

Raises:
  ValueError: If required columns are missing from inputs (e.g., id, title, level, community, or entity_ids) or if downstream read_communities raises due to malformed data.
  Exceptions propagated from read_communities (e.g., KeyError, TypeError) as a result of input validation or data shape issues.

Notes:
  - If there are communities in final_communities that do not appear in final_community_reports,
    a warning is logged and those communities (and their exploded entity mappings) are dropped to
    yield results consistent with the available reports.
  - Internal steps include exploding entity_ids to map entities to communities, filtering by
    reported communities, and delegating to read_communities with specific column mappings:
      id_col="id", short_id_col="community", title_col="title", level_col="level",
      parent_col="parent", children_col="children".

## Dependencies

This function calls:

- `graphrag/query/input/loaders/dfs.py::read_communities`

## Called By

This function is called by:

- `graphrag/api/query.py::global_search_streaming`

