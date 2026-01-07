---
sidebar_position: 229
---

# create_community_reports_text

**File:** `graphrag/index/workflows/create_community_reports_text.py` (lines 74-114)

## Signature

```python
def create_community_reports_text(
    entities: pd.DataFrame,
    communities: pd.DataFrame,
    text_units: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    summarization_strategy: dict,
    async_mode: AsyncType = AsyncType.AsyncIO,
    num_threads: int = 4,
) -> pd.DataFrame
```

## Description

Transforms input data into finalized community reports by building local contexts and summarizing communities.

Args:
    entities: DataFrame containing entities data used to explode communities into nodes.
    communities: DataFrame containing community definitions and metadata.
    text_units: DataFrame containing text unit data.
    callbacks: WorkflowCallbacks instance for workflow callbacks.
    cache: PipelineCache instance used for caching results.
    summarization_strategy: dict configuring the summarization process (e.g., prompts and model settings).
    async_mode: AsyncType indicating the asynchronous backend to use.
    num_threads: int number of worker threads to use.

Returns:
    pd.DataFrame: Finalized community reports.

Raises:
    Propagates exceptions raised by underlying helper functions and data processing steps.

## Dependencies

This function calls:

- `graphrag/config/models/language_model_config.py::LanguageModelConfig`
- `graphrag/index/operations/finalize_community_reports.py::finalize_community_reports`
- `graphrag/index/operations/summarize_communities/explode_communities.py::explode_communities`
- `graphrag/index/operations/summarize_communities/summarize_communities.py::summarize_communities`
- `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py::build_local_context`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports_text.py::run_workflow`

