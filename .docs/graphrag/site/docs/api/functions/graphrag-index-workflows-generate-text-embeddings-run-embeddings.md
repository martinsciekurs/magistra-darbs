---
sidebar_position: 249
---

# _run_embeddings

**File:** `graphrag/index/workflows/generate_text_embeddings.py` (lines 174-192)

## Signature

```python
def _run_embeddings(
    name: str,
    data: pd.DataFrame,
    embed_column: str,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    text_embed_config: dict,
) -> pd.DataFrame
```

## Description

All steps to generate a single embedding.

Args:
  name: The name of the embedding, used as the embedding_name when calling embed_text.
  data: DataFrame containing input data; the function adds an embedding column and returns a DataFrame with only id and embedding.
  embed_column: The column in data to embed; passed to embed_text as the embed_column.
  callbacks: WorkflowCallbacks used to report progress and handle lifecycle events during embedding.
  cache: PipelineCache used by embed_text for caching and resource management.
  text_embed_config: Dictionary with embedding configuration; should include a strategy key.

Returns:
  pd.DataFrame: A DataFrame containing the id and embedding columns.

Raises:
  May raise exceptions from embed_text or DataFrame operations.

## Dependencies

This function calls:

- `graphrag/index/operations/embed_text/embed_text.py::embed_text`

## Called By

This function is called by:

- `graphrag/index/workflows/generate_text_embeddings.py::generate_text_embeddings`

