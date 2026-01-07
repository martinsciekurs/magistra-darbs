---
sidebar_position: 31
---

# Tokenizer

**File:** `graphrag/tokenizer/tokenizer.py`

## Overview

Abstract interface for tokenization operations.

This abstract base class defines the contract for encoding text into a sequence of token identifiers, determining how many tokens a given text would yield, and decoding a list of tokens back into text. Subclasses must implement encode, num_tokens, and decode.

Key attributes:
None defined at this level. Concrete implementations may expose internal state such as a vocabulary or encoding rules.

Returns:
This class does not produce values by itself. The concrete methods return the types described by their signatures when implemented in subclasses (list[int] for encode, int for num_tokens, and str for decode).

Raises:
NotImplementedError: The encode, num_tokens, and decode methods must be implemented by subclasses.

## Methods

### `encode`

```python
def encode(self, text: str) -> list[int]
```

### `num_tokens`

```python
def num_tokens(self, text: str) -> int
```

### `decode`

```python
def decode(self, tokens: list[int]) -> str
```

