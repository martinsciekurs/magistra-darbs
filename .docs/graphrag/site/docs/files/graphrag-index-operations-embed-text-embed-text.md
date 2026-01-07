---
sidebar_position: 64
---

# graphrag/index/operations/embed_text/embed_text.py

## Overview

Module for embedding text into vector spaces using configurable strategies and optional vector stores.

Overview:
This module provides the core workflow to embed text from a DataFrame and either return embeddings directly or store them in a vector store, depending on the strategy configuration. It supports multiple embedding strategies (for example OpenAI-based or mock strategies) and handles vector store creation and index naming.

Exports:
- load_strategy(strategy: TextEmbedStrategyType) -&gt; TextEmbeddingStrategy
- TextEmbedStrategyType: Enum describing available text embedding strategies
- embed_text(input: pd.DataFrame, callbacks: WorkflowCallbacks, cache: PipelineCache, embed_column: str, strategy: dict, embedding_name: str, id_column: str = "id", title_column: str | None = None) -&gt; list
- DEFAULT_EMBEDDING_BATCH_SIZE: int

Internal helpers (for internal use):
- _create_vector_store(vector_store_config: dict, index_name: str, embedding_name: str | None = None) -&gt; BaseVectorStore
- _text_embed_in_memory(input: pd.DataFrame, callbacks: WorkflowCallbacks, cache: PipelineCache, embed_column: str, strategy: dict) -&gt; list
- _text_embed_with_vector_store(input: pd.DataFrame, callbacks: WorkflowCallbacks, cache: PipelineCache, embed_column: str, strategy: dict[str, Any], vector_store: BaseVectorStore, vector_store_config: dict, id_column: str = "id", title_column: str | None = None) -&gt; list
- _get_index_name(vector_store_config: dict, embedding_name: str) -&gt; str

This module integrates with PipelineCache, WorkflowCallbacks, and VectorStoreFactory to facilitate end-to-end text embedding workflows for the graphrag framework.

## Classes

- [`TextEmbedStrategyType`](../api/classes/graphrag-index-operations-embed-text-embed-text-textembedstrategytype)

## Functions

- [`load_strategy`](../api/functions/graphrag-index-operations-embed-text-embed-text-load-strategy)
- [`__repr__`](../api/functions/graphrag-index-operations-embed-text-embed-text-repr)
- [`_create_vector_store`](../api/functions/graphrag-index-operations-embed-text-embed-text-create-vector-store)
- [`_text_embed_in_memory`](../api/functions/graphrag-index-operations-embed-text-embed-text-text-embed-in-memory)
- [`_text_embed_with_vector_store`](../api/functions/graphrag-index-operations-embed-text-embed-text-text-embed-with-vector-store)
- [`_get_index_name`](../api/functions/graphrag-index-operations-embed-text-embed-text-get-index-name)
- [`embed_text`](../api/functions/graphrag-index-operations-embed-text-embed-text-embed-text)

