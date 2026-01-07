---
sidebar_position: 517
---

# test_run_strategy_arr_tuple

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 101-128)

## Signature

```python
def test_run_strategy_arr_tuple()
```

## Description

Test run_strategy with input as a list of (text, token) tuples.

Verifies that when input is [("text test for run strategy", "3"), ("use for strategy", "5")] and the strategy returns two TextChunk objects with text_chunk values corresponding to the input texts and n_tokens values 5 and 3, run_strategy returns a list of tuples where each tuple is: ( [corresponding source texts], text_chunk, n_tokens as int ). For the given setup, the expected result is:

- ( ["text test for run strategy"], "text test for run strategy", 5 )
- ( ["use for strategy"], "use for strategy", 3 )

The test uses mocks for config and tick and asserts the produced value matches the expected list.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::run_strategy`
- `graphrag/index/operations/chunk_text/typing.py::TextChunk`

