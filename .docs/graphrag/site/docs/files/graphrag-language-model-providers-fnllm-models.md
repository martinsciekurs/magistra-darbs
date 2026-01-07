---
sidebar_position: 147
---

# graphrag/language_model/providers/fnllm/models.py

## Overview

FNLLM-based language model providers for Graphrag.

This module implements concrete providers for embeddings and chat using FNLLM's OpenAI and Azure OpenAI interfaces. It wires FNLLM clients to Graphrag's language-model framework, deriving configuration from LanguageModelConfig and integrating with Graphrag's caching (PipelineCache), event handling, and error utilities. The providers support synchronous and asynchronous operations, including streaming variants, and can be wrapped with optional WorkflowCallbacks.

Key exports:
- OpenAIEmbeddingFNLLM: Embedding FNLLM provider for OpenAI embeddings
- OpenAIChatFNLLM: Chat FNLLM provider for OpenAI chat
- AzureOpenAIEmbeddingFNLLM: Embedding FNLLM provider for Azure OpenAI embeddings
- AzureOpenAIChatFNLLM: Chat FNLLM provider for Azure OpenAI chat

Brief summary:
Offers embedding and chat providers backed by FNLLM LLMs, exposing synchronous, asynchronous, and streaming interfaces that integrate with Graphrag's configuration, caching, and workflow systems.

## Classes

- [`OpenAIEmbeddingFNLLM`](../api/classes/graphrag-language-model-providers-fnllm-models-openaiembeddingfnllm)
- [`OpenAIChatFNLLM`](../api/classes/graphrag-language-model-providers-fnllm-models-openaichatfnllm)
- [`AzureOpenAIEmbeddingFNLLM`](../api/classes/graphrag-language-model-providers-fnllm-models-azureopenaiembeddingfnllm)
- [`AzureOpenAIChatFNLLM`](../api/classes/graphrag-language-model-providers-fnllm-models-azureopenaichatfnllm)

## Functions

- [`aembed_batch`](../api/functions/graphrag-language-model-providers-fnllm-models-aembed-batch)
- [`chat_stream`](../api/functions/graphrag-language-model-providers-fnllm-models-chat-stream)
- [`aembed`](../api/functions/graphrag-language-model-providers-fnllm-models-aembed)
- [`achat`](../api/functions/graphrag-language-model-providers-fnllm-models-achat)
- [`achat`](../api/functions/graphrag-language-model-providers-fnllm-models-achat)
- [`achat_stream`](../api/functions/graphrag-language-model-providers-fnllm-models-achat-stream)
- [`aembed_batch`](../api/functions/graphrag-language-model-providers-fnllm-models-aembed-batch)
- [`achat_stream`](../api/functions/graphrag-language-model-providers-fnllm-models-achat-stream)
- [`aembed`](../api/functions/graphrag-language-model-providers-fnllm-models-aembed)
- [`chat_stream`](../api/functions/graphrag-language-model-providers-fnllm-models-chat-stream)
- [`chat`](../api/functions/graphrag-language-model-providers-fnllm-models-chat)
- [`embed_batch`](../api/functions/graphrag-language-model-providers-fnllm-models-embed-batch)
- [`embed`](../api/functions/graphrag-language-model-providers-fnllm-models-embed)
- [`chat`](../api/functions/graphrag-language-model-providers-fnllm-models-chat)
- [`embed_batch`](../api/functions/graphrag-language-model-providers-fnllm-models-embed-batch)
- [`embed`](../api/functions/graphrag-language-model-providers-fnllm-models-embed)
- [`__init__`](../api/functions/graphrag-language-model-providers-fnllm-models-init)
- [`__init__`](../api/functions/graphrag-language-model-providers-fnllm-models-init)
- [`__init__`](../api/functions/graphrag-language-model-providers-fnllm-models-init)
- [`__init__`](../api/functions/graphrag-language-model-providers-fnllm-models-init)

