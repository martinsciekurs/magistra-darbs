---
sidebar_position: 410
---

# load_table_from_storage

**File:** `graphrag/utils/storage.py` (lines 16-27)

## Signature

```python
def load_table_from_storage(name: str, storage: PipelineStorage) -> pd.DataFrame
```

## Description

Load a parquet from the storage instance.

Args:
  name: str
      Base name for the parquet file to load. The expected file name is &#123;name&#125;.parquet.
  storage: PipelineStorage
      The storage backend to read the parquet file from.

Returns:
  pd.DataFrame
      DataFrame loaded from the parquet file stored at &#123;name&#125;.parquet.

Raises:
  ValueError
      Could not find &#123;name&#125;.parquet in storage!
  Exception
      Exceptions raised by the storage backend or parquet reader during the load operation may propagate.

## Called By

This function is called by:

- `graphrag/cli/query.py::_resolve_output_files`
- `graphrag/index/run/run_pipeline.py::_copy_previous_output`
- `graphrag/index/update/incremental_index.py::get_delta_docs`
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
- `graphrag/index/workflows/prune_graph.py::run_workflow`
- `graphrag/index/workflows/update_communities.py::_update_communities`
- `graphrag/index/workflows/update_community_reports.py::_update_community_reports`
- `graphrag/index/workflows/update_covariates.py::_update_covariates`
- `graphrag/index/workflows/update_entities_relationships.py::_update_entities_and_relationships`
- `graphrag/index/workflows/update_text_units.py::_update_text_units`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata_included_in_chunk`
- `tests/verbs/test_create_communities.py::test_create_communities`
- `tests/verbs/test_create_community_reports.py::test_create_community_reports`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents_with_metadata_column`
- `tests/verbs/test_create_final_text_units.py::test_create_final_text_units`
- `tests/verbs/test_extract_covariates.py::test_extract_covariates`
- `tests/verbs/test_extract_graph.py::test_extract_graph`
- `tests/verbs/test_extract_graph_nlp.py::test_extract_graph_nlp`
- `tests/verbs/test_finalize_graph.py::test_finalize_graph`
- `tests/verbs/test_finalize_graph.py::test_finalize_graph_umap`
- `tests/verbs/test_generate_text_embeddings.py::test_generate_text_embeddings`
- `tests/verbs/test_prune_graph.py::test_prune_graph`
- `tests/verbs/util.py::update_document_metadata`

