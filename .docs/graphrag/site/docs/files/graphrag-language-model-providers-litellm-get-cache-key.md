---
sidebar_position: 151
---

# graphrag/language_model/providers/litellm/get_cache_key.py

## Overview

Utilities for generating cache keys for Litellm-based language model providers.

Purpose
This module provides helper functions to derive deterministic cache keys based on a language model configuration and inputs such as messages or prompt input. It mirrors the key-generation approach used by fnllm.

Key exports
- _get_parameters(model_config: LanguageModelConfig, **kwargs: Any) -&gt; dict[str, Any]
- _hash(input: str) -&gt; str
- get_cache_key(model_config: LanguageModelConfig, prefix: str, messages: str | None = None, input: str | None = None, **kwargs: Any) -&gt; str

Brief summary
- _get_parameters selects the parameters that influence the cache key (excluding request timeout).
- _hash returns the SHA-256 hex digest of a string.
- get_cache_key builds a complete cache key using the model configuration, prefix, optional messages or input, and any additional kwargs, following the pattern used in fnllm's cache key generation.

## Functions

- [`_get_parameters`](../api/functions/graphrag-language-model-providers-litellm-get-cache-key-get-parameters)
- [`_hash`](../api/functions/graphrag-language-model-providers-litellm-get-cache-key-hash)
- [`get_cache_key`](../api/functions/graphrag-language-model-providers-litellm-get-cache-key-get-cache-key)

