---
sidebar_position: 346
---

# embed_community_reports

**File:** `graphrag/query/indexer_adapters.py` (lines 219-235)

## Signature

```python
def embed_community_reports(
    reports_df: pd.DataFrame,
    embedder: EmbeddingModel,
    source_col: str = "full_content",
    embedding_col: str = "full_content_embedding",
) -> pd.DataFrame
```

## Description

Embed a source column of the reports dataframe using the given embedder.

Args:
    reports_df (pd.DataFrame): The reports dataframe to embed. This function may mutate the dataframe in place by adding a new embedding column if it does not already exist.
    embedder (EmbeddingModel): The model used to generate embeddings from the content of the source column.
    source_col (str): Name of the column in reports_df that contains the text to embed. Defaults to "full_content".
    embedding_col (str): Name of the column to store the generated embeddings. If this column does not exist, it will be created and populated. Defaults to "full_content_embedding".

Returns:
    pd.DataFrame: The input DataFrame, augmented with embedding_col. The same DataFrame object is returned (in-place mutation when embedding_col is created).

Raises:
    ValueError: If the source_col is missing from reports_df.

Examples:
    # Basic usage
    df = embed_community_reports(reports_df, embedder)

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_reports`

