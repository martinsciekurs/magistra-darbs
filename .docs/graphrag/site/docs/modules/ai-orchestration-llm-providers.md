---
sidebar_position: 6
---

# AI Orchestration & LLM Providers

Abstractions and backends for language models, tokenization, and LLM service management used across indexing and querying.

## Overview

Abstractions and backends for language models, tokenization, and LLM service orchestration used across indexing and querying.

Architectural purpose
Provide an extensible, registry-based framework to register, instantiate, and manage chat and embedding LLM backends, decoupling model providers from Graphrag's language-model stack and enabling on-demand creation and lifecycle management.

Key components and responsibilities
- graphrag/language_model/__init__.py: module surface that exposes the language_model package.
- graphrag/language_model/factory.py: ModelFactory with registries for embedding and chat models; exposes API to register model backends and instantiate models by type.
- graphrag/language_model/manager.py: ModelManager singleton for on-demand creation, registration, retrieval, and listing of ChatModel and EmbeddingModel instances; delegates instantiation to ModelFactory.
- graphrag/language_model/providers/fnllm/models.py: FNLLM-based providers for embeddings and chat (OpenAI and Azure OpenAI); concrete classes: OpenAIEmbeddingFNLLM, OpenAIChatFNLLM, AzureOpenAIEmbeddingFNLLM, AzureOpenAIChatFNLLM.
- graphrag/language_model/providers/fnllm/utils.py: Utilities for FNLLM OpenAI provider; helpers for error handling, coroutine execution, model parameter derivation, and OpenAI config.
- graphrag/language_model/providers/litellm/chat_model.py: Graphrag Litellm chat model wrapper with streaming, caching, and resilience features; class: LitellmChatModel.
- graphrag/language_model/providers/litellm/embedding_model.py: Litellm embedding wrapper for vector endpoints; class: LitellmEmbeddingModel.
- graphrag/language_model/response/base.py: Typed containers for LLM provider responses; classes: ModelResponse, ModelOutput; helpers: output, history, parsed_response, content, full_response.

Main entry points / public APIs
- ModelFactory: registry-based factory for creating chat and embedding backends. Exposed API surface includes:
  - register_embedding
  - get_embedding_models
  - create_chat_model
  - is_supported_model
  - is_supported_chat_model
  - create_embedding_model
  - is_supported_embedding_model
  - get_chat_models
- ModelManager: singleton coordinating lifecycle of model instances; exposed methods include:
  - get_or_create_chat_model
  - list_chat_models
  - remove_chat
  - list_embedding_models
  - get_chat_model
  - get_or_create_embedding_model
  - get_instance
  - register_embedding
- Provider classes:
  - OpenAIEmbeddingFNLLM
  - OpenAIChatFNLLM
  - AzureOpenAIEmbeddingFNLLM
  - AzureOpenAIChatFNLLM
  - LitellmEmbeddingModel
  - LitellmChatModel
- Response containers and helpers:
  - ModelResponse
  - ModelOutput
  - output
  - history
  - parsed_response
  - content
  - full_response

Notes
- Public API methods document parameter expectations, return values, and possible errors in their own docstrings; this module-level docstring provides architectural context and a high-level API surface.
- Implementations may raise runtime errors such as unsupported model types or invalid configurations; refer to individual components for exact exceptions and handling.

Implementation details
- Implementation specifics are trimmed from this docstring; see the respective module and class docstrings for behavior, parameters, returns, and error handling.

## Files in this Module

- [`graphrag/language_model/__init__.py`](../files/graphrag-language-model-init)
- [`graphrag/language_model/factory.py`](../files/graphrag-language-model-factory)
- [`graphrag/language_model/manager.py`](../files/graphrag-language-model-manager)
- [`graphrag/language_model/providers/fnllm/models.py`](../files/graphrag-language-model-providers-fnllm-models)
- [`graphrag/language_model/providers/fnllm/utils.py`](../files/graphrag-language-model-providers-fnllm-utils)
- [`graphrag/language_model/providers/litellm/chat_model.py`](../files/graphrag-language-model-providers-litellm-chat-model)
- [`graphrag/language_model/providers/litellm/embedding_model.py`](../files/graphrag-language-model-providers-litellm-embedding-model)
- [`graphrag/language_model/response/base.py`](../files/graphrag-language-model-response-base)
