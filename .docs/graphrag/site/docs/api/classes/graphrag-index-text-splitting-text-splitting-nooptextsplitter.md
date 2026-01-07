---
sidebar_position: 129
---

# NoopTextSplitter

**File:** `graphrag/index/text_splitting/text_splitting.py`

## Overview

NoopTextSplitter is a no-op text splitter that returns the input text unchanged as a sequence of strings. It is stateless and serves as a minimal default splitter when no actual splitting is required.

split_text(self, text: str | list[str]) -&gt; Iterable[str]:
    Split text into chunks without modification. If text is a string, returns a single-element list containing that string; if text is a list of strings, returns that list as-is.

Args:
    text: The input text to split. A single string or a list of strings.

Returns:
    Iterable[str]: The input text as an iterable of strings. Behavior is:
    - string input -&gt; [string]
    - list[str] input -&gt; that same list

Raises:
    None

## Methods

### `split_text`

```python
def split_text(self, text: str | list[str]) -> Iterable[str]
```

