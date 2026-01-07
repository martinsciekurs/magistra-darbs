---
sidebar_position: 389
---

# batched

**File:** `graphrag/query/llm/text_utils.py` (lines 21-33)

## Signature

```python
def batched(iterable: Iterator, n: int)
```

## Description

Batch data into tuples of length n. The last batch may be shorter.

Args:
    iterable (Iterator): The input iterable to batch.
    n (int): The batch size (must be at least 1).

Returns:
    Iterator[tuple]: An iterator that yields batches as tuples of length n (the last batch may be shorter).

Raises:
    ValueError: If n &lt; 1.

## Called By

This function is called by:

- `graphrag/query/llm/text_utils.py::chunk_text`

