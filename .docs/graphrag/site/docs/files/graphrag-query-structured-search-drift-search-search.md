---
sidebar_position: 208
---

# graphrag/query/structured_search/drift_search/search.py

## Overview

DRIFT-based search orchestrator for structured queries.

This module defines the DRIFTSearch class, which coordinates a ChatModel, a DRIFT
context builder, and local search components to perform iterative, DRIFT-style
structured searches for queries. It supports both reduction of the final answer and
streaming of results, enabling flexible interaction patterns with the underlying
language model.

Public API
- DRIFTSearch: orchestrates the DRIFT-style search workflow for structured queries.
  - __init__(model, context_builder, tokenizer=None, query_state=None, callbacks=None)
  - init_local_search() -&gt; LocalSearch
  - search(query, conversation_history=None, reduce=True, **kwargs) -&gt; SearchResult
  - stream_search(query, conversation_history=None) -&gt; AsyncGenerator[str, None]

Notes
- Internal helper methods (_reduce_response, _process_primer_results, _search_step,
  _reduce_response_streaming) implement internal steps of the workflow and are not
  part of the public API.

## Classes

- [`DRIFTSearch`](../api/classes/graphrag-query-structured-search-drift-search-search-driftsearch)

## Functions

- [`_reduce_response`](../api/functions/graphrag-query-structured-search-drift-search-search-reduce-response)
- [`_process_primer_results`](../api/functions/graphrag-query-structured-search-drift-search-search-process-primer-results)
- [`_search_step`](../api/functions/graphrag-query-structured-search-drift-search-search-search-step)
- [`_reduce_response_streaming`](../api/functions/graphrag-query-structured-search-drift-search-search-reduce-response-streaming)
- [`__init__`](../api/functions/graphrag-query-structured-search-drift-search-search-init)
- [`init_local_search`](../api/functions/graphrag-query-structured-search-drift-search-search-init-local-search)
- [`search`](../api/functions/graphrag-query-structured-search-drift-search-search-search)
- [`stream_search`](../api/functions/graphrag-query-structured-search-drift-search-search-stream-search)

