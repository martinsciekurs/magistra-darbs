---
sidebar_position: 358
---

# read_community_reports

**File:** `graphrag/query/input/loaders/dfs.py` (lines 191-226)

## Signature

```python
def read_community_reports(
    df: pd.DataFrame,
    id_col: str = "id",
    short_id_col: str | None = "community",
    title_col: str = "title",
    community_col: str = "community",
    summary_col: str = "summary",
    content_col: str = "full_content",
    rank_col: str | None = "rank",
    content_embedding_col: str | None = "full_content_embedding",
    attributes_cols: list[str] | None = None,
) -> list[CommunityReport]
```

## Description

Read community reports from a dataframe using pre-converted records.

Args:
    df: The DataFrame to process.
    id_col: The column name to use for the report id.
    short_id_col: The column name for the short identifier; if None, the code falls back to the index.
    title_col: The column name for the report title.
    community_col: The column name containing the community identifier.
    summary_col: The column name containing the summary.
    content_col: The column name containing the full content.
    rank_col: The column name containing the rank value, if present.
    content_embedding_col: The column name containing the full content embeddings, if present.
    attributes_cols: Optional list of additional attribute columns to include; if None, no extra attributes are added.

Returns:
    list[CommunityReport]: A list of CommunityReport objects constructed from the dataframe rows.

Raises:
    ValueError: If a required column is None or missing from the input data, or if value conversion fails in helper utilities.
    TypeError: If attribute column values are not of expected types.

## Dependencies

This function calls:

- `graphrag/data_model/community_report.py::CommunityReport`
- `graphrag/query/input/loaders/dfs.py::_prepare_records`
- `graphrag/query/input/loaders/utils.py::to_optional_float`
- `graphrag/query/input/loaders/utils.py::to_optional_list`
- `graphrag/query/input/loaders/utils.py::to_optional_str`
- `graphrag/query/input/loaders/utils.py::to_str`

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_reports`

