---
sidebar_position: 148
---

# graphrag/language_model/providers/fnllm/utils.py

## Overview

Utilities for FNLLM-based OpenAI provider.

This module contains internal helpers used by Graphrag's FNLLM OpenAI provider. It offers
support for error handling, synchronous execution of coroutines, derivation of OpenAI API
parameters from language model configurations, and a bridge to a pipeline cache via
FNLLMCacheProvider. It supports both Azure OpenAI and Public OpenAI configurations and
includes special handling for reasoning models.

Exports:
- _create_error_handler(callbacks: WorkflowCallbacks) -&gt; ErrorHandlerFn
- run_coroutine_sync(coroutine: Coroutine[Any, Any, T]) -&gt; T
- is_reasoning_model(model: str) -&gt; bool
- _create_cache(cache: PipelineCache | None, name: str) -&gt; FNLLMCacheProvider | None
- on_error(error: BaseException | None = None, stack: str | None = None, details: dict | None = None) -&gt; None
- get_openai_model_parameters_from_dict(config: dict[str, Any]) -&gt; dict[str, Any]
- get_openai_model_parameters_from_config(config: LanguageModelConfig) -&gt; dict[str, Any]
- _create_openai_config(config: LanguageModelConfig, azure: bool) -&gt; OpenAIConfig

Notes:
- This module relies on types and utilities from fnllm and graphrag; it is intended for internal use
  by the FNLLM provider.

## Functions

- [`_create_error_handler`](../api/functions/graphrag-language-model-providers-fnllm-utils-create-error-handler)
- [`run_coroutine_sync`](../api/functions/graphrag-language-model-providers-fnllm-utils-run-coroutine-sync)
- [`is_reasoning_model`](../api/functions/graphrag-language-model-providers-fnllm-utils-is-reasoning-model)
- [`_create_cache`](../api/functions/graphrag-language-model-providers-fnllm-utils-create-cache)
- [`on_error`](../api/functions/graphrag-language-model-providers-fnllm-utils-on-error)
- [`get_openai_model_parameters_from_dict`](../api/functions/graphrag-language-model-providers-fnllm-utils-get-openai-model-parameters-from-dict)
- [`get_openai_model_parameters_from_config`](../api/functions/graphrag-language-model-providers-fnllm-utils-get-openai-model-parameters-from-config)
- [`_create_openai_config`](../api/functions/graphrag-language-model-providers-fnllm-utils-create-openai-config)

