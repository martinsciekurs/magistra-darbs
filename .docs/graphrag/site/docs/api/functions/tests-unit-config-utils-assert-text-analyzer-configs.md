---
sidebar_position: 479
---

# assert_text_analyzer_configs

**File:** `tests/unit/config/utils.py` (lines 237-249)

## Signature

```python
def assert_text_analyzer_configs(
    actual: TextAnalyzerConfig, expected: TextAnalyzerConfig
) -> None
```

## Description

Assert that two TextAnalyzerConfig objects are equal for all relevant fields.

Args:
    actual: TextAnalyzerConfig - The actual configuration to validate.
    expected: TextAnalyzerConfig - The expected configuration to compare against.

Returns:
    None

Raises:
    AssertionError - If any of the compared fields do not match.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_extract_graph_nlp_configs`

