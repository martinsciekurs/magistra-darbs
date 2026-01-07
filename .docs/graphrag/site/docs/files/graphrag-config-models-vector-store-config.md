---
sidebar_position: 31
---

# graphrag/config/models/vector_store_config.py

## Overview

Configuration model and validation logic for vector stores used by graphrag.

This module defines VectorStoreConfig, a Pydantic-based model that centralizes validation and handling of vector store settings, including the store type, connection details (such as db_uri and url), embeddings schema validation, and the vector store schema configuration.

Exports:
- VectorStoreConfig: Configuration model for vector store settings used by graphrag, with internal validation hooks for database URIs, embeddings schemas, URLs, and model-level checks.

Summary:
This configuration object provides consistent, validated settings for downstream operations.

Raises:
- ValueError: If invalid database URI, URL, or embeddings schema is encountered during validation.

## Classes

- [`VectorStoreConfig`](../api/classes/graphrag-config-models-vector-store-config-vectorstoreconfig)

## Functions

- [`_validate_db_uri`](../api/functions/graphrag-config-models-vector-store-config-validate-db-uri)
- [`_validate_embeddings_schema`](../api/functions/graphrag-config-models-vector-store-config-validate-embeddings-schema)
- [`_validate_url`](../api/functions/graphrag-config-models-vector-store-config-validate-url)
- [`_validate_model`](../api/functions/graphrag-config-models-vector-store-config-validate-model)

