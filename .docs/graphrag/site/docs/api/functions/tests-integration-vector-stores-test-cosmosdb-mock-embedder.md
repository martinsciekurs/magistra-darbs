---
sidebar_position: 445
---

# mock_embedder

**File:** `tests/integration/vector_stores/test_cosmosdb.py` (lines 153-154)

## Signature

```python
def mock_embedder(text: str) -> list[float]
```

## Description

Return a fixed embedding vector for testing.

Args:
    text: Input text to embed.

Returns:
    list[float]: The fixed embedding vector [0.1, 0.2, 0.3, 0.4, 0.5].

Raises:
    None: This function does not raise any exceptions.

