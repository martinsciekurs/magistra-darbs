---
sidebar_position: 142
---

# graphrag/language_model/factory.py

## Overview

Registry-based factory for creating chat and embedding language model backends.

Purpose
- Maintains registries for embedding and chat model implementations and provides a uniform API to register model backends and instantiate models by type.

Key exports
- ModelFactory: A class that implements the registries and factory methods to register, query, and instantiate models.

Summary
- ModelFactory maintains _embedding_registry and _chat_registry mappings from model type identifiers to creator callables for EmbeddingModel and ChatModel. It exposes methods to register embedding and chat backends, get the lists of registered model names, check support for a model type, and create model instances by type.

## Classes

- [`ModelFactory`](../api/classes/graphrag-language-model-factory-modelfactory)

## Functions

- [`register_embedding`](../api/functions/graphrag-language-model-factory-register-embedding)
- [`get_embedding_models`](../api/functions/graphrag-language-model-factory-get-embedding-models)
- [`create_chat_model`](../api/functions/graphrag-language-model-factory-create-chat-model)
- [`is_supported_model`](../api/functions/graphrag-language-model-factory-is-supported-model)
- [`is_supported_chat_model`](../api/functions/graphrag-language-model-factory-is-supported-chat-model)
- [`create_embedding_model`](../api/functions/graphrag-language-model-factory-create-embedding-model)
- [`is_supported_embedding_model`](../api/functions/graphrag-language-model-factory-is-supported-embedding-model)
- [`get_chat_models`](../api/functions/graphrag-language-model-factory-get-chat-models)
- [`register_chat`](../api/functions/graphrag-language-model-factory-register-chat)

