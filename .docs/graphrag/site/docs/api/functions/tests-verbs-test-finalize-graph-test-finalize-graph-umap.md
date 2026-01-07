---
sidebar_position: 577
---

# test_finalize_graph_umap

**File:** `tests/verbs/test_finalize_graph.py` (lines 43-65)

## Signature

```python
def test_finalize_graph_umap()
```

## Description

Test the finalize_graph workflow with UMAP enabled to verify that x and y coordinates are produced and that final tables contain the expected columns.

Args:
    None: This function does not take any parameters.

Returns:
    None: This is an asynchronous test function and does not return a value.

Raises:
    Exception: Exceptions raised by create_test_context, load_test_table, or write_table_to_storage may propagate.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/finalize_graph.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/test_finalize_graph.py::_prep_tables`

