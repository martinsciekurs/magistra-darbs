---
sidebar_position: 92
---

# _text_embed_with_vector_store

**File:** `graphrag/index/operations/embed_text/embed_text.py` (lines 98-183)

## Signature

```python
def _text_embed_with_vector_store(
    input: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    embed_column: str,
    strategy: dict[str, Any],
    vector_store: BaseVectorStore,
    vector_store_config: dict,
    id_column: str = "id",
    title_column: str | None = None,
)
```

## Description

Embed text from a DataFrame into a vector store using a specified embedding strategy and load the resulting vectors into the provided vector store.

Args:
    input (pd.DataFrame): Input DataFrame containing the data to embed; must include the embed_column and id_column, and may include the title column.
    callbacks (WorkflowCallbacks): Callbacks used during embedding.
    cache (PipelineCache): Cache object used by the embedding strategy.
    embed_column (str): Name of the DataFrame column containing the text to embed (or lists of texts per row).
    strategy (dict[str, Any]): Embedding strategy configuration, including the type of strategy to load.
    vector_store (BaseVectorStore): Vector store where embeddings will be loaded.
    vector_store_config (dict): Configuration for the vector store (e.g., batch_size, overwrite).
    id_column (str): Name of the DataFrame column containing the identifier for each row.
    title_column (str | None): Optional column name to use as the title; defaults to embed_column when None.

Returns:
    list[Any]: Aggregated embeddings produced by the embedding strategy across all batches.

Raises:
    ValueError: If required columns are missing from the input DataFrame or if the necessary columns cannot be found (embed_column, id_column, and title_column as applicable).

## Dependencies

This function calls:

- `graphrag/index/operations/embed_text/embed_text.py::load_strategy`
- `graphrag/vector_stores/base.py::VectorStoreDocument`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/embed_text.py::embed_text`

