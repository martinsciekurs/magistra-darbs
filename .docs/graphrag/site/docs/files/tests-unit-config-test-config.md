---
sidebar_position: 247
---

# tests/unit/config/test_config.py

## Overview

Unit tests for Graphrag configuration creation and loading.

This module contains unit tests that validate Graphrag configuration handling, including ensuring required API keys are present for OpenAI and Azure OpenAI models, detecting conflicting authentication configurations, and verifying configuration loading with defaults, minimal configurations, and CLI/environment overrides. It exercises create_graphrag_config and load_config together with test utilities to assert correct behavior and error handling.

Key exports
- test_missing_openai_required_api_key
- test_missing_azure_api_key
- test_conflicting_auth_type
- test_conflicting_azure_api_key
- test_missing_azure_api_base
- test_missing_azure_api_version
- test_default_config
- test_load_minimal_config
- test_load_config_with_cli_overrides
- test_load_config_missing_env_vars

Note: Tests rely on pydantic ValidationError to indicate invalid configurations, such as missing API keys or invalid auth_type scenarios, and may exercise environment/CLI overrides during loading.

## Functions

- [`test_missing_openai_required_api_key`](../api/functions/tests-unit-config-test-config-test-missing-openai-required-api-key)
- [`test_missing_azure_api_key`](../api/functions/tests-unit-config-test-config-test-missing-azure-api-key)
- [`test_conflicting_auth_type`](../api/functions/tests-unit-config-test-config-test-conflicting-auth-type)
- [`test_conflicting_azure_api_key`](../api/functions/tests-unit-config-test-config-test-conflicting-azure-api-key)
- [`test_missing_azure_api_base`](../api/functions/tests-unit-config-test-config-test-missing-azure-api-base)
- [`test_missing_azure_api_version`](../api/functions/tests-unit-config-test-config-test-missing-azure-api-version)
- [`test_default_config`](../api/functions/tests-unit-config-test-config-test-default-config)
- [`test_load_minimal_config`](../api/functions/tests-unit-config-test-config-test-load-minimal-config)
- [`test_load_config_with_cli_overrides`](../api/functions/tests-unit-config-test-config-test-load-config-with-cli-overrides)
- [`test_load_config_missing_env_vars`](../api/functions/tests-unit-config-test-config-test-load-config-missing-env-vars)

