---
sidebar_position: 125
---

# compute_umap_positions

**File:** `graphrag/index/operations/layout_graph/umap.py` (lines 80-132)

## Signature

```python
def compute_umap_positions(
    embedding_vectors: np.ndarray,
    node_labels: list[str],
    node_categories: list[int] | None = None,
    node_sizes: list[int] | None = None,
    min_dist: float = 0.75,
    n_neighbors: int = 5,
    spread: int = 1,
    metric: str = "euclidean",
    n_components: int = 2,
    random_state: int = 86,
) -> list[NodePosition]
```

## Description

Project embedding vectors down to 2D/3D coordinates using UMAP.

Args:
  embedding_vectors: Embedding vectors to project, provided as a numpy array.
  node_labels: Labels for each node.
  node_categories: Optional per-node category identifiers. If None, defaults to 1 for all nodes.
  node_sizes: Optional per-node sizes. If None, defaults to 1 for all nodes.
  min_dist: UMAP min_dist hyperparameter controlling the minimum distance between embedded points.
  n_neighbors: UMAP n_neighbors hyperparameter controlling the local connectivity.
  spread: UMAP spread parameter influencing the layout.
  metric: Distance metric used by UMAP (e.g., "euclidean").
  n_components: Number of output dimensions (2 or 3) for the embedding.
  random_state: Seed for random number generation to ensure reproducibility.

Returns:
  list[NodePosition]: A list of NodePosition objects corresponding to each input label. Each NodePosition includes coordinates (x, y) for 2D layouts or x, y, z for 3D layouts, along with label, cluster (from node_categories or 1), and size (from node_sizes or 1).

Raises:
  ImportError: If the umap package is not installed or cannot be imported.

## Dependencies

This function calls:

- `graphrag/index/operations/layout_graph/typing.py::NodePosition`

## Called By

This function is called by:

- `graphrag/index/operations/layout_graph/umap.py::run`

