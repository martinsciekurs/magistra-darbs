---
sidebar_position: 535
---

# test_noop_text_splitter

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 19-23)

## Signature

```python
def test_noop_text_splitter() -> None
```

## Description

Test that NoopTextSplitter.split_text returns input unchanged.

This test constructs a NoopTextSplitter and asserts that:
- split_text("some text") yields ["some text"]
- split_text(["some", "text"]) yields ["some", "text"]

Returns:
    None: This test does not return a value.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::NoopTextSplitter`

