---
sidebar_position: 27
---

# graphrag/config/models/language_model_config.py

## Overview

LanguageModelConfig: configuration container and validation for Graphrag's language model integration.

This module defines LanguageModelConfig, a Pydantic-based model that centralizes settings for language model usage, including model_type, model_provider, encoding_model, rate limits, authentication, and Azure OpenAI (AOI) related settings. It provides validation hooks that enforce correct API keys, encoding model generation, Azure deployment details, and related constraints before the configuration is used by the rest of the system.

Exports
- LanguageModelConfig: Main configuration class used to configure and validate language model integration.

## Classes

- [`LanguageModelConfig`](../api/classes/graphrag-config-models-language-model-config-languagemodelconfig)

## Functions

- [`_validate_api_key`](../api/functions/graphrag-config-models-language-model-config-validate-api-key)
- [`_validate_encoding_model`](../api/functions/graphrag-config-models-language-model-config-validate-encoding-model)
- [`_validate_deployment_name`](../api/functions/graphrag-config-models-language-model-config-validate-deployment-name)
- [`_validate_azure_settings`](../api/functions/graphrag-config-models-language-model-config-validate-azure-settings)
- [`_validate_model_provider`](../api/functions/graphrag-config-models-language-model-config-validate-model-provider)
- [`_validate_requests_per_minute`](../api/functions/graphrag-config-models-language-model-config-validate-requests-per-minute)
- [`_validate_max_retries`](../api/functions/graphrag-config-models-language-model-config-validate-max-retries)
- [`_validate_tokens_per_minute`](../api/functions/graphrag-config-models-language-model-config-validate-tokens-per-minute)
- [`_validate_api_base`](../api/functions/graphrag-config-models-language-model-config-validate-api-base)
- [`_validate_type`](../api/functions/graphrag-config-models-language-model-config-validate-type)
- [`_validate_auth_type`](../api/functions/graphrag-config-models-language-model-config-validate-auth-type)
- [`_validate_model`](../api/functions/graphrag-config-models-language-model-config-validate-model)
- [`_validate_api_version`](../api/functions/graphrag-config-models-language-model-config-validate-api-version)

