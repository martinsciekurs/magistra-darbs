---
sidebar_position: 213
---

# graphrag/query/structured_search/local_search/search.py

## Overview

Local search orchestration for structured search within a single context window.

Overview:
This module provides the LocalSearch class, which orchestrates local search operations by building a compact context and querying a language model to generate an answer for a user query. It coordinates the context builder, optional tokenizer, system prompt, and callbacks to produce a structured search result or a streaming output.

Public interfaces:
- LocalSearch: Class that encapsulates local search orchestration.

- search(self, query: str, conversation_history: ConversationHistory | None = None, **kwargs) -&gt; SearchResult:
  Builds a local search context that fits a single context window and generates an answer for the user query.
  Args:
    query: The user query to process.
    conversation_history: Optional conversation history to incorporate into the search context.
    **kwargs: Additional keyword arguments passed to the context builder and the model.
  Returns:
    A SearchResult containing the generated answer and related metadata.
  Raises:
    Exceptions raised by the underlying components (model, builders, tokenizers).

- stream_search(self, query: str, conversation_history: ConversationHistory | None = None) -&gt; AsyncGenerator[str, None]:
  Build local search context that fits a single context window and generate answer for the user query as a stream.
  Args:
    query: The user query to process.
    conversation_history: Optional conversation history to incorporate into the search context.
  Returns:
    An asynchronous generator yielding strings representing chunks of the generated answer.
  Raises:
    Exceptions raised by the underlying components.

Notes:
- This module relies on interfaces such as ChatModel, LocalContextBuilder, ConversationHistory, Tokenizer, and QueryCallbacks.

## Classes

- [`LocalSearch`](../api/classes/graphrag-query-structured-search-local-search-search-localsearch)

## Functions

- [`search`](../api/functions/graphrag-query-structured-search-local-search-search-search)
- [`__init__`](../api/functions/graphrag-query-structured-search-local-search-search-init)
- [`stream_search`](../api/functions/graphrag-query-structured-search-local-search-search-stream-search)

