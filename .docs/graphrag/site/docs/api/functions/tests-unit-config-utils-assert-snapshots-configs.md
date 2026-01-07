---
sidebar_position: 490
---

# assert_snapshots_configs

**File:** `tests/unit/config/utils.py` (lines 220-224)

## Signature

```python
def assert_snapshots_configs(
    actual: SnapshotsConfig, expected: SnapshotsConfig
) -> None
```

## Description

Assert that two SnapshotsConfig objects have equal embeddings and graphml configurations.

Args:
    actual: The actual SnapshotsConfig instance.
    expected: The expected SnapshotsConfig instance.

Returns:
    None

Raises:
    AssertionError: If actual.embeddings != expected.embeddings or actual.graphml != expected.graphml.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

