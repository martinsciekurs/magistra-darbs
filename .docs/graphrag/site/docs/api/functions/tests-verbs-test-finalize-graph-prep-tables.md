---
sidebar_position: 575
---

# _prep_tables

**File:** `tests/verbs/test_finalize_graph.py` (lines 68-80)

## Signature

```python
def _prep_tables()
```

## Description

Prepare test tables for the finalize_graph workflow by loading test data into a test context, dropping final columns that wouldn't be present in inputs (x, y, degree from entities and combined_degree from relationships), and returning the initialized context.

Returns:
    PipelineRunContext: The initialized pipeline run context with the test data loaded into its output storage.

Raises:
    Exception: Exceptions raised by create_test_context, load_test_table, or write_table_to_storage may propagate.

## Dependencies

This function calls:

- `graphrag/utils/storage.py::write_table_to_storage`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::load_test_table`

## Called By

This function is called by:

- `tests/verbs/test_finalize_graph.py::test_finalize_graph`
- `tests/verbs/test_finalize_graph.py::test_finalize_graph_umap`

