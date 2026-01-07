---
sidebar_position: 254
---

# tests/unit/indexing/operations/chunk_text/test_chunk_text.py

## Overview

Unit tests for the chunk_text operations in graphrag.

Purpose
This module contains unit tests for the chunk_text module used to chunk text data according to various strategies. It exercises the _get_num_total helper, the chunk_text function, the load_strategy and run_strategy utilities, and the TextChunk typing, using ChunkStrategyType to validate behavior.

Key exports
- _get_num_total: computes the total number of elements in a pandas DataFrame column
- chunk_text: chunks text according to a configured strategy
- load_strategy: loads the strategy callable for a given ChunkStrategyType
- run_strategy: executes a strategy on input data
- TextChunk: typing data structure describing a text chunk

Brief summary
The tests cover total element counting for DataFrame columns containing strings and non-strings, running various chunking strategies with different input formats, loading strategies for tokens and sentences, and the end-to-end chunk_text workflow including progress reporting and returning a pandas Series of chunks.

## Functions

- [`test_get_num_total_default`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-get-num-total-default)
- [`test_get_num_total_array`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-get-num-total-array)
- [`test_run_strategy_str`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-run-strategy-str)
- [`test_run_strategy_arr_str`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-run-strategy-arr-str)
- [`test_run_strategy_arr_tuple`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-run-strategy-arr-tuple)
- [`test_run_strategy_arr_tuple_same_doc`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-run-strategy-arr-tuple-same-doc)
- [`test_load_strategy_tokens`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-load-strategy-tokens)
- [`test_load_strategy_sentence`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-load-strategy-sentence)
- [`test_load_strategy_none`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-load-strategy-none)
- [`test_chunk_text`](../api/functions/tests-unit-indexing-operations-chunk-text-test-chunk-text-test-chunk-text)

