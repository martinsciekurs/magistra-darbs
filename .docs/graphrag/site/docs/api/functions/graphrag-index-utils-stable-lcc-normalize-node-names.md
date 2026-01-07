---
sidebar_position: 212
---

# normalize_node_names

**File:** `graphrag/index/utils/stable_lcc.py` (lines 64-67)

## Signature

```python
def normalize_node_names(graph: nx.Graph | nx.DiGraph) -> nx.Graph | nx.DiGraph
```

## Description

Normalize node names for a graph by applying HTML unescaping, converting to uppercase, and trimming whitespace on each node label.

Args:
  graph (nx.Graph | nx.DiGraph): Input graph whose node names will be normalized.

Returns:
  nx.Graph | nx.DiGraph: The input graph with node names normalized (uppercased, stripped of whitespace, and HTML entities unescaped).

## Called By

This function is called by:

- `graphrag/index/utils/stable_lcc.py::stable_largest_connected_component`

