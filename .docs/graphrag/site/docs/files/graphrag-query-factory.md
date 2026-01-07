---
sidebar_position: 190
---

# graphrag/query/factory.py

## Overview

Factory utilities for constructing and configuring search engine components used by GraphRag queries. This module wires together data models, configuration, tokenization, vector stores, and optional callbacks to instantiate ready-to-use search engines (drift, local, global, and basic) based on a GraphRagConfig and provided data.

Functions:

- get_drift_search_engine(
    config: GraphRagConfig,
    reports: list[CommunityReport],
    text_units: list[TextUnit],
    entities: list[Entity],
    relationships: list[Relationship],
    description_embedding_store: BaseVectorStore,
    response_type: str,
    local_system_prompt: str | None = None,
    reduce_system_prompt: str | None = None,
    callbacks: list[QueryCallbacks] | None = None,
) -&gt; DRIFTSearch
  Args:
    config: GraphRagConfig - Drift-specific configuration object used to configure the search engine and models.
    reports: list[CommunityReport] - Community reports to be used by the drift search context.
    text_units: list[TextUnit] - Text units to be included in the search context.
    entities: list[Entity] - Entities to be considered by the drift search.
    relationships: list[Relationship] - Relationships to be included in the context.
    description_embedding_store: BaseVectorStore - Vector store containing description embeddings for retrieval.
    response_type: str - Response strategy or format requested from the engine.
    local_system_prompt: str | None - Optional system prompt used to influence generation locally.
    reduce_system_prompt: str | None - Optional system prompt fragment used to reduce prompt length/content.
    callbacks: list[QueryCallbacks] | None - Optional query callbacks to attach to the engine.
  Returns:
    DRIFTSearch - a configured drift search engine instance.
  Raises:
    Exceptions raised by underlying constructors or by input validation may propagate to the caller.

- get_local_search_engine(
    config: GraphRagConfig,
    reports: list[CommunityReport],
    text_units: list[TextUnit],
    entities: list[Entity],
    relationships: list[Relationship],
    covariates: dict[str, list[Covariate]],
    response_type: str,
    description_embedding_store: BaseVectorStore,
    system_prompt: str | None = None,
    callbacks: list[QueryCallbacks] | None = None,
) -&gt; LocalSearch
  Args:
    config: GraphRagConfig - Local search configuration object used to configure the search engine and models.
    reports: list[CommunityReport] - Community reports to be used by the local search engine context.
    text_units: list[TextUnit] - Text units to be included in the search context.
    entities: list[Entity] - Entities to be considered by the local search.
    relationships: list[Relationship] - Relationships to be included in the context.
    covariates: dict[str, list[Covariate]] - Covariates grouped by related keys to influence ranking/scoring.
    response_type: str - Response strategy or format requested from the engine.
    description_embedding_store: BaseVectorStore - Vector store containing description embeddings for retrieval.
    system_prompt: str | None - Optional system prompt to override default prompts.
    callbacks: list[QueryCallbacks] | None - Optional query callbacks to attach to the engine.
  Returns:
    LocalSearch - a configured local search engine instance.
  Raises:
    Exceptions raised by underlying constructors or by input validation may propagate to the caller.

- get_global_search_engine(
    config: GraphRagConfig,
    reports: list[CommunityReport],
    entities: list[Entity],
    communities: list[Community],
    response_type: str,
    dynamic_community_selection: bool = False,
    map_system_prompt: str | None = None,
    reduce_system_prompt: str | None = None,
    general_knowledge_inclusion_prompt: str | None = None,
    callbacks: list[QueryCallbacks] | None = None,
) -&gt; GlobalSearch
  Args:
    config: GraphRagConfig - Global search configuration object used to configure the global search engine and models.
    reports: list[CommunityReport] - Community reports to be used by the global search context.
    entities: list[Entity] - Entities to be included in the global search context.
    communities: list[Community] - Communities to consider during global search and selection.
    response_type: str - Response strategy or format requested from the engine.
    dynamic_community_selection: bool - If True, enables dynamic community selection logic.
    map_system_prompt: str | None - Optional prompt to map/guide system behavior.
    reduce_system_prompt: str | None - Optional prompt to reduce prompt length/content.
    general_knowledge_inclusion_prompt: str | None - Optional prompt to inject general knowledge guidance.
    callbacks: list[QueryCallbacks] | None - Optional query callbacks to attach to the engine.
  Returns:
    GlobalSearch - a configured global search engine instance.
  Raises:
    Exceptions raised by underlying constructors or by input validation may propagate to the caller.

- get_basic_search_engine(
    text_units: list[TextUnit],
    text_unit_embeddings: BaseVectorStore,
    config: GraphRagConfig,
    system_prompt: str | None = None,
    response_type: str = "multiple paragraphs",
    callbacks: list[QueryCallbacks] | None = None,
) -&gt; BasicSearch
  Args:
    text_units: list[TextUnit] - Text units to be included in the basic search context.
    text_unit_embeddings: BaseVectorStore - Vector store containing embeddings for text units.
    config: GraphRagConfig - Basic search configuration used to configure the search engine and models.
    system_prompt: str | None - Optional system prompt to override the default prompts.
    response_type: str - Response strategy or format requested from the engine.
    callbacks: list[QueryCallbacks] | None - Optional query callbacks to attach to the engine.
  Returns:
    BasicSearch - a configured basic search engine instance.
  Raises:
    Exceptions raised by underlying constructors or by input validation may propagate to the caller.

Accessories:
  Examples:
    drift_engine = get_drift_search_engine(config, reports, text_units, entities, relationships, embedding_store, "concise", None, None, None)
    local_engine = get_local_search_engine(config, reports, text_units, entities, relationships, covariates, "detailed", embedding_store, system_prompt=None, callbacks=None)
    global_engine = get_global_search_engine(config, reports, entities, communities, "stream", dynamic_community_selection=True)
    basic_engine = get_basic_search_engine(text_units, embedding_store, config, system_prompt="You are helpful", response_type="summary", callbacks=None)

## Functions

- [`get_drift_search_engine`](../api/functions/graphrag-query-factory-get-drift-search-engine)
- [`get_local_search_engine`](../api/functions/graphrag-query-factory-get-local-search-engine)
- [`get_global_search_engine`](../api/functions/graphrag-query-factory-get-global-search-engine)
- [`get_basic_search_engine`](../api/functions/graphrag-query-factory-get-basic-search-engine)

