---
sidebar_position: 23
---

# graphrag/config/models/community_reports_config.py

## Overview

Module for configuring and resolving the strategy used to extract and summarize community reports in GraphRag.

Overview:
- Defines CommunityReportsConfig, a Pydantic BaseModel that stores configuration governing how community reports are produced and prepared for downstream processing.
- Exposes a method resolved_strategy(self, root_dir: str, model_config: LanguageModelConfig) -&gt; dict that returns a concrete strategy dict. If a strategy is provided on the instance, that dict is returned as-is; otherwise a default strategy is constructed from graphrag_config_defaults and the given LanguageModelConfig.

Public exports:
- CommunityReportsConfig: Pydantic model representing the configuration for community report extraction and summarization.

Key data types:
- LanguageModelConfig: Used as input to resolved_strategy; its model_dump() result is included in the strategy under the key llm when constructing the default strategy.

Resolved strategy behavior:
- If self.strategy is provided, it is returned unchanged.
- If not provided, a default strategy is built using graphrag_config_defaults and the supplied model_config, including model_dump() output as llm.

Returns:
- dict: The resolved strategy to be applied to community report extraction and summarization.

Raises:
- Not explicitly documented in this module; exceptions from underlying components may propagate to the caller.

Usage example:
- cfg = CommunityReportsConfig(...)  # may include an optional strategy
- strategy = cfg.resolved_strategy(root_dir="/path/to/project", model_config=LanguageModelConfig(...))

Edge cases:
- The behavior depends on whether a strategy is provided on the instance; if so, that strategy is used as-is. Otherwise, defaults are constructed from graphrag_config_defaults and the given model_config.

## Classes

- [`CommunityReportsConfig`](../api/classes/graphrag-config-models-community-reports-config-communityreportsconfig)

## Functions

- [`resolved_strategy`](../api/functions/graphrag-config-models-community-reports-config-resolved-strategy)

