---
sidebar_position: 230
---

# run_workflow

**File:** `graphrag/index/workflows/create_community_reports_text.py` (lines 37-71)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Runs the workflow to transform community reports text and persists the results to storage.

This workflow loads input data from storage (entities, communities, and text_units), configures language-model and summarization settings, builds contextual prompts, generates the community reports text, and writes the resulting table to storage as "community_reports". The operation persists the final output to storage and relies on the provided callbacks and cache through the PipelineRunContext.

Args:
  config: GraphRagConfig containing settings used by the workflow, including language model, data extraction configurations, and summarization strategy.
  context: PipelineRunContext providing access to output_storage, callbacks, and cache used during the workflow.

Returns:
  WorkflowFunctionOutput: The output of the workflow, containing the generated community_reports DataFrame as the result.

Raises:
  FileNotFoundError: If required parquet inputs (entities.parquet, communities.parquet, or text_units.parquet) cannot be found in storage.
  Exception: Exceptions raised by the storage backend during load or write operations may propagate.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/create_community_reports_text.py::create_community_reports_text`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

