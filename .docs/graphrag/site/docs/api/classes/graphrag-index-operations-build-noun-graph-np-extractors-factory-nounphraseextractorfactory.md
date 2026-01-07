---
sidebar_position: 104
---

# NounPhraseExtractorFactory

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/factory.py`

## Overview

Factory for selecting and instantiating noun phrase extractors based on configuration.

This class provides a registry of available noun phrase extractors and a single entry point to instantiate the appropriate extractor according to a TextAnalyzerConfig. It relies on a class-level mapping from extractor type identifiers to extractor classes to resolve and instantiate the requested extractor.

Key attributes
- np_extractor_types: ClassVar mapping from extractor type identifiers (str) to extractor classes (the registry).

Methods
- get_np_extractor(cls, config: TextAnalyzerConfig) -&gt; BaseNounPhraseExtractor: Get the noun phrase extractor instance based on the configured type.
  Args: cls: The class (used as a classmethod parameter). config: TextAnalyzerConfig containing extractor_type and related options such as model_name, max_word_length, include_named_entities, exclude_entity_tags, exclude_pos_tags, exclude_nouns, word_delimiter, noun_phrase_grammars, and noun_phrase_tags.
  Returns: BaseNounPhraseExtractor
  Raises: Exceptions raised by underlying extractors or by configuration issues may propagate.

- register(cls, np_extractor_type: str, np_extractor: type): Register a noun phrase extractor in NounPhraseExtractorFactory by adding it to the class-level registry np_extractor_types.
  Args: cls: The class on which this classmethod is invoked. np_extractor_type: The string identifier for the extractor type. np_extractor: The extractor class to register.
  Returns: None
  Raises: Exceptions raised during registration may propagate.

## Methods

### `get_np_extractor`

```python
def get_np_extractor(cls, config: TextAnalyzerConfig) -> BaseNounPhraseExtractor
```

### `register`

```python
def register(cls, np_extractor_type: str, np_extractor: type)
```

