---
sidebar_position: 91
---

# _text_embed_in_memory

**File:** `graphrag/index/operations/embed_text/embed_text.py` (lines 81-95)

## Signature

```python
def _text_embed_in_memory(
    input: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    embed_column: str,
    strategy: dict,
)
```

## Description

Embed a piece of text into a vector space in memory using the specified embedding strategy.

Args:
    input: DataFrame containing the text data to embed
    callbacks: WorkflowCallbacks used during embedding
    cache: PipelineCache used for caching intermediary results
    embed_column: Name of the column in input containing the text to embed
    strategy: Dictionary describing the embedding strategy to use (must include a "type" key)

Returns:
    embeddings: The embeddings produced by the embedding strategy

Raises:
    ValueError: If an unknown strategy is provided
    KeyError: If embed_column is not found in the input dataframe

## Dependencies

This function calls:

- `graphrag/index/operations/embed_text/embed_text.py::load_strategy`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/embed_text.py::embed_text`

