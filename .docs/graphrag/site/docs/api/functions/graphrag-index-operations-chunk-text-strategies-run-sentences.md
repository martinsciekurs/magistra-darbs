---
sidebar_position: 77
---

# run_sentences

**File:** `graphrag/index/operations/chunk_text/strategies.py` (lines 58-69)

## Signature

```python
def run_sentences(
    input: list[str], _config: ChunkingConfig, tick: ProgressTicker
) -> Iterable[TextChunk]
```

## Description

Chunks text into multiple parts by sentence.

Args:
  input: list[str] - list of input documents to chunk into sentences.
  _config: ChunkingConfig - chunking configuration (unused by this strategy).
  tick: ProgressTicker - progress reporter; invoked to indicate progress after processing each input document.

Returns:
  Iterable[TextChunk] - yields TextChunk objects for each sentence, with text_chunk set to the sentence and source_doc_indices containing the index of the source document.

Raises:
  Exceptions raised by nltk.sent_tokenize during sentence tokenization.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/typing.py::TextChunk`

## Called By

This function is called by:

- `tests/unit/indexing/operations/chunk_text/test_strategies.py::TestRunSentences.test_basic_functionality`
- `tests/unit/indexing/operations/chunk_text/test_strategies.py::TestRunSentences.test_multiple_documents`
- `tests/unit/indexing/operations/chunk_text/test_strategies.py::TestRunSentences.test_mixed_whitespace_handling`

