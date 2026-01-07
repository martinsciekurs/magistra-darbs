---
sidebar_position: 493
---

# assert_local_search_configs

**File:** `tests/unit/config/utils.py` (lines 315-326)

## Signature

```python
def assert_local_search_configs(
    actual: LocalSearchConfig, expected: LocalSearchConfig
) -> None
```

## Description

Assert that two LocalSearchConfig objects have equal local search configuration values.

Args:
    actual: LocalSearchConfig to compare against expected.
    expected: LocalSearchConfig to compare with actual.

Returns:
    None

Raises:
    AssertionError: If any corresponding fields differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

