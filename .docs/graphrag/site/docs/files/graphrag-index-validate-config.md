---
sidebar_position: 117
---

# graphrag/index/validate_config.py

## Overview

GraphRag configuration validation utility.

Purpose:
Provide pre-deployment runtime validation of the GraphRagConfig by performing lightweight per-model checks to surface typos or misconfigurations in deployment names.

Key exports:
- validate_config_names(parameters: GraphRagConfig) -&gt; None: Validate the config by issuing quick per-model test messages for each configured model to surface invalid names.

Brief summary:
Exposes a single function that validates model deployment names through lightweight test messages. On failure, validation may terminate the process (exit with status 1 via SystemExit) or raise an exception depending on runtime and environment. A successful validation yields a None return.

Args:
- parameters: GraphRagConfig containing models to validate.

Returns:
- None

Raises:
- SystemExit: If validation fails and the runtime terminates the process.
- ValueError, TypeError, or other exceptions may be raised if inputs are invalid or configurations are malformed.

Edge cases:
- Empty models list, missing deployment names, or unusual characters in model names.

## Functions

- [`validate_config_names`](../api/functions/graphrag-index-validate-config-validate-config-names)

