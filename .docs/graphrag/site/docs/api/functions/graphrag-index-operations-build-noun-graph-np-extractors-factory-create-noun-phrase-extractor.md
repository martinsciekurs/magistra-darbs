---
sidebar_position: 65
---

# create_noun_phrase_extractor

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/factory.py` (lines 78-82)

## Signature

```python
def create_noun_phrase_extractor(
    analyzer_config: TextAnalyzerConfig,
) -> BaseNounPhraseExtractor
```

## Description

Create a noun phrase extractor from a configuration.

Args:
    analyzer_config (TextAnalyzerConfig): Configuration for text analysis used to configure the noun phrase extractor.

Returns:
    BaseNounPhraseExtractor: An instance of a noun phrase extractor created according to the given configuration.

Raises:
    Exception: If the underlying factory fails to create the extractor (propagates from NounPhraseExtractorFactory.get_np_extractor).

## Called By

This function is called by:

- `graphrag/index/workflows/extract_graph_nlp.py::extract_graph_nlp`

