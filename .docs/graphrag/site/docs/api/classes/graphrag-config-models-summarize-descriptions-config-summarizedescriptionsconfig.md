---
sidebar_position: 140
---

# SummarizeDescriptionsConfig

**File:** `graphrag/config/models/summarize_descriptions_config.py`

## Overview

Config model that controls how descriptions are summarized and resolves the concrete summarization strategy at runtime.

Attributes:
  strategy: Optional[SummarizeStrategyType]. Custom strategy to override the default description summarization strategy. If provided, this strategy will be used during strategy resolution by resolved_strategy(). Default: None.

Methods:
  resolved_strategy(self, root_dir: str, model_config: LanguageModelConfig) -&gt; Any
    Get the resolved description summarization strategy.
    root_dir: The root directory used to resolve graph and text prompt file paths.
    model_config: The LanguageModelConfig instance; its model_dump() result is included in the strategy under the key llm.
    Returns: The resolved strategy representation. The exact type depends on the underlying components; it could be a dict or another strategy object. If a custom strategy was provided via self.strategy, that strategy participates in resolution and may appear in the final result.
    Raises: Exceptions raised by underlying components during strategy resolution may propagate to callers.

## Methods

### `resolved_strategy`

```python
def resolved_strategy(
        self, root_dir: str, model_config: LanguageModelConfig
    ) -> dict
```

