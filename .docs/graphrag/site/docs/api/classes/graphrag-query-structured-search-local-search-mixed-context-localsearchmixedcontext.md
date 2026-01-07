---
sidebar_position: 136
---

# LocalSearchMixedContext

**File:** `graphrag/query/structured_search/local_search/mixed_context.py`

## Overview

Local search context builder that mixes community data with local entity/relationship/covariate context for structured searches.

This class aggregates data from community reports, entity/relationship/covariate tables, and text units to create a comprehensive context for local search prompts. It relies on a vector store of entity text embeddings and a text embedding model to rank and assemble relevant content.

Args:
  entities: The list of entities to include.
  entity_text_embeddings: The vector store containing embeddings for entity text.
  text_embedder: The embedding model used to embed text for similarity search.
  text_units: Optional list of TextUnit.
  community_reports: Optional list of CommunityReport.
  relationships: Optional list of Relationship.
  covariates: Optional dict[str, list[Covariate]]; covariate data grouped by key.
  tokenizer: Optional Tokenizer.
  embedding_vectorstore_key: Key to select the embedding store (default EntityVectorStoreKey.ID).

Returns:
  An initialized LocalSearchMixedContext instance.

Raises:
  Not specified in the provided information.

## Methods

### `filter_by_entity_keys`

```python
def filter_by_entity_keys(self, entity_keys: list[int] | list[str])
```

### `__init__`

```python
def __init__(
        self,
        entities: list[Entity],
        entity_text_embeddings: BaseVectorStore,
        text_embedder: EmbeddingModel,
        text_units: list[TextUnit] | None = None,
        community_reports: list[CommunityReport] | None = None,
        relationships: list[Relationship] | None = None,
        covariates: dict[str, list[Covariate]] | None = None,
        tokenizer: Tokenizer | None = None,
        embedding_vectorstore_key: str = EntityVectorStoreKey.ID,
    )
```

### `_build_text_unit_context`

```python
def _build_text_unit_context(
        self,
        selected_entities: list[Entity],
        max_context_tokens: int = 8000,
        return_candidate_context: bool = False,
        column_delimiter: str = "|",
        context_name: str = "Sources",
    ) -> tuple[str, dict[str, pd.DataFrame]]
```

### `build_context`

```python
def build_context(
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
    ) -> ContextBuilderResult
```

### `_build_community_context`

```python
def _build_community_context(
        self,
        selected_entities: list[Entity],
        max_context_tokens: int = 4000,
        use_community_summary: bool = False,
        column_delimiter: str = "|",
        include_community_rank: bool = False,
        min_community_rank: int = 0,
        return_candidate_context: bool = False,
        context_name: str = "Reports",
    ) -> tuple[str, dict[str, pd.DataFrame]]
```

### `_build_local_context`

```python
def _build_local_context(
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
    ) -> tuple[str, dict[str, pd.DataFrame]]
```

