---
sidebar_position: 476
---

# assert_chunking_configs

**File:** `tests/unit/config/utils.py` (lines 210-217)

## Signature

```python
def assert_chunking_configs(actual: ChunkingConfig, expected: ChunkingConfig) -> None
```

## Description

Assert that two ChunkingConfig objects have equal values for the configured fields.

Args:
    actual: ChunkingConfig to compare against expected.
    expected: ChunkingConfig containing the expected values.

Returns:
    None

Raises:
    AssertionError: If any of the checked fields do not match: size, overlap, group_by_columns, strategy, encoding_model, prepend_metadata, chunk_size_includes_metadata.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

