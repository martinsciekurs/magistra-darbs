---
sidebar_position: 349
---

# read_indexer_relationships

**File:** `graphrag/query/indexer_adapters.py` (lines 63-71)

## Signature

```python
def read_indexer_relationships(final_relationships: pd.DataFrame) -> list[Relationship]
```

## Description

Read in the Relationships from the raw indexing outputs.

This function delegates to read_relationships with the following mappings: df = final_relationships, short_id_col = "human_readable_id", rank_col = "combined_degree", description_embedding_col = None, attributes_cols = None.

Args:
    final_relationships (pd.DataFrame): The DataFrame containing raw indexing outputs for relationships.

Returns:
    list[Relationship]: A list of Relationship objects constructed from the input data.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/dfs.py::read_relationships`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`

