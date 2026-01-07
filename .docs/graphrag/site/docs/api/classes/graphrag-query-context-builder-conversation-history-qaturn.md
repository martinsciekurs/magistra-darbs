---
sidebar_position: 17
---

# QATurn

**File:** `graphrag/query/context_builder/conversation_history.py`

## Overview

QATurn is a dataclass that represents a single turn in a question-and-answer conversation history, pairing a user query with optional assistant answers and providing helpers to derive text for display.

Attributes:
  user_query: Optional[object] - The user query for this turn. The object should have a 'content' attribute used for display. May be None.
  assistant_answers: Optional[List[str]] - The assistant's answers for this turn. If None, no answer has been provided yet.

Args:
  user_query: Optional[object] - The user query component for this turn. The object should have a 'content' attribute.
  assistant_answers: Optional[List[str]] - The assistant's answers for this turn. None indicates no answer yet.

Methods:
  get_answer_text(self) -&gt; Optional[str]: Returns the assistant answers contents joined by newline characters, or None if there are no answers.
  __str__(self) -&gt; str: Returns a readable representation of the turn. If assistant answers exist, the string is "Question: &lt;user_query.content&gt;\nAnswer: &lt;concatenated answers&gt;"; otherwise, it's "Question: &lt;user_query.content&gt;".

## Methods

### `get_answer_text`

```python
def get_answer_text(self) -> str | None
```

### `__str__`

```python
def __str__(self) -> str
```

