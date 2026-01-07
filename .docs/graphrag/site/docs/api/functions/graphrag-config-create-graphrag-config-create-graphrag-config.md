---
sidebar_position: 39
---

# create_graphrag_config

**File:** `graphrag/config/create_graphrag_config.py` (lines 12-43)

## Signature

```python
def create_graphrag_config(
    values: dict[str, Any] | None = None,
    root_dir: str | None = None,
) -> GraphRagConfig
```

## Description

Load Configuration Parameters from a dictionary.

Args:
    values: dict[str, Any] | None
        Dictionary of configuration values to pass into pydantic model.
    root_dir: str | None
        Root directory for the project.

Returns:
    GraphRagConfig
        The configuration object.

Raises:
    ValidationError
        If the configuration values do not satisfy pydantic validation.

## Dependencies

This function calls:

- `graphrag/config/models/graph_rag_config.py::GraphRagConfig`

## Called By

This function is called by:

- `graphrag/config/load_config.py::load_config`
- `tests/unit/config/test_config.py::test_missing_openai_required_api_key`
- `tests/unit/config/test_config.py::test_missing_azure_api_key`
- `tests/unit/config/test_config.py::test_conflicting_auth_type`
- `tests/unit/config/test_config.py::test_conflicting_azure_api_key`
- `tests/unit/config/test_config.py::test_missing_azure_api_base`
- `tests/unit/config/test_config.py::test_missing_azure_api_version`
- `tests/unit/config/test_config.py::test_default_config`
- `tests/unit/indexing/test_init_content.py::test_init_yaml`
- `tests/unit/indexing/test_init_content.py::test_init_yaml_uncommented`
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
- `tests/verbs/test_pipeline_state.py::test_pipeline_state`
- `tests/verbs/test_pipeline_state.py::test_pipeline_existing_state`
- `tests/verbs/test_prune_graph.py::test_prune_graph`
- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::BlobDatasource.read_settings`

