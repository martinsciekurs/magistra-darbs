---
sidebar_position: 423
---

# test_init_loggers_custom_filename

**File:** `tests/integration/logging/test_standard_logging.py` (lines 100-118)

## Signature

```python
def test_init_loggers_custom_filename()
```

## Description

Test that init_loggers writes logs to a custom filename.

This test creates a temporary Graphrag configuration, initializes the loggers with a custom
filename ("custom-log.log"), and asserts that a file named logs/custom-log.log is created inside
the temporary root directory. It then cleans up by closing and removing any FileHandler instances
attached to the graphrag logger.

Returns:
    None: The test function does not return a value.

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `tests/unit/config/utils.py::get_default_graphrag_config`

