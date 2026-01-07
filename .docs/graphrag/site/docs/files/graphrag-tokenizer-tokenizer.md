---
sidebar_position: 223
---

# graphrag/tokenizer/tokenizer.py

## Overview

Abstract interface for tokenization operations.

This module defines the Tokenizer abstract base class, which specifies how text is
encoded into a sequence of token identifiers, how many tokens a given text would yield,
and how to decode a list of tokens back into text. Subclasses must implement encode,
num_tokens, and decode.

Key exports:
- Tokenizer

Brief summary:
Concrete implementations provide actual tokenization logic by implementing encode, num_tokens, and
decode.

Public API:
encode(self, text: str) -&gt; list[int]
- text: The input text to encode.

Returns:
- list[int]: A list of tokens representing the encoded text.

Raises:
- NotImplementedError: The encode method must be implemented by subclasses.

num_tokens(self, text: str) -&gt; int
- text: The input text to analyze.

Returns:
- int: The number of tokens in the input text.

Raises:
- NotImplementedError: If the encode method is not implemented by a subclass.

decode(self, tokens: list[int]) -&gt; str
- tokens: A list of tokens to decode.

Returns:
- str: The decoded string from the list of tokens.

Raises:
- NotImplementedError: If the decode method has not been implemented by subclasses.

## Classes

- [`Tokenizer`](../api/classes/graphrag-tokenizer-tokenizer-tokenizer)

## Functions

- [`encode`](../api/functions/graphrag-tokenizer-tokenizer-encode)
- [`num_tokens`](../api/functions/graphrag-tokenizer-tokenizer-num-tokens)
- [`decode`](../api/functions/graphrag-tokenizer-tokenizer-decode)

