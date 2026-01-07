---
sidebar_position: 143
---

# LocalContextBuilder

**File:** `graphrag/query/context_builder/builders.py`

## Overview

Abstract base class for building the local-context used in local search mode.

This builder defines the contract for assembling the user query and optional conversation history into a ContextBuilderResult that downstream components can use to perform a local (on-device) search.

Attributes:
    No explicit data attributes are defined on this base class. Concrete implementations may define configuration parameters, caches, or data sources as needed.

Args:
    query (str): The user query to build context for.
    conversation_history (ConversationHistory | None): Optional conversation history to consider while constructing the context.
    **kwargs: Additional keyword arguments that may influence how the context is built. Implementations may interpret or ignore these as needed.

Returns:
    ContextBuilderResult: The result containing the built context for downstream processing.

Raises:
    NotImplementedError: If invoked on the abstract base class.
    ValueError: If inputs are invalid or inconsistent (implementation-specific).

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

