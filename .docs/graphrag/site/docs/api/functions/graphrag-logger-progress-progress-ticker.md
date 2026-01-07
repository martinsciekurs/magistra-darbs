---
sidebar_position: 306
---

# progress_ticker

**File:** `graphrag/logger/progress.py` (lines 74-78)

## Signature

```python
def progress_ticker(
    callback: ProgressHandler | None, num_total: int, description: str = ""
) -> ProgressTicker
```

## Description

Create a progress ticker.

Args:
    callback: ProgressHandler | None
        Optional callback to be invoked with Progress updates.
    num_total: int
        Total number of items to track progress for.
    description: str
        Optional description to accompany the progress updates.

Returns:
    ProgressTicker
        A ProgressTicker instance configured with the provided callback, total, and description.

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/chunk_text.py::chunk_text`
- `graphrag/index/operations/embed_text/strategies/mock.py::run`
- `graphrag/index/operations/embed_text/strategies/openai.py::run`
- `graphrag/index/operations/summarize_communities/summarize_communities.py::summarize_communities`
- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::get_summarized`
- `graphrag/index/utils/derive_from_rows.py::_derive_from_rows_base`

