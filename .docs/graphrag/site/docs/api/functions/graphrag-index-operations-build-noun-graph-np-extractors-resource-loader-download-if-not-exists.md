---
sidebar_position: 69
---

# download_if_not_exists

**File:** `graphrag/index/operations/build_noun_graph/np_extractors/resource_loader.py` (lines 9-38)

## Signature

```python
def download_if_not_exists(resource_name) -> bool
```

## Description

Download nltk resources if they haven't been already.

Args:
    resource_name: The name of the nltk resource to locate or download.

Returns:
    bool: True if the resource was found without downloading; False if the resource was not found and had to be downloaded.

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/np_extractors/regex_extractor.py::RegexENNounPhraseExtractor.__init__`

