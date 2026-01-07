---
sidebar_position: 246
---

# run_workflow

**File:** `graphrag/index/workflows/extract_graph_nlp.py` (lines 24-48)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the extract_graph_nlp workflow to build the base entity graph and persist results to storage.

This coroutine orchestrates the extraction of noun-phrase based graph components by loading text units from storage, invoking extract_graph_nlp to produce entities and relationships, writing the resulting tables back to storage, and returning a WorkflowFunctionOutput containing the produced data.

Args:
  config: GraphRagConfig
      Configuration for the extract_graph_nlp workflow, including extraction_config parameters.
  context: PipelineRunContext
      The runtime context containing storage handles and cache used by the workflow.

Returns:
  WorkflowFunctionOutput
      The output with a result dictionary containing:
        entities: DataFrame of extracted entities
        relationships: DataFrame of extracted relationships

Raises:
  ValueError
      Could not find the required text_units.parquet in storage (text_units).
  Exception
      Exceptions raised by the storage backend or parquet reader/writer during load or write operations, or errors raised by extract_graph_nlp.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/extract_graph_nlp.py::extract_graph_nlp`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_extract_graph_nlp.py::test_extract_graph_nlp`

