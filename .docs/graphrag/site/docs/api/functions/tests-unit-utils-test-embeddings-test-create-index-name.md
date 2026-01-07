---
sidebar_position: 559
---

# test_create_index_name

**File:** `tests/unit/utils/test_embeddings.py` (lines 9-11)

## Signature

```python
def test_create_index_name()
```

## Description

Create an index name for the embedding store.

This function creates a string by prefixing the embedding's index with the container_name and replacing dots in the embedding_name with dashes to accommodate vector stores that do not support dots.

Args:
    container_name (str): The partition/prefix for the index name.
    embedding_name (str): The embedding name; must be one of the supported embeddings defined in graphrag.index.config.embeddings.
    validate (bool): Whether to validate the embedding_name against the supported list. Defaults to True.

Returns:
    str: The generated index name in the format "&lt;container_name&gt;-&lt;embedding_name_with_dashes&gt;".

Raises:
    KeyError: If validate is True and the embedding_name is not a supported embedding.

## Dependencies

This function calls:

- `graphrag/config/embeddings.py::create_index_name`

