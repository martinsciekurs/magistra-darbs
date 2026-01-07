---
sidebar_position: 494
---

# assert_summarize_descriptions_configs

**File:** `tests/unit/config/utils.py` (lines 272-278)

## Signature

```python
def assert_summarize_descriptions_configs(
    actual: SummarizeDescriptionsConfig, expected: SummarizeDescriptionsConfig
) -> None
```

## Description

Assert that two SummarizeDescriptionsConfig objects have identical fields: prompt, max_length, strategy, and model_id.

Args:
    actual (SummarizeDescriptionsConfig): The actual config to compare.
    expected (SummarizeDescriptionsConfig): The expected config to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the compared fields differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

