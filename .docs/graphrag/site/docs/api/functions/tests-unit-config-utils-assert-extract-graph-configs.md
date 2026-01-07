---
sidebar_position: 488
---

# assert_extract_graph_configs

**File:** `tests/unit/config/utils.py` (lines 227-234)

## Signature

```python
def assert_extract_graph_configs(
    actual: ExtractGraphConfig, expected: ExtractGraphConfig
) -> None
```

## Description

Assert that the actual and expected ExtractGraphConfig instances have equal values for their core fields.

Args:
    actual: The actual ExtractGraphConfig instance produced by the code under test.
    expected: The expected ExtractGraphConfig instance to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the fields prompt, entity_types, max_gleanings, strategy, or model_id differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

