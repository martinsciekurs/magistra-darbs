---
sidebar_position: 351
---

# read_indexer_reports

**File:** `graphrag/query/indexer_adapters.py` (lines 74-127)

## Signature

```python
def read_indexer_reports(
    final_community_reports: pd.DataFrame,
    final_communities: pd.DataFrame,
    community_level: int | None,
    dynamic_community_selection: bool = False,
    content_embedding_col: str = "full_content_embedding",
    config: GraphRagConfig | None = None,
) -> list[CommunityReport]
```

## Description

Read in the Community Reports from the raw indexing outputs.

If not dynamic_community_selection, then select reports with the max community level that an entity belongs to.

Args:
    final_community_reports: pd.DataFrame
        The DataFrame containing raw community reports produced by the indexer.
    final_communities: pd.DataFrame
        The DataFrame containing final communities; entities are exploded from the entity_ids column.
    community_level: int | None
        Threshold on community level to filter results. If None, no filtering is applied.
    dynamic_community_selection: bool
        If False, perform a community level roll up to the maximum level per title.
    content_embedding_col: str
        Column name for content embeddings. Defaults to "full_content_embedding".
    config: GraphRagConfig | None
        Optional configuration object for embedding model lookup and generation.

Returns:
    list[CommunityReport]
        A list of CommunityReport objects read from the processed reports dataframe.

Raises:
    AttributeError: if the input DataFrame does not have a level column....

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/query/indexer_adapters.py::_filter_under_community_level`
- `graphrag/query/indexer_adapters.py::embed_community_reports`
- `graphrag/query/input/loaders/dfs.py::read_community_reports`

## Called By

This function is called by:

- `graphrag/api/query.py::global_search_streaming`
- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`

