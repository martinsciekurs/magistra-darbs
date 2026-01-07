---
sidebar_position: 245
---

# extract_graph_nlp

**File:** `graphrag/index/workflows/extract_graph_nlp.py` (lines 51-73)

## Signature

```python
def extract_graph_nlp(
    text_units: pd.DataFrame,
    cache: PipelineCache,
    extraction_config: ExtractGraphNLPConfig,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Asynchronously extract the base entity graph (nodes and edges) from the given text units.

Args:
    text_units: pd.DataFrame: Input text units used to extract noun phrases for graph construction.
    cache: PipelineCache: Cache used during extraction and graph construction.
    extraction_config: ExtractGraphNLPConfig: Configuration for extraction settings, including text_analyzer, normalize_edge_weights, concurrent_requests, and async_mode.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A tuple containing extracted_nodes and extracted_edges. extracted_nodes has an added 'type' column with value 'NOUN PHRASE' and an added 'description' column (empty string); extracted_edges has an added 'description' column (empty string).

Raises:
    Exception: Propagates exceptions raised by the underlying noun-phrase extractor creation or by build_noun_graph.

## Dependencies

This function calls:

- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::build_noun_graph`
- `graphrag/index/operations/build_noun_graph/np_extractors/factory.py::create_noun_phrase_extractor`

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph_nlp.py::run_workflow`

