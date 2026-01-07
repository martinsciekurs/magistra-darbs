---
sidebar_position: 17
---

# graphrag/config/embeddings.py

## Overview

Utilities for embedding configuration in Graphrag.

Purpose
This module provides helpers for embedding configuration, including generating consistent index names for embedding stores used by Graphrag. It is used to organize multiple embedding sets within a vector store by partitioning with a container_name and naming each embedding set with embedding_name (the embedding_name is selected from graphrag.index.config.embeddings).

Key exports
- create_index_name(container_name: str, embedding_name: str, validate: bool = True) -&gt; str: Create an index name for the embedding store. Within any given vector store, we can have multiple sets of embeddings organized into projects. The container_name parameter is used for this partitioning, and is added as a prefix to the index name for differentiation. The embedding_name is fixed, with the available list defined in graphrag.index.config.embeddings.

Args
container_name: The project/container prefix used to partition embeddings.
embedding_name: The fixed embedding set name selected from graphrag.index.config.embeddings.
validate: If True, validate that embedding_name is in the allowed list.

Returns
str: The generated index name.

Raises
Exception: If validate is True and embedding_name is not in the allowed list.

Brief summary
Provides a straightforward helper to generate a namespaced index name for embedding stores, ensuring consistent naming across projects and embedding sets.

## Functions

- [`create_index_name`](../api/functions/graphrag-config-embeddings-create-index-name)

