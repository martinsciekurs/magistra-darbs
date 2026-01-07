---
sidebar_position: 150
---

# graphrag/language_model/providers/litellm/embedding_model.py

## Overview

LitellmEmbeddingModel module

Purpose
Provide a wrapper around Litellm's embedding endpoints to generate vector representations for text inputs. It supports batch and single-input embeddings and can be augmented with optional request-handling wrappers for caching, logging, rate limiting, and retries.

Public exports
- LitellmEmbeddingModel: Primary class exposing batch and single-input embedding methods.

Summary
The LitellmEmbeddingModel wraps Litellm's embedding functionality, composing base embedding calls with the model configuration and optional middleware to produce consistent embeddings. It supports synchronous and asynchronous operations and can be configured with a per-model PipelineCache.

Usage example
# Initialize with a LanguageModelConfig instance (details omitted)
config = LanguageModelConfig(...)  # configure as needed
model = LitellmEmbeddingModel(name="my-model", config=config)

# Single embedding
vec = model.embed("Sample text to embed")

# Batch embeddings
batch_vecs = model.embed_batch(["First text", "Second text"])

Parameters
- __init__(name: str, config: LanguageModelConfig, cache: PipelineCache | None = None, **kwargs) -&gt; None
  name: The model instance name.
  config: The configuration for the language model.
  cache: Optional cache to use for embeddings; if provided, a scoped cache is created.
  **kwargs: Additional options forwarded to the underlying embedding machinery.

Returns
- None

Methods
- embed_batch(text_list: list[str], **kwargs: Any) -&gt; list[list[float]]
  Batch generate embeddings for a list of texts.
- aembed_batch(text_list: list[str], **kwargs: Any) -&gt; list[list[float]]
  Async batch embeddings.
- embed(text: str, **kwargs: Any) -&gt; list[float]
  Embed a single text input.
- aembed(text: str, **kwargs: Any) -&gt; list[float]
  Async single embedding.
- Internal helpers: _get_kwargs, _base_embedding, _base_aembedding, _create_base_embeddings, _create_embeddings

Exceptions
- May raise ValueError or TypeError for invalid inputs; RuntimeError or network-related exceptions may propagate from the underlying embedding service. Implementations may retry or log as configured.

## Classes

- [`LitellmEmbeddingModel`](../api/classes/graphrag-language-model-providers-litellm-embedding-model-litellmembeddingmodel)

## Functions

- [`_get_kwargs`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-get-kwargs)
- [`embed_batch`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-embed-batch)
- [`aembed_batch`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-aembed-batch)
- [`_base_aembedding`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-base-aembedding)
- [`_base_embedding`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-base-embedding)
- [`aembed`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-aembed)
- [`_create_base_embeddings`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-create-base-embeddings)
- [`embed`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-embed)
- [`_create_embeddings`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-create-embeddings)
- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-embedding-model-init)

