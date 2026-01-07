---
sidebar_position: 49
---

# graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py

## Overview

CFG-based noun phrase extractor for graph-building combining CFG-based noun-chunk matching with optional named-entity recognition (NER).

This module defines the CFGNounPhraseExtractor class, which uses a SpaCy model to process text, applies configured CFG grammars to identify candidate noun phrases, and then filters and merges results according to configured rules. The extractor aims to be faster than dependency-parser-based extractors, with grammar customization allowing adaptation to different languages.

Public API:
- CFGNounPhraseExtractor: Fast noun-phrase extractor combining CFG-based noun-chunk matching with optional NER to support graph-building. Public methods include extract(text) -&gt; list[str], extract_cfg_matches(doc) -&gt; list[tuple[str, str]], and internal helper _tag_noun_phrases(noun_chunk, entities=None) -&gt; dict[str, Any]. The __str__ method is provided for cache key generation.

## Classes

- [`CFGNounPhraseExtractor`](../api/classes/graphrag-index-operations-build-noun-graph-np-extractors-cfg-extractor-cfgnounphraseextractor)

## Functions

- [`__str__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-cfg-extractor-str)
- [`__init__`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-cfg-extractor-init)
- [`extract`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-cfg-extractor-extract)
- [`extract_cfg_matches`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-cfg-extractor-extract-cfg-matches)
- [`_tag_noun_phrases`](../api/functions/graphrag-index-operations-build-noun-graph-np-extractors-cfg-extractor-tag-noun-phrases)

