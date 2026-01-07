---
sidebar_position: 30
---

# graphrag/config/models/text_embedding_config.py

## Overview

TextEmbeddingConfig module for Graphrag.

This module defines TextEmbeddingConfig, a Pydantic-based configuration holder that governs the text embedding strategy used by Graphrag. It encapsulates an optional user-provided custom strategy and provides a resolution path to a concrete strategy that the embedding process will use, by combining the custom strategy (if present) with a default strategy resolved from LanguageModelConfig and graphrag_config_defaults.

Public API

- TextEmbeddingConfig: A Pydantic model that stores an optional strategy dictionary used to embed text. Field: strategy: dict | None = None. Inheritance: TextEmbeddingConfig(BaseModel).

Public methods

- resolved_strategy(model_config: LanguageModelConfig) -&gt; dict: Return the concrete text embedding strategy to apply. If a custom strategy was provided via self.strategy, that dictionary is returned unchanged; otherwise, a default strategy dictionary is returned with the key 'type' set to TextEmbedStrategyType.openai, and any additional required parameters derived from the supplied model_config and graphrag_config_defaults.

Notes

- This class inherits from pydantic.BaseModel.
- The field strategy is optional; if omitted, resolution falls back to defaults.

Error behavior

- Construction may raise pydantic.ValidationError if types are invalid.

## Classes

- [`TextEmbeddingConfig`](../api/classes/graphrag-config-models-text-embedding-config-textembeddingconfig)

## Functions

- [`resolved_strategy`](../api/functions/graphrag-config-models-text-embedding-config-resolved-strategy)

