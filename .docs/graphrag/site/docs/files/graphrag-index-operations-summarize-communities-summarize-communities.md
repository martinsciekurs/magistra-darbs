---
sidebar_position: 89
---

# graphrag/index/operations/summarize_communities/summarize_communities.py

## Overview

Utilities to load community reporting strategies and generate summarized reports for hierarchical communities.

Overview:
  This module provides helpers to determine the appropriate reporting strategy, generate per-community reports, and summarize these reports across levels into a DataFrame of CommunityReport records.

Key exports:
- load_strategy
- _generate_report
- run_generate
- summarize_communities

Functions:
- load_strategy(strategy: CreateCommunityReportsStrategyType) -&gt; CommunityReportsStrategy
  Load the strategy method for community reports based on the provided type.
  Args:
    strategy: The strategy type used to determine which community reports strategy to load.
  Returns:
    CommunityReportsStrategy: The callable strategy function corresponding to the supplied strategy type.
  Raises:
    ValueError: If an unknown strategy type is provided.

- _generate_report(runner: CommunityReportsStrategy, callbacks: WorkflowCallbacks, cache: PipelineCache, strategy: dict, community_id: int, community_level: int, community_context: str) -&gt; CommunityReport | None
  Generate a report for a single community.
  Args:
    runner: The strategy function used to generate the report for the community.
    callbacks: Callbacks to use during report generation.
    cache: Cache instance used by the report generation process.
    strategy: Strategy configuration for the report generation.
    community_id: Identifier of the community for which to generate the report.
    community_level: Level of the community.
    community_context: Context string for the community.
  Returns:
    CommunityReport | None: The generated report for the given community, or None.

- run_generate(record)
  Generate a community summary for a single record.
  Args:
    record: dict-like containing the keys defined by schemas.COMMUNITY_ID, schemas.COMMUNITY_LEVEL, and schemas.CONTEXT_STRING.
  Returns:
    CommunityReport | None: The generated report for the given community record.

- summarize_communities(
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
  Generate community summaries across all levels and return a DataFrame of CommunityReport records.
  Args:
    nodes: DataFrame containing node data used to determine levels and contexts.
    communities: DataFrame containing community definitions and hierarchical relationships.
    local_contexts: Local context data used to build level contexts.
    level_context_builder: Callable to build level contexts from inputs.
    callbacks: Callbacks to use during report generation.
    cache: Cache instance used by the report generation process.
    strategy: Strategy configuration for the report generation.
    tokenizer: Tokenizer used for processing text in reports.
    max_input_length: Maximum input length for the tokenizer/model.
    async_mode: Async execution mode.
    num_threads: Number of threads to use during processing.
  Returns:
    pd.DataFrame: DataFrame containing CommunityReport records.

## Functions

- [`load_strategy`](../api/functions/graphrag-index-operations-summarize-communities-summarize-communities-load-strategy)
- [`_generate_report`](../api/functions/graphrag-index-operations-summarize-communities-summarize-communities-generate-report)
- [`run_generate`](../api/functions/graphrag-index-operations-summarize-communities-summarize-communities-run-generate)
- [`summarize_communities`](../api/functions/graphrag-index-operations-summarize-communities-summarize-communities-summarize-communities)

