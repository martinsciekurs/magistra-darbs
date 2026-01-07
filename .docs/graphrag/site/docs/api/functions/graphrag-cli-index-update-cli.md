---
sidebar_position: 21
---

# update_cli

**File:** `graphrag/cli/index.py` (lines 72-100)

## Signature

```python
def update_cli(
    root_dir: Path,
    method: IndexingMethod,
    verbose: bool,
    memprofile: bool,
    cache: bool,
    config_filepath: Path | None,
    skip_validation: bool,
    output_dir: Path | None,
)
```

## Description

Run the update pipeline with the given config.

This function applies optional output directory overrides, loads the configuration, and executes the update phase of the indexing pipeline.

Args:
    root_dir: The root directory of the project. Will search for the config file in this directory.
    method: The indexing method to use for this run.
    verbose: Enable verbose logging/output.
    memprofile: Enable memory profiling during execution.
    cache: Whether to enable caching; if False, caching is disabled.
    config_filepath: The path to the config file. If None, searches for config file in root.
    skip_validation: Whether to skip validation of the loaded configuration.
    output_dir: Optional output directory to override base directories used by the pipeline.

Returns:
    None

Raises:
    FileNotFoundError: If the config file is not found.
    ValueError: If the configuration is invalid.

## Dependencies

This function calls:

- `graphrag/cli/index.py::_run_index`
- `graphrag/config/load_config.py::load_config`

## Called By

This function is called by:

- `graphrag/cli/main.py::_update_cli`

