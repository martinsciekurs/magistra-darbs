---
sidebar_position: 210
---

# _sort_source_target

**File:** `graphrag/index/utils/stable_lcc.py` (lines 45-51)

## Signature

```python
def _sort_source_target(edge)
```

## Description

Sorts a graph edge so that the source and target are in a stable, canonical order.

Args:
    edge: A 3-tuple (source, target, edge_data) representing an edge from a graph.

Returns:
    A 3-tuple (source, target, edge_data) with source and target ordered such that source &lt;= target.

Raises:
    ValueError: If edge does not contain exactly three elements.
    TypeError: If edge elements do not support comparison.

## Called By

This function is called by:

- `graphrag/index/utils/stable_lcc.py::_stabilize_graph`

