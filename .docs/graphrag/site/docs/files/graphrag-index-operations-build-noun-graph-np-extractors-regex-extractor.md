---
sidebar_position: 52
---

# graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py

## Overview

RegexENNounPhraseExtractor: a fast, regex-based English noun phrase extractor used for building noun graphs.

Purpose:
This module implements a lightweight, fast noun phrase extractor that relies on a regular-expression strategy. It is designed for speed over exhaustive accuracy and is suitable for constructing noun graphs. The extractor uses TextBlob and NLTK data and will lazily download required NLP resources on first use if they are not already present. Resource initialization is performed via a generic loader without assuming specific corpus identifiers.

Public API:
- RegexENNounPhraseExtractor: Primary export of this module. A class that exposes an extract method for noun phrase extraction and internal helpers for phrase analysis.

Class RegexENNounPhraseExtractor:
- Purpose: Regular-expression-based English noun phrase extractor for building noun graphs. Note: significantly faster than syntactic parser-based extractors, with potential trade-offs in accuracy. The class can be extended in the future to remove external dependencies.
- Constructor: exclude_nouns: list[str] — nouns to exclude from results; max_word_length: int — maximum length of any token to consider; word_delimiter: str — delimiter used to join multi-word phrases in the output.
- Methods:
  - extract(text: str) -&gt; list[str]: Extract noun phrases from the provided text, applying the base configuration (exclude_nouns, max_word_length, word_delimiter) to filter and format results.
  - _tag_noun_phrases(noun_phrase: str, all_proper_nouns: list[str] | None = None) -&gt; dict[str, Any]: Analyze a noun phrase and return attributes used for filtering, including cleaned_tokens and cleaned_text.
  - __str__(self) -&gt; str: Return a cache-key-like string encoding the extractor's configuration for reuse.
  - __init__(exclude_nouns: list[str], max_word_length: int, word_delimiter: str): Initialize the extractor with configuration.

Resource and dependency loading:
- The extractor ensures required resources (TextBlob/NLTK data) are available, downloading them on first use if missing. This avoids hard-coding exact resource names in documentation and supports lazy initialization.

Returns:
- extract returns a list[str] of noun phrases.
- _tag_noun_phrases returns a dict[str, Any] with analysis results (e.g., cleaned_tokens, cleaned_text).
- __str__ returns a string representing current configuration.

Raises:
- Exceptions may propagate from resource loading or underlying NLP tooling if resource downloads fail or inputs are invalid.

Usage example:
Example:
from graphrag.index.operations.build_noun_graph.np_extractors.regex_extractor import RegexENNounPhraseExtractor
extractor = RegexENNounPhraseExtractor(exclude_nouns=["the", "and"], max_word_length=6, word_delimiter="_")
phrases = extractor.extract("Sample text to process.")

File location:
graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py

## Classes

- [`RegexENNounPhraseExtractor`](../api/classes/graphrag-index-operations-build-noun-graph-np-extractors-regex-extractor-regexennounphraseextractor)

## Functions

- [`extract`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-regex-extractor-extract)
- [`_tag_noun_phrases`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-regex-extractor-tag-noun-phrases)
- [`__str__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-regex-extractor-str)
- [`__init__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-regex-extractor-init)

