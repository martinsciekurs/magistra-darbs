---
sidebar_position: 117
---

# run_graph_intelligence

**File:** `graphrag/index/operations/extract_graph/graph_intelligence_strategy.py` (lines 26-42)

## Signature

```python
def run_graph_intelligence(
    docs: list[Document],
    entity_types: EntityTypes,
    cache: PipelineCache,
    args: StrategyConfig,
) -> EntityExtractionResult
```

## Description

Run the graph intelligence entity extraction strategy.

Args:
    docs: list[Document] - The input documents to process.
    entity_types: EntityTypes - The types of entities to extract.
    cache: PipelineCache - Cache to use for the language model and computations.
    args: StrategyConfig - Strategy configuration, including llm settings and extraction prompts.

Returns:
    EntityExtractionResult - The extraction results.

Raises:
    Exceptions propagated from LanguageModelConfig initialization, ModelManager.get_or_create_chat_model, or run_extract_graph.

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/extract_graph/graph_intelligence_strategy.py::run_extract_graph`
- `graphrag/language_model/manager.py::ModelManager`

