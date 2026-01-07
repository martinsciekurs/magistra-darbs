---
sidebar_position: 216
---

# gen_uuid

**File:** `graphrag/index/utils/uuid.py` (lines 10-14)

## Signature

```python
def gen_uuid(rd: Random | None = None)
```

## Description

Generate a random UUID v4 and return its hex representation.

Args:
    rd: Random | None. Optional random number generator to use. If None, randomness is sourced from the default RNG.

Returns:
    str: Hexadecimal string representation of the generated UUID v4.

