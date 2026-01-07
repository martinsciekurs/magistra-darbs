---
sidebar_position: 144
---

# graphrag/language_model/protocol/base.py

## Overview

Protocols for language model interfaces used by Graphrag.

This module defines Protocols for chat-based language models and embeddings generation. It declares the required method signatures that concrete models must implement, covering both synchronous and asynchronous operation and support for streaming where applicable.

Key exports:
- ChatModel: Protocol for chat-based language model interfaces with methods achat, chat, chat_stream, and achat_stream.
- EmbeddingModel: Protocol for embedding generation interfaces with methods aembed_batch, embed, embed_batch, and aembed.

Summary:
The protocols describe the contracts for generating text responses and embeddings from language models, including optional conversation history, batch processing, and streaming capabilities.

## Classes

- [`ChatModel`](../api/classes/graphrag-language-model-protocol-base-chatmodel)
- [`EmbeddingModel`](../api/classes/graphrag-language-model-protocol-base-embeddingmodel)

## Functions

- [`achat`](../api/functions/graphrag-language-model-protocol-base-achat)
- [`aembed_batch`](../api/functions/graphrag-language-model-protocol-base-aembed-batch)
- [`chat`](../api/functions/graphrag-language-model-protocol-base-chat)
- [`embed`](../api/functions/graphrag-language-model-protocol-base-embed)
- [`embed_batch`](../api/functions/graphrag-language-model-protocol-base-embed-batch)
- [`aembed`](../api/functions/graphrag-language-model-protocol-base-aembed)
- [`chat_stream`](../api/functions/graphrag-language-model-protocol-base-chat-stream)
- [`achat_stream`](../api/functions/graphrag-language-model-protocol-base-achat-stream)

