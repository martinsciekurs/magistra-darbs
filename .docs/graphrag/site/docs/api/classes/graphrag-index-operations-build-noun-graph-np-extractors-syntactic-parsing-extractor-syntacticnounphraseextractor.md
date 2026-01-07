---
sidebar_position: 43
---

# SyntacticNounPhraseExtractor

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py`

## Overview

SyntacticNounPhraseExtractor extracts noun phrases from text using syntactic parsing with SpaCy, with configurable filters and optional named-entity integration.

Args:
    model_name: The name of the NLP model used by the underlying SpaCy pipeline.
    max_word_length: Maximum number of words allowed in a noun phrase.
    include_named_entities: Whether to include named entities as noun phrases.
    exclude_entity_tags: List of entity tags to exclude from consideration.
    exclude_pos_tags: List of part-of-speech tags to exclude from noun phrases.
    exclude_nouns: List of noun strings to exclude from results.
    word_delimiter: Delimiter used to join tokens into a noun phrase.

Returns:
    None

Attributes:
    model_name: The NLP model identifier used for parsing.
    max_word_length: Maximum length of a noun phrase by word count.
    include_named_entities: Flag indicating whether named entities are included.
    exclude_entity_tags: Entity tags to skip during extraction.
    exclude_pos_tags: POS tags to skip when forming noun phrases.
    exclude_nouns: Specific nouns to exclude from results.
    word_delimiter: Delimiter used to join tokens inside a noun phrase.

## Methods

### `extract`

```python
def extract(
        self,
        text: str,
    ) -> list[str]
```

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
    )
```

### `_tag_noun_phrases`

```python
def _tag_noun_phrases(
        self, noun_chunk: Span, entities: list[Span]
    ) -> dict[str, Any]
```

