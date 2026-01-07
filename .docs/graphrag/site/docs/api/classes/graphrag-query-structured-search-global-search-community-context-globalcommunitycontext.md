---
sidebar_position: 154
---

# GlobalCommunityContext

**File:** `graphrag/query/structured_search/global_search/community_context.py`

## Overview

GlobalCommunityContext is a global context builder for structured search across multiple communities. It extends GlobalContextBuilder and coordinates community reports, communities, optional entities, and tokenizer-driven text processing to assemble a unified context used by the global search workflow. It also supports optional dynamic community selection to tailor context content to the query.

Args:
  community_reports (list[CommunityReport]): Reports for communities to consider.
  communities (list[Community]): Community objects used to build the hierarchy and starting points.
  entities (list[Entity] | None, optional): Optional list of Entity objects to include in the context.
  tokenizer (Tokenizer | None, optional): Tokenizer to use; if None, a default tokenizer is obtained via get_tokenizer.
  dynamic_community_selection (bool): Enable dynamic community selection.
  dynamic_community_selection_kwargs (dict[str, Any] | None, optional): Optional kwargs for dynamic selection.
  random_state (int): Random seed for reproducibility.

Attributes:
  community_reports: The provided CommunityReport objects.
  communities: The provided Community objects.
  entities: Optional list of Entity objects included in the context.
  tokenizer: The Tokenizer instance in use.
  dynamic_community_selection: Flag indicating if dynamic selection is enabled.
  dynamic_community_selection_kwargs: Additional kwargs for dynamic selection.
  random_state: Random seed for reproducibility.

Initialization:
  This constructor initializes the instance with the provided data and configuration. It does not return a value. If tokenizer is None, a default tokenizer is obtained via get_tokenizer. If dynamic_community_selection is True, dynamic selection will be configured using dynamic_community_selection_kwargs. The class relies on the base GlobalContextBuilder for shared behavior and may raise TypeError or ValueError for invalid inputs.

See Also:
  GlobalContextBuilder

Methods:
  build_context: Prepare batches of community report data as context data for global search. Returns a ContextBuilderResult.

## Methods

### `__init__`

```python
def __init__(
        self,
        community_reports: list[CommunityReport],
        communities: list[Community],
        entities: list[Entity] | None = None,
        tokenizer: Tokenizer | None = None,
        dynamic_community_selection: bool = False,
        dynamic_community_selection_kwargs: dict[str, Any] | None = None,
        random_state: int = 86,
    )
```

### `build_context`

```python
def build_context(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
        use_community_summary: bool = True,
        column_delimiter: str = "|",
        shuffle_data: bool = True,
        include_community_rank: bool = False,
        min_community_rank: int = 0,
        community_rank_name: str = "rank",
        include_community_weight: bool = True,
        community_weight_name: str = "occurrence",
        normalize_community_weight: bool = True,
        max_context_tokens: int = 8000,
        context_name: str = "Reports",
        conversation_history_user_turns_only: bool = True,
        conversation_history_max_turns: int | None = 5,
        **kwargs: Any,
    ) -> ContextBuilderResult
```

