---
sidebar_position: 163
---

# graphrag/language_model/providers/litellm/types.py

## Overview

Module providing typed aliases and lightweight wrappers for Litellm types used by graphrag's language model providers.

This module centralizes interoperability between litellm and OpenAI-compatible APIs by exposing a clean, deduplicated public API surface. It defines strongly typed aliases for common litellm/OpenAI types and a small set of wrapper classes that provide a consistent interface for chat completions and embeddings. This reduces repetition and improves type safety across graphrag's litellm-backed providers.

Public API:
- LMChatCompletionMessageParam
- LMChatCompletion
- LMChoice
- LMChatCompletionMessage
- LMChatCompletionChunk
- LMChoiceChunk
- LMChoiceDelta
- LMCompletionUsage
- LMPromptTokensDetails
- LMCompletionTokensDetails
- LMEmbeddingResponse
- LMEmbedding
- LMEmbeddingUsage
- LitellmRequestFunc
- AsyncLitellmRequestFunc
- FixedModelCompletion
- FixedModelEmbedding
- AFixedModelCompletion
- AFixedModelEmbedding

Typical usage:
Typical usage involves importing the aliases to annotate provider implementations, and using the wrapper classes to perform chat completions or embeddings in a type-safe manner. Import the needed symbols from graphrag.language_model.providers.litellm.types and reuse them across providers.

Notes:
This module exposes types and interfaces only; it does not perform API calls. Import-time dependencies may raise ImportError if optional packages are unavailable, but the public API surface remains a stable, deduplicated contract.

## Classes

- [`AFixedModelCompletion`](../api/classes/graphrag-language-model-providers-litellm-types-afixedmodelcompletion)
- [`AFixedModelEmbedding`](../api/classes/graphrag-language-model-providers-litellm-types-afixedmodelembedding)
- [`FixedModelCompletion`](../api/classes/graphrag-language-model-providers-litellm-types-fixedmodelcompletion)
- [`AsyncLitellmRequestFunc`](../api/classes/graphrag-language-model-providers-litellm-types-asynclitellmrequestfunc)
- [`FixedModelEmbedding`](../api/classes/graphrag-language-model-providers-litellm-types-fixedmodelembedding)
- [`LitellmRequestFunc`](../api/classes/graphrag-language-model-providers-litellm-types-litellmrequestfunc)

## Functions

- [`__call__`](../api/functions/graphrag-language-model-providers-litellm-types-call)
- [`__call__`](../api/functions/graphrag-language-model-providers-litellm-types-call)
- [`__call__`](../api/functions/graphrag-language-model-providers-litellm-types-call)
- [`__call__`](../api/functions/graphrag-language-model-providers-litellm-types-call)
- [`__call__`](../api/functions/graphrag-language-model-providers-litellm-types-call)
- [`__call__`](../api/functions/graphrag-language-model-providers-litellm-types-call)

