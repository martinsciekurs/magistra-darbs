---
sidebar_position: 57
---

# graphrag/index/operations/chunk_text/strategies.py

## Overview

Utilities for text chunking strategies used in graphrag's chunking pipeline.

This module implements encoding/decoding helpers and two chunking strategies:
sentence-based chunking and token-based chunking. It exposes the main functions
encode, decode, run_sentences, get_encoding_fn, and run_tokens to produce
TextChunk objects for downstream indexing.

Key exports:
- encode(text: str) -&gt; list[int]: Encodes input text into token IDs using the configured encoding model. If input is not a string, it will be converted to a string.
- decode(tokens: list[int]) -&gt; str: Decodes a list of token IDs back into a string.
- run_sentences(input: list[str], _config: ChunkingConfig, tick: ProgressTicker) -&gt; Iterable[TextChunk]:
  Chunks text into sentences; yields TextChunk objects for each sentence.
- get_encoding_fn(encoding_name): Returns a pair of callables (encode, decode) for the given encoding model.
- run_tokens(input: list[str], config: ChunkingConfig, tick: ProgressTicker) -&gt; Iterable[TextChunk]:
  Chunks text into chunks based on token counts using the configured encoding model.

Brief summary:
Provides core strategies for chunking text by sentence and by token count, leveraging
a configurable encoding model and a progress reporter to produce TextChunk results.

## Functions

- [`encode`](../api/functions/graphrag-index-operations-chunk-text-strategies-encode)
- [`decode`](../api/functions/graphrag-index-operations-chunk-text-strategies-decode)
- [`run_sentences`](../api/functions/graphrag-index-operations-chunk-text-strategies-run-sentences)
- [`get_encoding_fn`](../api/functions/graphrag-index-operations-chunk-text-strategies-get-encoding-fn)
- [`run_tokens`](../api/functions/graphrag-index-operations-chunk-text-strategies-run-tokens)

