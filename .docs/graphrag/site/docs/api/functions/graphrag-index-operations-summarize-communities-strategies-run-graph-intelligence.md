---
sidebar_position: 148
---

# run_graph_intelligence

**File:** `graphrag/index/operations/summarize_communities/strategies.py` (lines 25-43)

## Signature

```python
def run_graph_intelligence(
    community: str | int,
    input: str,
    level: int,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    args: StrategyConfig,
) -> CommunityReport | None
```

## Description

Run the graph intelligence entity extraction strategy.

Args:
    community: Identifier for the community being processed.
    input: The input text to extract information from.
    level: The reporting level to assign to the resulting CommunityReport.
    callbacks: WorkflowCallbacks instance providing callback hooks during processing.
    cache: PipelineCache instance used for caching language model results and computations.
    args: StrategyConfig containing strategy settings, including llm configuration and extraction prompts.

Returns:
    CommunityReport | None: The produced CommunityReport if extraction succeeds, otherwise None.

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/summarize_communities/strategies.py::_run_extractor`
- `graphrag/language_model/manager.py::ModelManager`

