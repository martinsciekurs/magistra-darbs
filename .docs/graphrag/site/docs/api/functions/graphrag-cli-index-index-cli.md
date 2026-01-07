---
sidebar_position: 20
---

# index_cli

**File:** `graphrag/cli/index.py` (lines 42-69)

## Signature

```python
def index_cli(
    root_dir: Path,
    method: IndexingMethod,
    verbose: bool,
    memprofile: bool,
    cache: bool,
    config_filepath: Path | None,
    dry_run: bool,
    skip_validation: bool,
    output_dir: Path | None,
)
```

## Description

Run the indexing pipeline with the given configuration.

Parameters:
    root_dir (Path): The root directory of the project. Will search for the configuration file in this directory.
    method (IndexingMethod): The indexing method to use for this run.
    verbose (bool): Enable verbose logging/output.
    memprofile (bool): Enable memory profiling during execution.
    cache (bool): Whether to enable caching; if False, caching is disabled.
    config_filepath (Path | None): Path to the configuration file. If None, searches for the config file in root_dir.
    dry_run (bool): If True, perform a dry run without making changes.
    skip_validation (bool): Skip validation of the loaded configuration.
    output_dir (Path | None): Directory to write outputs. If provided, overrides base output/reporting directories.

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

- `graphrag/cli/main.py::_index_cli`

