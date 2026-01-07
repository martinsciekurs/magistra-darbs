---
sidebar_position: 583
---

# test_prune_graph

**File:** `tests/verbs/test_prune_graph.py` (lines 17-31)

## Signature

```python
def test_prune_graph()
```

## Description

Test that pruning the graph results in 20 entities.

Returns:
    None
        No return value.

Raises:
    Exception
        Exceptions may propagate from the underlying operations used in the test (e.g., test utilities, storage I/O, or workflow execution).

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/config/models/prune_graph_config.py::PruneGraphConfig`
- `graphrag/index/workflows/prune_graph.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::create_test_context`

