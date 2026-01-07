---
sidebar_position: 472
---

# test_load_config_missing_env_vars

**File:** `tests/unit/config/test_config.py` (lines 166-170)

## Signature

```python
def test_load_config_missing_env_vars() -> None
```

## Description

Load configuration from a file and environment variables.

Note: Loading may depend on environment variables (for example API keys) in addition to the configuration file.

Args:
    root_dir (Path): The root directory to search for the config file.
    config_filepath (Path | None): The path to the config file. If None, searches for the config file in root_dir.
    cli_overrides (dict[str, Any] | None): Flat dictionary of CLI overrides. Example: &#123;'output.base_dir': 'override_value'&#125;. Overrides are applied after loading the base configuration.

Returns:
    GraphRagConfig: The loaded configuration.

Raises:
    FileNotFoundError: If the config file cannot be found.
    KeyError: If a required environment variable is missing.
    ValidationError: If the loaded configuration fails validation (e.g., invalid structure or types).

## Dependencies

This function calls:

- `graphrag/config/load_config.py::load_config`

