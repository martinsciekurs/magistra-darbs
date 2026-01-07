---
sidebar_position: 475
---

# assert_community_reports_configs

**File:** `tests/unit/config/utils.py` (lines 281-289)

## Signature

```python
def assert_community_reports_configs(
    actual: CommunityReportsConfig, expected: CommunityReportsConfig
) -> None
```

## Description

Assert that two CommunityReportsConfig objects have the same values for their configuration fields.

Args:
    actual: The actual CommunityReportsConfig instance.
    expected: The expected CommunityReportsConfig instance.

Returns:
    None

Raises:
    AssertionError: If graph_prompt, text_prompt, max_length, max_input_length, strategy, or model_id differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

