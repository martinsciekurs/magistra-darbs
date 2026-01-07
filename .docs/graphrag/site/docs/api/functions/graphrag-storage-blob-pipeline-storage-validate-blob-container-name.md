---
sidebar_position: 392
---

# validate_blob_container_name

**File:** `graphrag/storage/blob_pipeline_storage.py` (lines 315-365)

## Signature

```python
def validate_blob_container_name(container_name: str)
```

## Description

Validate a blob container name against Azure rules.

This function verifies the following constraints:
- The name length is between 3 and 63 characters.
- The name starts with a letter or a number.
- All characters are lowercase letters, numbers, or hyphen.
- The name does not contain consecutive hyphens.
- The name does not end with a hyphen.

Args:
    container_name (str): The blob container name to be validated.

Returns:
    bool: True if the container name is valid.
    ValueError: If the input is invalid, a ValueError instance describing the reason is returned (note: the function does not raise exceptions; invalid input signals are returned).

