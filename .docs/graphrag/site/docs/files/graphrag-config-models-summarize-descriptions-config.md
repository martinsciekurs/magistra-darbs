---
sidebar_position: 29
---

# graphrag/config/models/summarize_descriptions_config.py

## Overview

Config model that controls how descriptions are summarized and resolves the concrete summarization strategy at runtime.

Overview
This module defines SummarizeDescriptionsConfig, a Pydantic BaseModel used to configure the summarization of descriptions. It supports an optional custom strategy that, when provided, overrides the default strategy during resolution. The concrete strategy is resolved at runtime by resolved_strategy(), which takes a root directory and a LanguageModelConfig, and returns a dictionary describing the chosen strategy. The llm portion of the model_config (via model_dump()) is included in the resolved strategy.

Public exports
- SummarizeDescriptionsConfig: Pydantic config model with strategy attribute and resolved_strategy() method.

Attributes
- strategy: Optional[SummarizeStrategyType]. Custom strategy to override the default description summarization strategy. Default: None.

Methods
- resolved_strategy(self, root_dir: str, model_config: LanguageModelConfig) -&gt; dict: Get the resolved description summarization strategy.
  Args:
    root_dir: The root directory used to resolve the graph and text prompt file paths.
    model_config: The LanguageModelConfig instance containing the model configuration; its model_dump() result is included in the strategy as llm.
  Returns:
    dict: The resolved strategy.

## Classes

- [`SummarizeDescriptionsConfig`](../api/classes/graphrag-config-models-summarize-descriptions-config-summarizedescriptionsconfig)

## Functions

- [`resolved_strategy`](../api/functions/graphrag-config-models-summarize-descriptions-config-resolved-strategy)

