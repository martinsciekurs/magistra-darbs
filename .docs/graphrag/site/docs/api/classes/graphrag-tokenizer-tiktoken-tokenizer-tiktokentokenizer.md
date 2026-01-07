---
sidebar_position: 21
---

# TiktokenTokenizer

**File:** `graphrag/tokenizer/tiktoken_tokenizer.py`

## Overview

TiktokenTokenizer is a Tokenizer implementation that uses the tiktoken library to encode and decode text using a specified encoding.

Parameters:
  encoding_name (str): The name of the Tiktoken encoding to use for tokenization.

Attributes:
  encoding_name (str): The name of the Tiktoken encoding used for tokenization.
  encoding: The tiktoken encoding object created from encoding_name.

Notes:
  - Encoding and decoding are performed via the underlying tiktoken encoding.
  - encode(text) returns a list of token IDs for the provided text.
  - decode(tokens) returns the string corresponding to the given list of token IDs.

## Methods

### `decode`

```python
def decode(self, tokens: list[int]) -> str
```

### `__init__`

```python
def __init__(self, encoding_name: str) -> None
```

### `encode`

```python
def encode(self, text: str) -> list[int]
```

