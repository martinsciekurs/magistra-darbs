---
sidebar_position: 66
---

# is_compound

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py` (lines 7-12)

## Signature

```python
def is_compound(tokens: list[str]) -> bool
```

## Description

Return True if any token in the provided list is a hyphenated compound token.

Args:
    tokens: List[str] - The list of tokens to inspect.

Returns:
    bool - True if at least one token contains a hyphen, has length greater than 1 after stripping whitespace, and splits into more than one part when split by hyphen; otherwise False.

Raises:
    None

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py::CFGNounPhraseExtractor._tag_noun_phrases`
- `graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py::is_valid_entity`
- `graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py::SyntacticNounPhraseExtractor._tag_noun_phrases`

