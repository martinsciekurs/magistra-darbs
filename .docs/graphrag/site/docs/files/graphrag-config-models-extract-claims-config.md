---
sidebar_position: 24
---

# graphrag/config/models/extract_claims_config.py

## Overview

Configuration model and resolver for claim extraction strategy.

Purpose:
  This module defines a Pydantic-based configuration container for the claim extraction strategy used during claim extraction and runtime logic to resolve a concrete strategy.

Exports:
  - ClaimExtractionConfig: configuration container that stores the claim extraction strategy and exposes resolution logic via resolved_strategy.
  - resolved_strategy: method of ClaimExtractionConfig that resolves the concrete strategy at runtime.

Summary:
  The ClaimExtractionConfig class stores the configured claim extraction strategy. If provided, the strategy is returned unchanged by resolved_strategy; otherwise, a default strategy dictionary is built, incorporating the model configuration (via model_dump()) as llm and using the root_dir to resolve graph and text prompt file paths.

Args (for resolved_strategy):
  root_dir: The root directory used to resolve the graph and text prompt file paths.
  model_config: The LanguageModelConfig instance containing the model configuration; its model_dump() result is included in the strategy as llm.

Returns:
  dict: The resolved strategy.

Raises:
  None

## Classes

- [`ClaimExtractionConfig`](../api/classes/graphrag-config-models-extract-claims-config-claimextractionconfig)

## Functions

- [`resolved_strategy`](../api/functions/graphrag-config-models-extract-claims-config-resolved-strategy)

