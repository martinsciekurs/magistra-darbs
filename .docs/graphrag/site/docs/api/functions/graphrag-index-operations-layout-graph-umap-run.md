---
sidebar_position: 126
---

# run

**File:** `graphrag/index/operations/layout_graph/umap.py` (lines 26-69)

## Signature

```python
def run(
    graph: nx.Graph,
    embeddings: NodeEmbeddings,
    on_error: ErrorHandlerFn,
) -> GraphLayout
```

## Description

Compute a UMAP-based layout for the given graph using node embeddings and optional per-node attributes, with a fallback layout if the UMAP computation fails.

Args:
  graph: nx.Graph
      The input graph. Nodes may have attributes such as cluster (or community) and degree (or size) that are used to influence the layout.
  embeddings: NodeEmbeddings
      Mapping of node identifiers to embedding vectors; entries with None are ignored.
  on_error: ErrorHandlerFn
      Callback invoked when an error occurs during layout computation.

Returns:
  GraphLayout
      The resulting layout as a list of NodePosition objects representing node positions. If UMAP succeeds, positions reflect the embeddings; otherwise a fallback layout with all nodes at (0,0) is returned.

Raises:
  None
      This function does not raise exceptions; errors are reported via on_error and a fallback layout is returned.

## Dependencies

This function calls:

- `graphrag/index/operations/layout_graph/typing.py::NodePosition`
- `graphrag/index/operations/layout_graph/umap.py::_filter_raw_embeddings`
- `graphrag/index/operations/layout_graph/umap.py::compute_umap_positions`

