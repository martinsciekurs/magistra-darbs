---
sidebar_position: 221
---

# graphrag/tokenizer/litellm_tokenizer.py

## Overview

Litellm tokenizer wrapper for Litellm models.

Purpose:
This module provides a wrapper around litellm's encode and decode functions to operate on a single model identified by model_name. It exposes the LitellmTokenizer class that uses the configured model for text-to-token and token-to-text conversions.

Key exports:
- LitellmTokenizer: A tokenizer that uses a Litellm model to encode text into tokens and decode tokens back into text.

Public API details:
- __init__(model_name: str) -&gt; None
  Args:
      model_name (str): The name of the Litellm model to use for tokenization.
  Returns:
      None: This initializer does not return a value.
  Raises:
      Exception: If initialization fails due to a...
- encode(text: str) -&gt; list[int]
  Args:
      text (str): The input text to encode.
  Returns:
      list[int]: A list of tokens representing the encoded text.
  Raises:
      Exception: If encoding fails due to underlying encoder error...
- decode(tokens: list[int]) -&gt; str
  Args:
      tokens (list[int]): A list of tokens to decode.
  Returns:
      str: The decoded string from the list of tokens.
  Raises:
      Exception: If decoding fails due to an underlying error in the decoding process....

## Classes

- [`LitellmTokenizer`](../api/classes/graphrag-tokenizer-litellm-tokenizer-litellmtokenizer)

## Functions

- [`decode`](../api/functions/graphrag-tokenizer-litellm-tokenizer-decode)
- [`__init__`](../api/functions/graphrag-tokenizer-litellm-tokenizer-init)
- [`encode`](../api/functions/graphrag-tokenizer-litellm-tokenizer-encode)

