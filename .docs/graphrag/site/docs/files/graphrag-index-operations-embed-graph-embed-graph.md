---
sidebar_position: 62
---

# graphrag/index/operations/embed_graph/embed_graph.py

## Overview

Embed graphs into vector space using node2vec.

Purpose:
This module implements the graph embedding operation used by Graphrag. It exposes the embed_graph function, which embeds a NetworkX graph into a mapping from node names to embedding vectors using node2vec. The embedding configuration, including dimensions, num_walks, walk_length, window_size, iterations, random_seed, and use_lcc, is provided via EmbedGraphConfig.

Exports:
- embed_graph(graph: nx.Graph, config: EmbedGraphConfig) -&gt; NodeEmbeddings

Summary:
The embed_graph function takes a graph and a configuration and returns a NodeEmbeddings object that maps each node to its embedding vector. It delegates to embed_node2vec and can utilize the stable_largest_connected_component utility when requested by the config.

## Functions

- [`embed_graph`](../api/functions/graphrag-index-operations-embed-graph-embed-graph-embed-graph)

