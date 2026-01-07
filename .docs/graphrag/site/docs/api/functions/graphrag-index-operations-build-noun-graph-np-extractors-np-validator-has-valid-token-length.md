---
sidebar_position: 67
---

# has_valid_token_length

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py` (lines 15-17)

## Signature

```python
def has_valid_token_length(tokens: list[str], max_length: int) -> bool
```

## Description

Check if all tokens have valid length.

Args:
    tokens: List of tokens to validate lengths for.
    max_length: Maximum allowed length for any token.

Returns:
    bool: True if all tokens have length &lt;= max_length, otherwise False.

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py::CFGNounPhraseExtractor._tag_noun_phrases`
- `graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py::SyntacticNounPhraseExtractor._tag_noun_phrases`

