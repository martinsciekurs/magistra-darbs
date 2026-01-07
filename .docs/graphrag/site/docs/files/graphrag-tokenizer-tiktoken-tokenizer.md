---
sidebar_position: 222
---

# graphrag/tokenizer/tiktoken_tokenizer.py

## Overview

Module providing a Tiktoken-based Tokenizer using the tiktoken library.

Purpose:
Provide a Tokenizer implementation that encodes and decodes text using a specified tiktoken encoding.

Key exports:
- TiktokenTokenizer: A Tokenizer implementation that uses tiktoken to encode and decode text with a specified encoding_name.

Summary:
The module exposes TiktokenTokenizer, which accepts encoding_name (str) in its constructor and uses it to initialize a tiktoken encoding object. It provides the public methods decode(tokens: list[int]) -&gt; str and encode(text: str) -&gt; list[int], conforming to the graphrag.tokenizer.tokenizer.Tokenizer interface.

## Classes

- [`TiktokenTokenizer`](../api/classes/graphrag-tokenizer-tiktoken-tokenizer-tiktokentokenizer)

## Functions

- [`decode`](../api/functions/graphrag-tokenizer-tiktoken-tokenizer-decode)
- [`__init__`](../api/functions/graphrag-tokenizer-tiktoken-tokenizer-init)
- [`encode`](../api/functions/graphrag-tokenizer-tiktoken-tokenizer-encode)

