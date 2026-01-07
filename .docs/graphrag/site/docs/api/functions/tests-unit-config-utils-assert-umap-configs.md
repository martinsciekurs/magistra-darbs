---
sidebar_position: 489
---

# assert_umap_configs

**File:** `tests/unit/config/utils.py` (lines 311-312)

## Signature

```python
def assert_umap_configs(actual: UmapConfig, expected: UmapConfig) -> None
```

## Description

Assert that the enabled attribute of two UmapConfig objects matches. Only the enabled attribute is checked; other fields are not compared.

Note: If full equivalence is intended, align the implementation or docstring accordingly.

Parameters:
    actual (UmapConfig): The actual UmapConfig to validate.
    expected (UmapConfig): The expected UmapConfig to compare against.

Returns:
    None

Raises:
    AssertionError: if actual.enabled != expected.enabled

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

