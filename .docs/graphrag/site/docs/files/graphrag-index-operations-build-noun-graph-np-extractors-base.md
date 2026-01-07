---
sidebar_position: 48
---

# graphrag/index/operations/build_noun_graph/np_extractors/base.py

## Overview

Base module for noun-phrase extraction using SpaCy.

Purpose:
This module provides an abstract base class for noun-phrase extraction and a helper function to load SpaCy language models, enabling consistent configuration and reuse across concrete extractors.

Key exports:
- load_spacy_model(model_name: str, exclude: list[str] | None = None) -&gt; spacy.language.Language
  Load a SpaCy model. Args: model_name: Name of the SpaCy model to load. exclude: Optional list of components to exclude from loading. Returns: spacy.language.Language: The loaded SpaCy language object. Raises: OSError: If the model cannot be loaded (after attempting to download if necessary).
- BaseNounPhraseExtractor: Abstract base class for noun phrase extraction. __init__(self, model_name: str | None, exclude_nouns: list[str] | None = None, max_word_length: int = 15, word_delimiter: str = " ") -&gt; None; Public methods: extract(text: str) -&gt; list[str], __str__() -&gt; str. Subclasses implement the concrete extraction logic and a meaningful string representation.

Brief summary:
The module defines the scaffolding for noun-phrase extraction using SpaCy models. Concrete extractors implement the actual extraction algorithm and provide string representations, while the base class handles shared configuration and interface.

## Classes

- [`BaseNounPhraseExtractor`](../api/classes/graphrag-index-operations-build-noun-graph-np-extractors-base-basenounphraseextractor)

## Functions

- [`load_spacy_model`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-base-load-spacy-model)
- [`__init__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-base-init)
- [`extract`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-base-extract)
- [`__str__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-base-str)

