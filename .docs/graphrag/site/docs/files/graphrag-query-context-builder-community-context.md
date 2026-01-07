---
sidebar_position: 183
---

# graphrag/query/context_builder/community_context.py

## Overview

Builds contextual data from community reports for system prompts in Graphrag.

Purpose
This module provides utilities to construct prompt-ready context from CommunityReport objects (and optionally related Entity objects). It can compute per-community weights based on the number of text units associated with entities, assemble a tabular or text-based context representation, and render content suitable for inclusion in system prompts. It respects configuration options such as use_community_summary, include_community_rank, include_community_weight, column_delimiter, shuffle_data, max_context_tokens, single_batch, and context_name, and interacts with CommunityReport, Entity, Tokenizer, and pandas.DataFrame.

Key exports (public API and helpers)
- build_community_context(community_reports, entities=None, tokenizer=None, use_community_summary=True, column_delimiter="|", shuffle_data=True, include_community_rank=False, min_community_rank=0, community_rank_name="rank", include_community_weight=True, community_weight_name="occurrence weight", normalize_community_weight=True, max_context_tokens=8000, single_batch=True, context_name="Reports", random_state=86) -&gt; tuple[str | list[str], dict[str, pd.DataFrame]]
  Build context data from community reports for use in a system prompt. If entities are provided, compute per-community weights from the number of text units associated with entities and attach the weight to each CommunityReport's attributes for inclusion in the context table.

- _report_context_text(report: CommunityReport, attributes: list[str]) -&gt; tuple[str, list[str]]
  Build a single-line representation of a CommunityReport using the given attributes.

- _rank_report_context(report_df: pd.DataFrame, weight_column: str | None = "occurrence weight", rank_column: str | None = "rank") -&gt; pd.DataFrame
  Sort the context by weight and rank in descending order, in-place. If a provided column is missing, the DataFrame is returned unchanged.

- _init_batch() -&gt; None
  Initialize batch state for the current context (header construction, token budgeting, and reset of batch storage).

- _get_header(attributes: list[str]) -&gt; list[str]
  Build the header row for the data table, incorporating defaults, filtered attributes, and optional summary/content and weight/rank columns based on configuration.

- _compute_community_weights(community_reports: list[CommunityReport], entities: list[Entity] | None, weight_attribute: str = "occurrence", normalize: bool = True) -&gt; list[CommunityReport]
  Compute per-community weights derived from text-unit counts linked to entities. Optionally normalize weights.

- _is_included(report: CommunityReport) -&gt; bool
  Determine whether a given CommunityReport should be included in the final context based on its rank and the min_community_rank threshold.

- _convert_report_context_to_df(context_records: list[list[str]], header: list[str], weight_column: str | None = None, rank_column: str | None = None) -&gt; pd.DataFrame
  Convert a collection of context records into a DataFrame and sort by provided weight/rank columns when specified.

- _cut_batch() -&gt; None
  Convert the current batch of records to a DataFrame (and optional CSV) and append it to the aggregated context.

- NO_COMMUNITY_RECORDS_WARNING (str)
  Warning message emitted when no community records remain after filtering. Used to surface empty-context scenarios without failing hard.

Notes on error handling and edge cases
- Public API functions validate input types and may raise standard Python errors (e.g., TypeError, ValueError) for invalid inputs. Implementations may also raise or emit warnings for edge cases.
- If no CommunityReport records survive filtering (or inputs are empty), the module will surface NO_COMMUNITY_RECORDS_WARNING and return an empty or minimal context structure suitable for prompt construction.
- When entities are provided, weights are computed from the linked text units; if entities do not reference any communities or tokens cannot be computed, weights may be omitted and the context will fall back to the configured defaults.
- The behavior of token counting (via the tokenizer) respects max_context_tokens and can influence batching or truncation as needed by the caller.

Brief usage notes
- Typical usage involves calling build_community_context with prepared CommunityReport objects (and optionally Entity objects) to obtain a prompt-ready string or list of context lines, along with a DataFrame containing metadata about the context for downstream use.
- Internal helpers are intentionally private (prefixed with underscores) to encapsulate the construction steps and allow unit testing of individual stages.

## Functions

- [`_report_context_text`](../api/functions/graphrag-query-context-builder-community-context-report-context-text)
- [`_rank_report_context`](../api/functions/graphrag-query-context-builder-community-context-rank-report-context)
- [`_init_batch`](../api/functions/graphrag-query-context-builder-community-context-init-batch)
- [`_get_header`](../api/functions/graphrag-query-context-builder-community-context-get-header)
- [`_compute_community_weights`](../api/functions/graphrag-query-context-builder-community-context-compute-community-weights)
- [`_is_included`](../api/functions/graphrag-query-context-builder-community-context-is-included)
- [`_convert_report_context_to_df`](../api/functions/graphrag-query-context-builder-community-context-convert-report-context-to-df)
- [`_cut_batch`](../api/functions/graphrag-query-context-builder-community-context-cut-batch)
- [`build_community_context`](../api/functions/graphrag-query-context-builder-community-context-build-community-context)

