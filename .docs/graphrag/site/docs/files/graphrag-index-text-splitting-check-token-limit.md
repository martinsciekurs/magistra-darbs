---
sidebar_position: 101
---

# graphrag/index/text_splitting/check_token_limit.py

## Overview

Module for checking whether input text fits within a token limit for a single chunk, using TokenTextSplitter for tokenization.

Purpose
This module exposes a small utility, check_token_limit, that determines if a given text can be represented as a single tokenized chunk without exceeding the specified maximum number of tokens.

Key exports
- check_token_limit(text: str, max_token: int) -&gt; int

Args
text (str): The input text to check against the token limit.
max_token (int): The maximum number of tokens allowed for a single chunk.

Returns
int: 1 if the text can be represented as a single chunk under the limit, 0 otherwise.

Raises
TypeError: If text is not a string or max_token is not an int.
ValueError: If max_token is non-positive.
RuntimeError: If an error occurs during tokenization or splitting using TokenTextSplitter.

Summary
The utility relies on TokenTextSplitter to perform tokenization and determines the single-chunk feasibility by comparing the resulting token count to max_token.

## Functions

- [`check_token_limit`](../api/functions/graphrag-index-text-splitting-check-token-limit-check-token-limit)

