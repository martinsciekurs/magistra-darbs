---
sidebar_position: 211
---

# _get_edge_key

**File:** `graphrag/index/utils/stable_lcc.py` (lines 55-56)

## Signature

```python
def _get_edge_key(source: Any, target: Any) -> str
```

## Description

Return a string key for the edge in the format 'source -&gt; target'.

Args:
    source (Any): The source node of the edge.
    target (Any): The target node of the edge.

Returns:
    str: The edge key as a string in the format 'source -&gt; target'.

## Called By

This function is called by:

- `graphrag/index/utils/stable_lcc.py::_stabilize_graph`

