---
sidebar_position: 88
---

# embed_node2vec

**File:** `graphrag/index/operations/embed_graph/embed_node2vec.py` (lines 20-43)

## Signature

```python
def embed_node2vec(
    graph: nx.Graph | nx.DiGraph,
    dimensions: int = 1536,
    num_walks: int = 10,
    walk_length: int = 40,
    window_size: int = 2,
    iterations: int = 3,
    random_seed: int = 86,
) -> NodeEmbeddings
```

## Description

Generate node embeddings using Node2Vec.

Args:
    graph: Graph or DiGraph on which to compute node embeddings.
    dimensions: Dimensionality of the embeddings.
    num_walks: Number of random walks to start at every node.
    walk_length: Length of each random walk.
    window_size: Window size parameter for embedding model.
    iterations: Number of training iterations.
    random_seed: Seed for the random number generator.

Returns:
    NodeEmbeddings: Object containing embeddings (np.ndarray) and the corresponding list of node identifiers (list[str]).

## Called By

This function is called by:

- `graphrag/index/operations/embed_graph/embed_graph.py::embed_graph`

