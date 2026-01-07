---
sidebar_position: 227
---

# create_community_reports

**File:** `graphrag/index/workflows/create_community_reports.py` (lines 84-137)

## Signature

```python
def create_community_reports(
    edges_input: pd.DataFrame,
    entities: pd.DataFrame,
    communities: pd.DataFrame,
    claims_input: pd.DataFrame | None,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    summarization_strategy: dict,
    async_mode: AsyncType = AsyncType.AsyncIO,
    num_threads: int = 4,
) -> pd.DataFrame
```

## Description

Asynchronously transforms input data into finalized community reports by preparing nodes and edges, constructing local contexts, performing level-based summarization, and finalizing results. The function orchestrates multiple preprocessing steps, builds prompts and tokenizer settings, and runs the summarization asynchronously before returning the finalized reports.

High-level steps:
- Node and edge preparation: explode_communities, _prep_nodes, and _prep_edges; if claims_input is provided, _prep_claims is applied to incorporate claims into the context.
- Context setup: configure extraction_prompt from graph_prompt, initialize LanguageModelConfig and tokenizer, determine max_input_length, and build local contexts via build_local_context.
- Summarization: asynchronously summarize across community levels with summarize_communities using the provided callbacks, cache, and strategy, honoring async_mode and num_threads.
- Finalization: merge and enrich the summarized reports with community metadata via finalize_community_reports.

Notes:
- claims_input is optional; when provided, claims data are incorporated into local contexts.
- The preparation steps mutate their input DataFrames in place.
- This function executes asynchronously and may involve network or model API calls; latency and runtime errors may occur.
- Callbacks are used for progress reporting during processing.

Args:
  edges_input: pd.DataFrame - Edges data to process.
  entities: pd.DataFrame - Entity data used to explode communities.
  communities: pd.DataFrame - Community definitions and hierarchy.
  claims_input: pd.DataFrame | None - Optional claims data; if provided, used to augment context.
  callbacks: WorkflowCallbacks - Callbacks for progress reporting during processing.
  cache: PipelineCache - Cache for intermediate results during summarization.
  summarization_strategy: dict - Settings for summarization, including llm config and prompts.
  async_mode: AsyncType - Async execution mode for the summarization step.
  num_threads: int - Number of worker threads for parallel summarization.

Returns:
  pd.DataFrame: The finalized community reports.

Raises:
  OSError: If an I/O error occurs (e.g., storage or network interactions).
  ValueError: If input data or strategy configurations are invalid or missing required fields.
  KeyError: If expected keys are absent from dictionaries during setup.
  Exception: Other exceptions may be raised by underlying components (e.g., external services or the language model) during processing.

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/finalize_community_reports.py::finalize_community_reports`
- `graphrag/index/operations/summarize_communities/explode_communities.py::explode_communities`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_local_context`
- `graphrag/index/operations/summarize_communities/summarize_communities.py::summarize_communities`
- `graphrag/index/workflows/create_community_reports.py::_prep_claims`
- `graphrag/index/workflows/create_community_reports.py::_prep_edges`
- `graphrag/index/workflows/create_community_reports.py::_prep_nodes`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::run_workflow`

