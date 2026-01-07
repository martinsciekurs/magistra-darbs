---
sidebar_position: 86
---

# create_graph

**File:** `graphrag/index/operations/create_graph.py` (lines 10-23)

## Signature

```python
def create_graph(
    edges: pd.DataFrame,
    edge_attr: list[str | int] | None = None,
    nodes: pd.DataFrame | None = None,
    node_id: str = "title",
) -> nx.Graph
```

## Description

Create a NetworkX graph from edges and optional nodes dataframes.

Args:
    edges (pd.DataFrame): DataFrame containing edge information for the graph.
    edge_attr (list[str | int] | None): List of edge attribute column names (or None) to include as edge attributes.
    nodes (pd.DataFrame | None): Optional DataFrame containing node attributes to add to the graph. If provided, nodes are added with attributes from this DataFrame.
    node_id (str): Column name to use as the node identifier when adding nodes from the nodes DataFrame.

Returns:
    graph (nx.Graph): The constructed NetworkX Graph.

Raises:
    KeyError: If the specified node_id column does not exist in the nodes DataFrame when indexing.
    ValueError: If the edges DataFrame is missing required columns or edge_attr is invalid for from_pandas_edgelist.
    TypeError: If input data types are incompatible with the underlying operations.

## Called By

This function is called by:

- `graphrag/index/operations/finalize_entities.py::finalize_entities`
- `graphrag/index/operations/finalize_relationships.py::finalize_relationships`
- `graphrag/index/workflows/create_communities.py::create_communities`
- `graphrag/index/workflows/finalize_graph.py::run_workflow`
- `graphrag/index/workflows/prune_graph.py::prune_graph`

