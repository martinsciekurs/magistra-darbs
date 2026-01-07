---
sidebar_position: 495
---

# get_default_graphrag_config

**File:** `tests/unit/config/utils.py` (lines 60-65)

## Signature

```python
def get_default_graphrag_config(root_dir: str | None = None) -> GraphRagConfig
```

## Description

Return a GraphRagConfig instance configured with the default Graphrag settings.

Args:
    root_dir: Optional[str] - root directory to include in the returned GraphRagConfig. If None, the root_dir key is not set.

Returns:
    GraphRagConfig: The GraphRagConfig created by merging graphrag_config_defaults with DEFAULT_MODEL_CONFIG, and including root_dir when provided.

## Dependencies

This function calls:

- `graphrag/config/models/graph_rag_config.py::GraphRagConfig`

## Called By

This function is called by:

- `tests/integration/logging/test_standard_logging.py::test_logger_hierarchy`
- `tests/integration/logging/test_standard_logging.py::test_init_loggers_file_config`
- `tests/integration/logging/test_standard_logging.py::test_init_loggers_file_verbose`
- `tests/integration/logging/test_standard_logging.py::test_init_loggers_custom_filename`
- `tests/unit/config/test_config.py::test_default_config`
- `tests/unit/config/test_config.py::test_load_minimal_config`
- `tests/unit/config/test_config.py::test_load_config_with_cli_overrides`

