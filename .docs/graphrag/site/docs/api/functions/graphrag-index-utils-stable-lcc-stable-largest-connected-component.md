---
sidebar_position: 214
---

# stable_largest_connected_component

**File:** `graphrag/index/utils/stable_lcc.py` (lines 12-20)

## Signature

```python
def stable_largest_connected_component(graph: nx.Graph) -> nx.Graph
```

## Description

Return the largest connected component of the graph, with nodes and edges sorted in a stable way.

Args:
    graph (nx.Graph): Input graph from which to compute the stable largest connected component.

Returns:
    nx.Graph: The stabilized largest connected component graph with deterministic ordering of nodes and edges.

## Dependencies

This function calls:

- `graphrag/index/utils/stable_lcc.py::_stabilize_graph`
- `graphrag/index/utils/stable_lcc.py::normalize_node_names`

## Called By

This function is called by:

- `graphrag/index/operations/cluster_graph.py::_compute_leiden_communities`
- `graphrag/index/operations/embed_graph/embed_graph.py::embed_graph`
- `tests/unit/indexing/graph/utils/test_stable_lcc.py::TestStableLCC.test_undirected_graph_run_twice_produces_same_graph`
- `tests/unit/indexing/graph/utils/test_stable_lcc.py::TestStableLCC.test_directed_graph_keeps_source_target_intact`
- `tests/unit/indexing/graph/utils/test_stable_lcc.py::TestStableLCC.test_directed_graph_run_twice_produces_same_graph`

