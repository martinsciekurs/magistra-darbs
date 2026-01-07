---
sidebar_position: 576
---

# test_finalize_graph

**File:** `tests/verbs/test_finalize_graph.py` (lines 21-40)

## Signature

```python
def test_finalize_graph()
```

## Description

Test that the finalize_graph workflow produces final entities and relationships tables with default coordinates.

This test prepares a test context, creates a GraphRag configuration using the default model setup, executes the finalize_graph workflow, and then loads the resulting tables from storage to verify structure and values. Specifically, it asserts that:
- the x and y coordinates are zero sums when embedding/UMAP are disabled by default,
- all columns defined in ENTITIES_FINAL_COLUMNS are present in the entities table,
- all columns defined in RELATIONSHIPS_FINAL_COLUMNS are present in the relationships table.

Returns:
    None
        No return value.

Raises:
    Exception
        Exceptions raised by the underlying utilities used in this test (e.g., _prep_tables, create_test_context, load_test_table, or storage I/O) may propagate.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/finalize_graph.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/test_finalize_graph.py::_prep_tables`

