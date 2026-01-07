---
sidebar_position: 212
---

# graphrag/query/structured_search/local_search/mixed_context.py

## Overview

Local search context builder that blends community data with local entity/relationship/covariate context and text units to form a comprehensive prompt context for structured searches.

Overview
- This module defines LocalSearchMixedContext, a local search context builder that merges community data with local entity/relationship/covariate context and text units to produce a single, ranked prompt context for structured searches. It relies on a vector store of entity text embeddings and a text embedding model to rank and assemble relevant information.

Exports
- LocalSearchMixedContext: Main class that orchestrates data gathering and context construction.

Key features and methods
- __init__(entities: list[Entity], entity_text_embeddings: BaseVectorStore, text_embedder: EmbeddingModel, text_units: list[TextUnit] | None = None, community_reports: list[CommunityReport] | None = None, relationships: list[Relationship] | None = None, covariates: dict[str, list[Covariate]] | None = None, tokenizer: Tokenizer | None = None, embedding_vectorstore_key: str = EntityVectorStoreKey.ID)
  Initialize the builder with the data sources and configuration.
- filter_by_entity_keys(self, entity_keys: list[int] | list[str]) -&gt; None
  Filter the entity embeddings by the provided keys to limit context to specific entities.
- _build_text_unit_context(
    self,
    selected_entities: list[Entity],
    max_context_tokens: int = 8000,
    return_candidate_context: bool = False,
    column_delimiter: str = "|",
    context_name: str = "Sources",
  ) -&gt; tuple[str, dict[str, pd.DataFrame]]
  Rank and collect text units for the selected entities, respecting token limits.
- _build_community_context(
    self,
    selected_entities: list[Entity],
    max_context_tokens: int = 4000,
    use_community_summary: bool = False,
    column_delimiter: str = "|",
    include_community_rank: bool = False,
    min_community_rank: int = 0,
    return_candidate_context: bool = False,
    context_name: str = "Reports",
  ) -&gt; tuple[str, dict[str, pd.DataFrame]]
  Add community data to the context window up to the token limit.
- _build_local_context(
    self,
    selected_entities: list[Entity],
    max_context_tokens: int = 8000,
    include_entity_rank: bool = False,
    rank_description: str = "relationship count",
    include_relationship_weight: bool = False,
    top_k_relationships: int = 10,
    relationship_ranking_attribute: str = "rank",
    return_candidate_context: bool = False,
    column_delimiter: str = "|",
  ) -&gt; tuple[str, dict[str, pd.DataFrame]]
  Build data context for local search by combining entity/relationship/covariate data.
- build_context(
    self,
    query: str,
    conversation_history: ConversationHistory | None = None,
    include_entity_names: list[str] | None = None,
    exclude_entity_names: list[str] | None = None,
    conversation_history_max_turns: int | None = 5,
    conversation_history_user_turns_only: bool = True,
    max_context_tokens: int = 8000,
    text_unit_prop: float = 0.5,
    community_prop: float = 0.25,
    top_k_mapped_entities: int = 10,
    top_k_relationships: int = 10,
    include_community_rank: bool = False,
    include_entity_rank: bool = False,
    rank_description: str = "number of relationships",
    include_relationship_weight: bool = False,
    relationship_ranking_attribute: str = "rank",
    return_candidate_context: bool = False,
    use_community_summary: bool = False,
    min_community_rank: int = 0,
    community_context_name: str = "Reports",
    column_delimiter: str = "|",
    **kwargs: dict[str, Any],
  ) -&gt; ContextBuilderResult
  Build a combined data context for the given query, honoring ranking and token limits, and return a ContextBuilderResult.

Notes
- The class aggregates data from community reports, entity/relationship/covariate tables, and text units via internal helpers and wraps them into a ContextBuilderResult.
- Tokens are managed to fit within the configured max_context_tokens for the final prompt.

Exceptions
- May raise ValueError or TypeError for invalid inputs; underlying components may raise other exceptions as encountered.

Usage (pseudo-code)
- Instantiate and build a context for a query:
  lc = LocalSearchMixedContext(
      entities=my_entities,
      entity_text_embeddings=my_vector_store,
      text_embedder=my_embedder,
      text_units=my_text_units,
      community_reports=my_reports
  )
  result = lc.build_context(
      query="What factors connect X and Y?",
      conversation_history=conv_history
  )

Purpose
- Enables combining community-sourced context with local data to support structured search prompts in a vector-augmented retrieval workflow.

## Classes

- [`LocalSearchMixedContext`](../api/classes/graphrag-query-structured-search-local-search-mixed-context-localsearchmixedcontext)

## Functions

- [`filter_by_entity_keys`](../api/functions/graphrag-query-structured-search-local-search-mixed-context-filter-by-entity-keys)
- [`__init__`](../api/functions/graphrag-query-structured-search-local-search-mixed-context-init)
- [`_build_text_unit_context`](../api/functions/graphrag-query-structured-search-local-search-mixed-context-build-text-unit-context)
- [`build_context`](../api/functions/graphrag-query-structured-search-local-search-mixed-context-build-context)
- [`_build_community_context`](../api/functions/graphrag-query-structured-search-local-search-mixed-context-build-community-context)
- [`_build_local_context`](../api/functions/graphrag-query-structured-search-local-search-mixed-context-build-local-context)

