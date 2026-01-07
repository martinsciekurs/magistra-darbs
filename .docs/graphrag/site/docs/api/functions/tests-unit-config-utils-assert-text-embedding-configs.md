---
sidebar_position: 496
---

# assert_text_embedding_configs

**File:** `tests/unit/config/utils.py` (lines 199-207)

## Signature

```python
def assert_text_embedding_configs(
    actual: TextEmbeddingConfig, expected: TextEmbeddingConfig
) -> None
```

## Description

Assert that two TextEmbeddingConfig objects are equal for all relevant fields.

Args:
    actual: TextEmbeddingConfig - The actual configuration to validate.
    expected: TextEmbeddingConfig - The expected configuration to compare against.

Returns:
    None

Raises:
    AssertionError - If any of the compared fields do not match.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

