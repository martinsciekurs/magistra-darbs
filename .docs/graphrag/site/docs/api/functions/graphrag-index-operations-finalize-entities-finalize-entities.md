---
sidebar_position: 119
---

# finalize_entities

**File:** `graphrag/index/operations/finalize_entities.py` (lines 18-54)

## Signature

```python
def finalize_entities(
    entities: pd.DataFrame,
    relationships: pd.DataFrame,
    embed_config: EmbedGraphConfig | None = None,
    layout_enabled: bool = False,
) -> pd.DataFrame
```

## Description

Transforms input entities into final entity records by building a graph from relationships, optionally embedding, applying a layout, and attaching identifiers.

Args:
    entities (pd.DataFrame): Input entities to be transformed. The function merges on the 'title' column and augments with layout and degree information.
    relationships (pd.DataFrame): DataFrame containing edge information used to construct the graph; edge attributes include 'weight'.
    embed_config (EmbedGraphConfig | None): Embedding configuration. If provided and embed_config.enabled is True, graph embeddings are computed.
    layout_enabled (bool): If True, a layout is applied to the graph to compute node positions.

Returns:
    pd.DataFrame: The final entities DataFrame containing the columns defined by ENTITIES_FINAL_COLUMNS.

Raises:
    Exception: Propagates exceptions raised by underlying operations such as create_graph, embed_graph, layout_graph, and compute_degree, as well as DataFrame operations.

## Dependencies

This function calls:

- `graphrag/index/operations/compute_degree.py::compute_degree`
- `graphrag/index/operations/create_graph.py::create_graph`
- `graphrag/index/operations/embed_graph/embed_graph.py::embed_graph`
- `graphrag/index/operations/layout_graph/layout_graph.py::layout_graph`

## Called By

This function is called by:

- `graphrag/index/workflows/finalize_graph.py::finalize_graph`

