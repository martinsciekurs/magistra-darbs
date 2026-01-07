---
sidebar_position: 94
---

# embed_text

**File:** `graphrag/index/operations/embed_text/embed_text.py` (lines 39-78)

## Signature

```python
def embed_text(
    input: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    embed_column: str,
    strategy: dict,
    embedding_name: str,
    id_column: str = "id",
    title_column: str | None = None,
)
```

## Description

Embed text from a DataFrame into a vector space and return per-row embeddings. If a vector store is configured in the provided strategy, embeddings are generated and stored in that vector store using the given id and optional title information; otherwise embeddings are computed in memory. The function returns a sequence of embedding vectors, one per input row corresponding to embed_column.

Args:
    input (pd.DataFrame): Input data; must include embed_column and id_column, and may include title_column.
    callbacks (WorkflowCallbacks): Callbacks used during embedding.
    cache (PipelineCache): Cache object used by the embedding strategy.
    embed_column (str): Name of the DataFrame column to embed.
    strategy (dict): Embedding strategy configuration; must include a "type" key and may include vector_store settings.
    embedding_name (str): The embedding configuration name used to determine indexing in the vector store.
    id_column (str): The ID column name. Defaults to "id".
    title_column (str | None): Optional column containing the title for each document; may be None.

Returns:
    embeddings (List[List[float]]): The embeddings produced by the embedding process, one vector per input row. The shape is (N, D) where N is the number of rows and D is the embedding dimension.

Raises:
    Exception: Propagates exceptions raised by internal operations such as vector store creation or embedding strategy execution.

## Dependencies

This function calls:

- `graphrag/index/operations/embed_text/embed_text.py::_create_vector_store`
- `graphrag/index/operations/embed_text/embed_text.py::_get_index_name`
- `graphrag/index/operations/embed_text/embed_text.py::_text_embed_in_memory`
- `graphrag/index/operations/embed_text/embed_text.py::_text_embed_with_vector_store`

## Called By

This function is called by:

- `graphrag/index/workflows/generate_text_embeddings.py::_run_embeddings`

