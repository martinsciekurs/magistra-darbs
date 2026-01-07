---
sidebar_position: 16
---

# BaseNounPhraseExtractor

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/base.py`

## Overview

BaseNounPhraseExtractor is an abstract base class that defines the interface and shared configuration for noun phrase extraction using a SpaCy model. Concrete subclasses implement the actual extraction logic and provide a meaningful string representation.

Attributes:
- model_name: The name of the SpaCy model to use, or None to avoid loading a model at initialization time.
- exclude_nouns: Optional list of nouns to exclude from extraction. If None, an empty list is used. Subclasses may normalize or store this differently.
- max_word_length: Maximum length of a word to consider when forming noun phrases.
- word_delimiter: Delimiter used to join words within a noun phrase.

Args:
- model_name: The name of the SpaCy model to use, or None.
- exclude_nouns: List of nouns to exclude from extraction. If None, an empty list is used.
- max_word_length: Maximum length of a word to consider when forming noun phrases.
- word_delimiter: Delimiter used to join words within a noun phrase.

Returns:
- None

Raises:
- TypeError: If the abstract base class is instantiated directly (enforced by the abstract base class mechanism).

Notes:
- Instantiation of this class is prevented by the abstract base class mechanism; concrete subclasses must implement extract and __str__.

Load/spacy model helper:
- load_spacy_model model_name with optional exclude: Load a SpaCy model by name and optionally exclude components. Returns a SpaCy language object.

Subclass contract:
- Concrete subclasses must implement extract to return a list of noun phrases from input text and __str__ to provide a meaningful string representation. The base class provides a helper for loading the SpaCy model but does not dictate specific extraction logic.

## Methods

### `load_spacy_model`

```python
def load_spacy_model(
        model_name: str, exclude: list[str] | None = None
    ) -> spacy.language.Language
```

### `__init__`

```python
def __init__(
        self,
        model_name: str | None,
        exclude_nouns: list[str] | None = None,
        max_word_length: int = 15,
        word_delimiter: str = " ",
    ) -> None
```

### `extract`

```python
def extract(self, text: str) -> list[str]
```

### `__str__`

```python
def __str__(self) -> str
```

