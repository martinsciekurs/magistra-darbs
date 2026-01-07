---
sidebar_position: 525
---

# uncomment_line

**File:** `tests/unit/indexing/test_init_content.py` (lines 24-26)

## Signature

```python
def uncomment_line(line: str) -> str
```

## Description

Uncomments a line by removing a leading "# " prefix, preserving indentation.

Args:
- line: str - input line that may start with whitespace followed by "# " to be removed.

Returns:
- str - the line with the first occurrence of a leading "# " removed, preserving the original indentation.

Raises:
- None

## Called By

This function is called by:

- `tests/unit/indexing/test_init_content.py::test_init_yaml_uncommented`

