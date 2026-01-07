---
sidebar_position: 469
---

# test_default_config

**File:** `tests/unit/config/test_config.py` (lines 136-139)

## Signature

```python
def test_default_config() -> None
```

## Description

Test that the default Graphrag configuration is created as expected.

Returns:
    None

Raises:
    AssertionError: If the actual Graphrag configuration does not match the expected configuration.
    ValidationError: If the input configuration dictionary cannot be validated by pydantic when creating the config.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `tests/unit/config/utils.py::assert_graphrag_configs`
- `tests/unit/config/utils.py::get_default_graphrag_config`

