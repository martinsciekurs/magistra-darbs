---
sidebar_position: 308
---

# init_loggers

**File:** `graphrag/logger/standard_logging.py` (lines 50-83)

## Signature

```python
def init_loggers(
    config: GraphRagConfig,
    verbose: bool = False,
    filename: str = DEFAULT_LOG_FILENAME,
) -> None
```

## Description

Initialize logging for graphrag based on configuration.

Configures the top-level 'graphrag' logger with a handler derived from the provided GraphRagConfig. It sets the log level to DEBUG when verbose is True, otherwise INFO. Before attaching the new handler, all existing handlers on the logger are removed; any FileHandler instances are closed to avoid resource leaks and duplicate logs.

Args:
    config (GraphRagConfig): The GraphRagConfig instance providing logging settings (including reporting and root_dir).
    verbose (bool): If True, enable DEBUG logging; otherwise INFO.
    filename (str): The log filename on disk. If not provided, defaults to DEFAULT_LOG_FILENAME.

Returns:
    None

Raises:
    Propagates exceptions from internal components (for example, LoggerFactory.create_logger) if encountered.

## Called By

This function is called by:

- `graphrag/api/index.py::build_index`
- `graphrag/api/prompt_tune.py::generate_indexing_prompts`
- `graphrag/api/query.py::global_search`
- `graphrag/api/query.py::global_search_streaming`
- `graphrag/api/query.py::multi_index_global_search`
- `graphrag/api/query.py::local_search`
- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::multi_index_local_search`
- `graphrag/api/query.py::drift_search`
- `graphrag/api/query.py::drift_search_streaming`
- `graphrag/api/query.py::multi_index_drift_search`
- `graphrag/api/query.py::basic_search`
- `graphrag/api/query.py::basic_search_streaming`
- `graphrag/api/query.py::multi_index_basic_search`
- `graphrag/cli/index.py::_run_index`
- `graphrag/cli/prompt_tune.py::prompt_tune`
- `tests/integration/logging/test_standard_logging.py::test_logger_hierarchy`
- `tests/integration/logging/test_standard_logging.py::test_init_loggers_file_config`
- `tests/integration/logging/test_standard_logging.py::test_init_loggers_file_verbose`
- `tests/integration/logging/test_standard_logging.py::test_init_loggers_custom_filename`

