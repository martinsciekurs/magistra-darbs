---
sidebar_position: 70
---

# bootstrap

**File:** `graphrag/index/operations/chunk_text/bootstrap.py` (lines 15-31)

## Signature

```python
def bootstrap()
```

## Description

Bootstrap initialization for NLTK resources.

Downloads and prepares the required NLTK data on the first call, and sets the module-level flag initialized_nltk to True to prevent repeated work.

This function downloads the following resources and ensures WordNet is loaded: punkt, punkt_tab, averaged_perceptron_tagger, averaged_perceptron_tagger_eng, maxent_ne_chunker, maxent_ne_chunker_tab, words, and wordnet; it also calls wn.ensure_loaded().

Returns:
    None

Raises:
    ImportError: If the nltk package or required submodules are unavailable.

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/chunk_text.py::load_strategy`
- `tests/unit/indexing/operations/chunk_text/test_strategies.py::TestRunSentences.setup_method`

