---
sidebar_position: 110
---

# GlobalContextBuilder

**File:** `graphrag/query/context_builder/builders.py`

## Overview

GlobalContextBuilder builds the context used for the global search mode.

Purpose:
A specialized builder responsible for constructing the context used when performing a global search. It considers the user query and may incorporate optional conversation history and additional keyword arguments to assemble a ContextBuilderResult that downstream components can use to execute or facilitate the global search.

Attributes:
- No explicit instance attributes are defined in the provided interface.

Methods:
- build_context(self, query: str, conversation_history: ConversationHistory | None = None, **kwargs) -&gt; ContextBuilderResult
  Build the context for the global search mode.

Args (for build_context):
- query: The user query to build context for.
- conversation_history: Optional conversation history to consider while constructing the context.
- kwargs: Additional keyword arguments that may influence how the context is built.

Returns (for build_context):
- ContextBuilderResult: The result containing the built context for the global search operation. The exact contents depend on downstream usage and typically include the constructed context data and any necessary metadata.

Raises:
- NotImplementedError: This class declares build_context as an abstract method. Concrete subclasses must provide an implementation.

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

