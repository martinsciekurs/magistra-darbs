---
sidebar_position: 492
---

# assert_embed_graph_configs

**File:** `tests/unit/config/utils.py` (lines 186-196)

## Signature

```python
def assert_embed_graph_configs(
    actual: EmbedGraphConfig, expected: EmbedGraphConfig
) -> None
```

## Description

Assert that actual and expected EmbedGraphConfig instances have equal values for their core fields.

Args:
    actual: EmbedGraphConfig. The actual EmbedGraphConfig instance produced by the code under test.
    expected: EmbedGraphConfig. The expected EmbedGraphConfig instance to compare against.

Returns:
    None. The function does not return a value.

Raises:
    AssertionError: If any of the fields enabled, dimensions, num_walks, walk_length, window_size, iterations, random_seed, or use_lcc differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

