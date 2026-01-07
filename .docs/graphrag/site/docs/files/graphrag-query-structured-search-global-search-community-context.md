---
sidebar_position: 210
---

# graphrag/query/structured_search/global_search/community_context.py

## Overview

Global context builder for structured search across multiple communities.

This module defines the GlobalCommunityContext class, which extends GlobalContextBuilder and coordinates community reports, communities, optional entities, and tokenizer-driven text processing to assemble a unified context used by the global search workflow. It also supports optional dynamic community selection to tailor context content to the query.

Key exports:
- GlobalCommunityContext

Summary:
GlobalCommunityContext acts as a global context builder that aggregates data from CommunityReport, Community, and Entity models and processes text with a Tokenizer to produce a context suitable for a structured, multi-community search.

Classes:
- GlobalCommunityContext: Global context builder; coordinates data sources and tokenizer-driven text processing to assemble the context for global search.

Public methods:
- __init__(community_reports, communities, entities=None, tokenizer=None, dynamic_community_selection=False, dynamic_community_selection_kwargs=None, random_state=86): Initialize the GlobalCommunityContext instance with the provided data and optional configuration.
- build_context(query, conversation_history=None, use_community_summary=True, column_delimiter="|", shuffle_data=True, include_community_rank=False, min_community_rank=0, community_rank_name="rank", include_community_weight=True, community_weight_name="occurrence", normalize_community_weight=True, max_context_tokens=8000, context_name="Reports", conversation_history_user_turns_only=True, conversation_history_max_turns=5, **kwargs) -&gt; ContextBuilderResult: Prepare batches of community report data table as context data for global search.

Args:
- community_reports: Reports for communities to consider.
- communities: Community objects used to build the hierarchy and starting points.
- entities: Optional list of Entity objects to include in the context.
- tokenizer: Tokenizer to use; if None, a default tokenizer is obtained via get_tokenizer.
- dynamic_community_selection: Whether to enable dynamic community selection.
- dynamic_community_selection_kwargs: Additional kwargs for dynamic selection.
- random_state: Seed for randomness.
- query: The user query to build context for.
- conversation_history: Optional conversation history to consider while constructing the context.
- use_community_summary: Whether to use the community summary in the context data.
- column_delimiter: Delimiter used to separate columns in the context representation.
- shuffle_data: Whether to shuffle the context data.
- include_community_rank: Whether to include community rank in the context data.
- min_community_rank: Minimum community rank to include.
- community_rank_name: Name of the rank column in the context.
- include_community_weight: Whether to include community weight in the context data.
- community_weight_name: Name of the weight column in the context.
- normalize_community_weight: Whether to normalize community weights.
- max_context_tokens: Maximum number of tokens allowed in the context data.
- context_name: Name for the context data section.
- conversation_history_user_turns_only: If True, consider only user turns in the conversation history.
- conversation_history_max_turns: Maximum number of turns from conversation history to include.
- kwargs: Additional keyword arguments.

Returns:
- ContextBuilderResult: The result of building the context.

Raises:
- TypeError, ValueError: If inputs are invalid or incompatible.

## Classes

- [`GlobalCommunityContext`](../api/classes/graphrag-query-structured-search-global-search-community-context-globalcommunitycontext)

## Functions

- [`__init__`](../api/functions/graphrag-query-structured-search-global-search-community-context-init)
- [`build_context`](../api/functions/graphrag-query-structured-search-global-search-community-context-build-context)

