---
sidebar_position: 63
---

# graphrag/index/operations/embed_graph/embed_node2vec.py

## Overview

Module for generating node embeddings from graphs using Node2Vec.

Purpose:
This module exposes a single public function, embed_node2vec, which computes node embeddings
for NetworkX Graph or DiGraph objects using the Node2Vec algorithm. The resulting embeddings
are suitable for downstream tasks such as node classification, link prediction, or clustering.

Key exports:
- embed_node2vec(graph, dimensions=1536, num_walks=10, walk_length=40, window_size=2, iterations=3, random_seed=86) -&gt; NodeEmbeddings

Brief summary:
Given a graph, the function performs Node2Vec random walks and trains an embedding model to produce
a fixed-dimensional vector per node. The return value is a NodeEmbeddings object that stores the
embedding vectors aligned with the graph's node order.

Notes on NodeEmbeddings:
NodeEmbeddings is a type alias defined elsewhere in this package that describes the embedding representation
returned by embed_node2vec. The exact concrete type may be a 2D array-like structure or a mapping from
node identifiers to vectors; see the package type definitions for details. In all cases, the i-th embedding
corresponds to the i-th node yielded by graph.nodes().

Args:
- graph: Graph or DiGraph on which to compute node embeddings.
- dimensions: Embedding dimensionality (positive integer).
- num_walks: Number of random walks to start at every node (positive integer).
- walk_length: Length of each random walk (positive integer).
- window_size: Window size parameter for the embedding model (positive integer).
- iterations: Number of training iterations (non-negative integer).
- random_seed: Seed for random number generation (integer).

Returns:
- NodeEmbeddings: Embeddings for each node in the input graph. Shape is (num_nodes, dimensions). The
  order of embeddings matches graph.nodes() iteration order.

Raises:
- TypeError: If graph is not a NetworkX Graph or DiGraph.
- ValueError: If any numeric parameter is invalid (e.g., dimensions &lt;= 0, num_walks &lt;= 0, walk_length &lt;= 0,
  window_size &lt;= 0, iterations &lt; 0) or if the graph contains no nodes.

Example:
&gt;&gt;&gt; G = nx.path_graph(4)
&gt;&gt;&gt; embeddings = embed_node2vec(G, dimensions=64, random_seed=0)
&gt;&gt;&gt; embeddings.shape
(4, 64)

## Functions

- [`embed_node2vec`](../api/functions/graphrag-index-operations-embed-graph-embed-node2vec-embed-node2vec)

