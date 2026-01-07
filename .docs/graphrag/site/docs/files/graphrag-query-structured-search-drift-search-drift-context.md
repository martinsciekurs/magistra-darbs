---
sidebar_position: 206
---

# graphrag/query/structured_search/drift_search/drift_context.py

## Overview

DRIFT search context builder for structured search in DRIFT queries.

Overview:
This module defines the DRIFTSearchContextBuilder class, which wires together core DRIFT components to assemble a coherent DRIFT search context used for retrieval and reasoning over community reports, entities, covariates, and relationships. It binds the language model interface, embedding model, entity context, prompts, and optional metadata into a single context object consumed by DRIFT-style structured search.

Key exports:
- DRIFTSearchContextBuilder: Central integration point that binds the language model, embedding model, entity context, prompts, and optional metadata into a DRIFT search context.

Brief summary:
The builder exposes methods to initialize a local mixed context from the current DRIFT context, build a full context for a given query, check embedding compatibility, and convert reports into a DataFrame for downstream processing. It also provides a constructor that wires together the necessary components and defaults.

Public API (class and methods):
- __init__(
        self,
        model: ChatModel,
        text_embedder: EmbeddingModel,
        entities: list[Entity],
        entity_text_embeddings: BaseVectorStore,
        text_units: list[TextUnit] | None = None,
        reports: list[CommunityReport] | None = None,
        relationships: list[Relationship] | None = None,
        covariates: dict[str, list[Covariate]] | None = None,
        tokenizer: Tokenizer | None = None,
        embedding_vectorstore_key: str = EntityVectorStoreKey.ID,
        config: DRIFTSearchConfig | None = None,
        local_system_prompt: str | None = None,
        local_mixed_context: LocalSearchMixedContext | None = None,
        reduce_system_prompt: str | None = None,
        response_type: str | None = None
    )
- init_local_context_builder(self) -&gt; LocalSearchMixedContext
- build_context(self, query: str, **kwargs) -&gt; tuple[pd.DataFrame, dict[str, int]]
- check_query_doc_encodings(query_embedding: Any, embedding: Any) -&gt; bool
- convert_reports_to_df(reports: list[CommunityReport]) -&gt; pd.DataFrame

Constructor parameters (as defined in the code):
model: ChatModel
text_embedder: EmbeddingModel
entities: list[Entity]
entity_text_embeddings: BaseVectorStore
text_units: list[TextUnit] | None = None
reports: list[CommunityReport] | None = None
relationships: list[Relationship] | None = None
covariates: dict[str, list[Covariate]] | None = None
tokenizer: Tokenizer | None = None
embedding_vectorstore_key: str = EntityVectorStoreKey.ID
config: DRIFTSearchConfig | None = None
local_system_prompt: str | None = None
local_mixed_context: LocalSearchMixedContext | None = None
reduce_system_prompt: str | None = None
response_type: str | None = None

## Classes

- [`DRIFTSearchContextBuilder`](../api/classes/graphrag-query-structured-search-drift-search-drift-context-driftsearchcontextbuilder)

## Functions

- [`init_local_context_builder`](../api/functions/graphrag-query-structured-search-drift-search-drift-context-init-local-context-builder)
- [`build_context`](../api/functions/graphrag-query-structured-search-drift-search-drift-context-build-context)
- [`check_query_doc_encodings`](../api/functions/graphrag-query-structured-search-drift-search-drift-context-check-query-doc-encodings)
- [`convert_reports_to_df`](../api/functions/graphrag-query-structured-search-drift-search-drift-context-convert-reports-to-df)
- [`__init__`](../api/functions/graphrag-query-structured-search-drift-search-drift-context-init)

