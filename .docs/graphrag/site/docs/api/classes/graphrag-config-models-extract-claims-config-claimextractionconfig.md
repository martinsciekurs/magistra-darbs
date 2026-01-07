---
sidebar_position: 108
---

# ClaimExtractionConfig

**File:** `graphrag/config/models/extract_claims_config.py`

## Overview

Configuration container for the claim extraction strategy used during claim extraction.

This class stores the claim extraction strategy and exposes resolution logic to produce a concrete strategy at runtime via the resolved_strategy method.

Attributes:
- strategy: The configured claim extraction strategy. If provided, resolved_strategy returns it unchanged.

Methods:
- resolved_strategy(root_dir: str, model_config: LanguageModelConfig) -&gt; dict: Get the resolved claim extraction strategy. Args: root_dir: The root directory used to resolve the graph and text prompt file paths. model_config: The LanguageModelConfig instance containing the model configuration; its model_dump() result is included in the strategy as llm. Returns: dict: The resolved strategy. If self.strategy is provided, it is returned as-is; otherwise, a dict representing the resolved strategy is constructed, including the model_config dump as llm.

## Methods

### `resolved_strategy`

```python
def resolved_strategy(
        self, root_dir: str, model_config: LanguageModelConfig
    ) -> dict
```

