---
sidebar_position: 480
---

# assert_language_model_configs

**File:** `tests/unit/config/utils.py` (lines 68-106)

## Signature

```python
def assert_language_model_configs(
    actual: LanguageModelConfig, expected: LanguageModelConfig
) -> None
```

## Description

Assert that actual and expected LanguageModelConfig objects have equivalent field values, including optional responses when present.

Args:
    actual: LanguageModelConfig instance containing the actual configuration to validate.
    expected: LanguageModelConfig instance containing the expected configuration to compare against.

Returns:
    None

Raises:
    AssertionError: If any corresponding field differs between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

