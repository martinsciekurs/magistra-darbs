---
sidebar_position: 498
---

# assert_graphrag_configs

**File:** `tests/unit/config/utils.py` (lines 386-435)

## Signature

```python
def assert_graphrag_configs(actual: GraphRagConfig, expected: GraphRagConfig) -> None
```

## Description

Assert that two GraphRagConfig objects are equivalent by validating all nested configurations match.

Args:
    actual: GraphRagConfig - The actual GraphRagConfig instance to validate.
    expected: GraphRagConfig - The expected GraphRagConfig instance to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the fields differ between actual and expected.

## Dependencies

This function calls:

- `tests/unit/config/utils.py::assert_basic_search_configs`
- `tests/unit/config/utils.py::assert_cache_configs`
- `tests/unit/config/utils.py::assert_chunking_configs`
- `tests/unit/config/utils.py::assert_cluster_graph_configs`
- `tests/unit/config/utils.py::assert_community_reports_configs`
- `tests/unit/config/utils.py::assert_drift_search_configs`
- `tests/unit/config/utils.py::assert_embed_graph_configs`
- `tests/unit/config/utils.py::assert_extract_claims_configs`
- `tests/unit/config/utils.py::assert_extract_graph_configs`
- `tests/unit/config/utils.py::assert_extract_graph_nlp_configs`
- `tests/unit/config/utils.py::assert_global_search_configs`
- `tests/unit/config/utils.py::assert_input_configs`
- `tests/unit/config/utils.py::assert_language_model_configs`
- `tests/unit/config/utils.py::assert_local_search_configs`
- `tests/unit/config/utils.py::assert_output_configs`
- `tests/unit/config/utils.py::assert_prune_graph_configs`
- `tests/unit/config/utils.py::assert_reporting_configs`
- `tests/unit/config/utils.py::assert_snapshots_configs`
- `tests/unit/config/utils.py::assert_summarize_descriptions_configs`
- `tests/unit/config/utils.py::assert_text_embedding_configs`
- `tests/unit/config/utils.py::assert_umap_configs`
- `tests/unit/config/utils.py::assert_update_output_configs`
- `tests/unit/config/utils.py::assert_vector_store_configs`

## Called By

This function is called by:

- `tests/unit/config/test_config.py::test_default_config`
- `tests/unit/config/test_config.py::test_load_minimal_config`
- `tests/unit/config/test_config.py::test_load_config_with_cli_overrides`

