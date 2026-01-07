---
sidebar_position: 82
---

# graphrag/index/operations/snapshot_graphml.py

## Overview

Snapshot GraphMLs of graphs to a storage backend.

Purpose
This module provides a single utility, snapshot_graphml, to persist GraphML representations of graphs to a storage backend via PipelineStorage.

Exports
- snapshot_graphml(input: str | nx.Graph, name: str, storage: PipelineStorage) -&gt; None

Summary
The function accepts either a GraphML content string or a NetworkX Graph. If input is a string, it is treated as GraphML content (not a file path). If input is a Graph, it is converted to GraphML using NetworkX's GraphML generator. The resulting GraphML content is written to the provided storage backend under the given name. The exact storage location (path, key, or identifier) is determined by the storage backend implementation.

Behavior and errors
- Writes to the storage backend. The asynchronous vs. synchronous nature depends on the storage backend's API; this function completes when the write operation finishes or raises an exception if it fails.
- Raises ValueError if input type is not supported (not a string or NetworkX Graph).
- May raise exceptions propagated from the storage backend.

Dependencies
- networkx as nx
- graphrag.storage.pipeline_storage import PipelineStorage

## Functions

- [`snapshot_graphml`](../api/functions/graphrag-index-operations-snapshot-graphml-snapshot-graphml)

