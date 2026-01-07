---
sidebar_position: 207
---

# graphrag/query/structured_search/drift_search/primer.py

## Overview

Module with DRIFT drift-search primer and related utilities for structured search over community reports.

This module defines two public classes: DRIFTPrimer and PrimerQueryProcessor, which implement the DRIFT drift-search workflow for structured queries over community reports. The workflow includes decomposing queries with global guidance, splitting reports into folds for parallel processing, and executing asynchronous searches using a language model, with a tokenizer used to manage token counts.

Public API
- DRIFTPrimer
  - __init__(config: DRIFTSearchConfig, chat_model: ChatModel, tokenizer: Tokenizer | None = None) -&gt; None
  - __init__(chat_model: ChatModel, text_embedder: EmbeddingModel, reports: list[CommunityReport], tokenizer: Tokenizer | None = None) -&gt; None
  - split_reports(reports: pd.DataFrame) -&gt; list[pd.DataFrame]
  - search(query: str, top_k_reports: pd.DataFrame) -&gt; SearchResult
  - decompose_query(query: str, reports: pd.DataFrame) -&gt; tuple[dict, dict[str, int]]

- PrimerQueryProcessor
  - __init__(chat_model: ChatModel, text_embedder: EmbeddingModel, reports: list[CommunityReport], tokenizer: Tokenizer | None = None) -&gt; None
  - __init__(config: DRIFTSearchConfig, chat_model: ChatModel, tokenizer: Tokenizer | None = None) -&gt; None
  - expand_query(query: str) -&gt; tuple[str, dict[str, int]]

Notes
- The classes rely on DRIFTSearchConfig, CommunityReport, ChatModel, EmbeddingModel, Tokenizer, and the primer prompt DRIFT_PRIMER_PROMPT to guide query expansion and embedding.

## Classes

- [`DRIFTPrimer`](../api/classes/graphrag-query-structured-search-drift-search-primer-driftprimer)
- [`PrimerQueryProcessor`](../api/classes/graphrag-query-structured-search-drift-search-primer-primerqueryprocessor)

## Functions

- [`split_reports`](../api/functions/graphrag-query-structured-search-drift-search-primer-split-reports)
- [`search`](../api/functions/graphrag-query-structured-search-drift-search-primer-search)
- [`__call__`](../api/functions/graphrag-query-structured-search-drift-search-primer-call)
- [`expand_query`](../api/functions/graphrag-query-structured-search-drift-search-primer-expand-query)
- [`decompose_query`](../api/functions/graphrag-query-structured-search-drift-search-primer-decompose-query)
- [`__init__`](../api/functions/graphrag-query-structured-search-drift-search-primer-init)
- [`__init__`](../api/functions/graphrag-query-structured-search-drift-search-primer-init)

