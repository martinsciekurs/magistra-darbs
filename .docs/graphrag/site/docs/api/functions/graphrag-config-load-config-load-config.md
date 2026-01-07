---
sidebar_position: 49
---

# load_config

**File:** `graphrag/config/load_config.py` (lines 146-191)

## Signature

```python
def load_config(
    root_dir: Path,
    config_filepath: Path | None = None,
    cli_overrides: dict[str, Any] | None = None,
) -> GraphRagConfig
```

## Description

Load configuration from a file.

Args:
    root_dir: The root directory of the project. Will search for the config file in this directory.
    config_filepath: The path to the config file. If None, searches for config file in root.
    cli_overrides: A flat dictionary of cli overrides. Example: &#123;'output.base_dir': 'override_value'&#125;

Returns:
    GraphRagConfig
        The loaded configuration.

Raises:
    FileNotFoundError
        If the config file is not found.
    ValueError
        If the config file extension is not supported.
    TypeError
        If applying cli overrides to the config fails.
    KeyError
        If config file references a non-existent environment variable.
    ValidationError
        If there are pydantic validation errors when instantiating the config.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/config/load_config.py::_apply_overrides`
- `graphrag/config/load_config.py::_get_config_path`
- `graphrag/config/load_config.py::_load_dotenv`
- `graphrag/config/load_config.py::_parse`
- `graphrag/config/load_config.py::_parse_env_variables`

## Called By

This function is called by:

- `graphrag/cli/index.py::index_cli`
- `graphrag/cli/index.py::update_cli`
- `graphrag/cli/prompt_tune.py::prompt_tune`
- `graphrag/cli/query.py::run_global_search`
- `graphrag/cli/query.py::run_local_search`
- `graphrag/cli/query.py::run_drift_search`
- `graphrag/cli/query.py::run_basic_search`
- `tests/unit/config/test_config.py::test_load_minimal_config`
- `tests/unit/config/test_config.py::test_load_config_with_cli_overrides`
- `tests/unit/config/test_config.py::test_load_config_missing_env_vars`
- `unified-search-app/app/knowledge_loader/data_sources/local_source.py::LocalDatasource.read_settings`

