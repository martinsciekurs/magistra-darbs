---
sidebar_position: 159
---

# run_summarize_descriptions

**File:** `graphrag/index/operations/summarize_descriptions/graph_intelligence_strategy.py` (lines 41-65)

## Signature

```python
def run_summarize_descriptions(
    model: ChatModel,
    id: str | tuple[str, str],
    descriptions: list[str],
    args: StrategyConfig,
) -> SummarizedDescriptionResult
```

## Description

Run the entity extraction chain to summarize descriptions for graph intelligence.

Args:
    model: ChatModel
        The chat model instance used to invoke summarization.
    id: str | tuple[str, str]
        Identifier for the target item; could be a string or a pair of strings.
    descriptions: list[str]
        The descriptions to summarize.
    args: StrategyConfig
        Strategy configuration, including max_input_tokens, max_summary_length, and optional summarize_prompt.

Returns:
    SummarizedDescriptionResult
        The summarized description along with its identifier.

Raises:
    Exception
        If the underlying extraction process raises an exception during processing.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_descriptions/description_summary_extractor.py::SummarizeExtractor`
- `graphrag/index/operations/summarize_descriptions/typing.py::SummarizedDescriptionResult`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_descriptions/graph_intelligence_strategy.py::run_graph_intelligence`

