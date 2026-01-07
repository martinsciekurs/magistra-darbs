---
sidebar_position: 160
---

# run_graph_intelligence

**File:** `graphrag/index/operations/summarize_descriptions/graph_intelligence_strategy.py` (lines 23-38)

## Signature

```python
def run_graph_intelligence(
    id: str | tuple[str, str],
    descriptions: list[str],
    cache: PipelineCache,
    args: StrategyConfig,
) -> SummarizedDescriptionResult
```

## Description

Run the graph intelligence entity extraction strategy using a language model to summarize the provided descriptions.

Args:
    id: str | tuple[str, str]
        Identifier for the target item; could be a string or a pair of strings.
    descriptions: list[str]
        The descriptions to summarize.
    cache: PipelineCache
        Cache to use for the language model and computations.
    args: StrategyConfig
        Strategy configuration, including llm settings and summarization prompts.

Returns:
    SummarizedDescriptionResult
        The summarized description result containing the id and generated description.

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/summarize_descriptions/graph_intelligence_strategy.py::run_summarize_descriptions`
- `graphrag/language_model/manager.py::ModelManager`

