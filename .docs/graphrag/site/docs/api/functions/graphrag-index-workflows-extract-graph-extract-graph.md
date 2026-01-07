---
sidebar_position: 243
---

# extract_graph

**File:** `graphrag/index/workflows/extract_graph.py` (lines 82-132)

## Signature

```python
def extract_graph(
    text_units: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    extraction_strategy: dict[str, Any] | None = None,
    extraction_num_threads: int = 4,
    extraction_async_mode: AsyncType = AsyncType.AsyncIO,
    entity_types: list[str] | None = None,
    summarization_strategy: dict[str, Any] | None = None,
    summarization_num_threads: int = 4,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
```

## Description

All steps to create the base entity graph.

This asynchronous function processes the input text units to extract entities and relationships, validates
the extraction results, preserves raw extraction outputs, and summarizes the data to produce the final
entities and relationships DataFrames. It returns a tuple of (entities, relationships, raw_entities, raw_relationships).

Args:
    text_units: DataFrame containing the text units to process.
    callbacks: Callbacks to report progress during the workflow.
    cache: Cache to store/retrieve intermediate results.
    extraction_strategy: Strategy configuration for entity extraction.
    extraction_num_threads: Number of threads to use for extraction.
    extraction_async_mode: Async mode for extraction (e.g., AsyncIO).
    entity_types: Optional list of entity types to constrain extraction.
    summarization_strategy: Strategy configuration for summarization.
    summarization_num_threads: Number of threads to use for summarization.

Returns:
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        A tuple of four DataFrames:
        - entities: summarized entities
        - relationships: summarized relationships
        - raw_entities: entities extracted before summarization
        - raw_relationships: relationships extracted before summarization

Raises:
    ValueError: If no entities detected during extraction or no relationships detected during extraction.

## Dependencies

This function calls:

- `graphrag/index/workflows/extract_graph.py::_validate_data`
- `graphrag/index/workflows/extract_graph.py::get_summarized_entities_relationships`

