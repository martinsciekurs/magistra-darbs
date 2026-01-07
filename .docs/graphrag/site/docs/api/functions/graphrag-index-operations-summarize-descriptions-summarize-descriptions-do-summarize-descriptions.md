---
sidebar_position: 162
---

# do_summarize_descriptions

**File:** `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py` (lines 95-104)

## Signature

```python
def do_summarize_descriptions(
        id: str | tuple[str, str],
        descriptions: list[str],
        ticker: ProgressTicker,
        semaphore: asyncio.Semaphore,
    )
```

## Description

Run a summarization strategy on the provided descriptions for a given id or pair of ids.

Args:
  id: Identifier for the descriptions to summarize; can be a string or a tuple of two strings.
  descriptions: Descriptions to summarize.
  ticker: ProgressTicker used to report progress.
  semaphore: Semaphore controlling concurrency for the operation.

Returns:
  The results produced by strategy_exec for the given id and descriptions.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::get_summarized`

