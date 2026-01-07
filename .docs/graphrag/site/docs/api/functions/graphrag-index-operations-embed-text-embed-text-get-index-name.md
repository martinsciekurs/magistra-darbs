---
sidebar_position: 93
---

# _get_index_name

**File:** `graphrag/index/operations/embed_text/embed_text.py` (lines 220-226)

## Signature

```python
def _get_index_name(vector_store_config: dict, embedding_name: str) -> str
```

## Description

Get the index name for the embedding in the vector store.

Args:
    vector_store_config (dict): Configuration for the vector store; may include container_name (defaults to "default") and type.
    embedding_name (str): The embedding name used to construct the index name.

Returns:
    str: The computed index name.

Raises:
    Exception: Propagates exceptions raised by create_index_name or other internal calls.

## Dependencies

This function calls:

- `graphrag/config/embeddings.py::create_index_name`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/embed_text.py::embed_text`

