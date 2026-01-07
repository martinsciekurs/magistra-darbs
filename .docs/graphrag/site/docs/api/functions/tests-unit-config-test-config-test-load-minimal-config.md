---
sidebar_position: 470
---

# test_load_minimal_config

**File:** `tests/unit/config/test_config.py` (lines 143-148)

## Signature

```python
def test_load_minimal_config() -> None
```

## Description

Test loading a minimal Graphrag configuration and verify it matches the expected default Graphrag configuration for the given root directory.

Returns:
    None

## Dependencies

This function calls:

- `graphrag/config/load_config.py::load_config`
- `tests/unit/config/utils.py::assert_graphrag_configs`
- `tests/unit/config/utils.py::get_default_graphrag_config`

