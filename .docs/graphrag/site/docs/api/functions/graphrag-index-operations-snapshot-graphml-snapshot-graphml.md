---
sidebar_position: 131
---

# snapshot_graphml

**File:** `graphrag/index/operations/snapshot_graphml.py` (lines 11-18)

## Signature

```python
def snapshot_graphml(
    input: str | nx.Graph,
    name: str,
    storage: PipelineStorage,
) -> None
```

## Description

Take a snapshot of a graph in GraphML format and persist it to storage.

This function accepts either a GraphML content string or a NetworkX Graph. If input is a string, it is treated as GraphML content (not a file path). If input is a Graph, it is converted to GraphML using NetworkX's GraphML generator. The resulting GraphML content is written asynchronously to the provided storage backend under the key name + ".graphml".

Args:
    input: str | nx.Graph
        GraphML content as a string, or a NetworkX graph object to be converted to GraphML.
    name: str
        Base name for the stored GraphML entry; the actual storage key will be name + ".graphml".
    storage: PipelineStorage
        Storage backend used to persist the GraphML representation asynchronously.

Returns:
    None
        The function completes the storage operation asynchronously and does not return a value.

Raises:
    Exceptions raised by the storage backend or by GraphML generation may be propagated to the caller.

## Called By

This function is called by:

- `graphrag/index/workflows/finalize_graph.py::run_workflow`

