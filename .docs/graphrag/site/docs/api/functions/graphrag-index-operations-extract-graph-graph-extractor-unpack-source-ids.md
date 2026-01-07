---
sidebar_position: 114
---

# _unpack_source_ids

**File:** `graphrag/index/operations/extract_graph/graph_extractor.py` (lines 298-300)

## Signature

```python
def _unpack_source_ids(data: Mapping) -> list[str]
```

## Description

Unpack source_id values from a mapping.

Args:
    data (Mapping): A mapping that may contain the key "source_id" whose value is a string of IDs separated by comma-space.

Returns:
    list[str]: The list of source IDs. If the key is missing or the value is None, returns an empty list.

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/graph_extractor.py::GraphExtractor._process_results`

