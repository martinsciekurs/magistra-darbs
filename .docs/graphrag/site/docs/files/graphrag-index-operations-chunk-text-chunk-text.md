---
sidebar_position: 56
---

# graphrag/index/operations/chunk_text/chunk_text.py

## Overview

Chunk text chunking utilities for the GraphRag indexing workflow.

This module implements helpers to chunk text data contained in a pandas DataFrame column using token-based or sentence-based strategies, with optional NLP bootstrap. It exposes a small API to count elements, load and run chunking strategies, and to perform the actual chunking operation.

Key exports:
- _get_num_total(output, column): Compute the total number of elements in a DataFrame column, counting strings as a single element and non-string entries by their length.
- run_strategy(strategy_exec, input, config, tick): Run the given chunking strategy on the input data and return the produced chunks.
- load_strategy(strategy): Load the strategy method for the given chunking strategy.
- chunk_text(input, column, size, overlap, encoding_model, strategy, callbacks): Chunk a piece of text into smaller pieces.

## Functions

- [`_get_num_total`](../api/functions/graphrag-index-operations-chunk-text-chunk-text-get-num-total)
- [`run_strategy`](../api/functions/graphrag-index-operations-chunk-text-chunk-text-run-strategy)
- [`load_strategy`](../api/functions/graphrag-index-operations-chunk-text-chunk-text-load-strategy)
- [`chunk_text`](../api/functions/graphrag-index-operations-chunk-text-chunk-text-chunk-text)

