---
sidebar_position: 128
---

# run

**File:** `graphrag/index/operations/layout_graph/zero.py` (lines 24-60)

## Signature

```python
def run(
    graph: nx.Graph,
    on_error: ErrorHandlerFn,
) -> GraphLayout
```

## Description

Compute a zero-coordinate GraphLayout for the given graph, optionally using per-node cluster/category and size hints, and fall back to a default layout if an error occurs.

Args:
  graph: nx.Graph
      The input graph. Nodes may have attributes such as cluster (or community) and degree (or size) that are used to influence the layout.

  on_error: ErrorHandlerFn
      Callback invoked when an error occurs. It is called with the exception, a formatted traceback string, and None.

Returns:
  GraphLayout
      A layout (list of NodePosition) for all nodes in the graph. Coordinates are initialized to zero; cluster and size metadata are derived from node attributes when available. If an error occurs during layout computation, a fallback layout with all nodes at (0,0) is returned.

Raises:
  None

## Dependencies

This function calls:

- `graphrag/index/operations/layout_graph/typing.py::NodePosition`
- `graphrag/index/operations/layout_graph/zero.py::get_zero_positions`

