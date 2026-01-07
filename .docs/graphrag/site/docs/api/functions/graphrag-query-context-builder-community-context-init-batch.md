---
sidebar_position: 323
---

# _init_batch

**File:** `graphrag/query/context_builder/community_context.py` (lines 124-130)

## Signature

```python
def _init_batch() -> None
```

## Description

Initialize batch state for the current context.
This updates nonlocal batch_text, batch_tokens, and batch_records by:
- building the batch_text header as "-----&#123;context_name&#125;-----" followed by a newline and the header row joined by column_delimiter
- computing batch_tokens from the batch_text using tokenizer.num_tokens
- resetting batch_records to an empty list
Returns:
    None

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::build_community_context`

