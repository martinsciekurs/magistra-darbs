---
sidebar_position: 81
---

# AFixedModelCompletion

**File:** `graphrag/language_model/providers/litellm/types.py`

## Overview

Async fixed-model chat completion interface for litellm integration. This class exposes a callable, asynchronous surface to perform chat completions against an OpenAI compatible API using a fixed model, with optional streaming support via litellm. It is designed for straightforward, open-ended chat interactions and can be combined with function calling and tools when provided.

Args:
  messages: list. Chat messages to include in the request. Defaults to an empty list. Optional.
  stream: bool | None. If True, stream partial responses as they arrive. Defaults to None (non-streaming).
  stream_options: dict | None. Options controlling streaming behavior. Defaults to None.
  stop: Any. Stop sequence or sequences. Optional.
  max_completion_tokens: int | None. Maximum tokens allowed in the completion. Optional.
  max_tokens: int | None. Maximum tokens allowed for the response. Optional.
  modalities: list of ChatCompletionModality | None. Modality hints to apply. Optional.
  prediction: ChatCompletionPredictionContentParam | None. Prediction content to request. Optional.
  audio: ChatCompletionAudioParam | None. Audio-related parameters for the request. Optional.
  logit_bias: dict | None. Biases for logits of the model. Optional.
  user: str | None. User identifier for the request. Optional.
  response_format: dict | type BaseModel | None. Response format specification. Optional.
  seed: int | None. Random seed for reproducibility. Optional.
  tools: list | None. Tools to be used in processing the request. Optional.
  tool_choice: str | dict | None. Tool selection information. Optional.
  logprobs: bool | None. Whether to include log probabilities in the result. Optional.
  top_logprobs: int | None. Number of top log probabilities to return. Optional.
  parallel_tool_calls: bool | None. Allow parallel tool invocations. Optional.
  web_search_options: OpenAIWebSearchOptions | None. Options for web search augmentation. Optional.
  deployment_id: any. Deployment identifier. Optional.
  extra_headers: dict | None. Additional HTTP headers to include. Optional.
  functions: list | None. Deprecated parameter. Use function_call instead. Optional and deprecated.
  function_call: str | None. Behavior for function calling (eg, auto, none, or function name). Optional.
  thinking: AnthropicThinkingParam | None. Thinking constraints for the underlying model. Optional.
  kwargs: Any. Additional keyword arguments forwarded to the API. Optional.

Returns:
  ModelResponse | CustomStreamWrapper. The chat completion result or a streaming wrapper for partial results.

Raises:
  Exceptions raised by the underlying litellm/OpenAI API clients during request handling.

Example:
  # Non-streaming call
  ac = AFixedModelCompletion(...)
  result = await ac(messages=[&#123;"role": "user", "content": "Hello"&#125;])

  # Streaming call
  stream = ac(messages=[&#123;"role": "user", "content": "Tell me a story."&#125;], stream=True)
  async for chunk in stream:
      # process streaming chunks
      pass

## Methods

### `__call__`

```python
def __call__(
        self,
        *,
        # Optional OpenAI params: see https://platform.openai.com/docs/api-reference/chat/create
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

