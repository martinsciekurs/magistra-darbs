---
sidebar_position: 19
---

# _run_index

**File:** `graphrag/cli/index.py` (lines 103-161)

## Signature

```python
def _run_index(
    config,
    method,
    is_update_run,
    verbose,
    memprofile,
    cache,
    dry_run,
    skip_validation,
)
```

## Description

Run the indexing pipeline using the provided configuration.

Parameters (with types):
  config: GraphRagConfig - The GraphRagConfig instance containing run configuration.
  method: IndexingMethod - The indexing method to use for this run.
  is_update_run: bool - True if this is an update run, False otherwise.
  verbose: bool - Enable verbose logging/output.
  memprofile: bool - Enable memory profiling during execution.
  cache: bool - Whether to enable caching; if False, caching is disabled.
  dry_run: bool - If True, perform a dry run and exit before execution.
  skip_validation: bool - If True, skip validation of configuration names.

Returns (None):
  None

Raises:
  SystemExit:
    - If dry_run is True, the function exits with status 0.
    - At the end, the function exits with status 0 if no errors were encountered, or 1 if errors occurred.
    - If validate_config_names raises SystemExit due to validation failures (only when skip_validation is False).

## Dependencies

This function calls:

- `graphrag.api::build_index`
- `graphrag/callbacks/console_workflow_callbacks.py::ConsoleWorkflowCallbacks`
- `graphrag/cli/index.py::_register_signal_handlers`
- `graphrag/index/validate_config.py::validate_config_names`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/cli.py::redact`

## Called By

This function is called by:

- `graphrag/cli/index.py::index_cli`
- `graphrag/cli/index.py::update_cli`

