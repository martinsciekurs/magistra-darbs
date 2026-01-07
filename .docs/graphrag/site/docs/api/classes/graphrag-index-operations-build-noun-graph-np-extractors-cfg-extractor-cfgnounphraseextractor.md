---
sidebar_position: 38
---

# CFGNounPhraseExtractor

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py`

## Overview

CFGNounPhraseExtractor is a fast noun phrase extractor that combines CFG-based noun-chunk matching with optional named-entity recognition (NER) to support noun-phrase extraction for graph-building. It processes text with a SpaCy model, applies configured CFG grammars to identify candidate noun phrases, and then filters and merges results according to the configured rules. The extractor is configurable via instance attributes and aims to be robust across languages with grammar-driven matching and optional NER enrichment.

## Methods

### `__str__`

```python
def __str__(self) -> str
```

### `__init__`

```python
def __init__(
        self,
        model_name: str,
        max_word_length: int,
        include_named_entities: bool,
        exclude_entity_tags: list[str],
        exclude_pos_tags: list[str],
        exclude_nouns: list[str],
        word_delimiter: str,
        noun_phrase_grammars: dict[tuple, str],
        noun_phrase_tags: list[str],
    )
```

### `extract`

```python
def extract(
        self,
        text: str,
    ) -> list[str]
```

### `extract_cfg_matches`

```python
def extract_cfg_matches(self, doc: Doc) -> list[tuple[str, str]]
```

### `_tag_noun_phrases`

```python
def _tag_noun_phrases(
        self, noun_chunk: tuple[str, str], entities: set[str] | None = None
    ) -> dict[str, Any]
```

