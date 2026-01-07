---
sidebar_position: 143
---

# graphrag/language_model/manager.py

## Overview

Module for managing chat and embedding language model instances via a singleton ModelManager.

Overview:
The ModelManager singleton provides on-demand creation, registration, retrieval, and listing of ChatModel and EmbeddingModel instances. It delegates instantiation to ModelFactory and stores instances in internal registries for reuse.

Exports:
  - ModelManager: Singleton manager class responsible for creating, registering, retrieving, and listing ChatModel and EmbeddingModel instances. It exposes methods such as get_or_create_chat_model, list_chat_models, remove_chat, list_embedding_models, get_chat_model, get_or_create_embedding_model, get_instance, register_embedding, and register_chat.

Summary:
This module centralizes access to chat-based and embedding-based language models, ensuring a single source of truth for model registrations and lookups throughout the application.

## Classes

- [`ModelManager`](../api/classes/graphrag-language-model-manager-modelmanager)

## Functions

- [`get_or_create_chat_model`](../api/functions/graphrag-language-model-manager-get-or-create-chat-model)
- [`list_chat_models`](../api/functions/graphrag-language-model-manager-list-chat-models)
- [`remove_chat`](../api/functions/graphrag-language-model-manager-remove-chat)
- [`list_embedding_models`](../api/functions/graphrag-language-model-manager-list-embedding-models)
- [`get_chat_model`](../api/functions/graphrag-language-model-manager-get-chat-model)
- [`get_or_create_embedding_model`](../api/functions/graphrag-language-model-manager-get-or-create-embedding-model)
- [`get_instance`](../api/functions/graphrag-language-model-manager-get-instance)
- [`register_embedding`](../api/functions/graphrag-language-model-manager-register-embedding)
- [`__new__`](../api/functions/graphrag-language-model-manager-new)
- [`register_chat`](../api/functions/graphrag-language-model-manager-register-chat)
- [`__init__`](../api/functions/graphrag-language-model-manager-init)
- [`remove_embedding`](../api/functions/graphrag-language-model-manager-remove-embedding)
- [`get_embedding_model`](../api/functions/graphrag-language-model-manager-get-embedding-model)

