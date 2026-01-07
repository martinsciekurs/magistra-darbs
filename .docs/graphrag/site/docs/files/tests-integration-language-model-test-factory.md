---
sidebar_position: 233
---

# tests/integration/language_model/test_factory.py

## Overview

Tests for the ModelFactory integration in the graphrag.language_model package.

Overview
This module defines helper test models and test functions used to validate integration between
ModelFactory and ModelManager in the language_model subsystem. It includes:
- CustomChatModel: a lightweight test model implementing chat, achat, chat_stream, and achat_stream
  methods to simulate synchronous, streaming, and asynchronous chat interfaces.
- CustomEmbeddingModel: a stateless test model implementing aembed_batch, aembed, embed_batch, and embed
  to simulate embedding generation in both synchronous and asynchronous forms.

Exports
- CustomChatModel: Lightweight test-oriented chat model.
- CustomEmbeddingModel: Stateless embedding model.
- test_create_custom_chat_model: Test creating and using a custom chat model via the ModelFactory and ModelManager.
- test_create_custom_embedding_llm: Asynchronous test for creating a custom embedding LLM and validating its methods.
- Additional methods: achat, chat, chat_stream, achat_stream, aembed_batch, aembed, embed_batch, embed.

Brief summary
The tests exercise constructing custom LLMs through the factory, registering them with the manager,
and asserting expected behaviors of chat and embedding interfaces (e.g., achat returns content-only
response and chat returns content with a full_response payload).

Args
None. The module exposes test constructs and helper classes; there are no top-level parameters.

Returns
None. This module is for tests and does not return a value.

Raises
None. The tests do not raise exceptions at module import time.

## Classes

- [`CustomChatModel`](../api/classes/tests-integration-language-model-test-factory-customchatmodel)
- [`CustomEmbeddingModel`](../api/classes/tests-integration-language-model-test-factory-customembeddingmodel)

## Functions

- [`achat`](../api/functions/tests-integration-language-model-test-factory-achat)
- [`aembed_batch`](../api/functions/tests-integration-language-model-test-factory-aembed-batch)
- [`chat`](../api/functions/tests-integration-language-model-test-factory-chat)
- [`test_create_custom_chat_model`](../api/functions/tests-integration-language-model-test-factory-test-create-custom-chat-model)
- [`aembed`](../api/functions/tests-integration-language-model-test-factory-aembed)
- [`chat_stream`](../api/functions/tests-integration-language-model-test-factory-chat-stream)
- [`embed_batch`](../api/functions/tests-integration-language-model-test-factory-embed-batch)
- [`achat_stream`](../api/functions/tests-integration-language-model-test-factory-achat-stream)
- [`embed`](../api/functions/tests-integration-language-model-test-factory-embed)
- [`__init__`](../api/functions/tests-integration-language-model-test-factory-init)
- [`test_create_custom_embedding_llm`](../api/functions/tests-integration-language-model-test-factory-test-create-custom-embedding-llm)
- [`__init__`](../api/functions/tests-integration-language-model-test-factory-init)

