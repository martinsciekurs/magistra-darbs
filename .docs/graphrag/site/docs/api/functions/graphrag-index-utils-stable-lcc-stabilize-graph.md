---
sidebar_position: 213
---

# _stabilize_graph

**File:** `graphrag/index/utils/stable_lcc.py` (lines 23-61)

## Signature

```python
def _stabilize_graph(graph: nx.Graph) -> nx.Graph
```

## Description

Ensure an undirected graph with the same relationships will always be read the same way.

Args:
    graph: nx.Graph The input graph. May be directed or undirected; the function will preserve the directedness and return a new graph with deterministic ordering of nodes and edges.

Returns:
    nx.Graph The stabilized graph. If the input graph is directed, the returned graph is a nx.DiGraph; otherwise, a nx.Graph.

## Dependencies

This function calls:

- `graphrag/index/utils/stable_lcc.py::_get_edge_key`
- `graphrag/index/utils/stable_lcc.py::_sort_source_target`

## Called By

This function is called by:

- `graphrag/index/utils/stable_lcc.py::stable_largest_connected_component`

