---
sidebar_position: 46
---

# LanguageModelConfig

**File:** `graphrag/config/models/language_model_config.py`

## Overview

LanguageModelConfig encapsulates configuration for language model integration and performs validation for API keys, Azure AOI settings, rate limits, and model selection.

Args:
  model_type: The type of language model to configure, as defined by ModelType.
  model_provider: The provider of the model (e.g., "azure").
  encoding_model: The encoding model name used for tokenization. If omitted, it may be derived from the configured model.
  deployment_name: Azure OpenAI deployment name when using AOI; may be optional for non-AOI configurations.
  api_base: Base URL for API requests when AOI or OpenAI endpoints are used.
  api_version: API version for AOI usage.
  rate_limit_strategy: Strategy for rate limiting (e.g., None or "auto").
  requests_per_minute: Allowed requests per minute; integer &gt;= 1, "auto", or None.
  max_retries: Maximum number of retry attempts.
  tokens_per_minute: Allowed tokens per minute; integer &gt;= 1, "auto", or None.
  auth_type: Authentication type for API access (e.g., ApiKey, AzureManagedIdentity).

Returns:
  LanguageModelConfig: The same instance after validation.

Raises:
  ApiKeyMissingError: If an API key is required but not provided.
  AzureApiBaseMissingError: If the API base is required but missing.
  AzureApiVersionMissingError: If the API version is required but missing.
  ConflictingSettingsError: If settings conflict (e.g., auth/type mismatch or incompatible provider).

## Methods

### `_validate_api_key`

```python
def _validate_api_key(self) -> None
```

### `_validate_encoding_model`

```python
def _validate_encoding_model(self) -> None
```

### `_validate_deployment_name`

```python
def _validate_deployment_name(self) -> None
```

### `_validate_azure_settings`

```python
def _validate_azure_settings(self) -> None
```

### `_validate_model_provider`

```python
def _validate_model_provider(self) -> None
```

### `_validate_requests_per_minute`

```python
def _validate_requests_per_minute(self) -> None
```

### `_validate_max_retries`

```python
def _validate_max_retries(self) -> None
```

### `_validate_tokens_per_minute`

```python
def _validate_tokens_per_minute(self) -> None
```

### `_validate_api_base`

```python
def _validate_api_base(self) -> None
```

### `_validate_type`

```python
def _validate_type(self) -> None
```

### `_validate_auth_type`

```python
def _validate_auth_type(self) -> None
```

### `_validate_model`

```python
def _validate_model(self)
```

### `_validate_api_version`

```python
def _validate_api_version(self) -> None
```

