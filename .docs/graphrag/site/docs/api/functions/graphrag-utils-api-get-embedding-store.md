---
sidebar_position: 403
---

# get_embedding_store

**File:** `graphrag/utils/api.py` (lines 97-141)

## Signature

```python
def get_embedding_store(
    config_args: dict[str, dict],
    embedding_name: str,
) -> BaseVectorStore
```

## Description

Get the embedding description store.

Given a mapping of index configurations in config_args and a target embedding name embedding_name, construct and connect the appropriate vector store(s). If there is only a single configured index, this returns that single vector store; otherwise it returns a MultiVectorStore that aggregates multiple vector stores across indexes.

Args:
    config_args: dict[str, dict]
        Configuration for one or more embedding indexes. Each key is an index identifier and each value is a dictionary of store configuration options used to instantiate a vector store.
    embedding_name: str
        Name of the embedding to configure and fetch the store for.

Returns:
    BaseVectorStore
        A vector store capable of handling the requested embedding. If multiple indexes are configured, a MultiVectorStore is returned.

Raises:
    Exception
        If underlying vector store creation or connection fails.

## Dependencies

This function calls:

- `graphrag/config/embeddings.py::create_index_name`
- `graphrag/config/models/vector_store_schema_config.py::VectorStoreSchemaConfig`
- `graphrag/vector_stores/factory.py::VectorStoreFactory`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`
- `graphrag/api/query.py::basic_search_streaming`

