---
sidebar_position: 68
---

# is_valid_entity

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py` (lines 20-25)

## Signature

```python
def is_valid_entity(entity: tuple[str, str], tokens: list[str]) -> bool
```

## Description

Check if the given entity is valid with respect to the provided tokens.

Args:
    entity: tuple[str, str] - The entity as (text, label). The label indicates the category of the entity, e.g., CARDINAL or ORDINAL.
    tokens: list[str] - The tokens associated with the entity used to determine validity.

Returns:
    bool - True if the entity is valid according to the validation rules; otherwise False.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py::is_compound`

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/np_extractors/cfg_extractor.py::CFGNounPhraseExtractor._tag_noun_phrases`
- `graphrag/index/operations/build_noun_graph/np_extractors/syntactic_parsing_extractor.py::SyntacticNounPhraseExtractor._tag_noun_phrases`

