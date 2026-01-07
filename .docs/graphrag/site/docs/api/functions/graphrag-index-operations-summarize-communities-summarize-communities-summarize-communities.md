---
sidebar_position: 152
---

# summarize_communities

**File:** `graphrag/index/operations/summarize_communities/summarize_communities.py` (lines 31-94)

## Signature

```python
def summarize_communities(
    nodes: pd.DataFrame,
    communities: pd.DataFrame,
    local_contexts,
    level_context_builder: Callable,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    strategy: dict,
    tokenizer: Tokenizer,
    max_input_length: int,
    async_mode: AsyncType = AsyncType.AsyncIO,
    num_threads: int = 4,
)
```

## Description

Generate community summaries across all levels and return a DataFrame of CommunityReport records.

Args:
    nodes: pd.DataFrame
        DataFrame containing node data used to determine levels and contexts.
    communities: pd.DataFrame
        DataFrame containing community definitions and hierarchical relationships.
    local_contexts:
        Local context data used to build level contexts; passed to level_context_builder.
    level_context_builder: Callable
        Function used to construct context objects for each level.
    callbacks: WorkflowCallbacks
        Callbacks for progress reporting and other workflow events.
    cache: PipelineCache
        Cache to store intermediate results during report generation.
    strategy: dict
        Strategy configuration for report generation; expects a 'type' key to select the strategy.
    tokenizer: Tokenizer
        Tokenizer used to process text during context construction.
    max_input_length: int
        Maximum number of tokens allowed in the combined input for generation.
    async_mode: AsyncType
        Async scheduling mode to use (default AsyncType.AsyncIO).
    num_threads: int
        Number of concurrent worker threads to use.

Returns:
    pd.DataFrame
        DataFrame of generated CommunityReport records. Each row corresponds to a
        report for a specific community at a specific level; columns match the fields
        defined by the CommunityReport type.

Notes:
    - Strategy loading is performed dynamically via load_strategy based on strategy['type'];
      an unsupported type will be resolved at runtime by the strategy loader.

## Dependencies

This function calls:

- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/index/operations/summarize_communities/summarize_communities.py::load_strategy`
- `graphrag/index/operations/summarize_communities/utils.py::get_levels`
- `graphrag/index/utils/derive_from_rows.py::derive_from_rows`
- `graphrag/logger/progress.py::progress_ticker`

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`
- `graphrag/index/workflows/create_community_reports_text.py::create_community_reports_text`

