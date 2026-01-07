---
sidebar_position: 90
---

# _create_vector_store

**File:** `graphrag/index/operations/embed_text/embed_text.py` (lines 186-217)

## Signature

```python
def _create_vector_store(
    vector_store_config: dict, index_name: str, embedding_name: str | None = None
) -> BaseVectorStore
```

## Description

Create and configure a vector store from the provided configuration.

Args:
    vector_store_config (dict): Configuration for the vector store, including the type, embeddings_schema, and other parameters forwarded to the vector store constructor and connect().
    index_name (str): The index name to assign if not provided by the embedding config.
    embedding_name (str | None): Optional embedding name to select a specific embedding configuration from embeddings_schema.

Returns:
    BaseVectorStore: A connected vector store instance created according to the configuration.

Raises:
    Exception: If vector store creation or connection fails due to misconfiguration or underlying storage errors.

## Dependencies

This function calls:

- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`
- `graphrag/vector_stores/factory.py::VectorStoreFactory`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/embed_text.py::embed_text`

