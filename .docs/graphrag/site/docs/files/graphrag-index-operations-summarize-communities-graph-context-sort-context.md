---
sidebar_position: 87
---

# graphrag/index/operations/summarize_communities/graph_context/sort_context.py

## Overview

Utilities to generate, sort, and batch graph context strings for community summaries.

This module provides helpers to assemble textual representations of graph context from entity, edge, and claim data, optionally including sub-community reports, and to sort and batch-generate these contexts with token-length constraints. It supports efficient processing of many communities, including optional parallel execution, by leveraging the project data schemas and a Tokenizer to enforce maximum context length.

Exports:
- _get_context_string(entities, edges, claims, sub_community_reports=None) -&gt; str
  Concatenate structured data into a single context string.

- sort_context(
    local_context: list[dict],
    tokenizer: Tokenizer,
    sub_community_reports: list[dict] | None = None,
    max_context_tokens: int | None = None,
    node_name_column: str = schemas.TITLE,
    node_details_column: str = schemas.NODE_DETAILS,
    edge_id_column: str = schemas.SHORT_ID,
    edge_details_column: str = schemas.EDGE_DETAILS,
    edge_degree_column: str = schemas.EDGE_DEGREE,
    edge_source_column: str = schemas.EDGE_SOURCE,
    edge_target_column: str = schemas.EDGE_TARGET,
    claim_details_column: str = schemas.CLAIM_DETAILS,
  ) -&gt; str
  Sorts context by degree in descending order, enforcing token-length constraints via the tokenizer.

- parallel_sort_context_batch(
    community_df, tokenizer: Tokenizer, max_context_tokens, parallel=False
  ) -&gt; None
  Calculate context strings for each community entry, optionally using parallel execution, and populate related context columns.

Notes:
- max_context_tokens=None disables token-based trimming.
- sub_community_reports may be None to omit top-level reports.
- This module relies on the Tokenizer to determine token lengths; ensure it provides a compatible interface.

Edge cases and exceptions:
- If required input keys/columns are missing, functions may raise KeyError or produce incomplete context.
- If max_context_tokens is provided and invalid (e.g., negative), a ValueError may be raised by the caller or underlying logic.
- Empty inputs yield empty strings; downstream code should handle NaNs if present in DataFrames.

Usage example:
To generate a single context string:
context = _get_context_string(entities, edges, claims, sub_community_reports)

To sort and constrain by tokens:
context = sort_context(local_context, tokenizer, max_context_tokens=512)

To batch-process multiple communities:
parallel_sort_context_batch(community_df, tokenizer, max_context_tokens=512, parallel=True)

## Functions

- [`_get_context_string`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-sort-context-get-context-string)
- [`sort_context`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-sort-context-sort-context)
- [`parallel_sort_context_batch`](../api/functions/graphrag-index-operations-summarize-communities-graph-context-sort-context-parallel-sort-context-batch)

