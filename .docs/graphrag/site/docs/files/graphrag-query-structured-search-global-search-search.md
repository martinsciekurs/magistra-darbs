---
sidebar_position: 211
---

# graphrag/query/structured_search/global_search/search.py

## Overview

Module implementing a structured global search workflow that orchestrates parallel batches of community report summaries, maps each batch to an answer, and reduces the results into a final user-facing response using a language model. This module exposes the GlobalSearch class, which coordinates initialization, parallel querying, and optional streaming of results. It is designed to be configurable via prompts, behavior flags, and LLM parameters, and it relies on supporting components such as a GlobalContextBuilder and a Tokenizer.

Public API overview
- GlobalSearch: Primary orchestrator class that coordinates the end-to-end structured global search. Public surface includes initialization (__init__), batch-based search (search), and streaming search (stream_search).

Key components and flow
- GlobalContextBuilder: Builds per-batch contextual data used by the language model to generate batch-level answers.
- Tokenizer: Optional utility for text handling and length management.
- Prompts: Default system prompts for mapping, knowledge integration, and reduction are exposed as configurable defaults and may be overridden via constructor arguments (MAP_SYSTEM_PROMPT, GENERAL_KNOWLEDGE_INSTRUCTION, REDUCE_SYSTEM_PROMPT, NO_DATA_ANSWER).
- Mapping, reducing, and parsing helpers (private methods) implement the three-stage pipeline:
  - _map_response_single_batch: Generate an answer for a single chunk/batch of community reports.
  - _stream_reduce_response: Stream and reduce multiple map results into a single output by ranking key points and interacting with the LLM.
  - _reduce_response: Combine per-batch results into a final answer for non-streaming scenarios.
  - _parse_search_response: Parse a JSON-formatted response to extract structured key points.

Inputs and outputs
- __init__(model, context_builder, tokenizer=None, map_system_prompt=None, reduce_system_prompt=None, response_type="multiple paragraphs", allow_general_knowledge=False, general_knowledge_inclusion_prompt=None, json_mode=True, callbacks=None, max_data_tokens=8000, map_llm_params=None, reduce_llm_params=None, map_max_length=1000, reduce_max_length=2000, context_builder_params=None, concurrent_coroutines=32):
  Initializes a GlobalSearch instance with the language model, context builder, optional tokenizer, and various behavior/customization options. May raise underlying component exceptions as they occur during setup.
- search(query, conversation_history=None, **kwargs) -&gt; SearchResult:
  Perform a complete, non-streaming global search for the given query. Returns a SearchResult containing the final answer and associated metadata. Can raise exceptions from LLM calls or context construction.
- stream_search(query, conversation_history=None) -&gt; AsyncGenerator[str, None]:
  Stream the final answer as fragments. The generator yields string fragments representing streaming portions of the final response.
- Internal helpers (not part of public API): _map_response_single_batch, _stream_reduce_response, _reduce_response, _parse_search_response. These are used to implement the mapping, reduction, and parsing steps of the pipeline and are subject to change without breaking the public interface.

Behavior notes
- Streaming vs batch processing: stream_search yields incremental fragments during reduction, while search collects and returns a complete final result. The class supports parallel batch evaluation with a configurable level of concurrency via concurrent_coroutines.
- Error handling: callers should expect exceptions from the underlying components (ChatModel, GlobalContextBuilder, Tokenizer, JSON parsing, etc.). The module does not obscure or swallow these errors; wrap or translate them as needed for your application.

Exports
- GlobalSearch: The main orchestrator class for the structured global search workflow, with a focus on parallel batch querying, optional streaming, and final reduction of results.

## Classes

- [`GlobalSearch`](../api/classes/graphrag-query-structured-search-global-search-search-globalsearch)

## Functions

- [`__init__`](../api/functions/graphrag-query-structured-search-global-search-search-init)
- [`search`](../api/functions/graphrag-query-structured-search-global-search-search-search)
- [`_map_response_single_batch`](../api/functions/graphrag-query-structured-search-global-search-search-map-response-single-batch)
- [`_stream_reduce_response`](../api/functions/graphrag-query-structured-search-global-search-search-stream-reduce-response)
- [`stream_search`](../api/functions/graphrag-query-structured-search-global-search-search-stream-search)
- [`_reduce_response`](../api/functions/graphrag-query-structured-search-global-search-search-reduce-response)
- [`_parse_search_response`](../api/functions/graphrag-query-structured-search-global-search-search-parse-search-response)

