---
sidebar_position: 69
---

# MockTokenizer

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py`

## Overview

MockTokenizer is a simple, stateless tokenizer used in unit tests to deterministically encode and decode text by Unicode code points. It simulates a Unicode code point based tokenizer without relying on a real tokenizer implementation.

Attributes:
- Stateless; no persistent state or instance attributes are required or maintained.

Determinism:
- All operations are deterministic: encode uses ord() per character; decode reconstructs the string exactly from code points.

Usage:
mock = MockTokenizer()
text = 'Test'
tokens = mock.encode(text)
# tokens would be [84, 101, 115, 116]
decoded = mock.decode(tokens)
# decoded would be 'Test'

Methods:
encode(text)
  Description: Encode the input text as a list of Unicode code points.
  Args:
    text: str. The input text to encode as Unicode code points.
  Returns:
    list[int]. A list of integers where each integer is the Unicode code point of the corresponding character in text.
  Raises:
    TypeError: If text is None or not a string (or not iterable).

decode(token_ids)
  Description: Decode token ids to string by converting each integer to a character and concatenating.
  Args:
    token_ids: An iterable of integers representing token IDs to decode into a string.
  Returns:
    str: The decoded string.
  Raises:
    TypeError: If token_ids contains non-integer elements or elements cannot be processed by chr.
    ValueError: If any token_id is outside the valid Unicode range for chr (e.g., not in 0 &lt;= id &lt;= 0x10FFFF).

## Methods

### `encode`

```python
def encode(self, text)
```

### `decode`

```python
def decode(self, token_ids)
```

