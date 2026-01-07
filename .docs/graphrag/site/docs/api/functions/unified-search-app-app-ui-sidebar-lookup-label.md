---
sidebar_position: 639
---

# lookup_label

**File:** `unified-search-app/app/ui/sidebar.py` (lines 55-56)

## Signature

```python
def lookup_label(key: str)
```

## Description

Return the display label for the given dataset key.

Args:
    key: The dataset key to lookup the label for.

Returns:
    The label corresponding to the dataset key, as determined by dataset_name(key, sv).

Raises:
    Exception: Exceptions raised by dataset_name may be propagated.

