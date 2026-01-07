---
sidebar_position: 248
---

# run_workflow

**File:** `graphrag/index/workflows/finalize_graph.py` (lines 23-62)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the finalize_graph workflow to finalize the entity and relationship data, persist updates to storage, and optionally snapshot GraphML graphs.

## Dependencies

This function calls:

- `graphrag/index/operations/create_graph.py::create_graph`
- `graphrag/index/operations/snapshot_graphml.py::snapshot_graphml`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/finalize_graph.py::finalize_graph`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_finalize_graph.py::test_finalize_graph`
- `tests/verbs/test_finalize_graph.py::test_finalize_graph_umap`

