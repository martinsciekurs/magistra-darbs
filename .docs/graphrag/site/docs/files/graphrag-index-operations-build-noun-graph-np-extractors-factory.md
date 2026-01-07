---
sidebar_position: 50
---

# graphrag/index/operations/build_noun_graph/np_extractors/factory.py

## Overview

Module for building noun phrase extractors in the noun graph construction pipeline.

Purpose
- Provide a factory (NounPhraseExtractorFactory) to select and instantiate noun phrase extractors based on a TextAnalyzerConfig.
- Maintain a registry mapping extractor type identifiers to concrete extractor classes. This enables get_np_extractor to instantiate the correct extractor according to configuration (e.g., CFG-based, Regex-based, Syntactic Parsing).

Key exports
- NounPhraseExtractorFactory: factory class with classmethods get_np_extractor and register
- get_np_extractor(cls, config: TextAnalyzerConfig) -&gt; BaseNounPhraseExtractor: returns a noun phrase extractor instance dictated by the config
- register(cls, np_extractor_type: str, np_extractor: type): register a new extractor implementation under a type key
- create_noun_phrase_extractor(analyzer_config: TextAnalyzerConfig) -&gt; BaseNounPhraseExtractor: create an extractor from configuration; may raise Exception if creation fails

Brief summary
The module enables extensible noun phrase extraction by decoupling extractor implementations from their usage, using a registry and a unified creation interface to produce the appropriate extractor (CFG, Regex, Syntactic) based on TextAnalyzerConfig.

## Classes

- [`NounPhraseExtractorFactory`](../api/classes/graphrag-index-operations-build-noun-graph-np-extractors-factory-nounphraseextractorfactory)

## Functions

- [`get_np_extractor`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-factory-get-np-extractor)
- [`register`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-factory-register)
- [`create_noun_phrase_extractor`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-factory-create-noun-phrase-extractor)

