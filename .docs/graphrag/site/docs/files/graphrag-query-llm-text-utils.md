---
sidebar_position: 199
---

# graphrag/query/llm/text_utils.py

## Overview

Utilities for batching, JSON cleaning/parsing, and token-based text chunking to support LLM workflows.

This module provides helpers to:
- batch data into fixed-size chunks for batched LLM prompts or processing (batched)
- repair and parse JSON-like content produced by language models into native Python objects (try_parse_json_object)
- split large text into pieces that respect a maximum token budget, using a tokenizer (chunk_text)

Dependencies and defaults:
- A default tokenizer can be created via get_tokenizer using the encoding model defined in graphrag.config.defaults as ENCODING_MODEL. If a tokenizer is not supplied to chunk_text, one is created using that model.

Exported functions:
- batched(iterable, n)
- try_parse_json_object(input, verbose=True)
- chunk_text(text, max_tokens, tokenizer=None)

batched
Args:
- iterable (Iterator): The input sequence to batch.
- n (int): Batch size; must be at least 1.
Returns:
- Iterator[tuple]: Batches as tuples of length n; the final batch may be shorter.
Raises:
- ValueError: If n &lt; 1.

try_parse_json_object
Args:
- input (str): Raw string that may contain JSON or JSON-like content.
- verbose (bool): If True, log warnings/exceptions encountered during parsing.
Returns:
- tuple[str, dict]: The (potentially cleaned) input string and the parsed JSON object as a dict.
  If parsing is not recoverable, the dict will be empty and the input string will reflect any repairs.

Notes:
- The function repairs JSON-like content using repair_json before attempting to parse with json.loads.
- No exception is raised to the caller; on failure, an empty dict is returned (when applicable).

chunk_text
Args:
- text (str): The input text to chunk.
- max_tokens (int): Maximum tokens per chunk.
- tokenizer (Tokenizer | None): Tokenizer to use for encoding/decoding. If None, a default tokenizer is created via get_tokenizer(encoding_model=defs.ENCODING_MODEL).
Returns:
- Iterator[str]: An iterator that yields chunk strings decoded from token sequences, each not exceeding max_tokens.

Notes:
- The default tokenizer selection is performed by obtaining a Tokenizer for the encoding model defined in defs.ENCODING_MODEL when tokenizer=None.

## Functions

- [`batched`](../api/functions/graphrag-query-llm-text-utils-batched)
- [`try_parse_json_object`](../api/functions/graphrag-query-llm-text-utils-try-parse-json-object)
- [`chunk_text`](../api/functions/graphrag-query-llm-text-utils-chunk-text)

