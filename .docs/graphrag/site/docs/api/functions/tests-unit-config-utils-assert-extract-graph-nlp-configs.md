---
sidebar_position: 497
---

# assert_extract_graph_nlp_configs

**File:** `tests/unit/config/utils.py` (lines 252-257)

## Signature

```python
def assert_extract_graph_nlp_configs(
    actual: ExtractGraphNLPConfig, expected: ExtractGraphNLPConfig
) -> None
```

## Description

Assert that two ExtractGraphNLPConfig objects are equal for all relevant fields.

Args:
    actual: ExtractGraphNLPConfig - The actual configuration to validate.
    expected: ExtractGraphNLPConfig - The expected configuration to compare against.

Returns:
    None

Raises:
    AssertionError - If any of the compared fields do not match....

## Dependencies

This function calls:

- `tests/unit/config/utils.py::assert_text_analyzer_configs`

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

