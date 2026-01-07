---
sidebar_position: 75
---

# DRIFTSearchContextBuilder

**File:** `graphrag/query/structured_search/drift_search/drift_context.py`

## Overview

DRIFTSearchContextBuilder wires together core DRIFT components to assemble a coherent DRIFT search context used for retrieval and reasoning over community reports, entities, covariates, and relationships. It serves as the central integration point that binds the language model interface, embedding model, entity context, prompts, and optional metadata into a single context object consumed by DRIFT-style structured search workflows.

Key attributes:
- model: The chat-based language model interface used for conversational reasoning.
- text_embedder: The embedding model used to encode text for similarity search.
- entities: A list of Entity objects representing known entities in reports or queries.
- entity_text_embeddings: A vector store containing embeddings for entity mentions.
- text_units: Optional list of TextUnit describing units of text content.
- reports: Optional pre-loaded list of CommunityReport objects to consider.
- relationships: Optional relationships between entities.
- covariates: Optional mapping of covariates, keyed by domain, to lists of Covariate.
- tokenizer: Optional Tokenizer used to tokenize prompts/text.
- embedding_vectorstore_key: Key to locate entity embeddings in the vector store; defaults to EntityVectorStoreKey.ID.
- config: Optional DRIFTSearchConfig configuring DRIFT behavior.
- local_system_prompt: Optional custom system prompt for local DRIFT search.
- local_mixed_context: Optional pre-built LocalSearchMixedContext; if omitted, one will be constructed as needed.
- reduce_system_prompt: Optional prompt used during reduction steps.
- response_type: Optional hint for response formatting.

Args:
- model (ChatModel): The chat-based language model interface.
- text_embedder (EmbeddingModel): The embedding model used to encode text for retrieval.
- entities (list[Entity]): Entities referenced in reports and queries.
- entity_text_embeddings (BaseVectorStore): Vector store containing embeddings for entity mentions.
- text_units (list[TextUnit] | None): Optional list of text units; defaults to None.
- reports (list[CommunityReport] | None): Optional pre-loaded reports; defaults to None.
- relationships (list[Relationship] | None): Optional relationships between entities; defaults to None.
- covariates (dict[str, list[Covariate]] | None): Optional covariates by domain; defaults to None.
- tokenizer (Tokenizer | None): Optional tokenizer; if None, a tokenizer will be created as needed.
- embedding_vectorstore_key (str): Key for locating embeddings in the vector store; defaults to EntityVectorStoreKey.ID.
- config (DRIFTSearchConfig | None): Optional DRIFT configuration; defaults to None.
- local_system_prompt (str | None): Optional local system prompt; defaults to None (uses DRIFT_LOCAL_SYSTEM_PROMPT).
- local_mixed_context (LocalSearchMixedContext | None): Optional pre-built local mixed context; defaults to None.
- reduce_system_prompt (str | None): Optional reduction prompt; defaults to None (uses DRIFT_REDUCE_PROMPT).
- response_type (str | None): Optional response formatting hint; defaults to None.

Returns:
- None: This is a constructor that initializes and wires the components into the DRIFT search context.

Raises:
- ValueError: If required inputs are missing or embeddings are incompatible for downstream comparison.

Notes:
- When optional inputs are omitted, sensible defaults are created to enable DRIFT-style search operations.

Examples:
- Basic usage:
  builder = DRIFTSearchContextBuilder(
      model=my_chat_model,
      text_embedder=my_embedder,
      entities=entities_list,
      entity_text_embeddings=entity_embedding_store
  )
  local = builder.init_local_context_builder()
  df, stats = builder.build_context("find reports mentioning CityA")

## Methods

### `init_local_context_builder`

```python
def init_local_context_builder(self) -> LocalSearchMixedContext
```

### `build_context`

```python
def build_context(
        self, query: str, **kwargs
    ) -> tuple[pd.DataFrame, dict[str, int]]
```

### `check_query_doc_encodings`

```python
def check_query_doc_encodings(query_embedding: Any, embedding: Any) -> bool
```

### `convert_reports_to_df`

```python
def convert_reports_to_df(reports: list[CommunityReport]) -> pd.DataFrame
```

### `__init__`

```python
def __init__(
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
        response_type: str | None = None,
    )
```

