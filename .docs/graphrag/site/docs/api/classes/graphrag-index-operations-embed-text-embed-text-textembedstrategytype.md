---
sidebar_position: 147
---

# TextEmbedStrategyType

**File:** `graphrag/index/operations/embed_text/embed_text.py`

## Overview

Enum describing the available text embedding strategies used by the embedding operation.

Purpose:
Represent the different strategies that can generate text embeddings, enabling the embedding workflow to select and apply the appropriate strategy implementation (for example, OpenAI-based or mock strategies as evidenced by related modules).

Key attributes:
Enum members correspond to specific embedding strategies used by the system, as seen in the openai and mock strategy modules.

## Methods

### `__repr__`

```python
def __repr__(self)
```

