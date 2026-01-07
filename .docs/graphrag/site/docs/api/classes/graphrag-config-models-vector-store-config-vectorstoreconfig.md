---
sidebar_position: 84
---

# VectorStoreConfig

**File:** `graphrag/config/models/vector_store_config.py`

## Overview

Configuration model for vector store settings used by graphrag.

It centralizes validation and handling of vector store configuration, including the store type, connection details (such as db_uri and url), embeddings schema validation, and the vector store schema configuration. This ensures consistent, validated settings are available for downstream operations.

Key attributes:
  vector_store: The vector store configuration block that includes the store type and connection details.
  db_uri: The database URI for the vector store; may be set to a default when the type is LanceDB.
  url: The URL for the vector store; required when vector_store.type == azure_ai_search.
  embeddings_schema: A collection of embedding schema names to use; validated against all_embeddings.
  vector_store_schema_config: The schema configuration for the vector store, typically an instance of VectorStoreSchemaConfig.

Args:
  vector_store: The vector store configuration block containing the store type and connection details.
  db_uri: The database URI for the vector store; may be defaulted for LanceDB.
  url: The connection URL for the vector store.
  embeddings_schema: The list of embedding schema names to validate.
  vector_store_schema_config: The VectorStoreSchemaConfig object for schema validation.

Returns:
  None

Raises:
  ValueError: If vector_store.type is not LanceDB and a non-empty db_uri is provided.
  ValueError: If any entry in embeddings_schema is not a known embedding schema name present in all_embeddings.
  ValueError: If vector_store.type == azure_ai_search and vector_store.url is missing or empty.
  ValueError: If an invalid database URI, URL, or embeddings schema is encountered during validation.

## Methods

### `_validate_db_uri`

```python
def _validate_db_uri(self) -> None
```

### `_validate_embeddings_schema`

```python
def _validate_embeddings_schema(self) -> None
```

### `_validate_url`

```python
def _validate_url(self) -> None
```

### `_validate_model`

```python
def _validate_model(self)
```

