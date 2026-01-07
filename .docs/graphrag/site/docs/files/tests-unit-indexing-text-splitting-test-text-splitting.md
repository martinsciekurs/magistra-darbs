---
sidebar_position: 257
---

# tests/unit/indexing/text_splitting/test_text_splitting.py

## Overview

Text splitting utilities for token-based chunking used in indexing and downstream processing. This module provides small, deterministic building blocks to convert text into token sequences and then split those sequences into fixed-size chunks with optional overlap.

Exports:
- NoopTextSplitter: A no-op splitter that returns input text unchanged as a list of strings.
  API:
  - split_text(text) -&gt; list[str]
    • If text is a string, returns [text].
    • If text is an iterable of strings, returns a list copy of that iterable.
    • Raises TypeError if the input type is not a string or an iterable of strings.

- TokenChunkerOptions: Configuration for tokenization with encode/decode hooks.
  API:
  - __init__(tokens_per_chunk: int, chunk_overlap: int, encode: Callable[[str], list[int]], decode: Callable[[list[int]], str]) -&gt; None
  - properties:
    tokens_per_chunk (int): Number of tokens per output chunk.
    chunk_overlap (int): Number of overlapping tokens between consecutive chunks.
    encode(text: str) -&gt; list[int]: Convert text to a list of token IDs.
    decode(token_ids: list[int]) -&gt; str: Convert token IDs back to text.
  API guarantees:
  - tokens_per_chunk &gt; 0, 0 &lt;= chunk_overlap &lt; tokens_per_chunk (or behavior documented by encode/decode).
  - encode/decode are supplied by the tokenizer surface used by the splitter.

- TokenTextSplitter: Splits text into token-based chunks using a tokenizer.
  API:
  - __init__(chunk_size: int, chunk_overlap: int, tokenizer: TokenChunkerOptions) -&gt; None
  - split_text(text: str | None) -&gt; list[str]
    • If text is None or empty, returns [].
    • If text is not a string, raises TypeError.
    • On non-empty strings, encodes the text to tokens using tokenizer.encode and delegates to split_single_text_on_tokens to produce chunk strings by decoding token slices.

- split_single_text_on_tokens(text: str, tokenizer: TokenChunkerOptions) -&gt; list[str]
  • Splits a single text into chunks based on tokenizer configuration.
  • Returns a list of chunk strings decoded from contiguous token slices.
  • Raises TypeError if text is not a string.
  • May raise exceptions propagated from the provided encode/decode callbacks.

- split_multiple_texts_on_tokens(texts: Sequence[str], tokenizer: TokenChunkerOptions, on_tick: Optional[Callable[[int, int], None]] = None) -&gt; list[str]
  • Processes multiple texts in sequence, returning the concatenated list of chunk strings.
  • After processing each input text, if on_tick is provided, it is called to signal progress. The callback signature is typically on_tick(current_index: int, total_texts: int).
  • Raises TypeError if texts is not a sequence of strings.
  • May raise exceptions from per-text splitting or encode/decode calls.

Notes on API surface and behavior:
- Encode/decode responsibilities live on TokenChunkerOptions (or an equivalent tokenizer surface) and are used by the splitters to go between plain text and token IDs.
- Edge cases handled by the API include None/empty inputs and invalid types; corresponding methods either return empty results or raise TypeError as appropriate.
- The multi-text splitter supports an optional progress callback to report how many texts have been processed, enabling integration with long-running indexing workflows.

## Classes

- [`MockTokenizer`](../api/classes/tests-unit-indexing-text-splitting-test-text-splitting-mocktokenizer)

## Functions

- [`encode`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-encode)
- [`test_split_text_str_bool`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-text-str-bool)
- [`encode`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-encode)
- [`test_split_text_large_input`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-text-large-input)
- [`test_token_text_splitter`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-token-text-splitter)
- [`decode`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-decode)
- [`test_split_text_str_int`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-text-str-int)
- [`decode`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-decode)
- [`test_split_text_str_empty`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-text-str-empty)
- [`test_noop_text_splitter`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-noop-text-splitter)
- [`test_split_single_text_on_tokens`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-single-text-on-tokens)
- [`test_split_single_text_on_tokens_no_overlap`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-single-text-on-tokens-no-overlap)
- [`test_split_multiple_texts_on_tokens`](../api/functions/tests-unit-indexing-text-splitting-test-text-splitting-test-split-multiple-texts-on-tokens)

