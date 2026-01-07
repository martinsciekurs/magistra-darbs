---
sidebar_position: 149
---

# graphrag/language_model/providers/litellm/chat_model.py

## Overview

Graphrag Litellm chat model wrapper with streaming, caching, and resilience features.

Overview:
This module provides a Graphrag wrapper around a Litellm chat model. It composes the underlying Litellm client with request wrappers for caching, logging, rate limiting, and retries, and integrates with Graphrag's PipelineCache and LanguageModelConfig to offer a configurable, resilient language model interface. The main export is the LitellmChatModel class, which implements streaming and non-streaming chat capabilities.

Public exports:
- LitellmChatModel: Wrapper around a Litellm chat model that supports streaming, caching, and resilience features.

Public methods on LitellmChatModel:
- achat_stream(prompt: str, history: list | None = None, **kwargs: Any) -&gt; AsyncGenerator[str, None]
  Generate a response for the given prompt as a stream of strings.
- chat(prompt: str, history: list | None = None, **kwargs: Any) -&gt; MR
  Generate a response for the given prompt and history synchronously (returns a ModelResponse alias MR).
- chat_stream(prompt: str, history: list | None = None, **kwargs: Any) -&gt; Generator[str, None]
  Generate a response for the given prompt and history as a string stream.
- achat(prompt: str, history: list | None = None, **kwargs: Any) -&gt; MR
  Asynchronously generate a response for the given prompt and history.

Notes:
- The implementation wraps base litellm completion and acompletion with configured wrappers (with_cache, with_logging, with_rate_limiter, with_retries).
- Uses PipelineCache and LanguageModelConfig for configuration and caching; ModelResponse alias MR is used for return types.

## Classes

- [`LitellmChatModel`](../api/classes/graphrag-language-model-providers-litellm-chat-model-litellmchatmodel)

## Functions

- [`_get_kwargs`](../api/functions/graphrag-language-model-providers-litellm-chat-model-get-kwargs)
- [`achat_stream`](../api/functions/graphrag-language-model-providers-litellm-chat-model-achat-stream)
- [`chat`](../api/functions/graphrag-language-model-providers-litellm-chat-model-chat)
- [`chat_stream`](../api/functions/graphrag-language-model-providers-litellm-chat-model-chat-stream)
- [`_base_completion`](../api/functions/graphrag-language-model-providers-litellm-chat-model-base-completion)
- [`achat`](../api/functions/graphrag-language-model-providers-litellm-chat-model-achat)
- [`_base_acompletion`](../api/functions/graphrag-language-model-providers-litellm-chat-model-base-acompletion)
- [`_create_base_completions`](../api/functions/graphrag-language-model-providers-litellm-chat-model-create-base-completions)
- [`_create_completions`](../api/functions/graphrag-language-model-providers-litellm-chat-model-create-completions)
- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-chat-model-init)

