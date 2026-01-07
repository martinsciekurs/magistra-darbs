---
sidebar_position: 420
---

# test_logger_hierarchy

**File:** `tests/integration/logging/test_standard_logging.py` (lines 20-34)

## Signature

```python
def test_logger_hierarchy()
```

## Description

Test that logger hierarchy works correctly.

Args:
    None: This test does not accept any parameters.

Returns:
    None: The test does not return a value.

Raises:
    AssertionError: If the logger hierarchy does not propagate the root level to child loggers as expected.

## Dependencies

This function calls:

- `graphrag/logger/standard_logging.py::init_loggers`
- `tests/unit/config/utils.py::get_default_graphrag_config`

