---
sidebar_position: 63
---

# _extract_nodes

**File:** `graphrag/index/operations/build_noun_graph/build_noun_graph.py` (lines 43-89)

## Signature

```python
def _extract_nodes(
    text_unit_df: pd.DataFrame,
    text_analyzer: BaseNounPhraseExtractor,
    num_threads: int = 4,
    async_mode: AsyncType = AsyncType.Threaded,
    cache: PipelineCache | None = None,
) -> pd.DataFrame
```

## Description

Extract noun-phrase nodes from text units.

This internal helper asynchronously extracts noun phrases from each text unit and aggregates them into a node DataFrame. It does not create edges; edge creation is handled by _extract_edges elsewhere.

Args:
  text_unit_df (pd.DataFrame): Input text units with schema [id, text].
  text_analyzer (BaseNounPhraseExtractor): Noun-phrase extractor used to determine noun phrases from text.
  num_threads (int): Number of worker threads to use for parallel processing.
  async_mode (AsyncType): Scheduling type to use for asynchronous operations.
  cache (PipelineCache | None): Optional cache for intermediate results; if None, NoopPipelineCache is used.

Returns:
  pd.DataFrame: DataFrame with columns [title, frequency, text_unit_ids].

Raises:
  Exceptions raised by derive_from_rows and text_analyzer.extract propagate to the caller.

Notes:
  This function is focused on noun-phrase extraction only; edge construction is performed by _extract_edges elsewhere.

## Dependencies

This function calls:

- `graphrag.cache.noop_pipeline_cache::NoopPipelineCache`
- `graphrag/index/utils/derive_from_rows.py::derive_from_rows`

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::build_noun_graph`

