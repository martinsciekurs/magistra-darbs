---
sidebar_position: 115
---

# _unpack_descriptions

**File:** `graphrag/index/operations/extract_graph/graph_extractor.py` (lines 293-295)

## Signature

```python
def _unpack_descriptions(data: Mapping) -> list[str]
```

## Description

Unpack descriptions from a mapping by splitting the description string into lines.

Args:
    data (Mapping): input mapping that may contain a "description" key with a string value.

Returns:
    list[str]: The list of description lines. If no description is provided, returns an empty list.

Raises:
    AttributeError: If the description value exists but does not support the split method.

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/graph_extractor.py::GraphExtractor._process_results`

