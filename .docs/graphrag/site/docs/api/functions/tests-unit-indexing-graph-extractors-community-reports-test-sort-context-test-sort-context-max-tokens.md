---
sidebar_position: 500
---

# test_sort_context_max_tokens

**File:** `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py` (lines 216-221)

## Signature

```python
def test_sort_context_max_tokens()
```

## Description

Test that sort_context respects the max_context_tokens constraint by returning a non-null context whose token count is less than or equal to the specified maximum.

Parameters:
    None: This test has no input parameters.

Returns:
    None

Raises:
    AssertionError: If any assertion fails.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::sort_context`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

