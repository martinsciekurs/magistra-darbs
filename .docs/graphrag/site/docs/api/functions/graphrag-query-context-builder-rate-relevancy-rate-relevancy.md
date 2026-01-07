---
sidebar_position: 337
---

# rate_relevancy

**File:** `graphrag/query/context_builder/rate_relevancy.py` (lines 21-77)

## Signature

```python
def rate_relevancy(
    query: str,
    description: str,
    model: ChatModel,
    tokenizer: Tokenizer,
    rate_query: str = RATE_QUERY,
    num_repeats: int = 1,
    semaphore: asyncio.Semaphore | None = None,
    **model_params: Any,
) -> dict[str, Any]
```

## Description

Rate the relevancy between the query and description on a scale of 0 to 10.

Args:
    query (str): the query (or question) to rate against
    description (str): the community description to rate, it can be the community title, summary, or the full content.
    model (ChatModel): LLM model to use for rating
    tokenizer (Tokenizer): tokenizer
    rate_query (str): prompt template used to format the system message with the given description and question
    num_repeats (int): number of times to repeat the rating process for the same community (default: 1)
    semaphore (asyncio.Semaphore | None): asyncio.Semaphore to limit the number of concurrent LLM calls (default: None)
    model_params (dict[str, Any]): additional arguments to pass to the LLM model
Returns:
    dict[str, Any]: a dictionary containing the final rating and related metadata:
        rating (int): the final chosen rating
        ratings (list[int]): list of individual ratings collected
        llm_calls (int): number of LLM calls performed
        prompt_tokens (int): total number of tokens used for prompts
        output_tokens (int): total number of tokens produced by the model
Raises:
    Exception: if an error occurs during model invocation or response parsing that propagates from the underlying LLM API

## Dependencies

This function calls:

- `graphrag/query/llm/text_utils.py::try_parse_json_object`

## Called By

This function is called by:

- `graphrag/query/context_builder/dynamic_community_selection.py::DynamicCommunitySelection.select`

