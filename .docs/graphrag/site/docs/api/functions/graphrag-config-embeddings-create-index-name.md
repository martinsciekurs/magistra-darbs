---
sidebar_position: 40
---

# create_index_name

**File:** `graphrag/config/embeddings.py` (lines 32-48)

## Signature

```python
def create_index_name(
    container_name: str, embedding_name: str, validate: bool = True
) -> str
```

## Description

Create an index name for the embedding store.

Within any given vector store, we can have multiple sets of embeddings organized into projects.
The container_name parameter is used for this partitioning, and is added as a prefix to the index name for differentiation.

The embedding_name is fixed, with the available list defined in graphrag.index.config.embeddings

Note that we use dot notation in our names, but many vector stores do not support this - so we convert to dashes.

Args:
    container_name: The container name used as a prefix for differentiation.
    embedding_name: The embedding name to include in the index name.
    validate: Whether to validate embedding_name against the allowed set before constructing the name.

Returns:
    str: The constructed index name, with dots replaced by dashes.

Raises:
    KeyError: If validate is True and embedding_name is not in all_embeddings.

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/embed_text.py::_get_index_name`
- `graphrag/utils/api.py::get_embedding_store`
- `tests/unit/utils/test_embeddings.py::test_create_index_name`
- `tests/unit/utils/test_embeddings.py::test_create_index_name_invalid_embedding_throws`
- `tests/unit/utils/test_embeddings.py::test_create_index_name_invalid_embedding_does_not_throw`

