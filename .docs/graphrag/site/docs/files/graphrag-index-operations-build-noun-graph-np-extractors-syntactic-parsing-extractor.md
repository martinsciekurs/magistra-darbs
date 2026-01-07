---
sidebar_position: 54
---

# graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py

## Overview

Module for extracting noun phrases from text using syntactic parsing with SpaCy to support building noun graphs.

Exports:
    SyntacticNounPhraseExtractor: Extractor that uses syntactic parsing to identify noun phrases with optional named-entity integration and configurable filters.

Summary:
    Provides a syntactic parsing based noun phrase extractor that relies on SpaCy dependency parsing and optional named-entity recognition to extract noun phrases. It relies on a base extractor and validators to filter candidates by length, entity status, and noun exclusion, leveraging SpaCy's dependency parsing and optional NER.

Classes:
    SyntacticNounPhraseExtractor:
        A noun-phrase extractor that uses syntactic parsing via SpaCy, with configurable filters and optional named-entity integration.

        Args:
            model_name: The name of the NLP model used by the underlying SpaCy pipeline.
            max_word_length: Maximum number of words allowed in a noun phrase.
            include_named_entities: Whether to include named entities as noun phrases.
            exclude_entity_tags: Tags of entities to exclude.
            exclude_pos_tags: POS tags to exclude.
            exclude_nouns: Nouns to exclude.
            word_delimiter: Delimiter used to join tokens into a noun phrase.

        Public methods:
            extract(text: str) -&gt; list[str]: Extract noun phrases from text. Noun phrases may include named entities and noun chunks, which are filtered based on heuristics.
            __str__() -&gt; str: Returns the string representation used for cache key generation. The string encodes the extractor configuration from model_name, max_word_length, include_named_entities, exclude_entity_tags, exclude_pos_tags, exclude_nouns, and word_delimiter.
            _tag_noun_phrases(noun_chunk: Span, entities: list[Span]) -&gt; dict[str, Any]: Extract attributes of a noun chunk for filtering. Returns a dictionary containing keys such as cleaned_tokens: List[Token].

## Classes

- [`SyntacticNounPhraseExtractor`](../api/classes/graphrag-index-operations-build-noun-graph-np-extractors-syntactic-parsing-extractor-syntacticnounphraseextractor)

## Functions

- [`extract`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-syntactic-parsing-extractor-extract)
- [`__str__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-syntactic-parsing-extractor-str)
- [`__init__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-syntactic-parsing-extractor-init)
- [`_tag_noun_phrases`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-syntactic-parsing-extractor-tag-noun-phrases)

