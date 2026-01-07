---
sidebar_position: 90
---

# TextEmbeddingConfig

**File:** `graphrag/config/models/text_embedding_config.py`

## Overview

TextEmbeddingConfig: Configuration holder for the text embedding strategy used to embed text in Graphrag. It centralizes the selection between a user-provided custom strategy and a default strategy resolved from LanguageModelConfig and graphrag_config_defaults.

Initialization: __init__(strategy: dict | None = None) initializes the configuration with an optional custom strategy. If a strategy is provided, resolved_strategy(model_config) will return this value; otherwise, a default strategy is resolved based on the given LanguageModelConfig and the configured defaults.

Attributes:
- strategy: dict | None - Custom text embedding strategy to use when provided; otherwise None.

Methods:
- resolved_strategy(model_config: LanguageModelConfig) -&gt; dict - Returns the resolved text embedding strategy. If a custom strategy is provided via self.strategy, that value is returned; otherwise, a default strategy dictionary is produced. The default includes at least the key 'type' set to TextEmbedStrategyType.openai and other keys derived from the language model configuration and graphrag_config_defaults.

Raises:
- pydantic.ValidationError: if initialization receives an invalid strategy type or shape.
- Exception during resolution if required configuration is missing or invalid.

## Methods

### `resolved_strategy`

```python
def resolved_strategy(self, model_config: LanguageModelConfig) -> dict
```

