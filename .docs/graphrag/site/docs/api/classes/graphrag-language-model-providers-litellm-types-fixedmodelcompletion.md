---
sidebar_position: 126
---

# FixedModelCompletion

**File:** `graphrag/language_model/providers/litellm/types.py`

## Overview

FixedModelCompletion is a fixed-model chat completion provider backed by Litellm. It exposes a callable interface that forwards a set of chat completion parameters to the underlying service and returns either the model's final response or a streaming wrapper when streaming is requested.

Purpose
- Provide a lightweight, fixed-model completion integration built on Litellm for generating chat completions against a predetermined model.
- Offer a simple __call__ interface that mirrors the underlying client while surfacing the fixed-model semantics.

Key behavior
- Returns either a ModelResponse when streaming is not enabled, or a CustomStreamWrapper when stream is True, allowing incremental consumption of results.
- Delegates all additional keyword arguments to the underlying client via kwargs, enabling access to the full range of Litellm/OpenAI options.

Args
- messages: List of ChatCompletion messages to include in the request. Defaults to an empty list.
- stream: If True, stream partial responses as they arrive. Defaults to None (non-streaming).
- stream_options: Options for streaming.
- stop: Stop sequence or token.
- max_completion_tokens: Maximum number of tokens in the completion.
- max_tokens: Maximum tokens for the response.
- modalities: Modality to use for the completion.
- prediction: Prediction content parameter.
- audio: Audio parameter for audio-enabled modes.
- logit_bias: Token bias mapping.
- user: User identifier for the request.
- response_format: OpenAI v1.0+ response format parameter; may be a dict or a model type.
- seed: Random seed for deterministic behavior.
- tools: Tools to be used during the completion.
- tool_choice: Specific tool choice or mapping.
- logprobs: Whether to return log probabilities.
- top_logprobs: Number of top logprobs to return.
- parallel_tool_calls: Whether to perform tool calls in parallel.
- web_search_options: Web search options for information retrieval.
- deployment_id: Deployment identifier for the model.
- extra_headers: Additional headers to include in the request.
- functions: OpenAI function definitions (legacy).
- function_call: Function call type or directive.
- thinking: AnthropicThinkingParam to influence model thinking behavior.
- kwargs: Additional keyword arguments passed through to the underlying client.

Returns
- ModelResponse: The model's response when streaming is not enabled.
- CustomStreamWrapper: A streaming wrapper that yields results when streaming is enabled.

Raises
- Propagates exceptions raised by the underlying Litellm/OpenAI clients (e.g., network errors, validation errors) to surface service failures.

Examples
- Non-streaming use:
  FixedModelCompletion(...)(messages=[...])
- Streaming use:
  stream = FixedModelCompletion(...)(messages=[...], stream=True)
  for chunk in stream:
      ...

## Methods

### `__call__`

```python
def __call__(
        self,
        *,
        messages: list = [],  # type: ignore  # noqa: B006
        stream: bool | None = None,
        stream_options: dict | None = None,  # type: ignore
        stop=None,  # type: ignore
        max_completion_tokens: int | None = None,
        max_tokens: int | None = None,
        modalities: list[ChatCompletionModality] | None = None,
        prediction: ChatCompletionPredictionContentParam | None = None,
        audio: ChatCompletionAudioParam | None = None,
        logit_bias: dict | None = None,  # type: ignore
        user: str | None = None,
        # openai v1.0+ new params
        response_format: dict | type[BaseModel] | None = None,  # type: ignore
        seed: int | None = None,
        tools: list | None = None,  # type: ignore
        tool_choice: str | dict | None = None,  # type: ignore
        logprobs: bool | None = None,
        top_logprobs: int | None = None,
        parallel_tool_calls: bool | None = None,
        web_search_options: OpenAIWebSearchOptions | None = None,
        deployment_id=None,  # type: ignore
        extra_headers: dict | None = None,  # type: ignore
        # soon to be deprecated params by OpenAI
        functions: list | None = None,  # type: ignore
        function_call: str | None = None,
        # Optional liteLLM function params
        thinking: AnthropicThinkingParam | None = None,
        **kwargs: Any,
    ) -> ModelResponse | CustomStreamWrapper
```

