---
sidebar_position: 35
---

# ConversationHistory

**File:** `graphrag/query/context_builder/conversation_history.py`

## Overview

ConversationHistory is a helper for storing and manipulating a sequence of conversation turns used for prompt construction and QA-turn generation.

The history is stored as an ordered list of turns, where each turn is represented as a dictionary with keys "role" and "content". Roles typically correspond to the constants SYSTEM, USER, and ASSISTANT.

Attributes:
    turns: list[dict[str, str]]
        The conversation turns in chronological order. Each dictionary has keys "role" and "content".

This class provides methods to initialize from an existing list, add new turns, retrieve user turns, convert the history to QA-turns, and build context data for prompts.

## Methods

### `to_qa_turns`

```python
def to_qa_turns(self) -> list[QATurn]
```

### `from_list`

```python
def from_list(
        cls, conversation_turns: list[dict[str, str]]
    ) -> "ConversationHistory"
```

### `__init__`

```python
def __init__(self)
```

### `add_turn`

```python
def add_turn(self, role: ConversationRole, content: str)
```

### `get_user_turns`

```python
def get_user_turns(self, max_user_turns: int | None = 1) -> list[str]
```

### `build_context`

```python
def build_context(
        self,
        tokenizer: Tokenizer | None = None,
        include_user_turns_only: bool = True,
        max_qa_turns: int | None = 5,
        max_context_tokens: int = 8000,
        recency_bias: bool = True,
        column_delimiter: str = "|",
        context_name: str = "Conversation History",
    ) -> tuple[str, dict[str, pd.DataFrame]]
```

