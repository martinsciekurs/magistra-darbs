---
sidebar_position: 39
---

# RegexENNounPhraseExtractor

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py`

## Overview

Regular-expression-based English noun phrase extractor used for building noun graphs.

NOTE: This extractor was used in the first benchmarking of LazyGraphRAG and only works for English. It is much faster but likely less accurate than the syntactic parser-based extractor. TODO: Reimplement this using SpaCy to remove TextBlob dependency.

Args:
  exclude_nouns: Nouns to exclude from extraction.
  max_word_length: Maximum length of words to consider when forming noun phrases.
  word_delimiter: Delimiter used to join tokens within noun phrases.

## Methods

### `extract`

```python
def extract(
        self,
        text: str,
    ) -> list[str]
```

### `_tag_noun_phrases`

```python
def _tag_noun_phrases(
        self, noun_phrase: str, all_proper_nouns: list[str] | None = None
    ) -> dict[str, Any]
```

### `__str__`

```python
def __str__(self) -> str
```

### `__init__`

```python
def __init__(
        self,
        exclude_nouns: list[str],
        max_word_length: int,
        word_delimiter: str,
    )
```

