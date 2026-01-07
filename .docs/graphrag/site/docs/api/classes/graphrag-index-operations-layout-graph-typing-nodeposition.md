---
sidebar_position: 59
---

# NodePosition

**File:** `graphrag/index/operations/layout_graph/typing.py`

## Overview

NodePosition represents the position and rendering properties of a node in the layout graph.

Attributes:
  label: str
  x: float
  y: float
  cluster: int | str
  size: float

Args:
  label: The node's display label.
  x: The x-coordinate of the node in the layout.
  y: The y-coordinate of the node in the layout.
  cluster: The cluster identifier (int or str) to which the node belongs.
  size: The visual size of the node.

Returns:
  None: The dataclass constructor initializes a NodePosition instance and does not return a value.

to_pandas:
  def to_pandas(self) -&gt; tuple[str, float, float, str, float]:
    Converts this NodePosition to a pandas-friendly 5-tuple in the order: (label, x, y, cluster, size).
    The 4th element (cluster) is represented as a string to maintain consistency in pandas DataFrames.
    Returns: A 5-tuple containing (label, x, y, cluster, size).

## Methods

### `to_pandas`

```python
def to_pandas(self) -> tuple[str, float, float, str, float]
```

