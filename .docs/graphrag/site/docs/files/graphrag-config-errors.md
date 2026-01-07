---
sidebar_position: 20
---

# graphrag/config/errors.py

## Overview

GraphRAG configuration and internal API error definitions.

This module defines internal exception classes used to signal missing or misconfigured
GraphRAG settings related to Azure/API versions and keys, as well as missing language model
configurations. The key exports are the five exception classes: AzureApiBaseMissingError,
ApiKeyMissingError, LanguageModelConfigMissingError, ConflictingSettingsError, and AzureApiVersionMissingError.
Each class provides an initializer that formats an informative error message based on the related
LLM type, key, or authentication context as described in its docstring.

Exports:
  AzureApiBaseMissingError
  ApiKeyMissingError
  LanguageModelConfigMissingError
  ConflictingSettingsError
  AzureApiVersionMissingError

## Classes

- [`AzureApiBaseMissingError`](../api/classes/graphrag-config-errors-azureapibasemissingerror)
- [`ApiKeyMissingError`](../api/classes/graphrag-config-errors-apikeymissingerror)
- [`LanguageModelConfigMissingError`](../api/classes/graphrag-config-errors-languagemodelconfigmissingerror)
- [`ConflictingSettingsError`](../api/classes/graphrag-config-errors-conflictingsettingserror)
- [`AzureApiVersionMissingError`](../api/classes/graphrag-config-errors-azureapiversionmissingerror)

## Functions

- [`__init__`](../api/functions/graphrag-config-errors-init)
- [`__init__`](../api/functions/graphrag-config-errors-init)
- [`__init__`](../api/functions/graphrag-config-errors-init)
- [`__init__`](../api/functions/graphrag-config-errors-init)
- [`__init__`](../api/functions/graphrag-config-errors-init)

