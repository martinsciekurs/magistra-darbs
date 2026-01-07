---
sidebar_position: 491
---

# assert_basic_search_configs

**File:** `tests/unit/config/utils.py` (lines 379-383)

## Signature

```python
def assert_basic_search_configs(
    actual: BasicSearchConfig, expected: BasicSearchConfig
) -> None
```

## Description

Assert that two BasicSearchConfig objects have equal prompt and k values.

Args:
    actual: BasicSearchConfig to compare against expected
    expected: BasicSearchConfig to compare with actual

Returns:
    None

Raises:
    AssertionError: If actual.prompt != expected.prompt or actual.k != expected.k

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

