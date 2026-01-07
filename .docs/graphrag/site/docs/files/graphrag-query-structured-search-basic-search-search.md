---
sidebar_position: 204
---

# graphrag/query/structured_search/basic_search/search.py

## Overview

Module providing a BasicSearch orchestrator for single-context-window basic search.

Overview:
This module defines the BasicSearch class and two entry points, search and stream_search, to build a
context that fits within a single context window and generate an answer for a user query. It wires
together a language model (ChatModel), a context builder (BasicContextBuilder), an optional tokenizer,
and an optional system prompt to produce either a complete answer or a streaming sequence of
answer chunks suitable for chat-like interfaces.

Key exports:
- BasicSearch: Orchestrates context construction and model interaction for basic searches.
- search: Build the context and generate a full answer for a given query, optionally using conversation history.
- stream_search: Build the context and stream the answer for a given query, optionally using conversation history.

Classes:
- BasicSearch: See above.

Functions:
- search(query: str, conversation_history: ConversationHistory | None = None, **kwargs) -&gt; SearchResult: Generate a complete answer for the query.
- stream_search(query: str, conversation_history: ConversationHistory | None = None) -&gt; AsyncGenerator[str, None]: Stream answer chunks.

Constructor:
- __init__(self, model: ChatModel, context_builder: BasicContextBuilder, tokenizer: Tokenizer | None = None, system_prompt: str | None = None, response_type: str = "multiple paragraphs", callbacks: list[QueryCallbacks] | None = None, model_params: dict[str, Any] | None = None, context_builder_params: dict | None = None)

Brief summary:
Provides a single-context-window basic search workflow that can be used to obtain either a full reply or a stream of
response chunks by combining a chat model with a context builder and optional components.

Raises:
Exceptions raised by the underlying components (ChatModel, BasicContextBuilder, Tokenizer, prompts) may propagate to the caller.

## Classes

- [`BasicSearch`](../api/classes/graphrag-query-structured-search-basic-search-search-basicsearch)

## Functions

- [`search`](../api/functions/graphrag-query-structured-search-basic-search-search-search)
- [`stream_search`](../api/functions/graphrag-query-structured-search-basic-search-search-stream-search)
- [`__init__`](../api/functions/graphrag-query-structured-search-basic-search-search-init)

