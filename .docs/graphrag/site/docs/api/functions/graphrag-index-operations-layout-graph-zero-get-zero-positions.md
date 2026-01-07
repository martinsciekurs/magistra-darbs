---
sidebar_position: 127
---

# get_zero_positions

**File:** `graphrag/index/operations/layout_graph/zero.py` (lines 63-96)

## Signature

```python
def get_zero_positions(
    node_labels: list[str],
    node_categories: list[int] | None = None,
    node_sizes: list[int] | None = None,
    three_d: bool | None = False,
) -> list[NodePosition]
```

## Description

Create zero-coordinate positions for nodes

This function returns a list of NodePosition objects for every label in node_labels. No embedding or projection is performed; coordinates are initialized to zeros.

Args:
  node_labels (list[str]): Labels for each node.
  node_categories (list[int] | None): Optional list of category/cluster identifiers. If None, defaults to 1 for all nodes.
  node_sizes (list[int] | None): Optional list of node sizes. If None, defaults to 1 for all nodes.
  three_d (bool | None): If False or None, return 2D positions (x and y). If True, return 3D positions (x, y, z).

Returns:
  list[NodePosition]: A list of NodePosition objects, one per input label. Each position includes:
    label: str(node label)
    x, y (and z if three_d is True): coordinates initialized to 0
    cluster: str(int(node_category))
    size: int(node_size)

Notes:
  - If node_categories or node_sizes are provided and their lengths are shorter than the number of labels, an IndexError may be raised when indexing into these lists.
  - The cluster is derived from node_categories (default 1) and converted to a string.

## Dependencies

This function calls:

- `graphrag/index/operations/layout_graph/typing.py::NodePosition`

## Called By

This function is called by:

- `graphrag/index/operations/layout_graph/zero.py::run`

