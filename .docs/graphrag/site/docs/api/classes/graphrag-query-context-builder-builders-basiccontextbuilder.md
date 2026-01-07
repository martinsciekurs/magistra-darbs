---
sidebar_position: 106
---

# BasicContextBuilder

**File:** `graphrag/query/context_builder/builders.py`

## Overview

BasicContextBuilder is a concrete implementation of a context builder that constructs the minimal context required for the basic search mode by combining the user query with optional conversation history.

Args:
- None: The constructor takes no public parameters.

Returns:
- ContextBuilderResult: The result type produced when build_context is called, representing the assembled context for a basic search.

Raises:
- TypeError: If the provided inputs do not match expected types when building the context.
- ValueError: If inputs are invalid (e.g., non-string query).

Attributes:
- No public attributes are declared for this class. Internal state, if any, is encapsulated.

Summary:
- This class participates in Graphrag's query context builder system as the basic-mode context creator, supplying the minimal context necessary to perform basic search.

## Methods

### `build_context`

```python
def build_context(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
        **kwargs,
    ) -> ContextBuilderResult
```

