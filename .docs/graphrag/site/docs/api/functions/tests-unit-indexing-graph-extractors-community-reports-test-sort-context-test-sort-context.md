---
sidebar_position: 499
---

# test_sort_context

**File:** `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py` (lines 206-213)

## Signature

```python
def test_sort_context()
```

## Description

Test that sort_context returns a non-null context and that the token count matches platform-dependent expectations.

Returns:
    None. This is a unit test function and does not return a value.

Raises:
    AssertionError: If any assertion fails.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::sort_context`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

