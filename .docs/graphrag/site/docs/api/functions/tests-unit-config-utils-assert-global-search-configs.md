---
sidebar_position: 478
---

# assert_global_search_configs

**File:** `tests/unit/config/utils.py` (lines 329-343)

## Signature

```python
def assert_global_search_configs(
    actual: GlobalSearchConfig, expected: GlobalSearchConfig
) -> None
```

## Description

Assert that actual and expected GlobalSearchConfig objects have equal configuration values.

The function asserts equality for the following fields: map_prompt, reduce_prompt, knowledge_prompt, max_context_tokens, data_max_tokens, map_max_length, reduce_max_length, dynamic_search_threshold, dynamic_search_keep_parent, dynamic_search_num_repeats, dynamic_search_use_summary, dynamic_search_max_level.

Args:
    actual: GlobalSearchConfig - The actual configuration to validate.
    expected: GlobalSearchConfig - The expected configuration to compare against.

Returns:
    None

Raises:
    AssertionError - If the configurations do not match.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

