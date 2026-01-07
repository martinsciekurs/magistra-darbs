---
sidebar_position: 482
---

# assert_cluster_graph_configs

**File:** `tests/unit/config/utils.py` (lines 303-308)

## Signature

```python
def assert_cluster_graph_configs(
    actual: ClusterGraphConfig, expected: ClusterGraphConfig
) -> None
```

## Description

Assert that actual and expected ClusterGraphConfig objects are equal for cluster graph settings.

Args:
    actual: ClusterGraphConfig
        The actual cluster graph configuration to validate.
    expected: ClusterGraphConfig
        The expected cluster graph configuration to validate.

Returns:
    None
        The function does not return a value. It will raise AssertionError if the compared fields differ.

Raises:
    AssertionError
        If actual and expected values for max_cluster_size, use_lcc, or seed differ.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

