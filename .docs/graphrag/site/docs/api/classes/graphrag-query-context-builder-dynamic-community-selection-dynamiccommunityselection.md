---
sidebar_position: 122
---

# DynamicCommunitySelection

**File:** `graphrag/query/context_builder/dynamic_community_selection.py`

## Overview

DynamicCommunitySelection orchestrates dynamic selection of relevant communities for a given query using a language model and relevancy scoring.

Args:
  community_reports (list[CommunityReport]): Reports for communities to consider, mapped by community_id.
  communities (list[Community]): Community objects used to build the hierarchy and starting points.
  model (ChatModel): Language model instance used to rate relevancy of communities to the query.
  tokenizer (Tokenizer): Tokenizer instance used to prepare text for prompting and evaluation.
  rate_query (str): Rate query string used to guide the relevancy assessment. Default is RATE_QUERY.
  use_summary (bool): If True, summaries are incorporated into the evaluation context.
  threshold (int): Threshold determining the cutoff for considering a community relevant.
  keep_parent (bool): If True, keep parent relationships during hierarchical selection.
  num_repeats (int): Number of times to repeat the evaluation steps.
  max_level (int): Maximum depth level to traverse in the hierarchy.
  concurrent_coroutines (int): Maximum number of concurrent coroutines for asynchronous processing.
  model_params (dict[str, Any] | None): Optional dictionary of additional parameters for the model.

Returns:
  tuple[list[CommunityReport], dict[str, Any]]: A tuple containing:
    - A list of CommunityReport objects representing the relevant communities.
    - A dictionary with additional information, including llm usage metrics (llm_calls, prompt_tokens, output_tokens) and rating results.

Raises:
  Exception: If an error occurs during selection processing.

Attributes:
  community_reports: The provided community reports used for consideration.
  communities: The provided Community objects used for hierarchy and starting points.
  model: Language model used for prompting/rating.
  tokenizer: Tokenizer used for text processing.
  rate_query: The rate query string.
  use_summary: Whether summaries are used in evaluation.
  threshold: Selection threshold.
  keep_parent: Whether to retain parent relationships.
  num_repeats: Number of repeats in evaluation.
  max_level: Maximum hierarchy depth.
  concurrent_coroutines: Concurrency limit for asynchronous tasks.
  model_params: Optional model configuration parameters.

## Methods

### `__init__`

```python
def __init__(
        self,
        community_reports: list[CommunityReport],
        communities: list[Community],
        model: ChatModel,
        tokenizer: Tokenizer,
        rate_query: str = RATE_QUERY,
        use_summary: bool = False,
        threshold: int = 1,
        keep_parent: bool = False,
        num_repeats: int = 1,
        max_level: int = 2,
        concurrent_coroutines: int = 8,
        model_params: dict[str, Any] | None = None,
    )
```

### `select`

```python
def select(self, query: str) -> tuple[list[CommunityReport], dict[str, Any]]
```

