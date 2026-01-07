---
sidebar_position: 97
---

# CommunityReportsConfig

**File:** `graphrag/config/models/community_reports_config.py`

## Overview

Configuration model for extracting and summarizing community reports in GraphRag.

Overview:
- This Pydantic BaseModel stores the configuration that governs how community reports are produced and prepared for downstream processing. It supports resolving a concrete strategy to be used by other components, either by returning a provided strategy or by constructing a default one from configured defaults and the supplied language model configuration.

Attributes:
- strategy: Optional[CreateCommunityReportsStrategyType]. The optional strategy configuration for community report extraction. If provided, the resolved_strategy method will return this strategy as-is. If omitted, a default strategy is constructed from graphrag_config_defaults and later augmented with the llm from a LanguageModelConfig when resolved.

Resolved strategy behavior:
- If strategy is provided, resolved_strategy returns the provided strategy unchanged.
- If strategy is None, resolved_strategy builds a default strategy from graphrag_config_defaults and populates its llm field with the serialized model configuration obtained from model_config.model_dump(). This enables downstream components to know which language model to use during execution.

Methods:
- resolved_strategy(root_dir: str, model_config: LanguageModelConfig) -&gt; dict
  Returns: A dictionary describing the resolved community report extraction strategy, ready for downstream processing.

Raises:
- ValidationError: If invalid data is provided to initialize the model (e.g., missing required fields or inappropriate types).

Examples:
- Provided strategy:
  config = CommunityReportsConfig(strategy=&#123;"type": "custom", "params": &#123;"foo": 1&#125;&#125;)
  resolved = config.resolved_strategy("/root", some_model_config)
  # resolved is exactly config.strategy

- No strategy provided:
  config = CommunityReportsConfig(strategy=None)
  resolved = config.resolved_strategy("/root", some_model_config)
  # resolved is a dict built from graphrag_config_defaults with llm populated from some_model_config.model_dump().

## Methods

### `resolved_strategy`

```python
def resolved_strategy(
        self, root_dir: str, model_config: LanguageModelConfig
    ) -> dict
```

