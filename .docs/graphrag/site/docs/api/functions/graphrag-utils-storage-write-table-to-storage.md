---
sidebar_position: 408
---

# write_table_to_storage

**File:** `graphrag/utils/storage.py` (lines 30-34)

## Signature

```python
def write_table_to_storage(
    table: pd.DataFrame, name: str, storage: PipelineStorage
) -> None
```

## Description

Write a table to storage.

Args:
  table: pd.DataFrame
      The DataFrame to write to storage.
  name: str
      Base name for the parquet file to be stored as name.parquet.
  storage: PipelineStorage
      The storage backend to which the parquet file will be written.

Returns:
  None

Raises:
  Exception: Exceptions raised by the storage backend during the write operation may propagate.

## Called By

This function is called by:

- `graphrag/index/run/run_pipeline.py::run_pipeline`
- `graphrag/index/run/run_pipeline.py::_copy_previous_output`
- `graphrag/index/update/incremental_index.py::concat_dataframes`
- `graphrag/index/workflows/create_base_text_units.py::run_workflow`
- `graphrag/index/workflows/create_communities.py::run_workflow`
- `graphrag/index/workflows/create_community_reports.py::run_workflow`
- `graphrag/index/workflows/create_community_reports_text.py::run_workflow`
- `graphrag/index/workflows/create_final_documents.py::run_workflow`
- `graphrag/index/workflows/create_final_text_units.py::run_workflow`
- `graphrag/index/workflows/extract_covariates.py::run_workflow`
- `graphrag/index/workflows/extract_graph.py::run_workflow`
- `graphrag/index/workflows/extract_graph_nlp.py::run_workflow`
- `graphrag/index/workflows/finalize_graph.py::run_workflow`
- `graphrag/index/workflows/generate_text_embeddings.py::run_workflow`
- `graphrag/index/workflows/load_input_documents.py::run_workflow`
- `graphrag/index/workflows/load_update_documents.py::run_workflow`
- `graphrag/index/workflows/prune_graph.py::run_workflow`
- `graphrag/index/workflows/update_communities.py::_update_communities`
- `graphrag/index/workflows/update_community_reports.py::_update_community_reports`
- `graphrag/index/workflows/update_covariates.py::_update_covariates`
- `graphrag/index/workflows/update_entities_relationships.py::_update_entities_and_relationships`
- `graphrag/index/workflows/update_text_embeddings.py::run_workflow`
- `graphrag/index/workflows/update_text_units.py::_update_text_units`
- `tests/verbs/test_finalize_graph.py::_prep_tables`
- `tests/verbs/util.py::create_test_context`
- `tests/verbs/util.py::update_document_metadata`

