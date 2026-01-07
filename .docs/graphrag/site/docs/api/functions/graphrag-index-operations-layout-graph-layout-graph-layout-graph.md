---
sidebar_position: 123
---

# layout_graph

**File:** `graphrag/index/operations/layout_graph/layout_graph.py` (lines 17-55)

## Signature

```python
def layout_graph(
    graph: nx.Graph,
    enabled: bool,
    embeddings: NodeEmbeddings | None,
)
```

## Description

Apply a layout algorithm to a nx.Graph. The method returns a dataframe containing the node positions.

Args:
    graph: The nx.Graph to layout.
    enabled: If True, use the UMAP-based layout; otherwise fall back to the Zero layout.
    embeddings: NodeEmbeddings | None. Embeddings for each node in the graph. If None, embeddings are treated as empty.

Returns:
    pandas.DataFrame: A DataFrame containing the layout with columns 'label', 'x', 'y', 'size'.

Raises:
    Exceptions raised by the underlying layout implementations (UMAP or Zero) during layout computation.

## Dependencies

This function calls:

- `graphrag/index/operations/layout_graph/layout_graph.py::_run_layout`

## Called By

This function is called by:

- `graphrag/index/operations/finalize_entities.py::finalize_entities`

