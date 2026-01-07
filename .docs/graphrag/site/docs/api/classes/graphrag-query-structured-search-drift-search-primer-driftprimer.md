---
sidebar_position: 82
---

# DRIFTPrimer

**File:** `graphrag/query/structured_search/drift_search/primer.py`

## Overview

DRIFTPrimer coordinates the DRIFT drift-search workflow for structured query processing over community reports. It decomposes queries using global guidance, splits the input reports into folds for parallel processing, and executes asynchronous searches against a language model, using a tokenizer to manage tokens.

Attributes:
    config (DRIFTSearchConfig): Configuration settings for DRIFT search.
    chat_model (ChatModel): The language model used for searching.
    tokenizer (Tokenizer): Tokenizer used to manage tokens during processing.

Args:
    config (DRIFTSearchConfig): Configuration settings for DRIFT search.
    chat_model (ChatModel): The language model used for searching.
    tokenizer (Tokenizer, optional): Tokenizer for managing tokens. If not provided, a default tokenizer is obtained.

Returns:
    None

Raises:
    None

## Methods

### `split_reports`

```python
def split_reports(self, reports: pd.DataFrame) -> list[pd.DataFrame]
```

### `search`

```python
def search(
        self,
        query: str,
        top_k_reports: pd.DataFrame,
    ) -> SearchResult
```

### `decompose_query`

```python
def decompose_query(
        self, query: str, reports: pd.DataFrame
    ) -> tuple[dict, dict[str, int]]
```

### `__init__`

```python
def __init__(
        self,
        config: DRIFTSearchConfig,
        chat_model: ChatModel,
        tokenizer: Tokenizer | None = None,
    )
```

