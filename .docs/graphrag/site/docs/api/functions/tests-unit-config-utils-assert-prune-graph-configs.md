---
sidebar_position: 473
---

# assert_prune_graph_configs

**File:** `tests/unit/config/utils.py` (lines 260-269)

## Signature

```python
def assert_prune_graph_configs(
    actual: PruneGraphConfig, expected: PruneGraphConfig
) -> None
```

## Description

Asserts that actual and expected PruneGraphConfig have equal values for the prune-related fields: min_node_freq, max_node_freq_std, min_node_degree, max_node_degree_std, min_edge_weight_pct, remove_ego_nodes, and lcc_only.

Args:
    actual: PruneGraphConfig
        The actual prune graph configuration to validate.
    expected: PruneGraphConfig
        The expected prune graph configuration to compare against.

Returns:
    None
        This function does not return a value. It raises AssertionError if any of the
        prune graph configuration fields differ between actual and expected.

Raises:
    AssertionError
        If any of the asserted fields differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

