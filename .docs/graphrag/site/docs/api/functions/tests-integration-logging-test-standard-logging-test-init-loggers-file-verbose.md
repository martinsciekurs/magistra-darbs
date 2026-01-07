---
sidebar_position: 422
---

# test_init_loggers_file_verbose

**File:** `tests/integration/logging/test_standard_logging.py` (lines 72-97)

## Signature

```python
def test_init_loggers_file_verbose()
```

## Description

Initialize logging for graphrag using the provided GraphRagConfig.

A logger named "graphrag" is configured with a handler derived from the given configuration. The log level is set to DEBUG when verbose is True, otherwise INFO. Before attaching the new handler, all existing handlers on the logger are removed; any FileHandler instances are closed to avoid resource leaks and duplicate logs.

Args:
    config (GraphRagConfig): The GraphRagConfig instance providing logging settings.
    verbose (bool): If True, set the log level to DEBUG; otherwise INFO.
    filename (str): The log filename to use for the log output. Defaults to DEFAULT_LOG_FILENAME.

Returns:
    None

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `tests/unit/config/utils.py::get_default_graphrag_config`

