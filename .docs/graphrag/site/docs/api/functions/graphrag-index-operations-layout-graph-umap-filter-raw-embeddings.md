---
sidebar_position: 124
---

# _filter_raw_embeddings

**File:** `graphrag/index/operations/layout_graph/umap.py` (lines 72-77)

## Signature

```python
def _filter_raw_embeddings(embeddings: NodeEmbeddings) -> NodeEmbeddings
```

## Description

Filter out None entries from the input node embeddings mapping.

Args:
    embeddings: NodeEmbeddings - Mapping of node identifiers to embedding vectors; may contain None values.

Returns:
    NodeEmbeddings - A new mapping with all entries whose embeddings are not None.

## Called By

This function is called by:

- `graphrag/index/operations/layout_graph/umap.py::run`

