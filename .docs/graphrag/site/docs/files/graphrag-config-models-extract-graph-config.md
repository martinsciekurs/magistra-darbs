---
sidebar_position: 25
---

# graphrag/config/models/extract_graph_config.py

## Overview

Module for configuring and resolving the active graph extraction strategy used by Graphrag's extract-graph pipeline. It wires default configuration, a LanguageModelConfig, and the extract-graph strategy typing to produce a concrete, runtime-ready strategy dictionary for downstream graph extraction tasks.

Public API:
- ExtractGraphConfig: A Pydantic model that stores optional graph extraction settings. It exposes an optional strategy field (strategy: Optional[ExtractEntityStrategyType]); if provided, this overrides defaults, otherwise graphrag_config_defaults are used during resolution.
- resolved_strategy(self, root_dir: str, model_config: LanguageModelConfig) -&gt; dict: Resolves and returns the active extraction strategy as a dict. root_dir is a string path used to resolve graph and text prompt file paths; the LanguageModelConfig's model_dump() result is included in the strategy under the key llm.

Returns:
- dict: The resolved strategy describing the active extraction configuration. The dict may include an llm entry containing the serialized LanguageModelConfig data via model_dump().

Raises:
- ValueError, TypeError, FileNotFoundError, OSError (and other I/O/validation errors) may be raised during validation or resolution of the strategy depending on the provided configuration and filesystem state.

Fields:
- strategy: Optional[ExtractEntityStrategyType]. An optional override for the extraction strategy; when omitted, defaults from graphrag_config_defaults are applied during resolution.

Notes:
- The resolved strategy is intended for downstream graph extraction tasks and represents the final, runtime-ready configuration.

Example:
- Given a LanguageModelConfig instance and a root directory path, calling resolved_strategy(root_dir, model_config) yields a dict describing the active strategy, with llm containing the serialized model configuration.

## Classes

- [`ExtractGraphConfig`](../api/classes/graphrag-config-models-extract-graph-config-extractgraphconfig)

## Functions

- [`resolved_strategy`](../api/functions/graphrag-config-models-extract-graph-config-resolved-strategy)

