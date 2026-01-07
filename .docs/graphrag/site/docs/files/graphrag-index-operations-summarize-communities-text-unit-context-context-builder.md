---
sidebar_position: 90
---

# graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py

## Overview

Utilities to build text unit context for summarizing communities.

This module provides helpers to prepare and combine text unit data into per-community and per-level contexts used for generating community reports. It relies on prep_text_units to obtain text unit details (including short_id, text, and entity_degree) and on related utilities such as sort_context and build_mixed_context to assemble and rank contextual information.

Key exports
- build_local_context(community_membership_df: pd.DataFrame, text_units_df: pd.DataFrame, node_df: pd.DataFrame, tokenizer: Tokenizer, max_context_tokens: int = 16000) -&gt; pd.DataFrame
  Prepare local context data for community report generation using text unit data. Computes per-community local context by enriching text units with degree information, merging with community membership, and producing a per-community context string sorted by relevance. The function relies on prep_text_units to obtain text unit details (including short_id, text, and entity_degree).

- build_level_context(report_df: pd.DataFrame | None, community_hierarchy_df: pd.DataFrame, local_context_df: pd.DataFrame, level: int, tokenizer: Tokenizer, max_context_tokens: int = 16000) -&gt; pd.DataFrame
  Prep context for each community in a given level. For each community: - Check if local context fits within the limit, if yes use local context - If local context exceeds the limit, iteratively replace local context with sub-community reports, starting from the biggest sub-community.

Summary
- The module orchestrates local and level context preparation by leveraging text unit data, community membership, and hierarchy information to produce token-bounded, relevance-sorted context strings for downstream report generation.

## Functions

- [`build_local_context`](../api/functions/graphrag-index-operations-summarize-communities-text-unit-context-context-builder-build-local-context)
- [`build_level_context`](../api/functions/graphrag-index-operations-summarize-communities-text-unit-context-context-builder-build-level-context)

