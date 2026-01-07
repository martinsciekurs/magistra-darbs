---
sidebar_position: 574
---

# test_extract_graph_nlp

**File:** `tests/verbs/test_extract_graph_nlp.py` (lines 16-35)

## Signature

```python
def test_extract_graph_nlp()
```

## Description

Run the extract_graph_nlp workflow against a test context and verify the produced entities and relationships in storage.

This async test creates a test context with text units, builds a Graphrag config using DEFAULT_MODEL_CONFIG, executes the workflow, and then loads the resulting tables to assert exact row counts and schema.

Returns:
    None
        This test does not return a value; it performs assertions to validate correctness.

Raises:
    Exception
        Exceptions may propagate from the underlying operations used in the test (e.g., test utilities, storage I/O, or workflow execution).

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/extract_graph_nlp.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::create_test_context`

