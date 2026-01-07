---
sidebar_position: 64
---

# build_noun_graph

**File:** `graphrag/index/operations/build_noun_graph/build_noun_graph.py` (lines 22-40)

## Signature

```python
def build_noun_graph(
    text_unit_df: pd.DataFrame,
    text_analyzer: BaseNounPhraseExtractor,
    normalize_edge_weights: bool,
    num_threads: int = 4,
    async_mode: AsyncType = AsyncType.Threaded,
    cache: PipelineCache | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Build a noun graph from text units.

Args:
    text_unit_df (pd.DataFrame): Input text units with at least columns 'id' and 'text'; used to extract noun phrases for graph construction.
    text_analyzer (BaseNounPhraseExtractor): Noun-phrase extractor used to determine noun phrases from text.
    normalize_edge_weights (bool): If True, compute PMI-based weights for edges; otherwise use raw co-occurrence counts.
    num_threads (int): Number of worker threads to use for parallel processing.
    async_mode (AsyncType): Async processing mode to use (e.g., Threaded).
    cache (PipelineCache | None): Optional cache for results; if None, a NoopPipelineCache is used.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A pair of DataFrames (nodes_df, edges_df) representing extracted noun nodes and their connecting edges (with optional weights).

## Dependencies

This function calls:

- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::_extract_edges`
- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::_extract_nodes`

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph_nlp.py::extract_graph_nlp`

