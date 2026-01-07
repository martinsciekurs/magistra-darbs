---
sidebar_position: 244
---

# run_workflow

**File:** `graphrag/index/workflows/extract_graph.py` (lines 28-79)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Asynchronously run the extract_graph workflow to build the base entity graph and persist results to storage.

## Dependencies

This function calls:

- `graphrag/index/operations/extract_graph/extract_graph.py::extract_graph`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_extract_graph.py::test_extract_graph`

