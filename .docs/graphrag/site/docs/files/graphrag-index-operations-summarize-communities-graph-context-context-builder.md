---
sidebar_position: 86
---

# graphrag/index/operations/summarize_communities/graph_context/context_builder.py

## Overview

Utilities to construct graph context for the summarize communities workflow.

Purpose:
Provide helpers to build per-level and per-community local contexts by processing community data, sub-contexts, and token-limited contexts. This module orchestrates data transformations and trimming to fit token constraints and returns DataFrames or Series suitable for downstream steps.

Public API:
- build_local_context(nodes, edges, claims, tokenizer: Tokenizer, callbacks: WorkflowCallbacks, max_context_tokens: int = 16_000)
  Prepare initial local context for all communities, processing level-by-level.

- build_level_context(
    report_df: pd.DataFrame | None,
    community_hierarchy_df: pd.DataFrame,
    local_context_df: pd.DataFrame,
    tokenizer: Tokenizer,
    level: int,
    max_context_tokens: int,
  ) -&gt; pd.DataFrame
  Prepare context for communities at a given level.

Internal helpers (not exported):
- _drop_community_level(df: pd.DataFrame) -&gt; pd.DataFrame
  Drop the community level column from the dataframe.

- _antijoin_reports(df: pd.DataFrame, reports: pd.DataFrame) -&gt; pd.DataFrame
  Return records in df that are not in reports.

- _at_level(level: int, df: pd.DataFrame) -&gt; pd.DataFrame
  Return records at the given level.

- _sort_and_trim_context(
    df: pd.DataFrame, tokenizer: Tokenizer, max_context_tokens: int
) -&gt; pd.Series
  Sort and trim the context to fit the token limit.

- _get_subcontext_df(
    level: int, report_df: pd.DataFrame, local_context_df: pd.DataFrame
) -&gt; pd.DataFrame
  Get sub-community context for each community.

- _build_mixed_context(
    df: pd.DataFrame, tokenizer: Tokenizer, max_context_tokens: int
) -&gt; pd.Series
  Build mixed context for each row by applying build_mixed_context to the ALL_CONTEXT data and trimming to the token limit.

- _prepare_reports_at_level(
    node_df: pd.DataFrame,
    edge_df: pd.DataFrame,
    claim_df: pd.DataFrame | None,
    tokenizer: Tokenizer,
    level: int,
    max_context_tokens: int = 16_000,
) -&gt; pd.DataFrame
  Prepare reports at a given level.

- _get_community_df(
    level: int,
    invalid_context_df: pd.DataFrame,
    sub_context_df: pd.DataFrame,
    community_hierarchy_df: pd.DataFrame,
    tokenizer: Tokenizer,
    max_context_tokens: int,
) -&gt; pd.DataFrame
  Get community context for each community.

Notes:
The module relies on pandas, a Tokenizer, and various Graphrag utilities for DataFrame operations.

## Functions

- [`_drop_community_level`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-drop-community-level)
- [`_antijoin_reports`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-antijoin-reports)
- [`_at_level`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-at-level)
- [`_sort_and_trim_context`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-sort-and-trim-context)
- [`_get_subcontext_df`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-get-subcontext-df)
- [`_build_mixed_context`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-build-mixed-context)
- [`_prepare_reports_at_level`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-prepare-reports-at-level)
- [`_get_community_df`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-get-community-df)
- [`build_local_context`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-build-local-context)
- [`build_level_context`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-context-builder-build-level-context)

