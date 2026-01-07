---
sidebar_position: 203
---

# graphrag/query/structured_search/basic_search/basic_context.py

## Overview

Basic search context utilities for Graphrag.

Overview
This module provides the BasicSearchContext class to construct a compact, coherent
context for a user query in the basic search mode. It uses a text embedding model and a
vector store of TextUnit embeddings, and can optionally incorporate ConversationHistory
while enforcing a token limit to keep the resulting context within practical bounds.

Exports
- BasicSearchContext: Builds and manages the basic search context.
- _map_ids: Internal helper that maps each TextUnit's id to its short_id.

Key terms
- short_ids: The short_id attribute on a TextUnit; used for compact identifiers in the
  context payload.
- basic search mode: A lightweight search path that assembles a concise set of relevant
  TextUnits for a given query, using tokenization and optional conversation history.

Behavior and edge cases
- _map_ids raises AttributeError if any subject TextUnit in the configured text_units
  is missing 'id' or 'short_id'.
- __init__ accepts optional text_units and tokenizer; if omitted, defaults from the
  embedding store and context builder are used.
- build_context delegates to the BasicContextBuilder and returns a ContextBuilderResult that
  describes the selected TextUnits and their arrangement in the context.
- Any exceptions raised by the underlying embedding model, vector store, tokenizer, or
  builder may propagate to the caller and should be handled by the caller as part of
  integration.

Parameters
- __init__(text_embedder: EmbeddingModel, text_unit_embeddings: BaseVectorStore, text_units: list[TextUnit] | None = None, tokenizer: Tokenizer | None = None, embedding_vectorstore_key: str = "id") -&gt; None
  Initialize the BasicSearchContext with the embedding model, vector store, and optional text units and tokenizer.
  text_embedder: EmbeddingModel used to generate text embeddings for similarity search.
  text_unit_embeddings: BaseVectorStore containing embeddings for TextUnit objects.
  text_units: Optional list of TextUnit instances to be considered; if None, a default set may be discovered at runtime.
  tokenizer: Optional Tokenizer to tokenize text during context construction.
  embedding_vectorstore_key: The key in the vector store that maps to the text unit id (default "id").

- build_context(query: str, conversation_history: ConversationHistory | None = None, k: int = 10, max_context_tokens: int = 12_000, context_name: str = "Sources", column_delimiter: str = "|", text_id_col: str = "source_id", text_col: str = "text", **kwargs) -&gt; ContextBuilderResult
  Build the context for the given query in basic search mode.

Returns
- ContextBuilderResult describing the selected context (text units, token usage, and formatting for downstream pipelines).

Raises
- AttributeError: if any configured TextUnit is missing 'id' or 'short_id' attributes.

Summary
This module coordinates a lightweight, token-aware path to assemble a compact context for querying
in Graphrag's basic search workflow, suitable for downstream pipelines that expect a ContextBuilderResult.

## Classes

- [`BasicSearchContext`](../api/classes/graphrag-query-structured-search-basic-search-basic-context-basicsearchcontext)

## Functions

- [`_map_ids`](../api/functions/graphrag-query-structured-search-basic-search-basic-context-map-ids)
- [`build_context`](../api/functions/graphrag-query-structured-search-basic-search-basic-context-build-context)
- [`__init__`](../api/functions/graphrag-query-structured-search-basic-search-basic-context-init)

