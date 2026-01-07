---
sidebar_position: 123
---

# TextSplitter

**File:** `graphrag/index/text_splitting/text_splitting.py`

## Overview

Abstract base class for splitting input text into chunks for downstream processing (e.g., embeddings).

The class provides shared configuration for text chunking and defines the abstract interface split_text, which concrete subclasses must implement to perform the actual splitting.

Args:
    chunk_size (int): Maximum length of a chunk as measured by length_function. This follows the OpenAI embedding model's max input buffer length guidance. Default: 8191.
    chunk_overlap (int): Overlap between consecutive chunks, measured using length_function. Default: 100.
    length_function (LengthFn): Function to compute the length of a string. Default: len.
    keep_separator (bool): Whether to keep the separator between chunks. Default: False.
    add_start_index (bool): Whether to prefix each chunk with its start index. Default: False.
    strip_whitespace (bool): Whether to strip leading/trailing whitespace when forming chunks. Default: True.

Attributes:
    chunk_size
    chunk_overlap
    length_function
    keep_separator
    add_start_index
    strip_whitespace

Methods:
    split_text(text: str | list[str]) -&gt; Iterable[str]
        Abstract method. Split text into chunks according to the concrete implementation. Accepts a single string or a list of strings as input and yields an iterable of text chunks.

Notes:
    This is an abstract base class. split_text is not implemented here and must be provided by subclasses.

## Methods

### `split_text`

```python
def split_text(self, text: str | list[str]) -> Iterable[str]
```

### `__init__`

```python
def __init__(
        self,
        # based on text-ada-002-embedding max input buffer length
        # https://platform.openai.com/docs/guides/embeddings/second-generation-models
        chunk_size: int = 8191,
        chunk_overlap: int = 100,
        length_function: LengthFn = len,
        keep_separator: bool = False,
        add_start_index: bool = False,
        strip_whitespace: bool = True,
    )
```

