---
sidebar_position: 471
---

# test_load_config_with_cli_overrides

**File:** `tests/unit/config/test_config.py` (lines 152-163)

## Signature

```python
def test_load_config_with_cli_overrides() -> None
```

## Description

Test that load_config applies CLI overrides for the output base directory when an environment variable is provided.

The test patches the environment to include CUSTOM_API_KEY, derives the root_dir from the minimal_config fixture, overrides the output base directory via cli_overrides, loads the configuration, and asserts that the resulting GraphRagConfig matches the expected configuration with the overridden base directory.

## Dependencies

This function calls:

- `graphrag/config/load_config.py::load_config`
- `tests/unit/config/utils.py::assert_graphrag_configs`
- `tests/unit/config/utils.py::get_default_graphrag_config`

