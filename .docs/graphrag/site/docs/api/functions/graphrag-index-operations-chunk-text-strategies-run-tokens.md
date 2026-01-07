---
sidebar_position: 79
---

# run_tokens

**File:** `graphrag/index/operations/chunk_text/strategies.py` (lines 35-55)

## Signature

```python
def run_tokens(
    input: list[str],
    config: ChunkingConfig,
    tick: ProgressTicker,
) -> Iterable[TextChunk]
```

## Description

Chunks text into chunks based on encoding tokens.

Args:
    input: list[str] - The input texts to be chunked.
    config: ChunkingConfig - Chunking configuration. Uses:
        size: number of tokens per chunk,
        overlap: number of overlapping tokens between consecutive chunks,
        encoding_model: name of the encoding model used to tokenize.
    tick: ProgressTicker - Progress reporter; invoked to indicate progress.

Returns:
    Iterable[TextChunk] - An iterable of TextChunk objects representing the resulting chunks.

Raises:
    Exception - Propagates exceptions raised by underlying encoding retrieval or tokenization.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/strategies.py::get_encoding_fn`
- `graphrag/index/text_splitting/text_splitting.py::TokenChunkerOptions`
- `graphrag/index/text_splitting/text_splitting.py::split_multiple_texts_on_tokens`

## Called By

This function is called by:

- `tests/unit/indexing/operations/chunk_text/test_strategies.py::TestRunTokens.test_basic_functionality`
- `tests/unit/indexing/operations/chunk_text/test_strategies.py::TestRunTokens.test_non_string_input`

