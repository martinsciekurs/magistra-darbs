---
sidebar_position: 121
---

# graph_to_dataframes

**File:** `graphrag/index/operations/graph_to_dataframes.py` (lines 10-38)

## Signature

```python
def graph_to_dataframes(
    graph: nx.Graph,
    node_columns: list[str] | None = None,
    edge_columns: list[str] | None = None,
    node_id: str = "title",
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Deconstructs an nx.Graph into two pandas DataFrames: one for nodes and one for edges.

Args:
- graph: input graph
- node_columns: optional list of node attribute column names to include in the nodes DataFrame
- edge_columns: optional list of edge attribute column names to include in the edges DataFrame
- node_id: name of the column to store node identifiers in the nodes DataFrame (default "title")

Returns:
- tuple[pd.DataFrame, pd.DataFrame]: pair of DataFrames (nodes, edges). The nodes DataFrame includes a column named node_id containing node identifiers; if node_columns is provided, only those columns are included. The edges DataFrame contains an undirected edge representation with columns source and target, and any edge attributes; if edge_columns are provided, only those columns are included.

Raises:
- TypeError: If inputs are not of expected types (e.g., graph is not an nx.Graph) or required attributes are missing.

## Example 💡 Generated

```python
from module import graph_to_dataframes
import networkx as nx
g = nx.Graph()
g.add_node(1, kind="A")
g.add_node(2, kind="B")
g.add_edge(1, 2, weight=3.14)
ndf, edf = graph_to_dataframes(g)
print(ndf.head(), edf.head())  # shows nodes and edges
```

## Called By

This function is called by:

- `graphrag/index/workflows/prune_graph.py::prune_graph`

