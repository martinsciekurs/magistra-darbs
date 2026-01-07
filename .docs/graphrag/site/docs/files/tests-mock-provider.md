---
sidebar_position: 244
---

# tests/mock_provider.py

## Overview

Mock providers for testing chat and embedding LLM integrations.

Overview
This module provides two deterministic, dependency-free mock LLM implementations for unit tests: MockChatLLM and MockEmbeddingLLM. They simulate chat interactions and embedding generation without external services, enabling predictable, fast tests and easy debugging.

Public API
- MockChatLLM: deterministic mock chat LLM that cycles through a predefined sequence of responses. It supports synchronous chat via chat() and asynchronous streaming via achat_stream(). It can apply an optional LanguageModelConfig override and a json flag to indicate that responses should be treated as JSON where applicable.
- MockEmbeddingLLM: mock embedding provider exposing embedding methods aembed, aembed_batch, embed, and embed_batch.

Exports
- MockChatLLM
- MockEmbeddingLLM

Classes
MockChatLLM
A configurable mock chat language model provider used for testing. It cycles through a predefined sequence of responses and can emit them synchronously via chat() or asynchronously via achat_stream(). Optional LanguageModelConfig override and json flag are supported.

Constructor
__init__(responses: list[str | BaseModel] | None = None, config: LanguageModelConfig | None = None, json: bool = False, **kwargs)

Returns
None

Methods
achat(self, prompt: str, history: list | None = None, **kwargs) -&gt; ModelResponse
Return the next response in the configured sequence, cycling through available responses. If there are no configured responses, return an empty content response.

chat(self, prompt: str, history: list | None = None, **kwargs) -&gt; ModelResponse
Return the next response in the configured sequence. It cycles through responses; if none configured, return an empty response with content "".

achat_stream(self, prompt: str, history: list | None = None, **kwargs) -&gt; AsyncGenerator[str, None]
Asynchronously stream the configured responses in order. Yields each configured response, ignoring prompt and history.

chat_stream(self, prompt: str, history: list | None = None, **kwargs) -&gt; Generator[str, None]
Not implemented yet. Calling this will raise NotImplementedError.

aembed(self, text: str, **kwargs) -&gt; list[float]
Generate an embedding for the input text.

aembed_batch(self, text_list: list[str], **kwargs: Any) -&gt; list[list[float]]
Batch generate embeddings for a list of input texts.

embed(self, text: str, **kwargs) -&gt; list[float]
Synchronously generate an embedding for a single text.

embed_batch(self, text_list: list[str], **kwargs) -&gt; list[list[float]]
Batch compute embeddings for a list of input texts.

MockEmbeddingLLM
A mock embedding provider exposing the same embedding methods for testing.

Examples
- Instantiate MockChatLLM with a predefined sequence of responses and use chat and achat_stream in tests.
- Instantiate MockEmbeddingLLM and call aembed/aembed_batch or embed/embed_batch to generate deterministic embeddings for test inputs.

Notes
- chat_stream is not implemented and will raise NotImplementedError if called.
- Both providers are designed to be deterministic and dependency-free for reliable unit tests.

## Classes

- [`MockChatLLM`](../api/classes/tests-mock-provider-mockchatllm)
- [`MockEmbeddingLLM`](../api/classes/tests-mock-provider-mockembeddingllm)

## Functions

- [`achat`](../api/functions/tests-mock-provider-achat)
- [`__init__`](../api/functions/tests-mock-provider-init)
- [`aembed_batch`](../api/functions/tests-mock-provider-aembed-batch)
- [`embed_batch`](../api/functions/tests-mock-provider-embed-batch)
- [`achat_stream`](../api/functions/tests-mock-provider-achat-stream)
- [`aembed`](../api/functions/tests-mock-provider-aembed)
- [`embed`](../api/functions/tests-mock-provider-embed)
- [`chat`](../api/functions/tests-mock-provider-chat)
- [`chat_stream`](../api/functions/tests-mock-provider-chat-stream)
- [`__init__`](../api/functions/tests-mock-provider-init)

