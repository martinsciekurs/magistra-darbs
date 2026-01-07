---
sidebar_position: 187
---

# graphrag/query/context_builder/local_context.py

## Overview

Utilities for constructing context data for graph-based prompt systems.

Purpose:
This module provides helper functions to assemble context data tables (entities, covariates, and relationships) into text blocks and structured DataFrames suitable for inclusion in system prompts. It coordinates data extraction, token budgeting (via a Tokenizer), and formatting to support prompt-based retrieval workflows.

Key exports:
- build_entity_context(selected_entities: list[Entity], tokenizer: Tokenizer | None = None, max_context_tokens: int = 8000, include_entity_rank: bool = True, rank_description: str = "number of relationships", column_delimiter: str = "|", context_name: str = "Entities") -&gt; tuple[str, pd.DataFrame]
- build_covariates_context(selected_entities: list[Entity], covariates: list[Covariate], tokenizer: Tokenizer | None = None, max_context_tokens: int = 8000, column_delimiter: str = "|", context_name: str = "Covariates") -&gt; tuple[str, pd.DataFrame]
- get_candidate_context(selected_entities: list[Entity], entities: list[Entity], relationships: list[Relationship], covariates: dict[str, list[Covariate]], include_entity_rank: bool = True, entity_rank_description: str = "number of relationships", include_relationship_weight: bool = False) -&gt; dict[str, pd.DataFrame]
- _filter_relationships(selected_entities: list[Entity], relationships: list[Relationship], top_k_relationships: int = 10, relationship_ranking_attribute: str = "rank") -&gt; list[Relationship]
- build_relationship_context(selected_entities: list[Entity], relationships: list[Relationship], tokenizer: Tokenizer | None = None, include_relationship_weight: bool = False, max_context_tokens: int = 8000, top_k_relationships: int = 10, relationship_ranking_attribute: str = "rank", column_delimiter: str = "|", context_name: str = "Relationships") -&gt; tuple[str, pd.DataFrame]

Brief summary:
The module centralizes logic to build and constrain context data used by the prompting system, enabling generation of narrative and tabular sections for entities, covariates, and relationships while respecting token budgets.

## Functions

- [`build_entity_context`](../api/functions/graphrag-query-context-builder-local-context-build-entity-context)
- [`build_covariates_context`](../api/functions/graphrag-query-context-builder-local-context-build-covariates-context)
- [`get_candidate_context`](../api/functions/graphrag-query-context-builder-local-context-get-candidate-context)
- [`_filter_relationships`](../api/functions/graphrag-query-context-builder-local-context-filter-relationships)
- [`build_relationship_context`](../api/functions/graphrag-query-context-builder-local-context-build-relationship-context)

