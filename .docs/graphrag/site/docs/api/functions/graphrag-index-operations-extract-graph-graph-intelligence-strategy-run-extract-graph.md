---
sidebar_position: 116
---

# run_extract_graph

**File:** `graphrag/index/operations/extract_graph/graph_intelligence_strategy.py` (lines 45-102)

## Signature

```python
def run_extract_graph(
    model: ChatModel,
    docs: list[Document],
    entity_types: EntityTypes,
    args: StrategyConfig,
) -> EntityExtractionResult
```

## Description

async def run_extract_graph(
    model: ChatModel,
    docs: list[Document],
    entity_types: EntityTypes,
    args: StrategyConfig,
) -&gt; EntityExtractionResult:
    """Run the entity extraction chain."""

    Args:
        model: ChatModel
            The chat model instance used to invoke the extraction.
        docs: list[Document]
            The input documents from which to extract entities.
        entity_types: EntityTypes
            The types of entities to extract.
        args: StrategyConfig
            Strategy configuration for extraction. May include:
                tuple_delimiter: delimiter for grouping tuples (or None)
                record_delimiter: delimiter for grouping records (or None)
                completion_delimiter: delimiter for completing extractions (or None)
                extraction_prompt: optional prompt used by the extractor
                max_gleanings: maximum number of gleanings; defaults to graphrag_config_defaults.extract_graph.max_gleanings

    Returns:
        EntityExtractionResult
            The extracted entities, relationships, and the graph representing the extraction.

    Raises:
        Exception
            If an error occurs during extraction (propagated from the underlying GraphExtractor or processing steps).

## Dependencies

This function calls:

- `graphrag/index/operations/extract_graph/graph_extractor.py::GraphExtractor`
- `graphrag/index/operations/extract_graph/typing.py::EntityExtractionResult`

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/graph_intelligence_strategy.py::run_graph_intelligence`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_single_document_correct_entities_returned`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_entities_returned`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_edges_returned`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_entity_source_ids_mapped`
- `tests/unit/indexing/verbs/entities/extraction/strategies/graph_intelligence/test_gi_entity_extraction.py::TestRunChain.test_run_extract_graph_multiple_documents_correct_edge_source_ids_mapped`

