---
sidebar_position: 587
---

# create_test_context

**File:** `tests/verbs/util.py` (lines 36-50)

## Signature

```python
def create_test_context(storage: list[str] | None = None) -> PipelineRunContext
```

## Description

Create a test context with test tables loaded into storage.

Args:
    storage: list[str] | None
        A list of test table names to load from test data and write into the
        context's output storage. If None, only the documents table is loaded and stored.

Returns:
    PipelineRunContext
        The initialized pipeline run context with the test data loaded into its
        output storage.

Raises:
    Exception: Exceptions raised by load_test_table or write_table_to_storage may propagate.

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::create_run_context`
- `graphrag/utils/storage.py::write_table_to_storage`
- `tests/verbs/util.py::load_test_table`

## Called By

This function is called by:

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
- `tests/verbs/test_finalize_graph.py::_prep_tables`
- `tests/verbs/test_generate_text_embeddings.py::test_generate_text_embeddings`
- `tests/verbs/test_prune_graph.py::test_prune_graph`

