---
sidebar_position: 561
---

# test_create_index_name_invalid_embedding_does_not_throw

**File:** `tests/unit/utils/test_embeddings.py` (lines 19-21)

## Signature

```python
def test_create_index_name_invalid_embedding_does_not_throw()
```

## Description

Create an index name for the embedding store by prefixing the container name and normalizing the embedding name.

The container_name parameter is used for partitioning across multiple embedding sets within a vector store and is added as a prefix to the index name.
The embedding_name is fixed, with the available list defined in graphrag.index.config.embeddings. Dots in the embedding_name are replaced with dashes to accommodate vector stores that do not support dots.

Args:
    container_name (str): Partition identifier used for differentiating multiple embedding sets within a vector store; it is added as a prefix to the index name.
    embedding_name (str): The embedding name; the available list is defined in graphrag.index.config.embeddings.
    validate (bool): If True, validate embedding_name and raise KeyError if invalid; if False, skip validation.

Returns:
    str: The constructed index name.

Raises:
    KeyError: If validate is True and embedding_name is not a valid embedding name.

## Dependencies

This function calls:

- `graphrag/config/embeddings.py::create_index_name`

