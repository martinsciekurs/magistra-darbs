---
sidebar_position: 573
---

# test_extract_graph

**File:** `tests/verbs/test_extract_graph.py` (lines 37-78)

## Signature

```python
def test_extract_graph()
```

## Description

Test that the extract_graph workflow runs with a test context and mocked LLM responses, persists the resulting entities and relationships to storage, and validates the stored graph for expected schema and content (including a mocked description).

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/extract_graph.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::create_test_context`

