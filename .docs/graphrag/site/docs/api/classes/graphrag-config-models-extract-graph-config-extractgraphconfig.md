---
sidebar_position: 139
---

# ExtractGraphConfig

**File:** `graphrag/config/models/extract_graph_config.py`

## Overview

ExtractGraphConfig is a configuration container for graph extraction settings and the resolution of the final entity extraction strategy.

Purpose:
This class stores an optional strategy configuration and provides a method to resolve the active strategy using a root directory and a LanguageModelConfig. The resolved strategy is returned as a dict and may incorporate the LanguageModelConfig data via its model_dump() as llm.

Attributes:
strategy: Optional dict representing the base configuration for the extraction strategy. If provided, it participates in determining the final resolved strategy.

Args:
strategy: Optional dict. Base configuration for the extraction strategy used during resolution.

Returns:
dict: The final, resolved extraction strategy produced by resolving the configuration against the given root_dir and LanguageModelConfig. If a base strategy was provided, the result is derived from that configuration; otherwise a default strategy is constructed using graphrag_config_defaults and the provided inputs.

Raises:
ValueError: If root_dir is not a valid non-empty string or the model_config is invalid.
TypeError: If model_config is not an instance of LanguageModelConfig.
NotImplementedError: If strategy resolution is not implemented for the given inputs.

Example:
config = ExtractGraphConfig(strategy=&#123;'type': 'entity', 'params': &#123;&#125;&#125;)
resolved = config.resolved_strategy('/path/to/root', LanguageModelConfig(...))

## Methods

### `resolved_strategy`

```python
def resolved_strategy(
        self, root_dir: str, model_config: LanguageModelConfig
    ) -> dict
```

