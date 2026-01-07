---
sidebar_position: 97
---

# _reconstitute_embeddings

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 158-177)

## Signature

```python
def _reconstitute_embeddings(
    raw_embeddings: list[list[float]], sizes: list[int]
) -> list[list[float] | None]
```

## Description

Reconstitute the embeddings into the original input texts.

Args:
    raw_embeddings: list of embeddings, where each embedding is a list of floats
    sizes: list of ints indicating the number of embeddings that belong to each original input text

Returns:
    list of embeddings corresponding to each input text. Each element is either:
    - a list of floats representing the embedding for that input, or
    - None if the corresponding input text had size 0
    For entries with size &gt; 1, the returned embedding is the normalized average of the associated raw embeddings.

Raises:
    None

## Example 💡 Generated

```python
from module import _reconstitute_embeddings
raw = [[0.2,0.8],[0.4,0.4],[0.6,0.2],[0.5,0.5]]
sizes = [1,2,0,1]
result = _reconstitute_embeddings(raw, sizes)
# expected:
# [[0.2,0.8],[0.8575,0.5145],None,[0.5,0.5]]
```

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::run`

