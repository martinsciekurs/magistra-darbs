---
sidebar_position: 560
---

# test_create_index_name_invalid_embedding_throws

**File:** `tests/unit/utils/test_embeddings.py` (lines 14-16)

## Signature

```python
def test_create_index_name_invalid_embedding_throws()
```

## Description

Create an index name for the embedding store.

Args:
    container_name (str): Partition identifier used for differentiating multiple embedding sets within a vector store; it is added as a prefix to the index name.
    embedding_name (str): The fixed embedding name; the available list is defined in graphrag.index.config.embeddings.
    validate (bool): If True, validate embedding_name and raise KeyError for invalid names; if False, skip validation.

Returns:
    str: The constructed index name with dots in embedding_name replaced by dashes and concatenated with container_name using a dash (e.g., 'default-entity-title').

Raises:
    KeyError: If validate is True and embedding_name is not a valid embedding.

## Dependencies

This function calls:

- `graphrag/config/embeddings.py::create_index_name`

