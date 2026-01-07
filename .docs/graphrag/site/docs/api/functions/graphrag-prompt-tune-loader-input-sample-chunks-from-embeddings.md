---
sidebar_position: 319
---

# _sample_chunks_from_embeddings

**File:** `graphrag/prompt_tune/loader/input.py` (lines 28-38)

## Signature

```python
def _sample_chunks_from_embeddings(
    text_chunks: pd.DataFrame,
    embeddings: np.ndarray[float, np.dtype[np.float_]],
    k: int = K,
) -> pd.DataFrame
```

## Description

Sample k text chunks whose embeddings are closest to the center of the embedding set.

Args:
  text_chunks: DataFrame containing text chunks to sample from.
  embeddings: Array of embedding vectors corresponding to the text chunks.
  k: Number of chunks to sample (default K).

Returns:
  DataFrame containing the sampled text chunks.
  The rows correspond to the k chunks with embeddings closest to the mean embedding.

Raises:
  None

## Called By

This function is called by:

- `graphrag/prompt_tune/loader/input.py::load_docs_in_chunks`

