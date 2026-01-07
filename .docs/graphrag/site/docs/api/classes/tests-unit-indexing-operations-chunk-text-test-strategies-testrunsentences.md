---
sidebar_position: 153
---

# TestRunSentences

**File:** `tests/unit/indexing/operations/chunk_text/test_strategies.py`

## Overview

TestRunSentences validates the sentence-splitting behavior of the chunk_text strategies used by the indexing module. The tests focus on observable outcomes: input documents are split into sentences, each sentence is emitted as a TextChunk with the exact sentence text, and every chunk carries a reference to its originating document via source_doc_indices. A progress reporter is exercised to indicate per-document processing progress without asserting a specific invocation count. Setup initializes required resources by calling bootstrap before tests run. The suite examines basic functionality with a single document, handling of multiple documents, and mixed/edge whitespace scenarios.

## Methods

### `setup_method`

```python
def setup_method(self, method)
```

### `test_basic_functionality`

```python
def test_basic_functionality(self)
```

### `test_multiple_documents`

```python
def test_multiple_documents(self)
```

### `test_mixed_whitespace_handling`

```python
def test_mixed_whitespace_handling(self)
```

