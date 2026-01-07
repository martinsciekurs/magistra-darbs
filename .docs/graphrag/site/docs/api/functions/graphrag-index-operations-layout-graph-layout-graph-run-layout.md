---
sidebar_position: 122
---

# _run_layout

**File:** `graphrag/index/operations/layout_graph/layout_graph.py` (lines 58-84)

## Signature

```python
def _run_layout(
    graph: nx.Graph,
    enabled: bool,
    embeddings: NodeEmbeddings,
) -> GraphLayout
```

## Description

Run the layout algorithm on a graph and return the resulting GraphLayout.

Args:
    graph: nx.Graph
        The graph to layout.
    enabled: bool
        If True, use the UMAP-based layout; otherwise fall back to the Zero layout.
    embeddings: NodeEmbeddings
        Embeddings for each node in the graph.

Returns:
    GraphLayout
        The resulting layout as a GraphLayout.

## Example 💡 Generated

```python
from mod import _run_layout
import networkx as nx
G = nx.path_graph(4)
embeddings = {
    0: [0.1, 0.2],
    1: [0.2, 0.3],
    2: [0.3, 0.4],
    3: [0.4, 0.5],
}
enabled = True
layout = _run_layout(G, enabled, embeddings)
# layout is the resulting GraphLayout
```

## Called By

This function is called by:

- `graphrag/index/operations/layout_graph/layout_graph.py::layout_graph`

