---
sidebar_position: 87
---

# embed_graph

**File:** `graphrag/index/operations/embed_graph/embed_graph.py` (lines 16-50)

## Signature

```python
def embed_graph(
    graph: nx.Graph,
    config: EmbedGraphConfig,
) -> NodeEmbeddings
```

## Description

Embed a graph into a vector space using node2vec.

The graph is expected to be in nx.Graph format. The operation outputs a mapping between node name and vector.

Args:
    graph: Input graph to embed.
    config: Embedding configuration, including dimensions, num_walks, walk_length, window_size, iterations, random_seed, and use_lcc.

Returns:
    NodeEmbeddings: Mapping from node name to embedding vector.

Raises:
    Exception: If underlying operations fail.

## Dependencies

This function calls:

- `graphrag/index/operations/embed_graph/embed_node2vec.py::embed_node2vec`
- `graphrag/index/utils/stable_lcc.py::stable_largest_connected_component`

## Called By

This function is called by:

- `graphrag/index/operations/finalize_entities.py::finalize_entities`

